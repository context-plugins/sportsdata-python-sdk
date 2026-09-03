from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .betting_entity_metadata2 import BettingEntityMetadata2, BettingEntityMetadata2Dict


class BettingEntityMetadataCollection3(SdkBaseModel):
    betting_bet_types: Optional[list[BettingEntityMetadata2]] = Field(default=UNSET, alias="BettingBetTypes")
    """The list of the bet types that can be found within a market (e.g. Race Winner; Top 3 Finish)"""

    betting_market_types: Optional[list[BettingEntityMetadata2]] = Field(default=UNSET, alias="BettingMarketTypes")
    """A list of the possible market types within a betting event (e.g. Race Line; Drive Future)"""

    betting_period_types: Optional[list[BettingEntityMetadata2]] = Field(default=UNSET, alias="BettingPeriodTypes")
    """A list of the possible period types within a betting event (e.g. Race; Truck Series; Cup Series)"""

    betting_event_types: Optional[list[BettingEntityMetadata2]] = Field(default=UNSET, alias="BettingEventTypes")
    """A list of the possible BettingEventTypes"""

    betting_outcome_types: Optional[list[BettingEntityMetadata2]] = Field(default=UNSET, alias="BettingOutcomeTypes")
    """A list of the possible betting outcomes types (e.g. Yes; No)"""


class BettingEntityMetadataCollection3Dict(TypedDict):
    betting_bet_types: NotRequired[list[BettingEntityMetadata2 | BettingEntityMetadata2Dict]]
    betting_market_types: NotRequired[list[BettingEntityMetadata2 | BettingEntityMetadata2Dict]]
    betting_period_types: NotRequired[list[BettingEntityMetadata2 | BettingEntityMetadata2Dict]]
    betting_event_types: NotRequired[list[BettingEntityMetadata2 | BettingEntityMetadata2Dict]]
    betting_outcome_types: NotRequired[list[BettingEntityMetadata2 | BettingEntityMetadata2Dict]]
