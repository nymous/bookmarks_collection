from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from helpers import folder, entry, human_date, folder_or_entry
from bookmarks import BookmarkFolder

current_dir = Path(__file__).parent
template_dir = str(current_dir / "templates")

env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

env.filters["any"] = any
env.filters["human_date"] = human_date
env.tests["folder"] = folder
env.tests["entry"] = entry
env.tests["folder_or_entry"] = folder_or_entry

index_template = env.get_template("index.html")


def main():
    bookmarks = BookmarkFolder.parse_file("bookmarks-2020-08-19-Info.json")
    with open(Path("dist") / "index.html", "w") as f:
        f.write(index_template.render(bookmarks_root=bookmarks))


if __name__ == "__main__":
    main()
