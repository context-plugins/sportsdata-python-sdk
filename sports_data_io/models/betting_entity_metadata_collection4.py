from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .betting_entity_metadata1 import BettingEntityMetadata1, BettingEntityMetadata1Dict


class BettingEntityMetadataCollection4(SdkBaseModel):
    betting_bet_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingBetTypes")
    """A list of the bet types that can be found within a market (e.g. Total Significant Strikes Landed; To Win by
    Unanimous Decision; Moneyline)"""

    betting_market_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingMarketTypes")
    """A list of the possible market types that can be found within a market (e.g. Fight Line; Fighter Prop)"""

    betting_period_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingPeriodTypes")
    """A list of the period types that can be found within a market (e.g. Round 1; Round 2; Full Fight)"""

    betting_event_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingEventTypes")
    """A list of the possible betting events"""

    betting_outcome_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingOutcomeTypes")
    """A list of the possible BettingOutcomeTypes (e.g. Under; Over; X+; etc.)"""


class BettingEntityMetadataCollection4Dict(TypedDict):
    betting_bet_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_market_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_period_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_event_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_outcome_types: NotRequired[list[BettingEntityMetadata1Dict]]
