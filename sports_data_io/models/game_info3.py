from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game_odd1 import GameOdd1, GameOdd1Dict


class GameInfo3(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of this game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NHL season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 5=AllStar;
    6=Exhibition)."""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day that the game is scheduled to be played"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game in US Eastern Time"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Final, F/SO, F/OT, Postponed,
    Canceled, NotNecessary"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamId")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamId")
    """The unique ID of the home team"""

    away_team_name: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamName")
    """The name of the away team"""

    home_team_name: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamName")
    """The name of the home team"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameId")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamId")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamId")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    pregame_odds: Optional[list[GameOdd1]] = Field(default=UNSET, alias="PregameOdds")
    """List of Pregame GameOdds from different sportsbooks"""

    live_odds: Optional[list[GameOdd1]] = Field(default=UNSET, alias="LiveOdds")
    """List of live game odds from different sportsbooks"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total number of goals the home team scored in the game (updated after game ends to allow for resolving bets)"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of goals the away team scored in the game (updated after game ends to allow for resolving bets)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """Total goals scored in the game (updated after game ends to allow for resolving bets)"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """The rotation number of the home team for this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """The rotation number of the away team for a game"""

    alternate_market_pregame_odds: Optional[list[GameOdd1]] = Field(default=UNSET, alias="AlternateMarketPregameOdds")
    """A list of Alternate Market Pregame GameOdds from different sportsbooks (e.g. 1st Period; 2nd Period; etc.)"""


class GameInfo3Dict(TypedDict):
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
    pregame_odds: NotRequired[list[GameOdd1Dict]]
    live_odds: NotRequired[list[GameOdd1Dict]]
    home_team_score: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    total_score: NotRequired[int | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    alternate_market_pregame_odds: NotRequired[list[GameOdd1Dict]]
