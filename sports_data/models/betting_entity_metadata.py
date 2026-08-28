from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BettingEntityMetadata(SdkBaseModel):
    record_id: Optional[int] = Field(default=UNSET, alias="RecordId")
    """The id of the record. Unique only within the same entity type (i.e. BettingMarketType Ids overlap with
    BettingBetType Ids)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """A text value for the record (e.g. Moneyline, Player Prop, 3rd Quarter)"""

    active: OptionalNullable[bool] = Field(default=UNSET, alias="Active")
    """Denotes the name of the type (e.g. Betting Market Type, Betting Event Type, Betting Period Type)"""


class BettingEntityMetadataDict(TypedDict):
    record_id: NotRequired[int]
    name: NotRequired[str | None]
    active: NotRequired[bool | None]
