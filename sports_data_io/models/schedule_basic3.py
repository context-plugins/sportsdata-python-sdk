from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .series import Series, SeriesDict


class ScheduleBasic3(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NHL season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 5=AllStar;
    6=Exhibition)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Final, F/SO, F/OT, Postponed,
    Canceled, NotNecessary"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game in US Eastern Time"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (in US Eastern Time)"""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out. Note: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of goals scored by the away team in the game"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total number of goals scored by the home team in the game"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: Optional[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: Optional[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time that the game ended in US Eastern Time"""

    neutral_venue: OptionalNullable[bool] = Field(default=UNSET, alias="NeutralVenue")
    """Indicates whether this game is played in a neutral venue"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game in UTC"""

    series_info: Optional[Series] = Field(default=UNSET, alias="SeriesInfo")
    """Contains relevant series data for playoff series only - HomeTeamWins, AwayTeamWins, GameNumber, and MaxLength"""

    away_team_id: Optional[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: Optional[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""


class ScheduleBasic3Dict(TypedDict):
    game_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    status: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    updated: NotRequired[str | None]
    is_closed: NotRequired[bool | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    stadium_id: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int]
    global_home_team_id: NotRequired[int]
    game_end_date_time: NotRequired[str | None]
    neutral_venue: NotRequired[bool | None]
    date_time_utc: NotRequired[str | None]
    series_info: NotRequired[SeriesDict]
    away_team_id: NotRequired[int]
    home_team_id: NotRequired[int]
    rescheduled_from_game_id: NotRequired[int | None]
    rescheduled_game_id: NotRequired[int | None]
