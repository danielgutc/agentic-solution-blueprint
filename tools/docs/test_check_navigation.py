"""Focused, repository-neutral tests for Markdown navigation validation."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

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

    def test_short_design_pages_need_no_contents_but_still_check_links(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            for directory in ("foundation", "c4"):
                page = self.write(root, f"design/{directory}/short.md", "# Scope\n\n## Decision\n\nCurrent contract.\n")
                self.assertEqual(navigation.check(page, root), [])
                page.write_text(page.read_text() + "\n[Missing](missing.md)\n", encoding="utf-8")
                self.assertEqual(navigation.check(page, root), ["missing file: missing.md"])

    def test_contents_requirement_starts_above_eighty_nonblank_lines(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            content = "# Scope\n\n## Decision\n\n## Contract\n" + "Detail.\n" * 77
            page = self.write(root, "design/c4/page.md", content)
            self.assertEqual(navigation.check(page, root), [])
            page.write_text(content + "Another detail.\n", encoding="utf-8")
            self.assertEqual(navigation.check(page, root), ["missing second-level table of contents"])
            page.write_text(content + "\n## Table of contents\n\n- [Decision](#decision)\n- [Contract](#contract)\n", encoding="utf-8")
            self.assertEqual(navigation.check(page, root), [])

    def test_optional_contents_still_cover_every_section(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            for name in ("design/foundation/short.md", ".blueprint/templates/short.md"):
                page = self.write(root, name, "# Scope\n\n## Table of contents\n\n- [Decision](#decision)\n\n## Decision\n\n## Contract\n")
                self.assertEqual(navigation.check(page, root), ["missing contents link: Contract"])

    def test_long_single_section_or_fenced_example_needs_no_contents(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            for content in (
                "# Scope\n\n## Contract\n" + "Detail.\n" * 90,
                "# Scope\n\n## Decision\n\n## Contract\n\n```text\n" + "Example.\n" * 90 + "```\n",
            ):
                page = self.write(root, "design/c4/page.md", content)
                self.assertEqual(navigation.check(page, root), [])

    def test_inline_code_in_headings_remains_part_of_anchor(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            page = self.write(root, "design/c4/page.md", """# Page

## Table of contents

