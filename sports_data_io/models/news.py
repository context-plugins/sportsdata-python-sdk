from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class News(SdkBaseModel):
    news_id: Optional[int] = Field(default=UNSET, alias="NewsID")
    """Unique ID of news story"""

    source: OptionalNullable[str] = Field(default=UNSET, alias="Source")
    """The source of the story (RotoBaller, NBCSports.com, etc.)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date/time that the content was published (in US Eastern time)"""

    time_ago: OptionalNullable[str] = Field(default=UNSET, alias="TimeAgo")
    """A description of how long ago this content was published"""

    title: OptionalNullable[str] = Field(default=UNSET, alias="Title")
    """The brief title of the news (typically less than 100 characters)"""

    content: OptionalNullable[str] = Field(default=UNSET, alias="Content")
    """The full body content of the story"""

    url: OptionalNullable[str] = Field(default=UNSET, alias="Url")
    """The url of the full story"""

    terms_of_use: OptionalNullable[str] = Field(default=UNSET, alias="TermsOfUse")
    """The terms of use with using this news item, credit must be given to the originator of the story when specified in
    the terms of use"""

    author: OptionalNullable[str] = Field(default=UNSET, alias="Author")
    """The author of the content"""

    categories: OptionalNullable[str] = Field(default=UNSET, alias="Categories")
    """Comma delimited meta tags describing the categories of this content. Possible tags include: Top Headlines,
    Breaking News, Injury, Sit/Start, Waiver Wire, Risers, Fallers, Lineups, Transactions, Free Agents,
    Prospects/Rookies, Game Recap, Matchup Outlook, NFL Draft"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID as assigned by SportsDataIO of the player tied to this news story. Note: this ID will stay
    with the player throughout their entire career"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that relates to this story"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that relates to the story"""

    player_id2: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID2")
    """The unique PlayerID as assigned by SportsDataIO of the second player tied to this news story. Note: this ID will
    stay with the player throughout their entire career"""

    team_id2: OptionalNullable[int] = Field(default=UNSET, alias="TeamID2")
    """The unique ID of the second team that relates to this story"""

    team2: OptionalNullable[str] = Field(default=UNSET, alias="Team2")
    """The abbreviation [Key] of the second team that relates to the story"""

    original_source: OptionalNullable[str] = Field(default=UNSET, alias="OriginalSource")
    """The original source who broke this news (before it was picked up by the publisher of this blurb)"""

    original_source_url: OptionalNullable[str] = Field(default=UNSET, alias="OriginalSourceUrl")
    """The URL of the original source who broke this news blurb"""


class NewsDict(TypedDict):
    news_id: NotRequired[int]
    source: NotRequired[str | None]
    updated: NotRequired[str | None]
    time_ago: NotRequired[str | None]
    title: NotRequired[str | None]
    content: NotRequired[str | None]
    url: NotRequired[str | None]
    terms_of_use: NotRequired[str | None]
    author: NotRequired[str | None]
    categories: NotRequired[str | None]
    player_id: NotRequired[int | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    player_id2: NotRequired[int | None]
    team_id2: NotRequired[int | None]
    team2: NotRequired[str | None]
    original_source: NotRequired[str | None]
    original_source_url: NotRequired[str | None]
