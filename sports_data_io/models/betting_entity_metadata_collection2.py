from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .betting_entity_metadata1 import BettingEntityMetadata1, BettingEntityMetadata1Dict


class BettingEntityMetadataCollection2(SdkBaseModel):
    betting_bet_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingBetTypes")
    """The list of the bet types that can be found within a market (e.g. Best Score; Tournament Winner; Top 10
    Finish)"""

    betting_market_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingMarketTypes")
    """A list of the possible market types within a betting event (e.g. Tournament Prop; Matchup Prop; Group Prop)"""

    betting_period_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingPeriodTypes")
    """A list of the possible period types within a betting event (e.g. Round 1, Through Round 2; Tournament)"""

    betting_event_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingEventTypes")
    """A list of the possible BettingEventTypes"""

    betting_outcome_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingOutcomeTypes")
    """A list of the possible betting outcomes types (e.g. Yes; No)"""


class BettingEntityMetadataCollection2Dict(TypedDict):
    betting_bet_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_market_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_period_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_event_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_outcome_types: NotRequired[list[BettingEntityMetadata1Dict]]
