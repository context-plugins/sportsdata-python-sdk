from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .period2 import Period2, Period2Dict
from .stadium1 import Stadium1, Stadium1Dict


class Game14(SdkBaseModel):
    """The next scheduled game for the team"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season that the game occurs in. Note: season is a single year that the majority of the season occurs in"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Final, F/OT, Suspended, Postponed,
    Delayed, Canceled, Forfeit"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day that the game is scheduled to be played in"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

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
    """The current period of the game (Possible Values: 1; 2; Half; OT; NULL)"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """Number of minutes remaining in the half (from 0 to 20). Note: if game is scheduled or final this field is NULL"""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """Number of seconds remaining in the half (from 0 to 59). Note: if game is scheduled or final this field is NULL"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """The consensus Point Spread at game start from the perspective of the HomeTeam (in the Game table, the PointSpread
    field's negative numbers indicate the HomeTeam is favored; positive numbers indicate the AwayTeam is favored. Note
    that this rule does not hold in betting-related tables, where the spread is contingent on the bet line.)"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The total points line (over/under) as given by the sportsbook"""

    away_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamMoneyLine")
    """Money line from the perspective of the away team"""

    home_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamMoneyLine")
    """Money line from the perspective of the home team"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    tournament_id: OptionalNullable[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament. Note: this field is specific to the NCAA tournament & does not include other
    tournaments"""

    bracket: OptionalNullable[str] = Field(default=UNSET, alias="Bracket")
    """The specific bracket of the tournament (e.g. East; West; Midwest; South). Note: this is specific to the NCAA
    tournament"""

    round: OptionalNullable[int] = Field(default=UNSET, alias="Round")
    """The current round of the NCAA tournament. Rounds: 1 = Round of 64, 2 = Round of 32, 3 = Sweet Sixteen, 4 = Elite
    Eight, 5 = Final Four, 6 = Championship Note: First Four games Round = NULL"""

    away_team_seed: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamSeed")
    """The seed of the away team (1-16). Note: this is specific to the NCAA tournament & does not include other
    tournaments"""

    home_team_seed: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamSeed")
    """The seed of the home team (1-16). Note: this is specific to the NCAA tournament & does not include other
    tournaments"""

    away_team_previous_game_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamPreviousGameID")
    """The Id of one of the NCAA tournament games which feeds this game. This gameid will be inaccurate/invalid in free
    trial as it is scrambled. Null for some Round 1 and all play-in games. Used for rendering. Does not change after
    tournament records have been created."""

    home_team_previous_game_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamPreviousGameID")
    """The Id of one of the NCAA tournament games which feeds this game. This gameid will be inaccurate/invalid in free
    trial as it is scrambled. Null for some Round 1 and all play-in games. Used for rendering. Does not change after
    tournament records have been created."""

    away_team_previous_global_game_id: OptionalNullable[int] = Field(
        default=UNSET, alias="AwayTeamPreviousGlobalGameID"
    )
    """The unique global ID of the away team's previous game (This gameid will be inaccurate/invalid in free trial as it
    is scrambled)"""

    home_team_previous_global_game_id: OptionalNullable[int] = Field(
        default=UNSET, alias="HomeTeamPreviousGlobalGameID"
    )
    """The unique global ID of the away team's previous game (This gameid will be inaccurate/invalid in free trial as it
    is scrambled)"""

    tournament_display_order: OptionalNullable[int] = Field(default=UNSET, alias="TournamentDisplayOrder")
    """The display order of this game. This is used for rendering NCAA Tournament bracket."""

    tournament_display_order_for_home_team: OptionalNullable[str] = Field(
        default=UNSET, alias="TournamentDisplayOrderForHomeTeam"
    )
    """The display order of the home team for this game. This is used for rendering the NCAA Tournament bracket, and it
    indicates whether the home team should be displayed at the top or bottom of the game card. Possible values: Top,
    Bottom"""

    periods: Optional[list[Period2]] = Field(default=UNSET, alias="Periods")
    """The details of the periods (halves & overtime) for this game. Note: the scores are for that half/period only, not
    total score of game at that point"""

    is_closed: Optional[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out. Note: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status"""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time that the game ended (in US Eastern Time)"""

    stadium: Optional[Stadium1] = Field(default=UNSET, alias="Stadium")
    """The stadium details of where this game was played"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """Rotation number of home team for this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """Rotation number of away team for this game."""

    top_team_previous_game_id: OptionalNullable[int] = Field(default=UNSET, alias="TopTeamPreviousGameId")
    """Previous game id of the team in the top slot of an NCAA tournament game. Used for rendering."""

    bottom_team_previous_game_id: OptionalNullable[int] = Field(default=UNSET, alias="BottomTeamPreviousGameId")
    """Previous game id of the team in the bottom slot of an NCAA tournament game. Used for rendering."""

    channel: OptionalNullable[str] = Field(default=UNSET, alias="Channel")
    """The television station broadcasting the game"""

    neutral_venue: OptionalNullable[bool] = Field(default=UNSET, alias="NeutralVenue")
    """Indicates whether this game is played in a neutral venue. Note: Neutral = True, Not Neutral = False"""

    away_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="AwayPointSpreadPayout")
    """The sportsbook's point spread payout for the away team. Note: this line is a consensus"""

    home_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="HomePointSpreadPayout")
    """The sportsbook's point spread payout for the home team"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The odds at which the sportsbook will pay out winning over bets at"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The payout when betting the Under of the Over/Under"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game in UTC"""

    attendance: OptionalNullable[int] = Field(default=UNSET, alias="Attendance")
    """The attendance of the game when available"""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""


class Game14Dict(TypedDict):
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
    point_spread: NotRequired[float | None]
    over_under: NotRequired[float | None]
    away_team_money_line: NotRequired[int | None]
    home_team_money_line: NotRequired[int | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    tournament_id: NotRequired[int | None]
    bracket: NotRequired[str | None]
    round: NotRequired[int | None]
    away_team_seed: NotRequired[int | None]
    home_team_seed: NotRequired[int | None]
    away_team_previous_game_id: NotRequired[int | None]
    home_team_previous_game_id: NotRequired[int | None]
    away_team_previous_global_game_id: NotRequired[int | None]
    home_team_previous_global_game_id: NotRequired[int | None]
    tournament_display_order: NotRequired[int | None]
    tournament_display_order_for_home_team: NotRequired[str | None]
    periods: NotRequired[list[Period2 | Period2Dict]]
    is_closed: NotRequired[bool]
    game_end_date_time: NotRequired[str | None]
    stadium: NotRequired[Stadium1 | Stadium1Dict]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    top_team_previous_game_id: NotRequired[int | None]
    bottom_team_previous_game_id: NotRequired[int | None]
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
