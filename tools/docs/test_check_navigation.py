"""Focused, repository-neutral tests for Markdown navigation validation."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.docs import check_navigation as navigation


TEST_ARTIFACTS = navigation.ROOT / "artifacts"
TEST_ARTIFACTS.mkdir(exist_ok=True)


class NavigationTests(unittest.TestCase):
    def write(self, root: Path, name: str, content: str) -> Path:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_design_links_and_code_examples_are_checked_appropriately(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.write(root, "README.md", "# Home\n\n[Design](design/foundation/guide.md)\n")
            guide = self.write(root, "design/foundation/guide.md", """# Guide

## Table of contents

- [Use](#use)

## Use

[Home](../../README.md)

```markdown
[Example only](missing.md#missing)
```

Use `[inline](also-missing.md)` as literal syntax.
""")
            self.assertEqual(navigation.check(guide, root), [])
            self.assertEqual(navigation.discover(root), [root / "README.md", guide])

    def test_missing_link_and_anchor_are_reported(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            page = self.write(root, "design/c4/page.md", """# Page

## Table of contents

- [Known](#known)

## Known

[Missing](missing.md) and [Bad fragment](#unknown)
""")
            errors = navigation.check(page, root)
            self.assertIn("missing file: missing.md", errors)
            self.assertIn("missing anchor: #unknown", errors)

    def test_explicit_inputs_are_resolved_from_selected_root(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            page = self.write(root, "notes/one.md", "# One\n")
            self.assertEqual(navigation.selected_paths(root, ["notes/one.md"]), [page])

    def test_inline_code_in_headings_remains_part_of_anchor(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            page = self.write(root, "design/c4/page.md", """# Page

## Table of contents

- [Configure Widget](#configure-widget)

## Configure `Widget`
""")
            self.assertEqual(navigation.check(page, root), [])


if __name__ == "__main__":
    unittest.main()
