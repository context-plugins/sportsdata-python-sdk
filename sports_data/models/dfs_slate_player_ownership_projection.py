from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DfsSlatePlayerOwnershipProjection(SdkBaseModel):
    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)."""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """Unique ID of the Associated Player."""

    projected_ownership_percentage: Optional[float] = Field(default=UNSET, alias="ProjectedOwnershipPercentage")
    """Projected Ownership Percentage (0-100)"""


class DfsSlatePlayerOwnershipProjectionDict(TypedDict):
    slate_id: NotRequired[int]
    player_id: NotRequired[int]
    projected_ownership_percentage: NotRequired[float]
