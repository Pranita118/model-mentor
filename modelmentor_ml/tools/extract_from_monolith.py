"""
One-time extractor: reads mm_fixed__4_ (4).html and builds Flask app assets.
Line numbers match the source file as of extraction (1-based inclusive).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(r"C:\Users\Pranita Kumbhar\Downloads\mm_fixed__4_ (4).html")

# 1-based line slices (inclusive)
CHART_DEFAULTS = (11, 30)
MAIN_CSS = (34, 3250)
BODY_HTML = (3253, 6822)
MAIN_JS = (6825, 24519)
RESP_CSS = (24522, 24804)
RESP_JS = (24807, 24824)


def slice_lines(text: str, start: int, end: int) -> str:
    lines = text.splitlines()
    return "\n".join(lines[start - 1 : end]) + "\n"


def main() -> None:
    raw = SRC.read_text(encoding="utf-8", errors="replace")

    static_css = ROOT / "app" / "static" / "css"
    static_js = ROOT / "app" / "static" / "js"
    templates = ROOT / "app" / "templates"
    for d in (static_css, static_js, templates):
        d.mkdir(parents=True, exist_ok=True)

    (static_js / "chart_defaults.js").write_text(slice_lines(raw, *CHART_DEFAULTS), encoding="utf-8")
    (static_css / "main.css").write_text(slice_lines(raw, *MAIN_CSS), encoding="utf-8")
    body = slice_lines(raw, *BODY_HTML)
    body = body.replace("<!-- Chat -->at -->", "<!-- Chat -->")
    (templates / "_body_content.html").write_text(body, encoding="utf-8")
    (static_js / "app.js").write_text(slice_lines(raw, *MAIN_JS), encoding="utf-8")
    (static_css / "responsive.css").write_text(slice_lines(raw, *RESP_CSS), encoding="utf-8")
    (static_js / "responsive.js").write_text(slice_lines(raw, *RESP_JS), encoding="utf-8")

    index = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
<title>ModelMentor — ML Analysis Platform v13</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&family=Fira+Code:wght@300;400;500&family=Fraunces:ital,opsz,wght@0,9..144,700;0,9..144,900;1,9..144,700&family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script src="{{ url_for('static', filename='js/chart_defaults.js') }}"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body>
{% include '_body_content.html' %}
<script src="{{ url_for('static', filename='js/app.js') }}"></script>
<link rel="stylesheet" href="{{ url_for('static', filename='css/responsive.css') }}">
<script src="{{ url_for('static', filename='js/responsive.js') }}"></script>
</body>
</html>
"""
    (templates / "index.html").write_text(index, encoding="utf-8")
    print("Extracted to", ROOT)


if __name__ == "__main__":
    main()
