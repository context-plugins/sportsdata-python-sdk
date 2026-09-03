from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Membership(SdkBaseModel):
    membership_id: Optional[int] = Field(default=UNSET, alias="MembershipId")
    """The unique ID for the membership"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerId")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career."""

    player_name: OptionalNullable[str] = Field(default=UNSET, alias="PlayerName")
    """The player's full name"""

    team_name: OptionalNullable[str] = Field(default=UNSET, alias="TeamName")
    """The full name of the team"""

    team_area: OptionalNullable[str] = Field(default=UNSET, alias="TeamArea")
    """The area the team is located within their home country"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether the player's membership is active (true/false)"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date of the membership (in UTC)"""

    end_date: OptionalNullable[str] = Field(default=UNSET, alias="EndDate")
    """The end date of the membership (in UTC)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number on this team"""


class MembershipDict(TypedDict):
    membership_id: NotRequired[int]
    team_id: NotRequired[int]
    player_id: NotRequired[int]
    player_name: NotRequired[str | None]
    team_name: NotRequired[str | None]
    team_area: NotRequired[str | None]
    active: NotRequired[bool]
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
    updated: NotRequired[str | None]
    jersey: NotRequired[int | None]
