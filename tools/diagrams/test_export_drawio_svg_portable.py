"""Repository-neutral tests for the reusable Draw.io/SVG exporter."""

from __future__ import annotations

import html
from io import StringIO
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from contextlib import redirect_stderr, redirect_stdout

from tools.diagrams import export_drawio_svg as exporter


TEST_ARTIFACTS = exporter.ROOT / "artifacts"
TEST_ARTIFACTS.mkdir(exist_ok=True)


MODEL = """<mxfile><diagram><mxGraphModel pageWidth="200" pageHeight="100"><root>
<mxCell id="0"/><mxCell id="1" parent="0"/>
<UserObject id="first" label="First" link="child.svg"><mxCell vertex="1" parent="1" style="rounded=1;fillColor=#FFFFFF;strokeColor=#315B8A"><mxGeometry x="10" y="20" width="60" height="30" as="geometry"/></mxCell></UserObject>
<UserObject id="second" label="Second"><mxCell vertex="1" parent="1" style="fillColor=#FFFFFF;strokeColor=#315B8A"><mxGeometry x="120" y="20" width="60" height="30" as="geometry"/></mxCell></UserObject>
<mxCell id="edge" edge="1" source="first" target="second" value="uses" style="endArrow=block"><mxGeometry relative="1" as="geometry"/></mxCell>
</root></mxGraphModel></diagram></mxfile>"""


def native_svg(source: Path, anchors: tuple[str, ...]) -> bytes:
    content = html.escape(source.read_text(encoding="utf-8"), quote=True)
    links = "".join(f'<a href="{link}" />' for link in anchors)
    return f'<svg xmlns="{exporter.SVG_NS}" content="{content}">{links}</svg>'.encode()


class PortableExporterTests(unittest.TestCase):
    def diagram(self, root: Path) -> Path:
        source = root / "design/c4/_diagrams/sample.drawio"
        source.parent.mkdir(parents=True)
        source.write_text(MODEL, encoding="utf-8")
        source.with_name("child.svg").write_text("<svg/>", encoding="utf-8")
        return source

    def test_check_native_styles_without_portable_rendering(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            source = self.diagram(Path(temporary))
            source.write_text(MODEL.replace("endArrow=block", "endArrow=block;entryPerimeter=0"), encoding="utf-8")
            output = source.with_suffix(".svg")
            output.write_bytes(native_svg(source, ("child.svg",)))
            original = output.read_bytes()
            arguments = sys.argv
            try:
                sys.argv = ["export_drawio_svg.py", "--check", str(source)]
                with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                    self.assertEqual(exporter.main(), 0)
            finally:
                sys.argv = arguments
            self.assertEqual(output.read_bytes(), original)
            with self.assertRaisesRegex(ValueError, "unsupported Draw.io styles"):
                exporter.render(source)

    def test_check_rejects_stale_or_unlinked_native_styles(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            source = self.diagram(Path(temporary))
            source.write_text(MODEL.replace("endArrow=block", "endArrow=block;entryPerimeter=0"), encoding="utf-8")
            output = source.with_suffix(".svg")
            arguments = sys.argv
            try:
                sys.argv = ["export_drawio_svg.py", "--check", str(source)]
                for content in (native_svg(source, ()), native_svg(source, ("child.svg",)).replace(b'label=&quot;First&quot;', b'label=&quot;Stale&quot;')):
                    with self.subTest(content=content[:70]):
                        output.write_bytes(content)
                        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                            self.assertEqual(exporter.main(), 1)
            finally:
                sys.argv = arguments

    def test_discovery_render_and_check_are_root_neutral(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            root = Path(temporary)
            source = self.diagram(root)
            self.assertEqual(exporter.discover(root), (source,))
            expected = exporter.render(source)
            source.with_suffix(".svg").write_bytes(expected)
            self.assertTrue(exporter.is_current_svg(source, source.with_suffix(".svg"), expected))

    def test_matching_native_export_requires_drawio_links(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            source = self.diagram(Path(temporary))
            output = source.with_suffix(".svg")
            output.write_bytes(native_svg(source, ()))
            self.assertFalse(exporter.is_current_svg(source, output, exporter.render(source)))
            output.write_bytes(native_svg(source, ("child.svg",)))
            self.assertTrue(exporter.is_current_svg(source, output, exporter.render(source)))

    def test_stale_or_malformed_native_content_is_rejected(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            source = self.diagram(Path(temporary))
            output = source.with_suffix(".svg")
            output.write_bytes(native_svg(source, ("child.svg",)).replace(b'label=&quot;First&quot;', b'label=&quot;Stale&quot;'))
            self.assertFalse(exporter.is_current_svg(source, output, exporter.render(source)))
            output.write_text(f'<svg xmlns="{exporter.SVG_NS}" content="not XML"/>', encoding="utf-8")
            self.assertFalse(exporter.is_current_svg(source, output, exporter.render(source)))

    def test_native_content_on_a_non_svg_root_is_rejected(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            source = self.diagram(Path(temporary))
            output = source.with_suffix(".svg")
            native = native_svg(source, ("child.svg",)).replace(b"<svg ", b"<not-svg ", 1)
            output.write_bytes(native.replace(b"</svg>", b"</not-svg>"))
            self.assertFalse(exporter.is_current_svg(source, output, exporter.render(source)))

    def test_check_does_not_rewrite_native_export(self) -> None:
        with TemporaryDirectory(dir=TEST_ARTIFACTS) as temporary:
            source = self.diagram(Path(temporary))
            output = source.with_suffix(".svg")
            output.write_bytes(native_svg(source, ("child.svg",)))
            original, sources, arguments = output.read_bytes(), exporter.SOURCES, sys.argv
            try:
                exporter.SOURCES = (source,)
                sys.argv = ["export_drawio_svg.py", "--check"]
                with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                    self.assertEqual(exporter.main(), 0)
            finally:
                exporter.SOURCES, sys.argv = sources, arguments
            self.assertEqual(output.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
