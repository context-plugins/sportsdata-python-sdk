from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game_odd_result3 import GameOddResult3, GameOddResult3Dict


class GameInfoResult6(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The soccer regular season for which these totals apply"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in UTC)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Break, Final, Awarded, Postponed,
    Canceled, Suspended, Start Delay, Rain Delay, No Result, & NotNecessary. If a game is called off before it starts,
    the Status is set to Postponed, until a new date/time is scheduled, at which point, the DateTime is updated, and the
    Status is set back to Scheduled. If a game has already started, and temporarily interrupted, it's Status is set to
    Suspended, until it either resumes, or gets postponed and replayed at a later date. If the game is at halftime, then
    the Status will be Break. Awarded is used in cases where a game is decided on the so called "green table." That
    means that a game was decided by the Federation/League to one team for a reason. This can include situations like
    riots, where the opponent team gets 3:0 win awarded as punishment. Awarded is also used when a club withdraws during
    the season from the competition then all the remaining matches getting awarded 3:0."""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    away_team_name: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamName")
    """The name of the away team"""

    home_team_name: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamName")
    """The name of the home team"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    pregame_odds: Optional[list[GameOddResult3]] = Field(default=UNSET, alias="PregameOdds")
    """List of Pregame GameOdds from different sportsbooks with results"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Score of the home team (updated after game ends to allow for resolving bets)"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Score of the away team (updated after game ends to allow for resolving bets)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """The total combined score of both teams in the game (updated after game ends to allow for resolving bets)"""

    round_id: Optional[int] = Field(default=UNSET, alias="RoundID")
    """The unique ID of the round that this game is associated with"""

    week: OptionalNullable[int] = Field(default=UNSET, alias="Week")
    """The week during the season/round in which this game occurs"""

    alternate_market_pregame_odds: Optional[list[GameOddResult3]] = Field(
        default=UNSET, alias="AlternateMarketPregameOdds"
    )
    """List of Alternate Market GameOdds from different sportsbooks (such as 1st-half; 1st-qtr; etc)"""

    period: OptionalNullable[str] = Field(default=UNSET, alias="Period")
    """The final period of the game. Possible values: Regular = Game ended in 90 minutes of regular time; ExtraTime =
    Game ended in extra time / overtime; PenaltyShootout = Game finished in penalty shootout time"""

    clock: OptionalNullable[int] = Field(default=UNSET, alias="Clock")
    """The clock for the game if it is in progress. Note: if the game hasn't started or the game is over; then this will
    be NULL"""

    winner: OptionalNullable[str] = Field(default=UNSET, alias="Winner")
    """The winner of the game. Possible values: AwayTeam; HomeTeam; Draw"""

    away_team_score_period1: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScorePeriod1")
    """The first period score of the away team."""

    away_team_score_period2: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScorePeriod2")
    """The second period score of the away team."""

    away_team_score_extra_time: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScoreExtraTime")
    """The extra time (overtime) score of the away team (if applicable)."""

    away_team_score_penalty: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScorePenalty")
    """The penalty shootout score of the away team (if applicable)."""

    home_team_score_period1: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScorePeriod1")
    """The first period score of the home team"""

    home_team_score_period2: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScorePeriod2")
    """The second period score of the home team"""

    home_team_score_extra_time: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScoreExtraTime")
    """The extra time (overtime) score of the home team (if applicable)"""

    home_team_score_penalty: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScorePenalty")
    """The penalty shootout score of the home team (if applicable)"""

    clock_extra: OptionalNullable[int] = Field(default=UNSET, alias="ClockExtra")
    """The added stoppage time minute the game is currently in. Note: will be null when game is not in stoppage time"""

    clock_display: OptionalNullable[str] = Field(default=UNSET, alias="ClockDisplay")
    """A convenient string display of the current clock with format Clock+ClockExtra (ex 90+3)"""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score and stats have been verified and closed out"""

    live_odds: Optional[list[GameOddResult3]] = Field(default=UNSET, alias="LiveOdds")
    """List of Live Odds from different sportsbooks with results"""


class GameInfoResult6Dict(TypedDict):
    game_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    status: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    away_team_name: NotRequired[str | None]
    home_team_name: NotRequired[str | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    pregame_odds: NotRequired[list[GameOddResult3Dict]]
    home_team_score: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    total_score: NotRequired[int | None]
    round_id: NotRequired[int]
    week: NotRequired[int | None]
    alternate_market_pregame_odds: NotRequired[list[GameOddResult3Dict]]
    period: NotRequired[str | None]
    clock: NotRequired[int | None]
    winner: NotRequired[str | None]
    away_team_score_period1: NotRequired[int | None]
    away_team_score_period2: NotRequired[int | None]
    away_team_score_extra_time: NotRequired[int | None]
    away_team_score_penalty: NotRequired[int | None]
    home_team_score_period1: NotRequired[int | None]
    home_team_score_period2: NotRequired[int | None]
    home_team_score_extra_time: NotRequired[int | None]
    home_team_score_penalty: NotRequired[int | None]
    clock_extra: NotRequired[int | None]
    clock_display: NotRequired[str | None]
    is_closed: NotRequired[bool | None]
    live_odds: NotRequired[list[GameOddResult3Dict]]
