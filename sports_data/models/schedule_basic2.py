from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ScheduleBasic2(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season that the game occurs in. Note: season is a single year that the majority of the season occurs in"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
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

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    tournament_id: OptionalNullable[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament"""

    bracket: OptionalNullable[str] = Field(default=UNSET, alias="Bracket")
    """The specific bracket/region of the tournament"""

    round: OptionalNullable[int] = Field(default=UNSET, alias="Round")
    """The current round of the tournament"""

    away_team_seed: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamSeed")
    """The seed of the away team (1-16). Note: specific to March Madness tournament & does not include other
    tournaments"""

    home_team_seed: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamSeed")
    """The seed of the home team (1-16). Note: specific to March Madness tournament & does not include other
    tournaments"""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out."""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time that the game ended (in US Eastern Time)"""

    neutral_venue: OptionalNullable[bool] = Field(default=UNSET, alias="NeutralVenue")
    """Indicates whether this game is played in a neutral venue"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The timestamp in UTC of when the game is scheduled to start"""

    global_away_team_id: Optional[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: Optional[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""


class ScheduleBasic2Dict(TypedDict):
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
    global_game_id: NotRequired[int]
    tournament_id: NotRequired[int | None]
    bracket: NotRequired[str | None]
    round: NotRequired[int | None]
    away_team_seed: NotRequired[int | None]
    home_team_seed: NotRequired[int | None]
    is_closed: NotRequired[bool | None]
    game_end_date_time: NotRequired[str | None]
    neutral_venue: NotRequired[bool | None]
    date_time_utc: NotRequired[str | None]
    global_away_team_id: NotRequired[int]
    global_home_team_id: NotRequired[int]
    rescheduled_from_game_id: NotRequired[int | None]
    rescheduled_game_id: NotRequired[int | None]
