# Draw.io SVG exporter

`export_drawio_svg.py` renders the supported simple Draw.io XML subset to a
sibling SVG and checks freshness without requiring the desktop editor.

```powershell
python tools/diagrams/export_drawio_svg.py --check
python tools/diagrams/export_drawio_svg.py --root C:\work\another-repository --check
python tools/diagrams/export_drawio_svg.py --root C:\work\another-repository design/c4/_diagrams/view.drawio
```

With no explicit sources the tool discovers `*.drawio` files below an existing
`design/` directory. A repository with no such files succeeds with zero pairs;
an explicit missing source fails. `--check` never writes SVGs. It accepts either
the deterministic renderer bytes or a native Draw.io SVG only when its embedded
model canonically matches the source and every source drill-down link is present
in an SVG anchor.

Native freshness validation reads source links directly from XML and does not
apply portable rendering style limits. Native-only geometry/styles are accepted
only with a matching embedded source and complete anchors; a stale or unlinked
native export fails. Export mode still rejects unsupported styles rather than
rendering them approximately. This check preserves native editor layout.
