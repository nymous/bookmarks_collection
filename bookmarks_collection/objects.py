from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Union, List, Optional

from pydantic import BaseModel, AnyUrl

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


class BookmarkBase(BaseModel):
    guid: str
    title: str
    index: int
    dateAdded: datetime
    lastModified: datetime
    id: int
    typeCode: int
    type: str


class BookmarkSeparator(BookmarkBase):
    pass


class BookmarkFolder(BookmarkBase):
    children: List[
        Union[BookmarkEntry, BookmarkRoot, BookmarkFolder, BookmarkSeparator]
    ]


class BookmarkRoot(BookmarkFolder):
    root: BookmarkRootEnum


class BookmarkEntry(BookmarkBase):
    charset: Optional[str] = None
    iconuri: Optional[Union[AnyUrl, str]] = None
    uri: Union[AnyUrl, str]


BookmarkFolder.update_forward_refs()
BookmarkRoot.update_forward_refs()
