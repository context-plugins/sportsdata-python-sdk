from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .sportsbook import Sportsbook, SportsbookDict


class BettingOutcome2(SdkBaseModel):
    betting_outcome_id: Optional[int] = Field(default=UNSET, alias="BettingOutcomeID")
    """The unique ID of this outcome"""

    betting_market_id: Optional[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    sportsbook: Optional[Sportsbook] = Field(default=UNSET, alias="Sportsbook")
    """The sportsbook offering this outcome for betting"""

    betting_outcome_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeTypeID")
    """The BettingOutcomeTypeID of this outcome"""

    betting_outcome_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingOutcomeType")
    """The name of Betting Outcome Type (e.g. Under; Over; etc.)"""

    payout_american: Optional[int] = Field(default=UNSET, alias="PayoutAmerican")
    """The American odds payout"""

    payout_decimal: OptionalNullable[float] = Field(default=UNSET, alias="PayoutDecimal")
    """The decimal odds payout"""

    value: OptionalNullable[float] = Field(default=UNSET, alias="Value")
    """The number/handicap associated with the outcome (spread/total/etc.,)"""

    participant: OptionalNullable[str] = Field(default=UNSET, alias="Participant")
    """The name of the participant (typically team or player) associated with the outcome. NOTE: This is provided by the
    sportsbook. In the case of Player odds, we highly recommend using PlayerID as names of players can be inconsistent
    between sportsbooks."""

    is_available: Optional[bool] = Field(default=UNSET, alias="IsAvailable")
    """Indicates if this outcome is available for betting as of the last update"""

    is_alternate: OptionalNullable[bool] = Field(default=UNSET, alias="IsAlternate")
    """Indicates if this is an alternate value or the core value"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when the betting outcome was created"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The last updated timestamp of the outcome (in US Eastern Time)"""

    fighter_id: OptionalNullable[int] = Field(default=UNSET, alias="FighterId")
    """The unique ID of the fighter tied to this betting outcome (where applicable)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for the sportsbook event"""

    unlisted: OptionalNullable[str] = Field(default=UNSET, alias="Unlisted")
    """The datetime the outcome was unlisted (no longer available for bets)"""


class BettingOutcome2Dict(TypedDict):
    betting_outcome_id: NotRequired[int]
    betting_market_id: NotRequired[int]
    sportsbook: NotRequired[Sportsbook | SportsbookDict]
    betting_outcome_type_id: NotRequired[int | None]
    betting_outcome_type: NotRequired[str | None]
    payout_american: NotRequired[int]
    payout_decimal: NotRequired[float | None]
    value: NotRequired[float | None]
    participant: NotRequired[str | None]
    is_available: NotRequired[bool]
    is_alternate: NotRequired[bool | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    fighter_id: NotRequired[int | None]
    sportsbook_url: NotRequired[str | None]
    unlisted: NotRequired[str | None]
