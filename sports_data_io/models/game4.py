from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .quarter1 import Quarter1, Quarter1Dict
from .series2 import Series2, Series2Dict


class Game4(SdkBaseModel):
    """The details of the game associated with this box score"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NBA season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar; 6=Exhibition)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Final, F/OT, Suspended, Postponed,
    Delayed, Canceled, Forfeit, NotNecessary"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    away_team_id: Optional[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: Optional[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    channel: OptionalNullable[str] = Field(default=UNSET, alias="Channel")
    """The television station broadcasting the game"""

    attendance: OptionalNullable[int] = Field(default=UNSET, alias="Attendance")
    """The total number of people in attendance at the game"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of points the away team scored in the game"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total number of points the home team scored in this game"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when this game was last updated (in US Eastern Time)"""

    quarter: OptionalNullable[str] = Field(default=UNSET, alias="Quarter")
    """The current quarter in the game. Possible values include: 1, 2, 3, 4, Half, OT, NULL"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """The number of minutes remaining in the quarter"""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """The number of seconds remaining in the quarter"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """The oddsmaker Point Spread at game start from the perspective of the HomeTeam (negative numbers indicate the
    HomeTeam is favored; positive numbers indicate the AwayTeam is favored)"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The sportsbook's total points scored over under for the game"""

    away_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamMoneyLine")
    """Money line from the perspective of the away team"""

    home_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamMoneyLine")
    """Money line from the perspective of the home team"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: Optional[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: Optional[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    point_spread_away_team_money_line: OptionalNullable[int] = Field(
        default=UNSET, alias="PointSpreadAwayTeamMoneyLine"
    )
    """The money line payout odds when betting on the away team with the point spread."""

    point_spread_home_team_money_line: OptionalNullable[int] = Field(
        default=UNSET, alias="PointSpreadHomeTeamMoneyLine"
    )
    """The money line payout odds when betting on the away team with the point spread."""

    last_play: OptionalNullable[str] = Field(default=UNSET, alias="LastPlay")
    """The description of the most recent play/event of the game. This is for display purposes and does not include
    corresponding data points."""

    is_closed: Optional[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out. Note: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status"""

    quarters: Optional[list[Quarter1]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters (including overtime periods) for this game."""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time that the game ended (in US Eastern Time)"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """The rotation number of the home team for this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """The rotation number of the away team for this game"""

    neutral_venue: OptionalNullable[bool] = Field(default=UNSET, alias="NeutralVenue")
    """Indicates whether this game is played in a neutral venue"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for the over on the total points line"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under on the total points line"""

    crew_chief_id: OptionalNullable[int] = Field(default=UNSET, alias="CrewChiefID")
    """Unique ID of officiating Crew Chief"""

    umpire_id: OptionalNullable[int] = Field(default=UNSET, alias="UmpireID")
    """Unique ID of officiating Umpire referee"""

    referee_id: OptionalNullable[int] = Field(default=UNSET, alias="RefereeID")
    """Unique ID of officiating referee"""

    alternate_id: OptionalNullable[int] = Field(default=UNSET, alias="AlternateID")
    """Unique ID of officiating Alternate referee"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game in UTC"""

    series_info: Optional[Series2] = Field(default=UNSET, alias="SeriesInfo")
    """Contains relevant series data for playoff series only - HomeTeamWins, AwayTeamWins, GameNumber, and MaxLength"""

    inseason_tournament: OptionalNullable[bool] = Field(default=UNSET, alias="InseasonTournament")
    """A flag to indicate this game is part of the inseason NBA tournament (can be considered a part of regular season
    still) - a null would also indicate false"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""


class Game4Dict(TypedDict):
    game_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    status: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    away_team_id: NotRequired[int]
    home_team_id: NotRequired[int]
    stadium_id: NotRequired[int | None]
    channel: NotRequired[str | None]
    attendance: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    updated: NotRequired[str | None]
    quarter: NotRequired[str | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    point_spread: NotRequired[float | None]
    over_under: NotRequired[float | None]
    away_team_money_line: NotRequired[int | None]
    home_team_money_line: NotRequired[int | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int]
    global_home_team_id: NotRequired[int]
    point_spread_away_team_money_line: NotRequired[int | None]
    point_spread_home_team_money_line: NotRequired[int | None]
    last_play: NotRequired[str | None]
    is_closed: NotRequired[bool]
    quarters: NotRequired[list[Quarter1 | Quarter1Dict]]
    game_end_date_time: NotRequired[str | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    neutral_venue: NotRequired[bool | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
    crew_chief_id: NotRequired[int | None]
    umpire_id: NotRequired[int | None]
    referee_id: NotRequired[int | None]
    alternate_id: NotRequired[int | None]
    date_time_utc: NotRequired[str | None]
    series_info: NotRequired[Series2 | Series2Dict]
    inseason_tournament: NotRequired[bool | None]
    rescheduled_from_game_id: NotRequired[int | None]
    rescheduled_game_id: NotRequired[int | None]
