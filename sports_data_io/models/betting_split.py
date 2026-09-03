from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BettingSplit(SdkBaseModel):
    betting_market_split_id: Optional[int] = Field(default=UNSET, alias="BettingMarketSplitID")
    """The unique ID associated with the betting split"""

    betting_market_id: Optional[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    betting_outcome_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeTypeID")
    """The unique ID associated with this BettingOutcomeType"""

    betting_outcome_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingOutcomeType")
    """The name of BettingOutcomeType (e.g. Home; Away; Under; Over)"""

    bet_percentage: OptionalNullable[int] = Field(default=UNSET, alias="BetPercentage")
    """Percentage of bets placed on a specific outcome"""

    money_percentage: OptionalNullable[int] = Field(default=UNSET, alias="MoneyPercentage")
    """The percentage of the money placed in wagers on this market taken by this type of bet"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time this betting split was created in US Eastern Time"""

    last_seen: OptionalNullable[str] = Field(default=UNSET, alias="LastSeen")
    """The date and time this set of values was last seen"""


class BettingSplitDict(TypedDict):
    betting_market_split_id: NotRequired[int]
    betting_market_id: NotRequired[int]
    betting_outcome_type_id: NotRequired[int | None]
    betting_outcome_type: NotRequired[str | None]
    bet_percentage: NotRequired[int | None]
    money_percentage: NotRequired[int | None]
    created: NotRequired[str | None]
    last_seen: NotRequired[str | None]
