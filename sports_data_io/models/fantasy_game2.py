from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FantasyGame2(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their MLB career"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar)."""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The MLB season of the game"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game in US Eastern Time"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The name [Key] of the player's opponent in the game"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Whether the team is home or away"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's position associated with the given game or season. Possible values: 1B, 2B, 3B, C, CF, DH, IF, LF,
    OF, P, PH, PR, RF, RP, SP, SS"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category. Possible values: DH; IF; OF; P; PH; PR"""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The number of games played by the player. Note: for game feeds this will always = 1"""

    started: OptionalNullable[int] = Field(default=UNSET, alias="Started")
    """Whether the player started in the game. Note: started = 1 and not starting = 0"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points by the player during the game"""

    fantasy_points_batting: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsBatting")
    """Total batting fantasy points by the player in the game"""

    fantasy_points_pitching: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsPitching")
    """Total pitching fantasy points by the player in the game"""

    is_game_over: OptionalNullable[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether or not the game is over (returns ture/false)"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Total FanDuel fantasy points by the player in the game"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total Yahoo fantasy points by the player in the game"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total DraftKings fantasy points by the player in the game"""

    fan_duel_position: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelPosition")
    """The player's eligible position in FanDuel's daily fantasy sports platform."""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The player's eligible position in DraftKings' daily fantasy sports platform."""

    yahoo_position: OptionalNullable[str] = Field(default=UNSET, alias="YahooPosition")
    """The player's eligible position in Yahoo's daily fantasy sports platform"""

    opponent_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRank")
    """The ranking of the player's opponent with regards to fantasy points allowed"""

    opposition_position_rank: OptionalNullable[int] = Field(default=UNSET, alias="OppositionPositionRank")
    """The ranking of the player's opponent by position with regards to fantasy points allowed"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time of the late update made to this record (in US Eastern Time)"""


class FantasyGame2Dict(TypedDict):
    game_id: NotRequired[int]
    player_id: NotRequired[int]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    team: NotRequired[str | None]
    opponent: NotRequired[str | None]
    home_or_away: NotRequired[str | None]
    jersey: NotRequired[int | None]
    name: NotRequired[str | None]
    position: NotRequired[str | None]
    position_category: NotRequired[str | None]
    games: NotRequired[int | None]
    started: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    fantasy_points_batting: NotRequired[float | None]
    fantasy_points_pitching: NotRequired[float | None]
    is_game_over: NotRequired[bool | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    fan_duel_position: NotRequired[str | None]
    draft_kings_position: NotRequired[str | None]
    yahoo_position: NotRequired[str | None]
    opponent_rank: NotRequired[int | None]
    opposition_position_rank: NotRequired[int | None]
    global_game_id: NotRequired[int | None]
    updated: NotRequired[str | None]
