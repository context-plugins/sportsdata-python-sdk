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
    """The BettingOutcomeTypeID of this outcome"""

    betting_outcome_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingOutcomeType")
    """The name of betting outcome type (e.g. Home; Away; Under; Over)"""

    bet_percentage: OptionalNullable[int] = Field(default=UNSET, alias="BetPercentage")
    """Percentage of bets placed on a specific outcome"""

    money_percentage: OptionalNullable[int] = Field(default=UNSET, alias="MoneyPercentage")
    """Percentage of money bet on this outcome"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time when this betting split was created (in US Eastern Time)"""

    last_seen: OptionalNullable[str] = Field(default=UNSET, alias="LastSeen")
    """Timestamp of when a specific betting split was last updated (in US Eastern Time)"""


class BettingSplitDict(TypedDict):
    betting_market_split_id: NotRequired[int]
    betting_market_id: NotRequired[int]
    betting_outcome_type_id: NotRequired[int | None]
    betting_outcome_type: NotRequired[str | None]
    bet_percentage: NotRequired[int | None]
    money_percentage: NotRequired[int | None]
    created: NotRequired[str | None]
    last_seen: NotRequired[str | None]
