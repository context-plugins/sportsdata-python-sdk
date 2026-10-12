from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game_odd_result1 import GameOddResult1, GameOddResult1Dict
from .quarter1 import Quarter1, Quarter1Dict


class GameInfoResult1(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game."""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NBA season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar; 6=Exhibition)"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Final, F/OT, Suspended, Postponed,
    Delayed, Canceled, Forfeit, NotNecessary"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    away_team_name: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamName")
    """The abbreviation [Key] of the away team"""

    home_team_name: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamName")
    """The abbreviation [Key] of the home team"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    pregame_odds: Optional[list[GameOddResult1]] = Field(default=UNSET, alias="PregameOdds")
    """List of Pregame GameOdds from different sportsbooks with results"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total points scored by the home team in the game (updated after the game ends to allow for resolving bets)"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of points the away team scored in the game (updated after game ends to allow for resolving bets)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """The total amount of points scored in the game by both teams. Updated after the game ends to allow for resulting
    bets"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """The rotation number of the home team for this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """The rotation number of the away team for this game"""

    alternate_market_pregame_odds: Optional[list[GameOddResult1]] = Field(
        default=UNSET, alias="AlternateMarketPregameOdds"
    )
    """A list of Alternate Market Pregame GameOdds from different sportsbooks (such as 1st-half; 1st-qtr; etc)"""

    quarter: OptionalNullable[str] = Field(default=UNSET, alias="Quarter")
    """The current quarter in the game. Possible values include: 1, 2, 3, 4, Half, OT, NULL"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """The number of minutes remaining in the quarter"""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """The number of seconds remaining in the quarter"""

    quarters: Optional[list[Quarter1]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters (including overtime periods) for this game."""

    is_closed: Optional[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out. Note: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status"""

    live_odds: Optional[list[GameOddResult1]] = Field(default=UNSET, alias="LiveOdds")
    """List of Live Odds from different sportsbooks with results"""


class GameInfoResult1Dict(TypedDict):
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
    pregame_odds: NotRequired[list[GameOddResult1Dict]]
    home_team_score: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    total_score: NotRequired[int | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    alternate_market_pregame_odds: NotRequired[list[GameOddResult1Dict]]
    quarter: NotRequired[str | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    quarters: NotRequired[list[Quarter1Dict]]
    is_closed: NotRequired[bool]
    live_odds: NotRequired[list[GameOddResult1Dict]]
