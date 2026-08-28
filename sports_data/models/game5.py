from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .period import Period, PeriodDict


class Game5(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season that the game occurs in Note: season is a single year that the majority of the season occurs in"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled; InProgress; Final; F/OT; Suspended; Postponed;
    Delayed; Canceled; Forfeit"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date the game is scheduled to occur"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The timestamp of when the game is scheduled to start"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of points the away team scored in the game"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total number of points the home team scored in this game"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when this game was last updated (in US Eastern Time)"""

    period: OptionalNullable[str] = Field(default=UNSET, alias="Period")
    """The current quarter of the game (Possible Values: 1, 2, 3, 4, OT, NULL)"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """Number of minutes remaining in the quarter"""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """Number of seconds remaining in the quarter"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues"""

    periods: Optional[list[Period]] = Field(default=UNSET, alias="Periods")
    """The details of the periods (quarters & overtime) for this game"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The timestamp in UTC of when the game is scheduled to start"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""


class Game5Dict(TypedDict):
    game_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    status: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    updated: NotRequired[str | None]
    period: NotRequired[str | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    periods: NotRequired[list[Period | PeriodDict]]
    date_time_utc: NotRequired[str | None]
    rescheduled_from_game_id: NotRequired[int | None]
    rescheduled_game_id: NotRequired[int | None]
