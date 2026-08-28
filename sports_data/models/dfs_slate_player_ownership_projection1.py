from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DfsSlatePlayerOwnershipProjection1(SdkBaseModel):
    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)."""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """Unique ID of the Associated Player."""

    projected_ownership_percentage: Optional[float] = Field(default=UNSET, alias="ProjectedOwnershipPercentage")
    """Projected Ownership Percentage (0-100)"""

    is_captain: Optional[bool] = Field(default=UNSET, alias="IsCaptain")
    """Indicates if this is the MVP/Captain slot for single game slates"""


class DfsSlatePlayerOwnershipProjection1Dict(TypedDict):
    slate_id: NotRequired[int]
    player_id: NotRequired[int]
    projected_ownership_percentage: NotRequired[float]
    is_captain: NotRequired[bool]
