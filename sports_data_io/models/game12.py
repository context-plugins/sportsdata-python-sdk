from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .period import Period, PeriodDict
from .series import Series, SeriesDict


class Game12(SdkBaseModel):
    """The details of the game that this SlateGame refers to"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NHL season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 5=AllStar,
    6=Exhibition)."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Final, F/SO, F/OT, Postponed,
    Canceled, NotNecessary"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game in US Eastern Time"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (in US Eastern Time)."""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out. NOTE: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status"""

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
    """The total number of people who attended the game"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of goals scored by the away team in the game"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total number of goals scored by the home team in the game"""

    period: OptionalNullable[str] = Field(default=UNSET, alias="Period")
    """Indicates the current period of the game. Possible values include: 1; 2; 3; OT; SO; NULL"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """Number of minutes remaining in the current period"""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """Number of seconds that have passed in the current period. NOTE: this field name might be misleading as it
    actually represents the game clock sconds which are the number of minutes that have already passed in the period."""

    away_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamMoneyLine")
    """Moneyline from the perspective of the away team"""

    home_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamMoneyLine")
    """Moneyline from the perspective of the home team"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """The oddsmaker puck line at game start from the perspective of the HomeTeam (negative numbers indicate the
    HomeTeam is favored; positive numbers indicate the AwayTeam is favored)."""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The sportsbook's total goals scored line (Over/Under) for the game"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: Optional[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: Optional[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    point_spread_away_team_money_line: OptionalNullable[int] = Field(
        default=UNSET, alias="PointSpreadAwayTeamMoneyLine"
    )
    """The payout odds when betting on the away team with the puck line"""

    point_spread_home_team_money_line: OptionalNullable[int] = Field(
        default=UNSET, alias="PointSpreadHomeTeamMoneyLine"
    )
    """The payout odds when betting on the home team with the puck line"""

    last_play: OptionalNullable[str] = Field(default=UNSET, alias="LastPlay")
    """The description of the most recent play/event of the game. This is for display purposes and does not include
    corresponding data points."""

    periods: Optional[list[Period]] = Field(default=UNSET, alias="Periods")
    """The details of the periods (including overtime if applicable) for this game."""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time that the game ended in US Eastern Time"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """The rotation number of the home team for this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """The rotation number of the away team for a game"""

    neutral_venue: OptionalNullable[bool] = Field(default=UNSET, alias="NeutralVenue")
    """Indicates whether this game is played in a neutral venue"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for the over"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game in UTC"""

    series_info: Optional[Series] = Field(default=UNSET, alias="SeriesInfo")
    """Contains relevant series data for playoff series only - HomeTeamWins, AwayTeamWins, GameNumber, and MaxLength"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""

    referee1_id: OptionalNullable[int] = Field(default=UNSET, alias="Referee1ID")
    """The unique ID of the main referee of this game"""

    referee2_id: OptionalNullable[int] = Field(default=UNSET, alias="Referee2ID")
    """The unique ID of the secondary referee of this game"""

    linesperson1_id: OptionalNullable[int] = Field(default=UNSET, alias="Linesperson1ID")
    """The unique ID of the main linesperson of this game"""

    linesperson2_id: OptionalNullable[int] = Field(default=UNSET, alias="Linesperson2ID")
    """The unique ID of the secondary linesperson of this game"""


class Game12Dict(TypedDict):
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
    away_team_id: NotRequired[int]
    home_team_id: NotRequired[int]
    stadium_id: NotRequired[int | None]
    channel: NotRequired[str | None]
    attendance: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    period: NotRequired[str | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    away_team_money_line: NotRequired[int | None]
    home_team_money_line: NotRequired[int | None]
    point_spread: NotRequired[float | None]
    over_under: NotRequired[float | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int]
    global_home_team_id: NotRequired[int]
    point_spread_away_team_money_line: NotRequired[int | None]
    point_spread_home_team_money_line: NotRequired[int | None]
    last_play: NotRequired[str | None]
    periods: NotRequired[list[Period | PeriodDict]]
    game_end_date_time: NotRequired[str | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    neutral_venue: NotRequired[bool | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
    date_time_utc: NotRequired[str | None]
    series_info: NotRequired[Series | SeriesDict]
    rescheduled_from_game_id: NotRequired[int | None]
    rescheduled_game_id: NotRequired[int | None]
    referee1_id: NotRequired[int | None]
    referee2_id: NotRequired[int | None]
    linesperson1_id: NotRequired[int | None]
    linesperson2_id: NotRequired[int | None]
