from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .betting_entity_metadata import BettingEntityMetadata, BettingEntityMetadataDict
from .betting_resulting_metadata import BettingResultingMetadata, BettingResultingMetadataDict


class BettingEntityMetadataCollection(SdkBaseModel):
    betting_bet_types: Optional[list[BettingEntityMetadata]] = Field(default=UNSET, alias="BettingBetTypes")
    """The list of the bet types that can be found within a market"""

    betting_market_types: Optional[list[BettingEntityMetadata]] = Field(default=UNSET, alias="BettingMarketTypes")
    """A list of the possible Market Types within a Betting Event (e.g. Game Line, Team prop, Player Future, etc.)"""

    betting_period_types: Optional[list[BettingEntityMetadata]] = Field(default=UNSET, alias="BettingPeriodTypes")
    """A list of the possible BettingPeriodTypes (e.g. Full Game, Regulation Time, 1st Half)"""

    betting_event_types: Optional[list[BettingEntityMetadata]] = Field(default=UNSET, alias="BettingEventTypes")
    """A list of the possible BettingEventTypes (e.g. Game; Future)"""

    betting_outcome_types: Optional[list[BettingEntityMetadata]] = Field(default=UNSET, alias="BettingOutcomeTypes")
    """A list of the possible BettingOutcomeTypes (e.g. Home; Away; Under; Over)"""

    betting_result_types: Optional[list[BettingEntityMetadata]] = Field(default=UNSET, alias="BettingResultTypes")
    """A list of the possible BettingResultTypes (e.g. Win; Loss; Push; Not Resulted; Incomplete)"""

    resulted_market_meta_data: Optional[list[BettingResultingMetadata]] = Field(
        default=UNSET, alias="ResultedMarketMetaData"
    )
    """A list of the combinations of BettingMarketTypeID, BettingBetTypeID, and BettingPeriodTypeID that will be
    resulted"""


class BettingEntityMetadataCollectionDict(TypedDict):
    betting_bet_types: NotRequired[list[BettingEntityMetadata | BettingEntityMetadataDict]]
    betting_market_types: NotRequired[list[BettingEntityMetadata | BettingEntityMetadataDict]]
    betting_period_types: NotRequired[list[BettingEntityMetadata | BettingEntityMetadataDict]]
    betting_event_types: NotRequired[list[BettingEntityMetadata | BettingEntityMetadataDict]]
    betting_outcome_types: NotRequired[list[BettingEntityMetadata | BettingEntityMetadataDict]]
    betting_result_types: NotRequired[list[BettingEntityMetadata | BettingEntityMetadataDict]]
    resulted_market_meta_data: NotRequired[list[BettingResultingMetadata | BettingResultingMetadataDict]]
