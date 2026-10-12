from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .betting_entity_metadata1 import BettingEntityMetadata1, BettingEntityMetadata1Dict


class BettingEntityMetadataCollection1(SdkBaseModel):
    betting_bet_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingBetTypes")
    """The list of the bet types that can be found within a market"""

    betting_market_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingMarketTypes")
    """A list of the possible market types within a Betting Event (e.g. Game Line, Team prop, Player Future, etc.)"""

    betting_period_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingPeriodTypes")
    """The name of the period type of a market (e.g. Regular Season; 1st half; 90 Minutes and Stoppage Time; etc.)"""

    betting_event_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingEventTypes")
    """A list of the possible BettingEventTypes (e.g. Game, Future)"""

    betting_outcome_types: Optional[list[BettingEntityMetadata1]] = Field(default=UNSET, alias="BettingOutcomeTypes")
    """A list of the possible BettingOutcomeTypes (e.g. Home; Away; Under; Over)"""


class BettingEntityMetadataCollection1Dict(TypedDict):
    betting_bet_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_market_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_period_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_event_types: NotRequired[list[BettingEntityMetadata1Dict]]
    betting_outcome_types: NotRequired[list[BettingEntityMetadata1Dict]]
