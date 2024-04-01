from flask import Flask, render_template, render_template_string, Response
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
import sys
import os
import markdown2
from flask_frozen import Freezer
import feed


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = [".md"]


def prerender_jinja(text):
    text = markdown2.markdown(
        text,
        extras=[
            "codehilite",
            "header-ids",
            "code-friendly",
            "fenced-code-blocks",
            "break-on-newline",
            "cuddled-lists",
            "footnotes",
            # "header-ids",
            "metadata",
            "numbering",
            "smarty-pants",
            "spoiler",
            "strike",
            "toc",
            "tables",
            "task_list",
        ],
    )
    return pygmented_markdown(render_template_string(text))


FLATPAGES_HTML_RENDERER = prerender_jinja
FREEZER_DEFAULT_MIMETYPE = "application/octet-stream"
FREEZER_RELATIVE_URLS = True


app = Flask(__name__)

app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

posts = [page for page in list(pages)][:-1]


@app.route("site/")
def home_page():
    return render_template("index.html", the_title="Surya")


@app.route("site/blog/")
def blog_page():
    return render_template("blog.html", pages=posts, tag="all"), {
        "Content-Type": "text/html; charset=utf-8"
    }


@app.route("site/blog/<path:path>.html")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page), {
        "Content-Type": "text/html; charset=utf-8"
    }


@app.errorhandler(404)
def page_404(e):
    return render_template("404.html"), 404


@app.route("site/blog/feed.xml")
def feed_generator():
    feed_cont = feed.feed_gen(pages)
    return Response(feed_cont, mimetype="text/xml")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)
