from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FantasyGame4(SdkBaseModel):
    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The soccer regular season for which these totals apply"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in UTC)"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The name of the opponent team"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The position of the player. Possible values include: A (Attacker); M (Midfielder); D (Defender); GK
    (Goalkeeper)"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category"""

    started: OptionalNullable[int] = Field(default=UNSET, alias="Started")
    """The total number of games the player started"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points"""

    is_game_over: Optional[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether the game is over (true) or not (false)"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """This field is expected to be NULL"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """This field is expected to be NULL"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total DraftKings daily fantasy points scored by the player in the game"""

    fan_duel_position: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelPosition")
    """The player's eligible position in FanDuel's daily fantasy sports platform."""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The player's eligible position in DraftKings' daily fantasy sports platform."""

    yahoo_position: OptionalNullable[str] = Field(default=UNSET, alias="YahooPosition")
    """The player's eligible position in Yahoo's daily fantasy sports platform"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)"""


class FantasyGame4Dict(TypedDict):
    game_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    team: NotRequired[str | None]
    opponent: NotRequired[str | None]
    jersey: NotRequired[int | None]
    name: NotRequired[str | None]
    position: NotRequired[str | None]
    position_category: NotRequired[str | None]
    started: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    is_game_over: NotRequired[bool]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    fan_duel_position: NotRequired[str | None]
    draft_kings_position: NotRequired[str | None]
    yahoo_position: NotRequired[str | None]
    global_game_id: NotRequired[int | None]
    updated: NotRequired[str | None]
