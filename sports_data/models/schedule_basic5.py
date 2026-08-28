from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ScheduleBasic5(SdkBaseModel):
    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    score_id: OptionalNullable[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the score/game"""

    game_key: OptionalNullable[str] = Field(default=UNSET, alias="GameKey")
    """A 9 digit unique code identifying the game that this record corresponds to. The GameKey is composed of Season;
    SeasonType; Week and HomeTeam. Note: This value will be NULL for bye weeks"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The status of the game. For a description of possible values, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/14287629964567-Process-Guide-Game-Status"
    target="_blank">here.</a> For how suspended and postponed games are handled specifically, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/4404845580567-Postponed-and-Rescheduled-Games"
    target="_blank">here</a>."""

    canceled: OptionalNullable[bool] = Field(default=UNSET, alias="Canceled")
    """Indicates whether the game was canceled."""

    date: OptionalNullable[str] = Field(default=UNSET, alias="Date")
    """The date and time of the game (in US Eastern Time)"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game (in US Eastern Time)"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game (in UTC)"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the team's current home stadium"""

    closed: OptionalNullable[bool] = Field(default=UNSET, alias="Closed")
    """Indicates whether the game is over and the final score has been verified and closed out. Note: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status"""

    last_updated: OptionalNullable[str] = Field(default=UNSET, alias="LastUpdated")
    """The date and time that this game was last updated (in US Eastern Time)"""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out."""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""


class ScheduleBasic5Dict(TypedDict):
    game_id: NotRequired[int | None]
    global_game_id: NotRequired[int | None]
    score_id: NotRequired[int | None]
    game_key: NotRequired[str | None]
    season: NotRequired[int]
    season_type: NotRequired[int]
    status: NotRequired[str | None]
    canceled: NotRequired[bool | None]
    date: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    date_time_utc: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    stadium_id: NotRequired[int | None]
    closed: NotRequired[bool | None]
    last_updated: NotRequired[str | None]
    is_closed: NotRequired[bool | None]
    week: NotRequired[int]
    rescheduled_from_game_id: NotRequired[int | None]
    rescheduled_game_id: NotRequired[int | None]
