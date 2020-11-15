from datetime import datetime
from typing import Union

import pendulum

from bookmarks import BookmarkFolder, BookmarkEntry, BookmarkTypeEnum


######################
# Custom Jinja tests #
######################
def folder(bookmark: Union[BookmarkFolder, BookmarkEntry]) -> bool:
    return bookmark.type == BookmarkTypeEnum.folder


def entry(bookmark: Union[BookmarkFolder, BookmarkEntry]) -> bool:
    return bookmark.type == BookmarkTypeEnum.entry


def folder_or_entry(bookmark: Union[BookmarkFolder, BookmarkEntry]) -> bool:
    return folder(bookmark) or entry(bookmark)


########################
# Custom Jinja filters #
########################
def human_date(date: datetime) -> str:
    return pendulum.instance(date).diff_for_humans()
