from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BettingEntityMetadata2(SdkBaseModel):
    record_id: Optional[int] = Field(default=UNSET, alias="RecordId")
    """The ID of the record. Unique only within the same entity type (i.e. BettingMarketType IDs overlap with
    BettingBetType IDs)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """A text value for the record (e.g. Moneyline; Player Prop; 3rd Quarter)"""


class BettingEntityMetadata2Dict(TypedDict):
    record_id: NotRequired[int]
    name: NotRequired[str | None]
