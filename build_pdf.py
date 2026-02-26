#!/usr/bin/env python3
"""Convert Clone whitepaper markdown to styled PDF using WeasyPrint."""

import markdown
from weasyprint import HTML

# Read markdown
with open("/root/obly/clone/whitepaper.md") as f:
    md_content = f.read()

# Convert to HTML
html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

# Full HTML with CSS
html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400&display=swap');

@page {{
    size: A4;
    margin: 2.2cm 2.5cm;
    @bottom-center {{
        content: counter(page);
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        color: #999;
    }}
}}

body {{
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 10.5pt;
    line-height: 1.7;
    color: #1a1a1a;
    font-weight: 400;
}}

h1 {{
    font-size: 28pt;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-top: 3cm;
    margin-bottom: 0.3cm;
    color: #000;
}}

h1 + p {{
    font-size: 10pt;
    color: #666;
    margin-bottom: 0.2cm;
}}

h2 {{
    font-size: 16pt;
    font-weight: 600;
    margin-top: 1.5cm;
    margin-bottom: 0.5cm;
    color: #000;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 0.2cm;
    page-break-after: avoid;
}}

h3 {{
    font-size: 12pt;
    font-weight: 600;
    margin-top: 0.8cm;
    margin-bottom: 0.3cm;
    color: #222;
    page-break-after: avoid;
}}

p {{
    margin-bottom: 0.4cm;
    text-align: justify;
    orphans: 3;
    widows: 3;
}}

strong {{
    font-weight: 600;
    color: #000;
}}

em {{
    font-style: italic;
}}

hr {{
    border: none;
    border-top: 1px solid #ddd;
    margin: 1cm 0;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 0.6cm 0;
    font-size: 9.5pt;
}}

th {{
    background: #f5f5f5;
    font-weight: 600;
    text-align: left;
    padding: 8px 12px;
    border-bottom: 2px solid #ddd;
}}

td {{
    padding: 7px 12px;
    border-bottom: 1px solid #eee;
    vertical-align: top;
}}

code {{
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 9pt;
    background: #f7f7f7;
    padding: 1px 4px;
    border-radius: 3px;
}}

pre {{
    background: #f7f7f7;
    border: 1px solid #e8e8e8;
    border-radius: 4px;
    padding: 14px 18px;
    font-size: 8.5pt;
    line-height: 1.5;
    overflow-x: auto;
    page-break-inside: avoid;
}}

pre code {{
    background: none;
    padding: 0;
}}

ul, ol {{
    margin-bottom: 0.4cm;
    padding-left: 1.2cm;
}}

li {{
    margin-bottom: 0.15cm;
}}

blockquote {{
    border-left: 3px solid #000;
    margin: 0.5cm 0;
    padding: 0.3cm 0.8cm;
    background: #fafafa;
    font-style: italic;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

HTML(string=html).write_pdf("/root/obly/clone/Clone_Whitepaper.pdf")
print("PDF generated successfully.")
