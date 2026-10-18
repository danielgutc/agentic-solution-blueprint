"""Check Markdown links and second-level contents lists in a repository.

With no inputs this checks an existing README.md and all existing Markdown
below design/. Pass --root for another repository, or explicit Markdown paths
for a narrower check. Fenced and inline code are examples, not navigation.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
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
    design = root / "design"
    if design.is_dir():
        paths.extend(sorted(design.rglob("*.md")))
    return paths


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
    if needs_contents(path, root):
        headings = HEADING.findall(content)
        contents = re.search(r"(?ms)^## Table of contents\s*\n(.*?)(?=^## |\Z)", content)
        if not contents:
            errors.append("missing second-level table of contents")
        else:
            toc_anchors = {item.split("#", 1)[1].rstrip(")") for item in LINK.findall(contents.group(1)) if "#" in item}
            for heading in headings:
                if heading != "Table of contents" and slug(heading) not in toc_anchors:
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this tool's repository)")
    parser.add_argument("paths", nargs="*", help="optional Markdown paths relative to --root")
    args = parser.parse_args()
    root = args.root.resolve()
    paths = selected_paths(root, args.paths)
    missing = [path for path in paths if not path.is_file()]
    failures = [(path, "selected Markdown file does not exist") for path in missing]
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
