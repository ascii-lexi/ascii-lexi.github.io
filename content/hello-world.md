title: Hello, World
date: 2026-07-18
summary: The first post. Setting up a static blog without losing my mind to CSS.

## Why I built this

I'm a CS major and I've wanted a blog for years. Every time I tried, I got stuck
fighting a templating language instead of writing anything.

This generator has exactly one idea: write Markdown, get a page. No Jinja loops
to memorize, no build system, no Node.

### The stack

- Python + `markdown` for the conversion
- Hand-written HTML/CSS templates (edit them like any other file)
- Zero JavaScript frameworks — a few lines of vanilla JS for the mobile menu and scrollspy

## How the sidebar works

The table of contents on the left isn't hand-written. It's generated from the
`##` and `###` headings in this exact file, using Python-Markdown's `toc`
extension. Add a heading, it shows up. Delete one, it disappears.

```python
MD = markdown.Markdown(extensions=["meta", "fenced_code", "toc"])
html = MD.convert(markdown_text)
toc = MD.toc_tokens
```

### Deploying it

Since the output is just static HTML/CSS/JS, you can push the `output/` folder
to GitHub Pages, Netlify, or any static host, no server required.

## What's next

More posts, and slowly tuning the six color variables at the top of
`style.css` until it feels like mine.
