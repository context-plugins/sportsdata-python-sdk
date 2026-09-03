from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class News1(SdkBaseModel):
    news_id: Optional[int] = Field(default=UNSET, alias="NewsID")
    """The unique ID of the news story"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    title: OptionalNullable[str] = Field(default=UNSET, alias="Title")
    """The title of the news story"""

    content: OptionalNullable[str] = Field(default=UNSET, alias="Content")
    """The full body content of the story"""

    url: OptionalNullable[str] = Field(default=UNSET, alias="Url")
    """The URL of the full news story"""

    source: OptionalNullable[str] = Field(default=UNSET, alias="Source")
    """The source of the story (RotoBaller, NBCSports.com, etc.)"""

    terms_of_use: OptionalNullable[str] = Field(default=UNSET, alias="TermsOfUse")
    """The terms of use with using this news item, credit must be given to the originator of the story when specified in
    the terms of use"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the news story was last updated"""

    time_ago: OptionalNullable[str] = Field(default=UNSET, alias="TimeAgo")
    """A description of how long ago this content was published"""


class News1Dict(TypedDict):
    news_id: NotRequired[int]
    player_id: NotRequired[int | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    title: NotRequired[str | None]
    content: NotRequired[str | None]
    url: NotRequired[str | None]
    source: NotRequired[str | None]
    terms_of_use: NotRequired[str | None]
    updated: NotRequired[str | None]
    time_ago: NotRequired[str | None]
