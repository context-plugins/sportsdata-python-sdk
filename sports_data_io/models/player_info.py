from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerInfo(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that the player is on. Note: If the player is a free agent; this field is NULL"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on. Note: If this player is a free agent; this field is
    NULL"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The primary position of the player. Possible Values: C; CB; DB; DE; DL; DT; FB; FS; G; ILB; K; KR; LB; LS; NT;
    OL; OLB; OT; P; QB; RB; S; SS; T; TE; WR"""


class PlayerInfoDict(TypedDict):
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
