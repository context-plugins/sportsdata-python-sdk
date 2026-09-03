from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FantasyGame3(SdkBaseModel):
    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 5=AllStar;
    6=Exhibition)."""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The NHL season of the game"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game in US Eastern Time"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team this player is employed by"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Indicates whether the team is home or away"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: C; RW; LW; D; or G."""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """Total games played by the player in the game. NOTE: this will be 1 or 0 for single game feeds"""

    started: OptionalNullable[int] = Field(default=UNSET, alias="Started")
    """Indicates whether or not the player started the game Note: this will be one or zero for single game feeds"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points by the player in the game"""

    is_game_over: Optional[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether the game is over (returns true/false)"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Total FanDuel daily fantasy points by the player in the game"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total Yahoo daily fantasy points by the player in the game"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total DraftKings daily fantasy points by the player in the game"""

    fan_duel_position: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelPosition")
    """The player's eligible position in FanDuel's daily fantasy sports platform"""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The player's eligible position in DraftKings' daily fantasy sports platform"""

    yahoo_position: OptionalNullable[str] = Field(default=UNSET, alias="YahooPosition")
    """The player's eligible position in Yahoo's daily fantasy sports platform."""

    opponent_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRank")
    """The ranking of the player's opponent with regards to fantasy points allowed"""

    opponent_position_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPositionRank")
    """The ranking of the player's opponent by position with regards to fantasy points allowed"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (in US Eastern Time)"""


class FantasyGame3Dict(TypedDict):
    game_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
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
    games: NotRequired[int | None]
    started: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    is_game_over: NotRequired[bool]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    fan_duel_position: NotRequired[str | None]
    draft_kings_position: NotRequired[str | None]
    yahoo_position: NotRequired[str | None]
    opponent_rank: NotRequired[int | None]
    opponent_position_rank: NotRequired[int | None]
    global_game_id: NotRequired[int | None]
    updated: NotRequired[str | None]
