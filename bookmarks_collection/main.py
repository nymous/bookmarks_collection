import json

from objects import BookmarkRoot


def main():
    with open("bookmarks-2019-07-20-simple.json") as f:
        bookmarks_json = json.load(f)
        bookmarks = BookmarkRoot(**bookmarks_json)
        print(bookmarks)


if __name__ == "__main__":
    main()
