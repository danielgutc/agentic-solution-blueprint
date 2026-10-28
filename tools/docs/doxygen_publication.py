"""Schema v2 profile-canonical Doxygen publication model.

The module intentionally builds on the bounded Doxygen XML parser in
``doxygen_markdown``. It validates an independently declared symbol inventory;
it does not claim compiler-complete semantics from Doxygen.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Any

try:
    from . import doxygen_markdown as legacy
except ImportError:
    import doxygen_markdown as legacy


OWNER_ROLES = {"owned-implementation"}
INTERFACE_ROLES = {"provided-interface", "consumed-interface"}
ROLES = OWNER_ROLES | {"provided-interface", "consumed-interface", "supporting-code"}
INTERFACE_SCOPES = {"external-runtime", "internal-component"}
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


@dataclass(frozen=True)
class ArchitectureTarget:
    id: str
    title: str
    output_dir: Path
    architecture_page: Path
    container_id: str | None = None


@dataclass(frozen=True)
class CoverageExclusion:
    scope: str
    reason: str


@dataclass(frozen=True)
class SymbolSelector:
    compound_ids: tuple[str, ...]
    qualified_names: tuple[str, ...]
    source_prefixes: tuple[str, ...]


@dataclass(frozen=True)
class SymbolConfig:
    key: str
    qualified_name: str
    api_scope: str
    selectors: SymbolSelector


@dataclass(frozen=True)
class Binding:
    symbol_key: str
    role: str
    container_id: str
    component_id: str | None
    interface_scope: str | None
    narrative: str


@dataclass(frozen=True)
class CompatibilityStub:
    path: Path
    symbol_key: str


@dataclass(frozen=True)
class PublicationProfile:
    path: Path
    schema_version: int
    repository_root: Path
    reproduce_command: str
    id: str
    title: str
    implementation_unit: str
    doxygen_version: str
    doxyfile: Path
    doxygen_xml: Path
    code_fence_language: str
    parser_limitations: tuple[str, ...]
    included_coverage: tuple[str, ...]
    excluded_coverage: tuple[CoverageExclusion, ...]
    inventory_evidence: Path
    symbols: tuple[SymbolConfig, ...]
    bindings: tuple[Binding, ...]
    compatibility_stubs: tuple[CompatibilityStub, ...]
    legacy_stub_roots: tuple[Path, ...]
    canonical_root: Path


@dataclass(frozen=True)
class PublicationConfig:
    path: Path
    schema_version: int
    repository_root: Path
    reproduce_command: str
    containers: tuple[ArchitectureTarget, ...]
    components: tuple[ArchitectureTarget, ...]
    profiles: tuple[PublicationProfile, ...]


@dataclass(frozen=True)
class AssignedProfile:
    profile: PublicationProfile
    compounds: tuple[legacy.Compound, ...]
    symbols_by_key: dict[str, legacy.Compound]
    symbols_by_compound: dict[str, SymbolConfig]


def _required_string(data: dict[str, Any], key: str, context: str = "") -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        prefix = f"{context}." if context else ""
        raise legacy.DocumentationError(f"{prefix}{key} must be a non-empty string")
    return value.strip()


def _string_list(data: dict[str, Any], key: str, context: str) -> tuple[str, ...]:
    value = data.get(key, [])
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        raise legacy.DocumentationError(f"{context}.{key} must be a list of non-empty strings")
    return tuple(item.strip() for item in value)


def _safe_id(value: str, context: str) -> str:
    if not SAFE_ID.fullmatch(value) or value in {".", ".."}:
        raise legacy.DocumentationError(f"{context} must be a path-safe stable identifier: {value}")
    return value


def _repository_path(root: Path, value: str, context: str, *, must_exist: bool = False) -> Path:
    path = (root / value).resolve()
    if not legacy._within(path, root):
        raise legacy.DocumentationError(f"{context} escapes repository_root: {value}")
    if must_exist and not path.is_file():
        raise legacy.DocumentationError(f"{context} does not exist: {path}")
    return path


def _config_path(base: Path, value: str, context: str, *, directory: bool = False) -> Path:
    path = (base / value).resolve()
    exists = path.is_dir() if directory else path.is_file()
    if not exists:
        raise legacy.DocumentationError(f"{context} does not exist: {path}")
    return path


def _load_targets(
    raw_items: Any,
    repository_root: Path,
    kind: str,
    containers: dict[str, ArchitectureTarget] | None = None,
) -> tuple[ArchitectureTarget, ...]:
    if not isinstance(raw_items, list):
        raise legacy.DocumentationError(f"architecture.{kind} must be a list")
    result: list[ArchitectureTarget] = []
    seen_ids: set[str] = set()
    seen_outputs: set[str] = set()
    for index, raw in enumerate(raw_items):
        context = f"architecture.{kind}[{index}]"
        if not isinstance(raw, dict):
            raise legacy.DocumentationError(f"{context} must be an object")
        target_id = _safe_id(_required_string(raw, "id", context), f"{context}.id")
        container_id: str | None = None
        container: ArchitectureTarget | None = None
        if containers is not None:
            container_id = _required_string(raw, "container_id", context)
            container = containers.get(container_id.casefold())
            if container is None:
                raise legacy.DocumentationError(f"{context} references unknown container: {container_id}")
        folded = (
            target_id.casefold()
            if container_id is None
            else f"{container_id.casefold()}/{target_id.casefold()}"
        )
        if folded in seen_ids:
            raise legacy.DocumentationError(f"duplicate {kind[:-1]} id: {target_id}")
        seen_ids.add(folded)
        output_dir = _repository_path(
            repository_root, _required_string(raw, "output_dir", context), f"{context}.output_dir"
        )
        output_key = str(output_dir).casefold()
        if output_key in seen_outputs:
            raise legacy.DocumentationError(f"duplicate {kind[:-1]} output_dir: {output_dir}")
        seen_outputs.add(output_key)
        architecture_page = _repository_path(
            repository_root,
            _required_string(raw, "architecture_page", context),
            f"{context}.architecture_page",
            must_exist=True,
        )
        if not legacy._within(architecture_page, output_dir):
            raise legacy.DocumentationError(f"{context}.architecture_page must be inside output_dir")
        if container is not None:
            if not legacy._within(output_dir, container.output_dir):
                raise legacy.DocumentationError(f"{context}.output_dir is outside its container")
        result.append(
            ArchitectureTarget(
                id=target_id,
                title=_required_string(raw, "title", context),
                output_dir=output_dir,
                architecture_page=architecture_page,
                container_id=container_id,
            )
        )
    return tuple(result)


def _load_profile(
    raw: Any,
    index: int,
    config_path: Path,
    repository_root: Path,
    reproduce_command: str,
    containers: dict[str, ArchitectureTarget],
    components: dict[tuple[str, str], ArchitectureTarget],
) -> PublicationProfile:
    context = f"profiles[{index}]"
    if not isinstance(raw, dict):
        raise legacy.DocumentationError(f"{context} must be an object")
    profile_id = _safe_id(_required_string(raw, "id", context), f"{context}.id")
    implementation_unit = _safe_id(
        _required_string(raw, "implementation_unit", context), f"{context}.implementation_unit"
    )
    base = config_path.parent
    coverage = raw.get("source_coverage")
    if not isinstance(coverage, dict):
        raise legacy.DocumentationError(f"{context}.source_coverage must be an object")
    included = _string_list(coverage, "included", f"{context}.source_coverage")
    if not included:
        raise legacy.DocumentationError(f"{context}.source_coverage.included must not be empty")
    parser_limitations = _string_list(raw, "parser_limitations", context)
    if not parser_limitations:
        raise legacy.DocumentationError(f"{context}.parser_limitations must not be empty")
    raw_excluded = coverage.get("excluded")
    if not isinstance(raw_excluded, list):
        raise legacy.DocumentationError(f"{context}.source_coverage.excluded must be a list")
    exclusions: list[CoverageExclusion] = []
    for exclusion_index, item in enumerate(raw_excluded):
        item_context = f"{context}.source_coverage.excluded[{exclusion_index}]"
        if not isinstance(item, dict):
            raise legacy.DocumentationError(f"{item_context} must be an object")
        exclusions.append(
            CoverageExclusion(
                scope=_required_string(item, "scope", item_context),
                reason=_required_string(item, "reason", item_context),
            )
        )

    raw_symbols = raw.get("symbols")
    if not isinstance(raw_symbols, list) or not raw_symbols:
        raise legacy.DocumentationError(f"{context}.symbols must be a non-empty list")
    symbols: list[SymbolConfig] = []
    symbol_keys: set[str] = set()
    for symbol_index, item in enumerate(raw_symbols):
        symbol_context = f"{context}.symbols[{symbol_index}]"
        if not isinstance(item, dict):
            raise legacy.DocumentationError(f"{symbol_context} must be an object")
        key = _safe_id(_required_string(item, "key", symbol_context), f"{symbol_context}.key")
        folded = key.casefold()
        if folded in symbol_keys:
            raise legacy.DocumentationError(f"duplicate symbol key in profile {profile_id}: {key}")
        symbol_keys.add(folded)
        api_scope = _required_string(item, "api_scope", symbol_context)
        scope_path = Path(api_scope)
        if scope_path.is_absolute() or ".." in scope_path.parts or not SAFE_ID.fullmatch(api_scope):
            raise legacy.DocumentationError(f"{symbol_context}.api_scope must be one path-safe segment")
        selector_data = item.get("selectors")
        if not isinstance(selector_data, dict):
            raise legacy.DocumentationError(f"{symbol_context}.selectors must be an object")
        selector = SymbolSelector(
            compound_ids=_string_list(selector_data, "compound_ids", f"{symbol_context}.selectors"),
            qualified_names=_string_list(selector_data, "qualified_names", f"{symbol_context}.selectors"),
            source_prefixes=tuple(
                value.replace("\\", "/")
                for value in _string_list(selector_data, "source_prefixes", f"{symbol_context}.selectors")
            ),
        )
        if not (selector.compound_ids or selector.qualified_names or selector.source_prefixes):
            raise legacy.DocumentationError(f"{symbol_context} must declare at least one selector")
        symbols.append(
            SymbolConfig(
                key=key,
                qualified_name=_required_string(item, "qualified_name", symbol_context),
                api_scope=api_scope,
                selectors=selector,
            )
        )

    raw_bindings = raw.get("bindings")
    if not isinstance(raw_bindings, list):
        raise legacy.DocumentationError(f"{context}.bindings must be a list")
    bindings: list[Binding] = []
    owner_by_symbol: dict[str, Binding] = {}
    binding_keys: set[tuple[str, str, str, str, str]] = set()
    for binding_index, item in enumerate(raw_bindings):
        binding_context = f"{context}.bindings[{binding_index}]"
        if not isinstance(item, dict):
            raise legacy.DocumentationError(f"{binding_context} must be an object")
        symbol_key = _required_string(item, "symbol_key", binding_context)
        if symbol_key.casefold() not in symbol_keys:
            raise legacy.DocumentationError(f"{binding_context} references unknown symbol: {symbol_key}")
        role = _required_string(item, "role", binding_context)
        if role not in ROLES:
            raise legacy.DocumentationError(f"{binding_context}.role is unsupported: {role}")
        container_id = _required_string(item, "container_id", binding_context)
        container = containers.get(container_id.casefold())
        if container is None:
            raise legacy.DocumentationError(f"{binding_context} references unknown container: {container_id}")
        component_id_value = item.get("component_id")
        component_id = None
        if component_id_value is not None:
            if not isinstance(component_id_value, str) or not component_id_value.strip():
                raise legacy.DocumentationError(f"{binding_context}.component_id must be a non-empty string")
            component_id = component_id_value.strip()
            if (container_id.casefold(), component_id.casefold()) not in components:
                raise legacy.DocumentationError(
                    f"{binding_context} references unknown component {component_id} in container {container_id}"
                )
        scope_value = item.get("interface_scope")
        interface_scope = scope_value.strip() if isinstance(scope_value, str) else None
        if role in INTERFACE_ROLES and interface_scope not in INTERFACE_SCOPES:
            raise legacy.DocumentationError(
                f"{binding_context}.interface_scope must be external-runtime or internal-component"
            )
        if role not in INTERFACE_ROLES and scope_value is not None:
            raise legacy.DocumentationError(
                f"{binding_context}.interface_scope is valid only for interface roles"
            )
        binding = Binding(
            symbol_key=symbol_key,
            role=role,
            container_id=container_id,
            component_id=component_id,
            interface_scope=interface_scope,
            narrative=str(item.get("narrative", "")).strip(),
        )
        binding_key = (
            symbol_key.casefold(), role, container_id.casefold(),
            (component_id or "").casefold(), interface_scope or "",
        )
        if binding_key in binding_keys:
            raise legacy.DocumentationError(f"duplicate architecture binding in {binding_context}")
        binding_keys.add(binding_key)
        if role in OWNER_ROLES:
            previous = owner_by_symbol.get(symbol_key.casefold())
            if previous is not None:
                raise legacy.DocumentationError(
                    f"conflicting owner bindings for symbol {symbol_key}: "
                    f"{previous.container_id} and {container_id}"
                )
            owner_by_symbol[symbol_key.casefold()] = binding
        bindings.append(binding)

    raw_roots = raw.get("legacy_stub_roots", [])
    if not isinstance(raw_roots, list) or not all(isinstance(item, str) and item for item in raw_roots):
        raise legacy.DocumentationError(f"{context}.legacy_stub_roots must be a list of paths")
    legacy_roots = tuple(
        _repository_path(repository_root, value, f"{context}.legacy_stub_roots") for value in raw_roots
    )
    raw_stubs = raw.get("compatibility_stubs", [])
    if not isinstance(raw_stubs, list):
        raise legacy.DocumentationError(f"{context}.compatibility_stubs must be a list")
    stubs: list[CompatibilityStub] = []
    seen_stub_paths: set[str] = set()
    for stub_index, item in enumerate(raw_stubs):
        stub_context = f"{context}.compatibility_stubs[{stub_index}]"
        if not isinstance(item, dict):
            raise legacy.DocumentationError(f"{stub_context} must be an object")
        path = _repository_path(
            repository_root, _required_string(item, "path", stub_context), f"{stub_context}.path"
        )
        if not any(legacy._within(path, root) for root in legacy_roots):
            raise legacy.DocumentationError(f"{stub_context}.path is outside legacy_stub_roots")
        path_key = str(path).casefold()
        if path_key in seen_stub_paths:
            raise legacy.DocumentationError(f"duplicate compatibility stub path: {path}")
        seen_stub_paths.add(path_key)
        symbol_key = _required_string(item, "symbol_key", stub_context)
        if symbol_key.casefold() not in symbol_keys:
            raise legacy.DocumentationError(f"{stub_context} references unknown symbol: {symbol_key}")
        stubs.append(CompatibilityStub(path=path, symbol_key=symbol_key))

    canonical_root = (
        repository_root / "design" / "code" / implementation_unit / profile_id
    ).resolve()
    inventory_evidence = _repository_path(
        repository_root,
        _required_string(raw, "inventory_evidence", context),
        f"{context}.inventory_evidence",
        must_exist=True,
    )
    return PublicationProfile(
        path=config_path,
        schema_version=2,
        repository_root=repository_root,
        reproduce_command=reproduce_command,
        id=profile_id,
        title=_required_string(raw, "title", context),
        implementation_unit=implementation_unit,
        doxygen_version=_required_string(raw, "doxygen_version", context),
        doxyfile=_config_path(base, _required_string(raw, "doxyfile", context), f"{context}.doxyfile"),
        doxygen_xml=_config_path(
            base, _required_string(raw, "doxygen_xml", context), f"{context}.doxygen_xml", directory=True
        ),
        code_fence_language=str(raw.get("code_fence_language", "")).strip(),
        parser_limitations=parser_limitations,
        included_coverage=included,
        excluded_coverage=tuple(exclusions),
        inventory_evidence=inventory_evidence,
        symbols=tuple(symbols),
        bindings=tuple(bindings),
        compatibility_stubs=tuple(stubs),
        legacy_stub_roots=legacy_roots,
        canonical_root=canonical_root,
    )


def load_publication_config(path: Path, data: dict[str, Any]) -> PublicationConfig:
    base = path.parent
    repository_root = (base / _required_string(data, "repository_root")).resolve()
    if not repository_root.is_dir():
        raise legacy.DocumentationError(f"repository_root does not exist: {repository_root}")
    reproduce_command = _required_string(data, "reproduce_command")
    architecture = data.get("architecture")
    if not isinstance(architecture, dict):
        raise legacy.DocumentationError("architecture must be an object")
    containers_tuple = _load_targets(architecture.get("containers"), repository_root, "containers")
    if not containers_tuple:
        raise legacy.DocumentationError("architecture.containers must not be empty")
    containers = {item.id.casefold(): item for item in containers_tuple}
    components_tuple = _load_targets(
        architecture.get("components", []), repository_root, "components", containers
    )
    components = {
        ((item.container_id or "").casefold(), item.id.casefold()): item for item in components_tuple
    }
    raw_profiles = data.get("profiles")
    if not isinstance(raw_profiles, list) or not raw_profiles:
        raise legacy.DocumentationError("profiles must be a non-empty list")
    profiles: list[PublicationProfile] = []
    seen_profiles: set[tuple[str, str]] = set()
    seen_roots: set[str] = set()
    for index, raw in enumerate(raw_profiles):
        if not isinstance(raw, dict):
            raise legacy.DocumentationError(f"profiles[{index}] must be an object")
        raw_id = _required_string(raw, "id", f"profiles[{index}]")
        raw_unit = _required_string(raw, "implementation_unit", f"profiles[{index}]")
        identity = (raw_unit.casefold(), raw_id.casefold())
        if identity in seen_profiles:
            raise legacy.DocumentationError(
                f"duplicate profile id for implementation unit {raw_unit}: {raw_id}"
            )
        seen_profiles.add(identity)
        profile = _load_profile(
            raw, index, path, repository_root, reproduce_command, containers, components
        )
        root_key = str(profile.canonical_root).casefold()
        if root_key in seen_roots:
            raise legacy.DocumentationError(f"colliding canonical profile root: {profile.canonical_root}")
        seen_roots.add(root_key)
        profiles.append(profile)
    return PublicationConfig(
        path=path,
        schema_version=2,
        repository_root=repository_root,
        reproduce_command=reproduce_command,
        containers=containers_tuple,
        components=components_tuple,
        profiles=tuple(profiles),
    )


def run_publication_doxygen(config: PublicationConfig, executable: str) -> None:
    actual = legacy.doxygen_version(executable)
    for profile in config.profiles:
        if actual != profile.doxygen_version:
            raise legacy.DocumentationError(
                f"Doxygen version mismatch for profile {profile.id}: "
                f"configured {profile.doxygen_version}, found {actual}"
            )
        result = subprocess.run(
            [executable, str(profile.doxyfile)],
            cwd=profile.doxyfile.parent,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            detail = result.stderr.strip() or result.stdout.strip()
            raise legacy.DocumentationError(
                f"Doxygen generation failed for profile {profile.id}: {detail}"
            )
        if result.stderr.strip():
            raise legacy.DocumentationError(
                f"Doxygen reported diagnostics for profile {profile.id}: {result.stderr.strip()}"
            )


def _select_compounds(profile: PublicationProfile) -> AssignedProfile:
    compounds = legacy.load_compounds(profile)  # type: ignore[arg-type]
    symbols_by_key: dict[str, legacy.Compound] = {}
    symbols_by_compound: dict[str, SymbolConfig] = {}
    for symbol in profile.symbols:
        matches: list[legacy.Compound] = []
        for compound in compounds:
            source = legacy._source_path(profile, compound.location).relative_to(
                profile.repository_root
            ).as_posix()
            selector = symbol.selectors
            if (
                compound.id in selector.compound_ids
                or compound.qualified_name in selector.qualified_names
                or any(source.startswith(prefix) for prefix in selector.source_prefixes)
            ):
                matches.append(compound)
        if not matches:
            raise legacy.DocumentationError(
                f"profile {profile.id} expected symbol {symbol.key} was not found"
            )
        if len(matches) > 1:
            names = ", ".join(item.qualified_name for item in matches)
            raise legacy.DocumentationError(
                f"profile {profile.id} selector for {symbol.key} is ambiguous: {names}"
            )
        compound = matches[0]
        if compound.qualified_name != symbol.qualified_name:
            raise legacy.DocumentationError(
                f"profile {profile.id} canonical identity mismatch for {symbol.key}: "
                f"configured {symbol.qualified_name}, extracted {compound.qualified_name}"
            )
        if compound.id in symbols_by_compound:
            other = symbols_by_compound[compound.id]
            raise legacy.DocumentationError(
                f"profile {profile.id} duplicate canonical mapping for {compound.qualified_name}: "
                f"{other.key}, {symbol.key}"
            )
        symbols_by_key[symbol.key.casefold()] = compound
        symbols_by_compound[compound.id] = symbol
    unexpected = sorted(
        compound.qualified_name for compound in compounds if compound.id not in symbols_by_compound
    )
    if unexpected:
        raise legacy.DocumentationError(
            f"profile {profile.id} inventory has unconfigured exported symbols: " + ", ".join(unexpected)
        )
    return AssignedProfile(
        profile=profile,
        compounds=tuple(compounds),
        symbols_by_key=symbols_by_key,
        symbols_by_compound=symbols_by_compound,
    )


def _api_path(profile: PublicationProfile, symbol: SymbolConfig) -> Path:
    return profile.canonical_root / "api" / symbol.api_scope / f"{symbol.key}.md"


class PublicationLinkResolver:
    def __init__(self, assigned: AssignedProfile) -> None:
        self.assigned = assigned
        self.compounds = {item.id: item for item in assigned.compounds}
        self.members: dict[str, tuple[legacy.Compound, legacy.Member]] = {}
        for compound in assigned.compounds:
            for member in compound.members:
                self.members[member.id] = (compound, member)

    def link(self, refid: str, source_page: Path) -> str | None:
        compound = self.compounds.get(refid)
        if compound is not None:
            symbol = self.assigned.symbols_by_compound[compound.id]
            return legacy._relative_link(source_page, _api_path(self.assigned.profile, symbol))
        member = self.members.get(refid)
        if member is not None:
            owner, value = member
            symbol = self.assigned.symbols_by_compound[owner.id]
            return legacy._relative_link(
                source_page,
                _api_path(self.assigned.profile, symbol),
                f"member-{legacy._slug(value.id)}",
            )
        return None


def _config_sha(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def _profile_provenance(profile: PublicationProfile, page: Path) -> str:
    evidence = legacy._relative_link(page, profile.inventory_evidence)
    return (
        f"Doxygen {profile.doxygen_version}; profile `{profile.implementation_unit}/{profile.id}`; "
        f"[compiler/native inventory evidence]({evidence}); LF-normalized config SHA-256 "
        f"`{_config_sha(profile.path)}`; Doxyfile SHA-256 `{legacy._sha256(profile.doxyfile)}`. "
        f"Regenerate with `{profile.reproduce_command}`. Doxygen supplies the configured structural "
        "projection; it does not establish compiler-complete semantics."
    )


def _coverage_lines(profile: PublicationProfile) -> list[str]:
    lines = ["**Included source scope:** " + ", ".join(f"`{item}`" for item in profile.included_coverage)]
    if profile.excluded_coverage:
        lines.extend(["", "**Declared exclusions:**", ""])
        lines.extend(f"- `{item.scope}` — {item.reason}" for item in profile.excluded_coverage)
    else:
        lines.extend(["", "**Declared exclusions:** None."])
    lines.extend(
        [
            "",
            "**Generic extraction boundary:** public/protected `class`, `interface`, and `struct` compounds and their public/protected members.",
            "",
            "**Recorded parser limitations:**",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in profile.parser_limitations)
    return lines


def _architecture_maps(config: PublicationConfig) -> tuple[dict[str, ArchitectureTarget], dict[tuple[str, str], ArchitectureTarget]]:
    containers = {item.id.casefold(): item for item in config.containers}
    components = {
        ((item.container_id or "").casefold(), item.id.casefold()): item for item in config.components
    }
    return containers, components


def _bound_view_paths(
    config: PublicationConfig, profile: PublicationProfile, symbol_key: str
) -> list[tuple[str, Path]]:
    containers, components = _architecture_maps(config)
    result: dict[str, tuple[str, Path]] = {}
    for binding in profile.bindings:
        if binding.symbol_key.casefold() != symbol_key.casefold():
            continue
        container = containers[binding.container_id.casefold()]
        container_page = container.output_dir / "code.md"
        result[str(container_page).casefold()] = (container.title, container_page)
        if binding.role in INTERFACE_ROLES:
            interface_page = container.output_dir / "_code-views" / "interfaces.md"
            result[str(interface_page).casefold()] = (
                f"{container.title} interfaces", interface_page
            )
        if binding.component_id:
            component = components[(binding.container_id.casefold(), binding.component_id.casefold())]
            component_page = component.output_dir / "code.md"
            result[str(component_page).casefold()] = (component.title, component_page)
    return sorted(result.values(), key=lambda item: (item[0].casefold(), str(item[1]).casefold()))


def _render_api(
    config: PublicationConfig,
    assigned: AssignedProfile,
    symbol: SymbolConfig,
    compound: legacy.Compound,
    resolver: PublicationLinkResolver,
) -> str:
    profile = assigned.profile
    page = _api_path(profile, symbol)
    profile_index = profile.canonical_root / "index.md"
    lines = [
        legacy.GENERATED_MARKER,
        "",
        f"# `{compound.qualified_name}`",
        "",
        f"[Documentation profile]({legacy._relative_link(page, profile_index)})",
        "",
        f"**Canonical symbol key:** `{symbol.key}`",
        "",
        f"**Kind:** `{compound.kind}`",
        "",
        f"**Language:** `{compound.language or 'unspecified'}`",
        "",
        f"**Source:** {legacy._source_link(profile, page, compound.location)}",
        "",
        "## Summary",
        "",
        legacy._description(compound.brief, resolver, page, profile.code_fence_language)
        or "No summary was authored.",
    ]
    detail = legacy._description(compound.detail, resolver, page, profile.code_fence_language)
    if detail:
        lines.extend(["", "## Remarks", "", detail])
    if compound.base_ids:
        lines.extend(["", "## Relationships", ""])
        by_id = {item.id: item for item in assigned.compounds}
        for base_id in compound.base_ids:
            base = by_id.get(base_id)
            if base is None:
                raise legacy.DocumentationError(
                    f"unresolved base relationship {base_id} for {compound.qualified_name}"
                )
            relation = "implements" if base.kind == "interface" else "inherits"
            lines.append(
                f"- {relation} [`{base.qualified_name}`]({resolver.link(base_id, page)}) "
                "(Doxygen base relationship)"
            )
    if compound.members:
        lines.extend(["", "## Members", ""])
    for member in compound.members:
        signature = (member.definition + member.args).strip() or member.name
        lines.extend(
            [
                f'<a id="member-{legacy._slug(member.id)}"></a>',
                "",
                f"### `{member.name}`",
                "",
                f"```{profile.code_fence_language}\n{signature}\n```",
                "",
                f"**Kind:** `{member.kind}`",
                "",
                f"**Source:** {legacy._source_link(profile, page, member.location)}",
                "",
                legacy._description(member.brief, resolver, page, profile.code_fence_language)
                or "No summary was authored.",
            ]
        )
        member_detail = legacy._description(
            member.detail, resolver, page, profile.code_fence_language
        )
        if member_detail:
            lines.extend(["", member_detail])
    lines.extend(["", "## All bound views", ""])
    views = _bound_view_paths(config, profile, symbol.key)
    if views:
        lines.extend(
            f"- [{title}]({legacy._relative_link(page, target)})" for title, target in views
        )
    else:
        lines.append("No architecture view binding is configured for this symbol.")
    lines.extend(["", "## Coverage", "", *_coverage_lines(profile)])
    lines.extend(["", "## Provenance", "", _profile_provenance(profile, page), ""])
    return legacy._with_contents("\n".join(lines))


def _render_profile_index(assigned: AssignedProfile) -> str:
    profile = assigned.profile
    page = profile.canonical_root / "index.md"
    resolver = PublicationLinkResolver(assigned)
    lines = [
        legacy.GENERATED_MARKER,
        "",
        f"# {profile.title}",
        "",
        "This is the canonical API index for one validated implementation-unit/documentation-profile context.",
        "",
        "## Canonical symbols",
        "",
        "| Symbol | Kind | Summary | Source |",
        "| --- | --- | --- | --- |",
    ]
    for symbol in sorted(profile.symbols, key=lambda item: item.key.casefold()):
        compound = assigned.symbols_by_key[symbol.key.casefold()]
        summary = legacy._description(compound.brief, resolver, page, profile.code_fence_language).replace("\n", " ")
        lines.append(
            f"| [`{compound.qualified_name}`]({legacy._relative_link(page, _api_path(profile, symbol))}) "
            f"| `{compound.kind}` | {summary} | {legacy._source_link(profile, page, compound.location)} |"
        )
    lines.extend(["", "## Coverage", "", *_coverage_lines(profile)])
    lines.extend(["", "## Provenance", "", _profile_provenance(profile, page), ""])
    return legacy._with_contents("\n".join(lines))


def _binding_rows(
    page: Path,
    config: PublicationConfig,
    assigned_profiles: tuple[AssignedProfile, ...],
    bindings: list[tuple[AssignedProfile, Binding]],
) -> list[str]:
    rows = ["| Profile | Role | Symbol | Purpose | Source |", "| --- | --- | --- | --- | --- |"]
    for assigned, binding in sorted(
        bindings,
        key=lambda item: (
            item[0].profile.implementation_unit.casefold(), item[0].profile.id.casefold(),
            item[1].role, item[1].symbol_key.casefold(), item[1].component_id or "",
        ),
    ):
        profile = assigned.profile
        symbol = next(item for item in profile.symbols if item.key.casefold() == binding.symbol_key.casefold())
        compound = assigned.symbols_by_key[symbol.key.casefold()]
        resolver = PublicationLinkResolver(assigned)
        purpose = binding.narrative or legacy._description(
            compound.brief, resolver, page, profile.code_fence_language
        ).replace("\n", " ")
        source = legacy._source_link(profile, page, compound.location)
        rows.append(
            f"| `{profile.implementation_unit}/{profile.id}` | `{binding.role}` | "
            f"[`{compound.qualified_name}`]({legacy._relative_link(page, _api_path(profile, symbol))}) "
            f"| {purpose} | {source} |"
        )
    return rows


def _profile_context_lines(
    page: Path,
    bindings: list[tuple[AssignedProfile, Binding]],
) -> list[str]:
    unique: dict[tuple[str, str], PublicationProfile] = {}
    for assigned, _ in bindings:
        profile = assigned.profile
        unique[(profile.implementation_unit.casefold(), profile.id.casefold())] = profile
    lines = [
        "## Profile coverage and provenance",
        "",
        "Purpose text comes from explicit binding narrative when configured, otherwise from source-authored documentation. Exact signatures remain only on canonical API pages.",
    ]
    for profile in sorted(unique.values(), key=lambda item: (item.implementation_unit.casefold(), item.id.casefold())):
        lines.extend(
            [
                "",
                f"### `{profile.implementation_unit}/{profile.id}`",
                "",
                *_coverage_lines(profile),
                "",
                _profile_provenance(profile, page),
            ]
        )
    return lines


def _render_container_view(
    config: PublicationConfig,
    assigned_profiles: tuple[AssignedProfile, ...],
    container: ArchitectureTarget,
    bindings: list[tuple[AssignedProfile, Binding]],
) -> str:
    page = container.output_dir / "code.md"
    lines = [
        legacy.GENERATED_MARKER,
        "",
        f"# {container.title} code documentation",
        "",
        f"[Container architecture]({legacy._relative_link(page, container.architecture_page)})",
        "",
        "This entry view links configured canonical API profiles; it does not claim complete runtime coverage.",
        "",
        "## Participating profiles and symbols",
        "",
        *_binding_rows(page, config, assigned_profiles, bindings),
        "",
        "## Component navigation",
        "",
    ]
    component_bindings = [item for item in bindings if item[1].component_id]
    if component_bindings:
        _, components = _architecture_maps(config)
        seen: set[str] = set()
        for _, binding in sorted(component_bindings, key=lambda item: (item[1].component_id or "").casefold()):
            key = (binding.component_id or "").casefold()
            if key in seen:
                continue
            seen.add(key)
            component = components[(container.id.casefold(), key)]
            lines.append(
                f"- [{component.title}]({legacy._relative_link(page, component.output_dir / 'code.md')})"
            )
    else:
        lines.append("No approved component decomposition is configured for this published scope.")
    if any(item[1].role in INTERFACE_ROLES for item in bindings):
        lines.extend(
            [
                "",
                "## Interface navigation",
                "",
                f"- [Architectural interfaces]({legacy._relative_link(page, container.output_dir / '_code-views' / 'interfaces.md')})",
            ]
        )
    lines.extend(["", *_profile_context_lines(page, bindings), ""])
    return legacy._with_contents("\n".join(lines))


def _render_component_view(
    config: PublicationConfig,
    assigned_profiles: tuple[AssignedProfile, ...],
    component: ArchitectureTarget,
    bindings: list[tuple[AssignedProfile, Binding]],
) -> str:
    page = component.output_dir / "code.md"
    lines = [
        legacy.GENERATED_MARKER,
        "",
        f"# {component.title} code documentation",
        "",
        f"[Component architecture]({legacy._relative_link(page, component.architecture_page)})",
        "",
        "This filtered view carries architectural guidance and links exact signatures to canonical API pages.",
        "",
        "## Bound implementation and ports",
        "",
        *_binding_rows(page, config, assigned_profiles, bindings),
        "",
    ]
    lines.extend(["", *_profile_context_lines(page, bindings), ""])
    return legacy._with_contents("\n".join(lines))


def _render_interfaces_view(
    config: PublicationConfig,
    assigned_profiles: tuple[AssignedProfile, ...],
    container: ArchitectureTarget,
    bindings: list[tuple[AssignedProfile, Binding]],
) -> str:
    page = container.output_dir / "_code-views" / "interfaces.md"
    lines = [
        legacy.GENERATED_MARKER,
        "",
        f"# {container.title} architectural interfaces",
        "",
        f"[Container architecture]({legacy._relative_link(page, container.architecture_page)}) | "
        f"[Container code entry]({legacy._relative_link(page, container.output_dir / 'code.md')})",
        "",
        "Source visibility and architectural interface scope are separate. These bindings are explicit configuration, not access-modifier inference.",
    ]
    headings = [
        ("provided-interface", "external-runtime", "Provided external runtime ports"),
        ("consumed-interface", "external-runtime", "Consumed external runtime ports"),
        ("provided-interface", "internal-component", "Provided internal component ports"),
        ("consumed-interface", "internal-component", "Consumed internal component ports"),
    ]
    for role, scope, heading in headings:
        selected = [item for item in bindings if item[1].role == role and item[1].interface_scope == scope]
        lines.extend(["", f"## {heading}", ""])
        if selected:
            lines.extend(_binding_rows(page, config, assigned_profiles, selected))
        else:
            lines.append("No bindings are configured for this category.")
    lines.extend(["", *_profile_context_lines(page, bindings), ""])
    return legacy._with_contents("\n".join(lines))


def _render_stub(profile: PublicationProfile, stub: CompatibilityStub, symbol: SymbolConfig) -> str:
    canonical = _api_path(profile, symbol)
    return legacy._with_contents("\n".join(
        [
            legacy.GENERATED_MARKER,
            "",
            "# API reference moved",
            "",
            "This compatibility page contains no API content. The canonical symbol page moved to:",
            "",
            "## Canonical location",
            "",
            f"- [`{symbol.qualified_name}`]({legacy._relative_link(stub.path, canonical)})",
            "",
            "## Profile coverage and provenance",
            "",
            f"**Implementation unit/profile:** `{profile.implementation_unit}/{profile.id}`",
            "",
            *_coverage_lines(profile),
            "",
            _profile_provenance(profile, stub.path),
            "",
        ]
    ))


def _clean(content: str) -> str:
    lines: list[str] = []
    fenced = False
    for line in content.replace("\r\n", "\n").splitlines():
        if line.startswith("```"):
            fenced = not fenced
        line = line.rstrip()
        if not fenced and not line and lines and not lines[-1]:
            continue
        lines.append(line)
    return "\n".join(lines).rstrip() + "\n"


def render_publication_outputs(config: PublicationConfig) -> dict[Path, str]:
    assigned_profiles = tuple(_select_compounds(profile) for profile in config.profiles)
    outputs: dict[Path, str] = {}

    def add(path: Path, content: str) -> None:
        collision = next((item for item in outputs if str(item).casefold() == str(path).casefold()), None)
        if collision is not None:
            raise legacy.DocumentationError(f"colliding generated output paths: {collision} and {path}")
        outputs[path] = _clean(content)

    for assigned in assigned_profiles:
        profile = assigned.profile
        add(profile.canonical_root / "index.md", _render_profile_index(assigned))
        resolver = PublicationLinkResolver(assigned)
        for symbol in profile.symbols:
            compound = assigned.symbols_by_key[symbol.key.casefold()]
            add(_api_path(profile, symbol), _render_api(config, assigned, symbol, compound, resolver))
        for stub in profile.compatibility_stubs:
            symbol = next(item for item in profile.symbols if item.key.casefold() == stub.symbol_key.casefold())
            add(stub.path, _render_stub(profile, stub, symbol))

    containers, components = _architecture_maps(config)
    for container in config.containers:
        bindings = [
            (assigned, binding)
            for assigned in assigned_profiles
            for binding in assigned.profile.bindings
            if binding.container_id.casefold() == container.id.casefold()
        ]
        if not bindings:
            continue
        add(container.output_dir / "code.md", _render_container_view(config, assigned_profiles, container, bindings))
        interface_bindings = [item for item in bindings if item[1].role in INTERFACE_ROLES]
        if interface_bindings:
            add(
                container.output_dir / "_code-views" / "interfaces.md",
                _render_interfaces_view(config, assigned_profiles, container, interface_bindings),
            )
    for component in config.components:
        bindings = [
            (assigned, binding)
            for assigned in assigned_profiles
            for binding in assigned.profile.bindings
            if binding.container_id.casefold() == (component.container_id or "").casefold()
            and (binding.component_id or "").casefold() == component.id.casefold()
        ]
        if bindings:
            add(component.output_dir / "code.md", _render_component_view(config, assigned_profiles, component, bindings))
    return outputs


def _owned_generated_files(config: PublicationConfig) -> set[Path]:
    candidates: set[Path] = set()
    for profile in config.profiles:
        if profile.canonical_root.exists():
            candidates.update(profile.canonical_root.rglob("*.md"))
        for root in profile.legacy_stub_roots:
            if root.exists():
                candidates.update(root.rglob("*.md"))
    for container in config.containers:
        candidates.add(container.output_dir / "code.md")
        interface_root = container.output_dir / "_code-views"
        if interface_root.exists():
            candidates.update(interface_root.rglob("*.md"))
    for component in config.components:
        candidates.add(component.output_dir / "code.md")
    result: set[Path] = set()
    for path in candidates:
        if not path.is_file():
            continue
        first = path.read_text(encoding="utf-8").splitlines()[0:1]
        if first and first[0] == legacy.GENERATED_MARKER:
            result.add(path.resolve())
    return result


def synchronize_publication(config: PublicationConfig, check: bool) -> list[str]:
    outputs = render_publication_outputs(config)
    for path in outputs:
        if path.is_file():
            first = path.read_text(encoding="utf-8").splitlines()[0:1]
            if not first or first[0] != legacy.GENERATED_MARKER:
                raise legacy.DocumentationError(
                    f"refusing to replace a file not owned by this generator: {path}"
                )
    broken = legacy._broken_links(outputs)
    if broken:
        raise legacy.DocumentationError("broken generated links:\n" + "\n".join(broken))
    expected = {path.resolve() for path in outputs}
    existing = _owned_generated_files(config)
    orphans = sorted(existing - expected)
    stale = sorted(
        path for path, content in outputs.items()
        if not path.is_file() or path.read_text(encoding="utf-8") != content
    )
    if check:
        return [*(f"stale generated output: {path}" for path in stale),
                *(f"orphan generated output: {path}" for path in orphans)]
    messages: list[str] = []
    for path in orphans:
        path.unlink()
        messages.append(f"removed orphan: {path}")
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8", newline="\n")
            messages.append(f"wrote: {path}")
    return messages
