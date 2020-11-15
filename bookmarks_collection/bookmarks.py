from __future__ import annotations

from abc import ABCMeta
from datetime import datetime
from enum import Enum
from typing import Union, List, Optional, Literal, Iterator

from pydantic import BaseModel, AnyUrl, Field

"""
{
  "guid": "root________",
  "title": "",
  "index": 0,
  "dateAdded": 1509553862576000,
  "lastModified": 1563557348382000,
  "id": 1,
  "typeCode": 2,
  "type": "text/x-moz-place-container",
  "root": "placesRoot",
  "children": [
    {
      "guid": "1GXuDpWKuzaZ",
      "title": "Docs",
      "index": 23,
      "dateAdded": 1514400981910000,
      "lastModified": 1563557349000000,
      "id": 1330,
      "typeCode": 2,
      "type": "text/x-moz-place-container",
      "children": [
        {
          "guid": "irnkVN3Z0Wm8",
          "title": "facebook/Docusaurus: Easy to maintain open source documentation websites.",
          "index": 0,
          "dateAdded": 1514400959484000,
          "lastModified": 1563557349000000,
          "id": 1329,
          "typeCode": 1,
          "charset": "UTF-8",
          "iconuri": "https://assets-cdn.github.com/favicon.ico",
          "type": "text/x-moz-place",
          "uri": "https://github.com/facebook/Docusaurus"
        },
        {
          "guid": "ioFmy5yuXCAv",
          "title": "",
          "index": 16,
          "dateAdded": 1497742450465000,
          "lastModified": 1563557349000000,
          "id": 343,
          "typeCode": 3,
          "type": "text/x-moz-place-separator"
        }
      ]
    }
  ]
}
"""


class BookmarkTypeEnum(str, Enum):
    folder = "text/x-moz-place-container"
    entry = "text/x-moz-place"
    separator = "text/x-moz-place-separator"


class BookmarkRootEnum(str, Enum):
    root = "placesRoot"
    bookmarks_menu = "bookmarksMenuFolder"
    toolbar = "toolbarFolder"
    unfiled_bookmarks = "unfiledBookmarksFolder"
    mobile = "mobileFolder"


class BookmarkBase(BaseModel, metaclass=ABCMeta):
    guid: str
    title: str
    index: int
    dateAdded: datetime
    lastModified: datetime
    id: int
    typeCode: int
    type: BookmarkTypeEnum


class BookmarkSeparator(BookmarkBase):
    type: Literal[BookmarkTypeEnum.separator]
    typeCode: Literal[3]


class BookmarkFolder(BookmarkBase):
    type: Literal[BookmarkTypeEnum.folder]
    typeCode: Literal[2]
    children: List[
        Union[BookmarkEntry, BookmarkRoot, BookmarkFolder, BookmarkSeparator]
    ] = Field(default_factory=list)


class BookmarkRoot(BookmarkFolder):
    type: Literal[BookmarkTypeEnum.folder]
    typeCode: Literal[2]
    root: BookmarkRootEnum


class BookmarkEntry(BookmarkBase):
    type: Literal[BookmarkTypeEnum.entry]
    typeCode: Literal[1]
    uri: Union[AnyUrl, str]
    charset: Optional[str] = None
    iconuri: Optional[Union[AnyUrl, str]] = None


BookmarkFolder.update_forward_refs()
BookmarkRoot.update_forward_refs()


def recursive_iter(bookmark: BookmarkBase) -> Iterator[BookmarkBase]:
    if isinstance(bookmark, BookmarkFolder):
        for child in bookmark.children:
            yield from recursive_iter(child)
    yield bookmark
