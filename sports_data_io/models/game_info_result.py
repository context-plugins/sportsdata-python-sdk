from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game_odd_result import GameOddResult, GameOddResultDict


class GameInfoResult(SdkBaseModel):
    score_id: Optional[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the score/game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The year of the season during which this game occurs."""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this game corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)."""

    week: OptionalNullable[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game (in US Eastern Time)"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The status of the game. For a description of possible values, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/14287629964567-Process-Guide-Game-Status"
    target="_blank">here.</a> For how suspended and postponed games are handled specifically, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/4404845580567-Postponed-and-Rescheduled-Games"
    target="_blank">here</a>."""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    away_team_name: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamName")
    """The name of the away team"""

    home_team_name: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamName")
    """The name of the home team"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: Optional[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues"""

    pregame_odds: Optional[list[GameOddResult]] = Field(default=UNSET, alias="PregameOdds")
    """List of Pregame Odds from different sportsbooks with results"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Score of the home team (updated after game ends to allow for resolving bets)"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Score of the away team (updated after game ends to allow for resolving bets)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """The total points scored by both teams in the game tied to this event (updated after game ends to allow for
    resulting bets)"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """Rotation Number of home team in this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """Rotation Number of away team in this game"""

    alternate_market_pregame_odds: Optional[list[GameOddResult]] = Field(
        default=UNSET, alias="AlternateMarketPregameOdds"
    )
    """List of Alternate Market Pregame Odds from different sportsbooks with results"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    quarter: OptionalNullable[str] = Field(default=UNSET, alias="Quarter")
    """The current quarter of the game (1, 2, 3, 4, Half, OT, F, F/OT or NULL if game has not yet started)"""

    time_remaining: OptionalNullable[str] = Field(default=UNSET, alias="TimeRemaining")
    """The amount of time remaining in the current quarter (e.g. 11:23; 5:34; NULL if game is not in progress or at
    halftime)"""

    away_score_quarter1: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreQuarter1")
    """Points scored by the away team in Quarter 1"""

    away_score_quarter2: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreQuarter2")
    """Points scored by the away team in Quarter 2"""

    away_score_quarter3: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreQuarter3")
    """Points scored by the away team in Quarter 3"""

    away_score_quarter4: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreQuarter4")
    """Points scored by the away team in Quarter 4"""

    away_score_overtime: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreOvertime")
    """Points scored by the away team in overtime"""

    home_score_quarter1: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreQuarter1")
    """Points scored by the home team in Quarter 1"""

    home_score_quarter2: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreQuarter2")
    """Points scored by the home team in Quarter 2"""

    home_score_quarter3: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreQuarter3")
    """Points scored by the home team in Quarter 3"""

    home_score_quarter4: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreQuarter4")
    """Points scored by the home team in Quarter 4"""

    home_score_overtime: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreOvertime")
    """Points scored by the home team in overtime"""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out."""

    live_odds: Optional[list[GameOddResult]] = Field(default=UNSET, alias="LiveOdds")
    """List of Live Odds from different sportsbooks with results"""


class GameInfoResultDict(TypedDict):
    score_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    week: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    status: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    away_team_name: NotRequired[str | None]
    home_team_name: NotRequired[str | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int]
    pregame_odds: NotRequired[list[GameOddResult | GameOddResultDict]]
    home_team_score: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    total_score: NotRequired[int | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    alternate_market_pregame_odds: NotRequired[list[GameOddResult | GameOddResultDict]]
    game_id: NotRequired[int]
    quarter: NotRequired[str | None]
    time_remaining: NotRequired[str | None]
    away_score_quarter1: NotRequired[int | None]
    away_score_quarter2: NotRequired[int | None]
    away_score_quarter3: NotRequired[int | None]
    away_score_quarter4: NotRequired[int | None]
    away_score_overtime: NotRequired[int | None]
    home_score_quarter1: NotRequired[int | None]
    home_score_quarter2: NotRequired[int | None]
    home_score_quarter3: NotRequired[int | None]
    home_score_quarter4: NotRequired[int | None]
    home_score_overtime: NotRequired[int | None]
    is_closed: NotRequired[bool | None]
    live_odds: NotRequired[list[GameOddResult | GameOddResultDict]]
