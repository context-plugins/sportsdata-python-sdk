from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Timeframe(SdkBaseModel):
    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The season type of the timeframe (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason, 5=All-Star)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The league year of the timeframe (this gets incremented on the first day of the league year during free
    agency)"""

    week: OptionalNullable[int] = Field(default=UNSET, alias="Week")
    """The week of the timeframe (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to4; offseason=NULL). Note:
    seasons after 2021 will have only 3 preseason weeks"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The friendly name of the Timeframe"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The shorter name of the Timeframe"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date/time of this Timeframe"""

    end_date: OptionalNullable[str] = Field(default=UNSET, alias="EndDate")
    """The end date and time of the timeframe"""

    first_game_start: OptionalNullable[str] = Field(default=UNSET, alias="FirstGameStart")
    """The start date/time of the first game of the Timeframe (if no games then returns the StartDate)"""

    first_game_end: OptionalNullable[str] = Field(default=UNSET, alias="FirstGameEnd")
    """The end date/time of the first game of the Timeframe (if no games then returns the EndDate)"""

    last_game_end: OptionalNullable[str] = Field(default=UNSET, alias="LastGameEnd")
    """The end date/time of the last game of the Timeframe (if no games then returns the EndDate)"""

    has_games: Optional[bool] = Field(default=UNSET, alias="HasGames")
    """Whether there are any games in this Timeframe"""

    has_started: Optional[bool] = Field(default=UNSET, alias="HasStarted")
    """Whether this Timeframe has started"""

    has_ended: Optional[bool] = Field(default=UNSET, alias="HasEnded")
    """Whether this Timeframe has ended"""

    has_first_game_started: Optional[bool] = Field(default=UNSET, alias="HasFirstGameStarted")
    """Whether the first game has started"""

    has_first_game_ended: Optional[bool] = Field(default=UNSET, alias="HasFirstGameEnded")
    """Whether the first game has ended"""

    has_last_game_ended: Optional[bool] = Field(default=UNSET, alias="HasLastGameEnded")
    """Whether the last game has ended"""

    api_season: OptionalNullable[str] = Field(default=UNSET, alias="ApiSeason")
    """The value of the Season parameter used to pass into the API"""

    api_week: OptionalNullable[str] = Field(default=UNSET, alias="ApiWeek")
    """The value of the Week parameter used to pass into the API"""


class TimeframeDict(TypedDict):
    season_type: NotRequired[int]
    season: NotRequired[int]
    week: NotRequired[int | None]
    name: NotRequired[str | None]
    short_name: NotRequired[str | None]
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
    first_game_start: NotRequired[str | None]
    first_game_end: NotRequired[str | None]
    last_game_end: NotRequired[str | None]
    has_games: NotRequired[bool]
    has_started: NotRequired[bool]
    has_ended: NotRequired[bool]
    has_first_game_started: NotRequired[bool]
    has_first_game_ended: NotRequired[bool]
    has_last_game_ended: NotRequired[bool]
    api_season: NotRequired[str | None]
    api_week: NotRequired[str | None]
