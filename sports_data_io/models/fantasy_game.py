from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FantasyGame(SdkBaseModel):
    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO tied to this FantasyGame record Note: this ID will
    stay with the player throughout their entire career"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this player corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)."""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the game"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game (in US Eastern Time)"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Whether the team is home or away"""

    number: Optional[int] = Field(default=UNSET, alias="Number")
    """Player's jersey number"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The primary position of the player Possible Values: C; CB; DB; DE; DL; DT; FB; FS; G; ILB; K; KR; LB; LS; NT; OL;
    OLB; OT; P; QB; RB; S; SS; T; TE; WR"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The category of the player's position (OFF; DEF; ST)"""

    activated: Optional[int] = Field(default=UNSET, alias="Activated")
    """Whether or not the player was active for the game"""

    played: Optional[int] = Field(default=UNSET, alias="Played")
    """Whether the player played at least one snap in the game Note: Will return "1" if player played at least one snap
    and "0" if they did not"""

    started: Optional[int] = Field(default=UNSET, alias="Started")
    """Whether the player started the game (on offensive or defense) Note: Started = 1 / Did Not Start = 0"""

    fantasy_points: Optional[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points by the player in the game"""

    fantasy_points_ppr: Optional[float] = Field(default=UNSET, alias="FantasyPointsPPR")
    """Fantasy points scored based on basic PPR fantasy scoring system by the player in the game"""

    fantasy_position: OptionalNullable[str] = Field(default=UNSET, alias="FantasyPosition")
    """The player's fantasy football position Possible values: QB; RB; WR; TE; DL; LB; DB; K; P; OL"""

    is_game_over: OptionalNullable[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether the game is over (true/false)"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Fantasy points based on FanDuel's scoring system by the player in the game"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Fantasy points based on Yahoo's daily fantasy scoring system by the player in the game"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total DraftKings daily fantasy points scored by the player in the game"""

    fan_duel_position: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelPosition")
    """The player's eligible position in FanDuel's daily fantasy sports platform"""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The player's eligible position in DraftKings' daily fantasy sports platform"""

    yahoo_position: OptionalNullable[str] = Field(default=UNSET, alias="YahooPosition")
    """The player's eligible position in Yahoo's daily fantasy sports platform"""

    opponent_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRank")
    """The ranking of the player's opponent with regards to fantasy points allowed"""

    opponent_position_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPositionRank")
    """The ranking of the player's opponent by position with regards to fantasy points allowed"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """Time of last update (in US Eastern time) Note: this does not indicate that stats changed"""


class FantasyGameDict(TypedDict):
    game_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    season_type: NotRequired[int]
    season: NotRequired[int]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    week: NotRequired[int]
    team: NotRequired[str | None]
    opponent: NotRequired[str | None]
    home_or_away: NotRequired[str | None]
    number: NotRequired[int]
    name: NotRequired[str | None]
    position: NotRequired[str | None]
    position_category: NotRequired[str | None]
    activated: NotRequired[int]
    played: NotRequired[int]
    started: NotRequired[int]
    fantasy_points: NotRequired[float]
    fantasy_points_ppr: NotRequired[float]
    fantasy_position: NotRequired[str | None]
    is_game_over: NotRequired[bool | None]
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
