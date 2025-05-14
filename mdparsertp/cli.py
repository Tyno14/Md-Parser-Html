import os
import re
import random
import sys
import argparse

footnotes = {}

def format_inline(text):
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', text)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'~~(.*?)~~', r'<del>\1</del>', text)
    text = re.sub(r'==(.+?)==', r'<mark>\1</mark>', text)
    text = re.sub(r'(\S+?)~(\S+?)~', r'\1<sub>\2</sub>', text)
    text = re.sub(r'(\S+?)\^(\S+?)\^', r'\1<sup>\2</sup>', text)
    text = re.sub(r'\[\^(\d+)\]', r'<sup id="ref-\1"><a href="#note-\1">[\1]</a></sup>', text)
    return text

def markdown_to_html(md):
    global footnotes
    html = []
    lines = md.strip().split('\n')
    in_ul = in_ol = in_code_block = in_table = in_deflist = False
    table_rows = []
    code_lang = ''
    page_title = "Document Markdown"
    footnotes = {}

    for line in lines:
        line = line.strip()

        footnote_match = re.match(r'\[\^(\d+)\]:\s+(.*)', line)
        if footnote_match:
            footnotes[footnote_match.group(1)] = footnote_match.group(2)
            continue

        def_match = re.match(r'^(.+)\n?:\s+(.*)', line)
        if def_match and not re.match(r'^- ', line):
            if not in_deflist:
                html.append("<dl>")
                in_deflist = True
            html.append(f"<dt>{format_inline(def_match.group(1))}</dt>")
            html.append(f"<dd>{format_inline(def_match.group(2))}</dd>")
            continue
        elif in_deflist and line == "":
            html.append("</dl>")
            in_deflist = False
            if page_title == "Document Markdown":
                match_title = re.match(r"#\s+(.*)", line)
                if match_title:
                    page_title = match_title.group(1)

        if re.fullmatch(r"-{3,}", line):
            if in_ul:
                html.append("</ul>")
            if in_ol:
                html.append("</ol>")
            in_ul = in_ol = False
            html.append("<hr>")
            continue

        code_match = re.match(r"^```(\w+)?", line)
        if code_match:
            if not in_code_block:
                code_lang = code_match.group(1) or ""
                html.append(f'<pre><code class="language-{code_lang}">')
                in_code_block = True
            else:
                html.append("</code></pre>")
                in_code_block = False
                code_lang = ''
            continue

        if in_code_block:
            html.append(line)
            continue

        if "|" in line and re.match(r"^\|?(.+\|)+.*$", line):
            table_rows.append(line)
            in_table = True
            continue
        elif in_table:
            html.append("<table>")
            headers = [h.strip() for h in table_rows[0].strip('|').split('|')]
            html.append("<thead><tr>" + ''.join(f"<th>{h}</th>" for h in headers) + "</tr></thead>")
            html.append("<tbody>")
            for row in table_rows[2:]:
                cols = [c.strip() for c in row.strip('|').split('|')]
                html.append("<tr>" + ''.join(f"<td>{c}</td>" for c in cols) + "</tr>")
            html.append("</tbody></table>")
            table_rows = []
            in_table = False
            match = re.match(r"^(#{1,6})\s+(.*)", line)
            if match:
                if in_ul:
                    html.append("</ul>")
                if in_ol:
                    html.append("</ol>")
                in_ul = in_ol = False
                level = len(match.group(1))
                content = format_inline(match.group(2))
                html.append(f"<h{level}>{content}</h{level}>")
                continue

        match = re.match(r"^(#{1,6})\s+(.*)", line)
        if match:
            if in_ul:
                html.append("</ul>")
            if in_ol:
                html.append("</ol>")
            in_ul = in_ol = False
            level = len(match.group(1))
            content = format_inline(match.group(2))
            html.append(f"<h{level}>{content}</h{level}>")
            continue

        if line.startswith("> "):
            if in_ul:
                html.append("</ul>")
            if in_ol:
                html.append("</ol>")
            in_ul = in_ol = False
            html.append(f"<blockquote>{format_inline(line[2:])}</blockquote>")
            continue

        if line.startswith("- "):
            if not in_ul:
                if in_ol:
                    html.append("</ol>")
                    in_ol = False
                html.append("<ul>")
                in_ul = True
            html.append(f"<li>{format_inline(line[2:])}</li>")
            continue

        if re.match(r"^\d+\.\s", line):
            if not in_ol:
                if in_ul:
                    html.append("</ul>")
                    in_ul = False
                html.append("<ol>")
                in_ol = True
            html.append(f"<li>{format_inline(re.sub(r'^\d+\.\s', '', line))}</li>")
            continue

        if in_ul:
            html.append("</ul>")
            in_ul = False
        if in_ol:
            html.append("</ol>")
            in_ol = False

        html.append(f"<p>{format_inline(line)}</p>" if line else "<p></p>")

    if in_ul:
        html.append("</ul>")
    if in_ol:
        html.append("</ol>")
    if in_deflist:
        html.append("</dl>")

    if footnotes:
        html.append("<hr><section id='footnotes'><h3>Notes</h3><ol>")
        for key, val in footnotes.items():
            html.append(f"<li id='note-{key}'>{val} <a href='#ref-{key}'>&uarr;</a></li>")
        html.append("</ol></section>")

    return '\n'.join(html), page_title

