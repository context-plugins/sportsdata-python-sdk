from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerLine(SdkBaseModel):
    line_number: Optional[int] = Field(default=UNSET, alias="LineNumber")
    """The line the player is on (e.g. 1, 2, 3, or 4)"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: C; RW; LW; D; or G"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the player on the line"""

    shoots: OptionalNullable[str] = Field(default=UNSET, alias="Shoots")
    """The hand the player shoots the puck with (right or left)"""

    line_type: OptionalNullable[str] = Field(default=UNSET, alias="LineType")
    """The type of line the player is on (e.g. EvenStrength (EV); PowerPlay (PP); ShortHanded (SH))"""


class PlayerLineDict(TypedDict):
    line_number: NotRequired[int]
    position: NotRequired[str | None]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    shoots: NotRequired[str | None]
    line_type: NotRequired[str | None]
