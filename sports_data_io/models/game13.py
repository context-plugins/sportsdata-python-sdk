from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .period1 import Period1, Period1Dict
from .stadium21 import Stadium21, Stadium21Dict


class Game13(SdkBaseModel):
    """The most recent future game for the team"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The College Football season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    week: OptionalNullable[int] = Field(default=UNSET, alias="Week")
    """The week of the game"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The status of the game. Possible values include: Scheduled; InProgress; Final; F/OT; Suspended; Postponed;
    Delayed; Canceled; Forfeit"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    away_team_id: Optional[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: Optional[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    away_team_name: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamName")
    """The name of the away team"""

    home_team_name: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamName")
    """The name of the home team"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of points the away team scored in this game"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total number of points the home team scored in this game"""

    period: OptionalNullable[str] = Field(default=UNSET, alias="Period")
    """The current quarter in the game (Possible Values: 1; 2; 3; 4; Half; OT; F; F/OT; NULL)"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """Total number of minutes remaining in the quarter"""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """Total number of seconds remaining in the quarter"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """The oddsmaker Point Spread at game start from the perspective of the HomeTeam. Note: negative numbers indicate
    the HomeTeam is favored; positive numbers indicate the AwayTeam is favored"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The sportsbook's total points line at game start"""

    away_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamMoneyLine")
    """The sportsbook's moneyline for the away team"""

    home_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamMoneyLine")
    """The sportsbook's moneyline for the home team"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when this game was last updated (US Eastern Time)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when this game was first created (in US Eastern Time)"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. Note: This value is guaranteed to be unique across all sports/leagues"""

    global_away_team_id: Optional[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. Note: This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: Optional[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. Note: This value is guaranteed to be unique across all sports/leagues"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium/venue where this game was played"""

    stadium: Optional[Stadium21] = Field(default=UNSET, alias="Stadium")
    """The details of the stadium where this game is played"""

    yard_line: OptionalNullable[int] = Field(default=UNSET, alias="YardLine")
    """The yard line that the ball is on at the current state of the game"""

    yard_line_territory: OptionalNullable[str] = Field(default=UNSET, alias="YardLineTerritory")
    """The team's side of the field that the ball is on"""

    down: OptionalNullable[int] = Field(default=UNSET, alias="Down")
    """The current down"""

    distance: OptionalNullable[int] = Field(default=UNSET, alias="Distance")
    """The current distance to a first down"""

    possession: OptionalNullable[str] = Field(default=UNSET, alias="Possession")
    """Which team currently has possession of the ball"""

    periods: Optional[list[Period1]] = Field(default=UNSET, alias="Periods")
    """The details of the periods (quarters & overtime) for this game"""

    is_closed: Optional[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified"""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time that the game ended (in US Eastern Time)"""

    title: OptionalNullable[str] = Field(default=UNSET, alias="Title")
    """The title of the game (e.g. Rose Bowl, Citrus Bowl, etc)"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """Rotation number of home team for this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """Rotation number of away team for this game"""

    channel: OptionalNullable[str] = Field(default=UNSET, alias="Channel")
    """The television station broadcasting the game"""

    neutral_venue: OptionalNullable[bool] = Field(default=UNSET, alias="NeutralVenue")
    """Indicates whether this game is played in a neutral venue"""

    away_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="AwayPointSpreadPayout")
    """The sportsbook's point spread payout for the away team"""

    home_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="HomePointSpreadPayout")
    """The point spread payout for the home team"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for the over in the total points line"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game (in UTC)"""

    attendance: OptionalNullable[int] = Field(default=UNSET, alias="Attendance")
    """The total number of people who attended the game"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""


class Game13Dict(TypedDict):
    game_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    week: NotRequired[int | None]
    status: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    away_team_id: NotRequired[int]
    home_team_id: NotRequired[int]
    away_team_name: NotRequired[str | None]
    home_team_name: NotRequired[str | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    period: NotRequired[str | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    point_spread: NotRequired[float | None]
    over_under: NotRequired[float | None]
    away_team_money_line: NotRequired[int | None]
    home_team_money_line: NotRequired[int | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int]
    global_home_team_id: NotRequired[int]
    stadium_id: NotRequired[int | None]
    stadium: NotRequired[Stadium21Dict]
    yard_line: NotRequired[int | None]
    yard_line_territory: NotRequired[str | None]
    down: NotRequired[int | None]
    distance: NotRequired[int | None]
    possession: NotRequired[str | None]
    periods: NotRequired[list[Period1Dict]]
    is_closed: NotRequired[bool]
    game_end_date_time: NotRequired[str | None]
    title: NotRequired[str | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    channel: NotRequired[str | None]
    neutral_venue: NotRequired[bool | None]
    away_point_spread_payout: NotRequired[int | None]
    home_point_spread_payout: NotRequired[int | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
    date_time_utc: NotRequired[str | None]
    attendance: NotRequired[int | None]
    rescheduled_from_game_id: NotRequired[int | None]
    rescheduled_game_id: NotRequired[int | None]