def generate_html(filename, body, title, theme, darkmode, output_dir):
    pastel_colors = {
        "green": "#a8d5ba",
        "blue": "#a7c7e7",
        "orange": "#ffcc99"
    }
    color = pastel_colors.get(theme, "#a8d5ba")
    bg = "#121212" if darkmode else "#ffffff"
    text = "#f5f5f5" if darkmode else "#333"

    css = f"""
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
html, body {{ height: 100%; overflow-x: hidden; }}
body {{
    font-family: 'Montserrat', sans-serif; font-size: 14px;
    margin: 0; padding: 0; background: {bg}; color: {text};
    display: flex; flex-direction: column; align-items: center;
}}
header, footer {{
    width: 100%; background-color: {color}; padding: 1rem; text-align: center;
}}
main {{ max-width: 1200px; width: 100%; padding: 2rem; flex: 1;}}
img {{ max-width: 100%; height: auto; }}
pre {{ overflow-x: auto; background: #2d2d2d; padding: 1em; }}
code {{ font-family: monospace; }}
blockquote {{
    border-left: 4px solid {color}; padding-left: 1em; color: {text}; margin: 1em 0;
}}
ul, ol {{ padding-left: 1.2em; }}
table {{
    border-collapse: collapse; margin: 1em 0; width: 100%;
}}
th, td {{
    border: 1px solid #ccc; padding: 0.5em; text-align: left; color: {text};
}}"""

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "style.css"), "w") as f:
        f.write(css)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
  <script>hljs.highlightAll();</script>
</head>
<body>
  <header><h1>{title}</h1></header>
  <main>
{body}
  </main>
  <footer><p>Généré avec ❤️ par mdparsertp</p></footer>
</body>
</html>"""

    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)

def create_index(pages, output_dir, theme, darkmode):
    links = "\n".join([f'<li><a href="{html}">{title}</a></li>' for html, title in pages])
    content = f"<h2>Sommaire</h2>\n<ul>\n{links}\n</ul>"
    generate_html("index.html", content, "Index", theme, darkmode, output_dir)

def main():
    parser = argparse.ArgumentParser(description="Convertisseur Markdown vers HTML.")
    parser.add_argument("markdown", help="Fichier ou dossier Markdown")
    parser.add_argument("--output", default="site", help="Dossier de sortie")
    parser.add_argument("--title", help="Titre forcé (single page)")
    parser.add_argument("--theme", choices=["blue", "green", "orange", "random"], default="random")
    parser.add_argument("--darkmode", action="store_true", help="Activer le mode sombre")
    parser.add_argument("--multipage", action="store_true", help="Convertir tous les .md d’un dossier")

    args = parser.parse_args()
    theme = random.choice(["blue", "green", "orange"]) if args.theme == "random" else args.theme

    if args.multipage and os.path.isdir(args.markdown):
        pages = []
        for fname in os.listdir(args.markdown):
            if fname.endswith(".md"):
                path = os.path.join(args.markdown, fname)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                body, title = markdown_to_html(content)
                html_name = os.path.splitext(fname)[0] + ".html"
                generate_html(html_name, body, title, theme, args.darkmode, args.output)
                pages.append((html_name, title))
        create_index(pages, args.output, theme, args.darkmode)
        print(f"✅ Multipage généré dans {args.output}")
    elif os.path.isfile(args.markdown):
        with open(args.markdown, "r", encoding="utf-8") as f:
            content = f.read()
        body, parsed_title = markdown_to_html(content)
        title = args.title or parsed_title
        generate_html("index.html", body, title, theme, args.darkmode, args.output)
        print(f"✅ Page générée dans {args.output}/index.html")
    else:
        print("❌ Fichier ou dossier invalide")

if __name__ == "__main__":
    main()
