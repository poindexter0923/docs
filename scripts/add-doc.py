#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_JSON = ROOT / 'docs.json'

SAFE_TAGS = {
    'br','hr','em','strong','b','i','u','code','pre','kbd','s','sub','sup',
    'a','img','p','div','span','ul','ol','li','table','thead','tbody','tr','td','th',
    'blockquote','details','summary','h1','h2','h3','h4','h5','h6'
}

ANGLE_RE = re.compile(r'<([^>]+)>')
BRACE_RE = re.compile(r'\{([^}]+)\}')
DATE_RE = re.compile(r'\d{8}')


def die(msg: str) -> None:
    print(f'error: {msg}', file=sys.stderr)
    sys.exit(1)


def title_from_content(content: str, fallback: str) -> str:
    for line in content.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return fallback


def add_frontmatter(content: str, title: str) -> str:
    if content.lstrip().startswith('---'):
        return content
    return f"---\ntitle: {title}\n---\n\n" + content


def should_escape_tag(tag: str) -> bool:
    name = tag.strip()
    name = name[1:] if name.startswith('/') else name
    base = name.split()[0].lower()
    return base not in SAFE_TAGS


def escape_placeholders(content: str) -> str:
    # Escape angle-bracket placeholders like <Count>, <Policy._modelName>, <number>, etc.
    def repl_angle(match: re.Match) -> str:
        inner = match.group(1)
        if should_escape_tag(inner):
            return f'&lt;{inner}&gt;'
        return match.group(0)

    # Escape {Parameter}-style placeholders that MDX treats as expressions
    def repl_brace(match: re.Match) -> str:
        inner = match.group(1)
        return f'\\{{{inner}\\}}'

    content = ANGLE_RE.sub(repl_angle, content)
    content = BRACE_RE.sub(repl_brace, content)
    return content


def extract_date(path_str: str) -> int:
    m = DATE_RE.search(path_str)
    return int(m.group(0)) if m else -1


def sort_pages(pages):
    def key(p):
        d = extract_date(p)
        return (-d, p)
    pages.sort(key=key)


def update_navigation(doc_path: Path) -> None:
    if not DOCS_JSON.exists():
        die('docs.json not found')

    rel = doc_path.relative_to(ROOT).with_suffix('')
    rel_str = str(rel).replace('\\', '/')

    docs = json.loads(DOCS_JSON.read_text(encoding='utf-8'))
    groups = docs.get('navigation', {}).get('groups', [])

    top = rel.parts[0] if len(rel.parts) > 1 else 'Overview'

    # Find or create top-level group
    group_obj = None
    for g in groups:
        if g.get('group') == top:
            group_obj = g
            break
    if group_obj is None:
        group_obj = {"group": top, "pages": []}
        groups.append(group_obj)

    # Claim-Domain has subgroups by second-level directory
    if top == 'Claim-Domain' and len(rel.parts) >= 3:
        sub_name = rel.parts[1]
        pages = group_obj.get('pages', [])
        subgroup = None
        for item in pages:
            if isinstance(item, dict) and item.get('group') == sub_name:
                subgroup = item
                break
        if subgroup is None:
            subgroup = {"group": sub_name, "expanded": True, "pages": []}
            pages.append(subgroup)
        if rel_str not in subgroup['pages']:
            subgroup['pages'].append(rel_str)
            sort_pages(subgroup['pages'])
        group_obj['pages'] = pages
    else:
        pages = group_obj.get('pages', [])
        if rel_str not in pages:
            pages.append(rel_str)
            sort_pages(pages)
        group_obj['pages'] = pages

    docs['navigation']['groups'] = groups
    DOCS_JSON.write_text(json.dumps(docs, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    if len(sys.argv) != 2:
        die('usage: scripts/add-doc.py path/to/doc.md')

    doc = Path(sys.argv[1])
    if not doc.is_absolute():
        doc = (ROOT / doc).resolve()

    if not doc.exists() or doc.suffix.lower() != '.md':
        die('please provide an existing .md file')

    content = doc.read_text(encoding='utf-8')
    fallback_title = doc.stem.replace('_', ' ').replace('-', ' ')
    title = title_from_content(content, fallback_title)
    content = add_frontmatter(content, title)
    content = escape_placeholders(content)
    doc.write_text(content, encoding='utf-8')

    update_navigation(doc)
    print(f'updated: {doc}')


if __name__ == '__main__':
    main()
