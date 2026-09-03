from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BettingResultingMetadata(SdkBaseModel):
    betting_market_type_id: Optional[int] = Field(default=UNSET, alias="BettingMarketTypeId")
    """The unique ID associated with the market type of the betting market"""

    betting_bet_type_id: Optional[int] = Field(default=UNSET, alias="BettingBetTypeId")
    """The ID associated with the name of the bet type within a market"""

    betting_period_type_id: Optional[int] = Field(default=UNSET, alias="BettingPeriodTypeId")
    """The BettingPeriodTypeID of this market"""


class BettingResultingMetadataDict(TypedDict):
    betting_market_type_id: NotRequired[int]
    betting_bet_type_id: NotRequired[int]
    betting_period_type_id: NotRequired[int]
