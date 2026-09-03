from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .series import Series, SeriesDict


class ScheduleBasic2(SdkBaseModel):
    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The MLB season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled; InProgress; Final; Suspended; Delayed;
    Postponed; Canceled; Forfeit; NotNecessary"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game in US Eastern Time"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the Home Team"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique TeamID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    is_closed: Optional[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out. Note: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time of the late update made to this record (in US Eastern Time)"""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time that the game ended in US Eastern Time"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game in UTC"""

    series_info: Optional[Series] = Field(default=UNSET, alias="SeriesInfo")
    """Contains relevant series data for postseason series only - HomeTeamWins; AwayTeamWins; GameNumber; and
    MaxLength"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    suspension_resume_day: OptionalNullable[str] = Field(default=UNSET, alias="SuspensionResumeDay")
    """The date a game that was suspended in play will be resumed for play. Useful for tracking when a Suspended game
    will return to an InProgress status."""

    suspension_resume_date_time: OptionalNullable[str] = Field(default=UNSET, alias="SuspensionResumeDateTime")
    """The date and start-time that the suspended in play game will be resumed for play. Useful for tracking when a
    Suspended game will return to an InProgress status."""


class ScheduleBasic2Dict(TypedDict):
    game_id: NotRequired[int | None]
    season: NotRequired[int]
    season_type: NotRequired[int]
    status: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    rescheduled_game_id: NotRequired[int | None]
    stadium_id: NotRequired[int | None]
    is_closed: NotRequired[bool]
    updated: NotRequired[str | None]
    game_end_date_time: NotRequired[str | None]
    date_time_utc: NotRequired[str | None]
    series_info: NotRequired[Series | SeriesDict]
    rescheduled_from_game_id: NotRequired[int | None]
    suspension_resume_day: NotRequired[str | None]
    suspension_resume_date_time: NotRequired[str | None]