- [Configure Widget](#configure-widget)

## Configure `Widget`
""")
            self.assertEqual(navigation.check(page, root), [])


class DocumentationPolicyTests(unittest.TestCase):
    write = NavigationTests.write
    def configure(self, root: Path, extra: str = "") -> None:
        self.write(root, ".blueprint/blueprint.toml", '''
[paths]
product = "design/foundation/product.md"
requirements = "design/foundation/requirements.md"
task_tracker = "design/foundation/task.md"
c4 = "design/c4"
c4_system = "design/c4/system/system.md"
c4_system_containers = "design/c4/containers/system-containers.md"

[documentation]
authored_design_policy = "canonical-only"
authored_design_roots = ["design"]
canonical_code_index_pattern = "design/code/<implementation-unit>/<documentation-profile>/index.md"
canonical_api_reference_pattern = "design/code/<implementation-unit>/<documentation-profile>/api/<scope>/<stable-symbol-id>.md"
''' + extra)
        self.write(root, "design/foundation/requirements.md", "# Requirements\n")

    def issues(self, root: Path) -> list[str]:
        return [message for _, message in navigation.documentation_policy(root)]

    def test_unregistered_documents_are_rejected_regardless_of_name(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.configure(root)
            for name in ("design/foundation/verification.md", "design/c4/handoff.md", "design/notes/ordinary.md"):
                self.write(root, name, "# Notes\n")
            self.assertEqual(sum("unregistered authored design document" in issue for issue in self.issues(root)), 3)

    def test_canonical_owners_are_allowed_without_exceptions(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.configure(root)
            for name in ("design/foundation/product.md", "design/c4/system/system.md", "design/c4/containers/system-containers.md", "design/c4/containers/app/container.md", "design/c4/containers/app/components/capture/component.md"):
                self.write(root, name, "# Current contract\n")
            self.assertEqual(self.issues(root), [])

    def test_navigation_readmes_do_not_admit_arbitrary_report_directories(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.configure(root)
            self.write(root, "design/foundation/_diagrams/README.md", "# Diagram navigation\n")
            self.assertEqual(self.issues(root), [])
            self.write(root, "design/reports/README.md", "# A report\n")
            self.assertTrue(any("unregistered" in issue for issue in self.issues(root)))

    def test_navigation_discovers_registered_design_roots(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.configure(root)
            manifest = root / ".blueprint/blueprint.toml"
            manifest.write_text(manifest.read_text(encoding="utf-8").replace('"design"', '"specification"').replace('design/', 'specification/'), encoding="utf-8")
            page = self.write(root, "specification/foundation/product.md", "# Product\n\n[Missing](missing.md)\n")
            self.assertIn(page, navigation.discover(root))
            self.assertTrue(navigation.check(page, root))

    def test_current_approvals_are_allowed_but_chronological_logs_are_rejected(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.configure(root)
            page = self.write(root, "design/foundation/task.md", "# Work\n\n## Approvals\nApproved 2026-11-13 for the bounded slice.\n\n```markdown\n## 2026-11-12 retry\n```\n")
            self.assertEqual(self.issues(root), [])
            page.write_text("# Work\n\n## 2026-11-12 retry\n\n## Done recently\n", encoding="utf-8")
            self.assertEqual(sum("chronological" in issue for issue in self.issues(root)), 2)

    def test_generated_pages_need_registered_paths_and_generated_markers(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.configure(root, 'additional_generated_documents = ["design/c4/containers/ledger/schema.md"]\n')
            marker = "<!-- Generated source reference; do not edit. -->\n"
            self.write(root, "design/code/app/default/api/Assembly/Type.md", marker)
            self.write(root, "design/c4/containers/ledger/schema.md", marker)
            self.assertEqual(self.issues(root), [])
            self.write(root, "design/code/app/default/index.md", "# Handwritten notes\n")
            self.write(root, "design/foundation/evidence.md", marker)
            issues = self.issues(root)
            self.assertTrue(any("generated marker" in issue for issue in issues))
            self.assertTrue(any("unregistered authored design document" in issue for issue in issues))

    def test_narrow_exception_requires_an_existing_canonical_owner(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.configure(root, '''
[[documentation.additional_authored_documents]]
path = "design/foundation/protocol.md"
owner = "design/foundation/requirements.md"
reason = "Durable protocol detail cannot fit clearly in the owner."
review_trigger = "Remove or merge when the protocol is retired."
''')
            self.write(root, "design/foundation/protocol.md", "# Protocol\n")
            self.assertEqual(self.issues(root), [])
            (root / "design/foundation/requirements.md").unlink()
            self.assertTrue(any("canonical owner" in issue for issue in self.issues(root)))

    def test_wildcard_incomplete_duplicate_and_stale_exceptions_are_rejected(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            for extra in (
                'additional_authored_documents = [{path="design/*.md", owner="design/foundation/requirements.md", reason="Detail", review_trigger="Retirement"}]',
                'additional_authored_documents = [{path="design/missing.md", owner="design/foundation/requirements.md", reason="Detail"}]',
                'additional_authored_documents = [{path="design/missing.md", owner="design/foundation/requirements.md", reason="Detail", review_trigger="Retirement"}]',
                'additional_authored_documents = [{path="design/foundation/requirements.md", owner="design/foundation/requirements.md", reason="Detail", review_trigger="Retirement"}, {path="design/foundation/requirements.md", owner="design/foundation/requirements.md", reason="Detail", review_trigger="Retirement"}]',
            ):
                with self.subTest(extra=extra):
                    self.configure(root, extra)
                    self.assertTrue(self.issues(root))

    def test_explicit_navigation_inputs_do_not_bypass_the_policy(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            self.configure(root)
            self.write(root, "README.md", "# Home\n")
            self.write(root, "design/foundation/run-report.md", "# Run\n")
            with patch("sys.argv", ["check_navigation", "--root", str(root), "README.md"]), redirect_stderr(StringIO()), redirect_stdout(StringIO()):
                self.assertEqual(navigation.main(), 1)

    def test_invalid_configuration_cannot_disable_the_guard(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            for content in ('[documentation\n', '[documentation]\nauthored_design_policy="off"', '[documentation]\nauthored_design_policy="canonical-only"\nauthored_design_roots=["../other"]'):
                with self.subTest(content=content):
                    self.write(root, ".blueprint/blueprint.toml", content)
                    self.assertTrue(self.issues(root))


if __name__ == "__main__":
    unittest.main()
