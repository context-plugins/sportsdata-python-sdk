from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dfs_slate_player_ownership_projection import (
    DfsSlatePlayerOwnershipProjection,
    DfsSlatePlayerOwnershipProjectionDict,
)


class DfsSlateWithOwnershipProjection(SdkBaseModel):
    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)."""

    operator: OptionalNullable[str] = Field(default=UNSET, alias="Operator")
    """The name of the operator who is running contests for this slate. Possible values: FanDuel, DraftKings, Yahoo,
    FantasyDraft, etc."""

    operator_slate_id: OptionalNullable[int] = Field(default=UNSET, alias="OperatorSlateID")
    """Unique ID of a slate (assigned by the operator)."""

    operator_name: OptionalNullable[str] = Field(default=UNSET, alias="OperatorName")
    """The name of the slate (assigned by the operator). Possible values: Main, Express, Arcade, Late Night, etc."""

    operator_day: OptionalNullable[str] = Field(default=UNSET, alias="OperatorDay")
    """The day that the slate begins; assigned by the operator (in US Eastern Time)"""

    operator_start_time: OptionalNullable[str] = Field(default=UNSET, alias="OperatorStartTime")
    """The date/time (in EST/EDT) that the slate begins (assigned by the operator)."""

    slate_ownership_projections: Optional[list[DfsSlatePlayerOwnershipProjection]] = Field(
        default=UNSET, alias="SlateOwnershipProjections"
    )
    """The list of projected ownership"""


class DfsSlateWithOwnershipProjectionDict(TypedDict):
    slate_id: NotRequired[int]
    operator: NotRequired[str | None]
    operator_slate_id: NotRequired[int | None]
    operator_name: NotRequired[str | None]
    operator_day: NotRequired[str | None]
    operator_start_time: NotRequired[str | None]
    slate_ownership_projections: NotRequired[
        list[DfsSlatePlayerOwnershipProjection | DfsSlatePlayerOwnershipProjectionDict]
    ]
