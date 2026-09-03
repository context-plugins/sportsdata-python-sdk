from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class News2(SdkBaseModel):
    news_id: Optional[int] = Field(default=UNSET, alias="NewsID")
    """The unique ID of the news story"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the golfer who relates to this news story"""

    title: OptionalNullable[str] = Field(default=UNSET, alias="Title")
    """The brief title of the news (typically less than 100 characters)"""

    content: OptionalNullable[str] = Field(default=UNSET, alias="Content")
    """The full body content of this news story"""

    url: OptionalNullable[str] = Field(default=UNSET, alias="Url")
    """The url of the full story"""

    source: OptionalNullable[str] = Field(default=UNSET, alias="Source")
    """The source of the story (RotoBaller, NBCSports.com, etc.)"""

    terms_of_use: OptionalNullable[str] = Field(default=UNSET, alias="TermsOfUse")
    """The terms of use with using this news item, credit must be given to the originator of the story when specified in
    the terms of use"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date/time that the content was published"""

    author: OptionalNullable[str] = Field(default=UNSET, alias="Author")
    """The details of the golfers who competed in this tournament"""

    categories: OptionalNullable[str] = Field(default=UNSET, alias="Categories")
    """The category of news this story is under"""

    original_source: OptionalNullable[str] = Field(default=UNSET, alias="OriginalSource")
    """The original source of the news item"""

    original_source_url: OptionalNullable[str] = Field(default=UNSET, alias="OriginalSourceUrl")
    """The URL of the original source of the news item"""


class News2Dict(TypedDict):
    news_id: NotRequired[int]
    player_id: NotRequired[int | None]
    title: NotRequired[str | None]
    content: NotRequired[str | None]
    url: NotRequired[str | None]
    source: NotRequired[str | None]
    terms_of_use: NotRequired[str | None]
    updated: NotRequired[str | None]
    author: NotRequired[str | None]
    categories: NotRequired[str | None]
    original_source: NotRequired[str | None]
    original_source_url: NotRequired[str | None]
