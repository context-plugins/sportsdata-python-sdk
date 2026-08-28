from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DfsSlatePlayerOwnershipProjection2(SdkBaseModel):
    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)."""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """Unique ID of the Associated Player (can be null when it is a Team Defense)"""

    fantasy_defense_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDefensePlayerID")
    """Unique ID of the Team Defense (only set for Team Defenses)"""

    projected_ownership_percentage: Optional[float] = Field(default=UNSET, alias="ProjectedOwnershipPercentage")
    """Projected Ownership Percentage (0-100)"""

    is_captain: Optional[bool] = Field(default=UNSET, alias="IsCaptain")
    """Indicates if this is the MVP/Captain slot for single game slates"""


class DfsSlatePlayerOwnershipProjection2Dict(TypedDict):
    slate_id: NotRequired[int]
    player_id: NotRequired[int | None]
    fantasy_defense_player_id: NotRequired[int | None]
    projected_ownership_percentage: NotRequired[float]
    is_captain: NotRequired[bool]
