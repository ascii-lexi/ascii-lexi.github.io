"""
toc_tree — builds article.toc_tree, a nested <li> tree of the article's
h2/h3 headings, for use in the sidebar navigation.

Pelican's built-in Markdown 'toc' extension only inserts a TOC where you
write [TOC] inline in the content. This plugin instead extracts the
already-rendered h2/h3 tags (with the ids the toc extension assigned them)
and reassembles them as a separate template variable, so the tree can live
in the fixed sidebar instead of inline in the post body.
"""

import re

from pelican import signals

_HEADING_RE = re.compile(r'<(h[23])\s+id="([^"]+)"[^>]*>(.*?)</\1>', re.S)
_TAG_RE = re.compile(r'<[^>]+>')


def _strip_tags(text):
    return _TAG_RE.sub("", text).strip()


def build_toc_tree(content):
    # Only articles/pages have rendered HTML content to scan.
    html = getattr(content, "_content", None)
    if not html:
        return

    matches = _HEADING_RE.findall(html)
    if not matches:
        content.toc_tree = ""
        return

    top_level = []
    current_h2 = None

    for tag, heading_id, inner_html in matches:
        label = _strip_tags(inner_html)
        if tag == "h2":
            current_h2 = {
                "li": f'<li><a href="#{heading_id}">{label}</a>',
                "children": [],
            }
            top_level.append(current_h2)
        else:  # h3 — nest under the most recent h2, or promote to top level
            child = f'<li><a href="#{heading_id}">{label}</a></li>'
            if current_h2 is None:
                top_level.append({"li": f'<li><a href="#{heading_id}">{label}</a>', "children": []})
            else:
                current_h2["children"].append(child)

    parts = []
    for node in top_level:
        li = node["li"]
        if node["children"]:
            li += '<ul class="tree">' + "".join(node["children"]) + "</ul>"
        li += "</li>"
        parts.append(li)

    content.toc_tree = "".join(parts)


def register():
    signals.content_object_init.connect(build_toc_tree)
