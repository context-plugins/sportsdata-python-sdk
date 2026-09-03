from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ScoringDetail(SdkBaseModel):
    game_key: OptionalNullable[str] = Field(default=UNSET, alias="GameKey")
    """A 9 digit unique code identifying the game that this record corresponds to. The GameID is composed of Season;
    SeasonType; Week and HomeTeam. Note: This value will be NULL for bye weeks"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this game corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO tied to this scoring detail. Note: this ID will
    stay with the player throughout their entire career"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season during which the score happened"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    scoring_type: OptionalNullable[str] = Field(default=UNSET, alias="ScoringType")
    """The type of scoring play (e.g. BlockedFieldGoalReturnTouchdown, BlockedPuntReturnTouchdown, FieldGoalMade,
    FieldGoalReturnTouchdown, FumbleReturnTouchdown, InterceptionReturnTouchdown, KickoffReturnTouchdown,
    PassingTouchdown, PuntReturnTouchdown, ReceivingTouchdown, RushingTouchdown, Safety)"""

    length: Optional[int] = Field(default=UNSET, alias="Length")
    """The length in yards of the score"""

    scoring_detail_id: Optional[int] = Field(default=UNSET, alias="ScoringDetailID")
    """Unique ID of this scoring detail"""

    player_game_id: Optional[int] = Field(default=UNSET, alias="PlayerGameID")
    """Unique ID of the PlayerGame record tied to this scoring detail"""

    score_id: OptionalNullable[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the score/game"""

    scoring_play_id: OptionalNullable[int] = Field(default=UNSET, alias="ScoringPlayID")
    """Unique ID of the scoring play"""


class ScoringDetailDict(TypedDict):
    game_key: NotRequired[str | None]
    season_type: NotRequired[int]
    player_id: NotRequired[int | None]
    team: NotRequired[str | None]
    season: NotRequired[int]
    week: NotRequired[int]
    scoring_type: NotRequired[str | None]
    length: NotRequired[int]
    scoring_detail_id: NotRequired[int]
    player_game_id: NotRequired[int]
    score_id: NotRequired[int | None]
    scoring_play_id: NotRequired[int | None]
