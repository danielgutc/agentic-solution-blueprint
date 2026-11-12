"""Check Markdown links and second-level contents lists in a repository.

With no inputs this checks an existing README.md and all existing Markdown
below design/. Pass --root for another repository, or explicit Markdown paths
for a narrower check. Fenced and inline code are examples, not navigation.
"""

from __future__ import annotations

import argparse
from fnmatch import fnmatchcase
import re
import sys
import tomllib
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r"!?(?<!\\)\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"(?m)^## (.+?)\s*$")
FENCE = re.compile(r"(?ms)^(?:```|~~~).*?^(?:```|~~~)\s*$")
INLINE_CODE = re.compile(r"(?<!`)`[^`\n]*`")


def discover(root: Path) -> list[Path]:
    paths = []
    readme = root / "README.md"
    if readme.is_file():
        paths.append(readme)
    directories = {root / "design"}
    manifest = root / ".blueprint/blueprint.toml"
    if manifest.is_file():
        try:
            configuration = tomllib.loads(manifest.read_text(encoding="utf-8"))
            documentation = configuration.get("documentation", {})
            if not isinstance(documentation, dict):
                raise ValueError("documentation must be a table")
            for value in documentation.get("authored_design_roots", []):
                candidate = root / value
                candidate.resolve().relative_to(root.resolve())
                directories.add(candidate)
        except (OSError, TypeError, ValueError, tomllib.TOMLDecodeError):
            pass
    for directory in sorted(directories):
        if directory.is_dir():
            paths.extend(sorted(directory.rglob("*.md")))
    return list(dict.fromkeys(paths))


MARKDOWN = discover(ROOT)


def visible_markdown(value: str, *, links: bool = False) -> str:
    """Mask fenced examples; inline code is masked only while scanning links."""
    value = FENCE.sub(lambda match: "\n" * match.group(0).count("\n"), value)
    return INLINE_CODE.sub("", value) if links else value


def slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\[[^\]]+\]\([^)]+\)", "", value)
    value = re.sub(r"[^\w\s-]", "", value.lower(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", value.strip())


def anchors(path: Path) -> set[str]:
    content = visible_markdown(path.read_text(encoding="utf-8"))
    result: set[str] = set()
    seen: dict[str, int] = {}
    for _, heading in re.findall(r"(?m)^(#{1,6}) (.+?)\s*$", content):
        base = slug(heading)
        count = seen.get(base, 0)
        seen[base] = count + 1
        result.add(base if count == 0 else f"{base}-{count}")
    result.update(re.findall(r'''<a\s+id=["']([^"']+)["']\s*>''', content))
    return result


def needs_contents(path: Path, root: Path) -> bool:
    relative = path.resolve().relative_to(root.resolve()).as_posix()
    if path.name == "README.md" or "_diagrams" in path.parts:
        return False
    return relative.startswith("design/foundation/") or relative.startswith("design/c4/")


def check(path: Path, root: Path = ROOT) -> list[str]:
    content = visible_markdown(path.read_text(encoding="utf-8"))
    link_content = visible_markdown(path.read_text(encoding="utf-8"), links=True)
    errors = []
    headings = [heading for heading in HEADING.findall(content) if heading != "Table of contents"]
    contents = re.search(r"(?ms)^## Table of contents\s*\n(.*?)(?=^## |\Z)", content)
    long_page = sum(bool(line.strip()) for line in content.splitlines()) > 80
    if not contents and needs_contents(path, root) and long_page and len(headings) >= 2:
        errors.append("missing second-level table of contents")
    if contents:
        toc_anchors = {item.split("#", 1)[1].rstrip(")") for item in LINK.findall(contents.group(1)) if "#" in item}
        for heading in headings:
            if slug(heading) not in toc_anchors:
                errors.append(f"missing contents link: {heading}")
    for target in LINK.findall(link_content):
        target = target.strip().split(" ", 1)[0]
        if "://" in target or target.startswith(("mailto:", "codex:")):
            continue
        raw_path, _, fragment = target.partition("#")
        linked = (path.parent / unquote(raw_path)).resolve() if raw_path else path
        if linked.is_dir():
            continue
        if not linked.is_file():
            errors.append(f"missing file: {target}")
        elif fragment and linked.suffix.lower() == ".md" and unquote(fragment) not in anchors(linked):
            errors.append(f"missing anchor: {target}")
    return errors


def selected_paths(root: Path, values: list[str]) -> list[Path]:
    if not values:
        return discover(root)
    paths = []
    for value in values:
        candidate = Path(value)
        paths.append(candidate if candidate.is_absolute() else root / candidate)
    return paths


CANONICAL_DOCUMENT_KEYS = (
    "product", "mvp", "requirements", "technology", "design", "delivery",
    "task_tracker", "traceability", "implementation_readiness", "c4_system",
    "c4_system_containers",
)
GENERATED_DOCUMENT_KEYS = (
    "canonical_code_index_pattern", "canonical_api_reference_pattern",
    "container_code_view_pattern", "component_code_view_pattern",
    "interface_code_view_pattern", "legacy_component_api_reference_pattern",
)
HISTORY_HEADINGS = {
    "done recently", "execution history", "test run history",
    "verification history", "handoff history", "iteration history",
}


def relative_document_path(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("document paths must be nonempty repository-relative strings")
    candidate = PurePosixPath(value)
    if candidate.is_absolute() or ":" in value or "\\" in value or any(part in {".", ".."} for part in value.split("/")) or any(character in value for character in "*?["):
        raise ValueError(f"document paths must be exact repository-relative paths: {value}")
    return candidate.as_posix()


def document_matches(relative: str, pattern: str) -> bool:
    parts = PurePosixPath(relative).parts
    expected = PurePosixPath(pattern).parts
    return len(parts) == len(expected) and all(fnmatchcase(part, template) for part, template in zip(parts, expected))


def documentation_policy(root: Path) -> list[tuple[Path, str]]:
    manifest = root / ".blueprint/blueprint.toml"
    if not manifest.is_file():
        return []
    try:
        configuration = tomllib.loads(manifest.read_text(encoding="utf-8"))
        policy = configuration.get("documentation", {})
        if not isinstance(policy, dict):
            raise ValueError("documentation must be a table")
        if "authored_design_policy" not in policy:
            if any(key in policy for key in ("authored_design_roots", "additional_authored_documents", "additional_generated_documents")):
                raise ValueError("authored_design_policy is required with documentation ownership settings")
            return []
        if policy["authored_design_policy"] != "canonical-only":
            raise ValueError("authored_design_policy must be canonical-only")
        roots = policy.get("authored_design_roots")
        if not isinstance(roots, list) or not roots:
            raise ValueError("authored_design_roots must list the governed documentation directories")
        roots = [relative_document_path(value) for value in roots]
        registry = configuration.get("paths", {})
        if not isinstance(registry, dict):
            raise ValueError("paths must be a table")
        canonical = {relative_document_path(registry[key]) for key in CANONICAL_DOCUMENT_KEYS if key in registry}
        c4 = relative_document_path(registry.get("c4", "design/c4"))
        authored_patterns = (f"{c4}/containers/*/container.md", f"{c4}/containers/*/components/*/component.md")
        generated = [re.sub(r"<[^>]+>", "*", relative_document_path(policy[key])) for key in GENERATED_DOCUMENT_KEYS if key in policy]
        additional_generated = policy.get("additional_generated_documents", [])
        if not isinstance(additional_generated, list):
            raise ValueError("additional_generated_documents must list exact generated paths")
        generated.extend(relative_document_path(value) for value in additional_generated)

        def canonical_owner(relative: str) -> bool:
            return relative in canonical or any(document_matches(relative, pattern) for pattern in authored_patterns)

        exceptions = policy.get("additional_authored_documents", [])
        if not isinstance(exceptions, list):
            raise ValueError("additional_authored_documents must be an array of scoped exceptions")
        admitted = set()
        for entry in exceptions:
            if not isinstance(entry, dict) or set(entry) != {"path", "owner", "reason", "review_trigger"}:
                raise ValueError("each additional authored document requires path, owner, reason, and review_trigger")
            relative = relative_document_path(entry["path"])
            owner = relative_document_path(entry["owner"])
            if not relative.endswith(".md") or relative in admitted or canonical_owner(relative):
                raise ValueError(f"duplicate or unnecessary authored-document exception: {relative}")
            if not canonical_owner(owner) or not (root / owner).is_file():
                raise ValueError(f"additional document requires an existing canonical owner: {owner}")
            if not all(isinstance(entry[field], str) and entry[field].strip() for field in ("reason", "review_trigger")):
                raise ValueError(f"document exception requires a reason and review trigger: {relative}")
            if not (root / relative).is_file():
                raise ValueError(f"remove stale authored-document exception: {relative}")
            if not any(PurePosixPath(relative).is_relative_to(PurePosixPath(directory)) for directory in roots):
                raise ValueError(f"document exception is outside authored_design_roots: {relative}")
            admitted.add(relative)

        files = sorted({page for directory in roots for page in (root / directory).rglob("*.md")})
        owner_directories = {PurePosixPath(value).parent for value in canonical}
        owner_directories.update(PurePosixPath(page.relative_to(root).as_posix()).parent for page in files if canonical_owner(page.relative_to(root).as_posix()))
        owner_directories.update(PurePosixPath(value) for value in roots)
        owner_directories.add(PurePosixPath(c4))
        failures = []
        for page in files:
            try:
                page.resolve().relative_to(root.resolve())
            except ValueError:
                failures.append((page, "documentation must stay inside the repository"))
                continue
            relative = page.relative_to(root).as_posix()
            content = page.read_text(encoding="utf-8")
            if any(document_matches(relative, pattern) for pattern in generated):
                if not re.search(r"<!--\s*Generated\b", content[:512], re.IGNORECASE):
                    failures.append((page, "registered generated documentation requires a generated marker"))
                continue
            navigation = page.name == "README.md" and (PurePosixPath(relative).parent in owner_directories or (page.parent.name == "_diagrams" and PurePosixPath(relative).parent.parent in owner_directories))
            if not canonical_owner(relative) and relative not in admitted and not navigation:
                failures.append((page, "unregistered authored design document; update its canonical owner or register a scoped additional_authored_documents exception"))
            for heading in re.findall(r"(?m)^#{2,6}\s+(.+?)\s*$", visible_markdown(content)):
                if re.match(r"20\d{2}-\d{2}-\d{2}\b", heading) or heading.casefold() in HISTORY_HEADINGS:
                    failures.append((page, f"chronological documentation heading: {heading}; retain current decisions and approval dates in the owning record"))
        return failures
    except (OSError, ValueError, TypeError, tomllib.TOMLDecodeError) as error:
        return [(manifest, f"invalid documentation policy: {error}")]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this tool's repository)")
    parser.add_argument("paths", nargs="*", help="optional Markdown paths relative to --root")
    args = parser.parse_args()
    root = args.root.resolve()
    paths = selected_paths(root, args.paths)
    missing = [path for path in paths if not path.is_file()]
    failures = documentation_policy(root)
    failures.extend((path, "selected Markdown file does not exist") for path in missing)
    failures.extend((path, issue) for path in paths if path.is_file() for issue in check(path, root))
    for path, issue in failures:
        try:
            name = path.relative_to(root)
        except ValueError:
            name = path
        print(f"{name}: {issue}", file=sys.stderr)
    if failures:
        return 1
    print(f"Validated links and contents in {len(paths)} Markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
