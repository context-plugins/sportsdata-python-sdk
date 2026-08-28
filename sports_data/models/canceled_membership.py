from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CanceledMembership(SdkBaseModel):
    canceled_membership_id: Optional[int] = Field(default=UNSET, alias="CanceledMembershipId")
    """The unique ID of the canceled membership"""

    membership_id: Optional[int] = Field(default=UNSET, alias="MembershipId")
    """The unique ID of the membership which is being canceled; should be used to find memberships which may be safely
    deleted."""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team associated with this canceled membership"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time when this canceled membership was created"""


class CanceledMembershipDict(TypedDict):
    canceled_membership_id: NotRequired[int]
    membership_id: NotRequired[int]
    team_id: NotRequired[int]
    player_id: NotRequired[int]
    created: NotRequired[str | None]
