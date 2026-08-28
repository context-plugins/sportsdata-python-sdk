from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BettingResultingMetadata(SdkBaseModel):
    betting_market_type_id: Optional[int] = Field(default=UNSET, alias="BettingMarketTypeId")
    """ID that distinguishes the different types of Market Types"""

    betting_bet_type_id: Optional[int] = Field(default=UNSET, alias="BettingBetTypeId")
    """The ID associated with the name of the bet type within a market that can be resulted"""

    betting_period_type_id: Optional[int] = Field(default=UNSET, alias="BettingPeriodTypeId")
    """The BettingPeriodTypeID of this type of market which we can result"""


class BettingResultingMetadataDict(TypedDict):
    betting_market_type_id: NotRequired[int]
    betting_bet_type_id: NotRequired[int]
    betting_period_type_id: NotRequired[int]
