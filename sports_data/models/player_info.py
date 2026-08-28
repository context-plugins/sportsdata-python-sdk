from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerInfo(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the player's team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the player's team"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: C; PF; PG; SF; SG"""


class PlayerInfoDict(TypedDict):
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
