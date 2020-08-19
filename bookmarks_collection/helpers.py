from typing import Union

from objects import BookmarkFolder, BookmarkEntry, BookmarkTypeEnum


def folder(bookmark: Union[BookmarkFolder, BookmarkEntry]) -> bool:
    return bookmark.type == BookmarkTypeEnum.folder


def entry(bookmark: Union[BookmarkFolder, BookmarkEntry]) -> bool:
    return bookmark.type == BookmarkTypeEnum.entry
