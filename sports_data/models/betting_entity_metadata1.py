from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BettingEntityMetadata1(SdkBaseModel):
    record_id: Optional[int] = Field(default=UNSET, alias="RecordID")
    """The ID of the record. Unique only within the same entity type (i.e. BettingMarketType Ids overlap with
    BettingBetType Ids)."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Denotes the name of the type (e.g. Betting Market Type, Betting Event Type, Betting Period Type)"""

    active: OptionalNullable[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this market is currently in use"""


class BettingEntityMetadata1Dict(TypedDict):
    record_id: NotRequired[int]
    name: NotRequired[str | None]
    active: NotRequired[bool | None]
