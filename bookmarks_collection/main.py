import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

from objects import BookmarkRoot

current_dir = Path(__file__).parent
template_dir = str(current_dir / "templates")

env = Environment(
    loader=FileSystemLoader(template_dir), autoescape=select_autoescape(["html"])
)

index_template = env.get_template("index.html")


def main():
    with open("bookmarks-2019-07-20-simple.json") as f:
        bookmarks_json = json.load(f)
        bookmarks = BookmarkRoot(**bookmarks_json)
        toolbar_root: BookmarkRoot = next(
            bookmark
            for bookmark in bookmarks.children
            if bookmark.guid == "toolbar_____"
        )
        informatique_root: BookmarkRoot = next(
            bookmark
            for bookmark in toolbar_root.children
            if bookmark.guid == "4R2TUlyxQpbx"
        )
    with open("index.html", "w") as f:
        f.write(index_template.render(bookmarks_root=informatique_root))


if __name__ == "__main__":
    main()
