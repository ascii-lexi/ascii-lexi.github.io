#!/usr/bin/env python3
AUTHOR = "lexi"
SITENAME = "lexi@blog"
SITE_TAGLINE = "digital sovereignty, forever"
MENU_LABEL = "cd ~"

# Extra links shown at the bottom of the sidebar on every page.
# Add/remove/reorder freely — each needs a label and an href.
SITE_LINKS = [
    {"label": "GitHub", "href": "https://github.com/ascii-lexi"},
]

PATH = "content"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

THEME = "theme"
THEME_STATIC_DIR = "static"   # keeps asset URLs as static/... instead of theme/...

SITEURL = ""
RELATIVE_URLS = True

# Flat output: hello-world.md -> hello-world.html, same as the old build.py
ARTICLE_URL = "{slug}.html"
ARTICLE_SAVE_AS = "{slug}.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

INDEX_SAVE_AS = "index.html"
DIRECT_TEMPLATES = ["index"]   # skip auto-generated tag/category/archive index pages
DEFAULT_PAGINATION = False
CATEGORY_SAVE_AS = ""          # don't write per-category pages
AUTHOR_SAVE_AS = ""            # don't write per-author pages
TAG_SAVE_AS = ""               # don't write per-tag pages

# Skip feed generation — remove this block if you want RSS/Atom later
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.meta": {},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.toc": {"permalink": False},
    },
    "output_format": "html5",
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["toc_tree"]


def read_time(html):
    """Jinja filter: '{{ article.content|read_time }}' -> 'N min read'."""
    import re
    if not html:
        return "1 min read"
    words = len(re.sub(r"<[^>]+>", " ", html).split())
    minutes = max(1, round(words / 200))
    return f"{minutes} min read"


JINJA_FILTERS = {"read_time": read_time}
