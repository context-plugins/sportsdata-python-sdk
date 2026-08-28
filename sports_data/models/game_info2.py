from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game_odd2 import GameOdd2, GameOdd2Dict


class GameInfo2(SdkBaseModel):
    score_id: Optional[int] = Field(default=UNSET, alias="ScoreId")
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

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamId")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamId")
    """The unique ID of the home team"""

    away_team_name: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamName")
    """The name of the away team"""

    home_team_name: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamName")
    """The name of the home team."""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameId")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamId")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamId")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues"""

    pregame_odds: Optional[list[GameOdd2]] = Field(default=UNSET, alias="PregameOdds")
    """List of Pregame Odds from different sportsbooks"""

    live_odds: Optional[list[GameOdd2]] = Field(default=UNSET, alias="LiveOdds")
    """List of Live Odds from different sportsbooks"""

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

    alternate_market_pregame_odds: Optional[list[GameOdd2]] = Field(default=UNSET, alias="AlternateMarketPregameOdds")
    """List of Alternate Market Pregame Odds from different sportsbooks"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of this game"""


class GameInfo2Dict(TypedDict):
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
    global_home_team_id: NotRequired[int | None]
    pregame_odds: NotRequired[list[GameOdd2 | GameOdd2Dict]]
    live_odds: NotRequired[list[GameOdd2 | GameOdd2Dict]]
    home_team_score: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    total_score: NotRequired[int | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    alternate_market_pregame_odds: NotRequired[list[GameOdd2 | GameOdd2Dict]]
    game_id: NotRequired[int]
