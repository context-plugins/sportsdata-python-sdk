from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PenaltyShootout(SdkBaseModel):
    penalty_shootout_id: Optional[int] = Field(default=UNSET, alias="PenaltyShootoutId")
    """The unique ID of the penalty shootout"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of the game tied to this penalty shootout"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The result of this penalty shootout kick. Possible values: Goal; Miss."""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerId")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the player in the penalty shootout"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The position of the player. Possible values include: A (Attacker); M (Midfielder); D (Defender); GK
    (Goalkeeper)."""

    order: Optional[int] = Field(default=UNSET, alias="Order")
    """The order of the penalty shootout"""


class PenaltyShootoutDict(TypedDict):
    penalty_shootout_id: NotRequired[int]
    game_id: NotRequired[int]
    type_: NotRequired[str | None]
    team_id: NotRequired[int]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    position: NotRequired[str | None]
    order: NotRequired[int]
