from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .sportsbook import Sportsbook, SportsbookDict


class BettingOutcome1(SdkBaseModel):
    betting_outcome_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeID")
    """The unique ID associated with this specific outcome"""

    betting_market_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    sports_book: Optional[Sportsbook] = Field(default=UNSET, alias="SportsBook")
    """The sportsbook offering this outcome for betting"""

    betting_outcome_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeTypeID")
    """The ID of this specific outcome type"""

    betting_outcome_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingOutcomeType")
    """The name of betting outcome type"""

    payout_american: OptionalNullable[int] = Field(default=UNSET, alias="PayoutAmerican")
    """The american odds payout"""

    payout_decimal: OptionalNullable[float] = Field(default=UNSET, alias="PayoutDecimal")
    """The decimal odds payout"""

    value: OptionalNullable[float] = Field(default=UNSET, alias="Value")
    """The number associated with the outcome (spread/total/etc)"""

    participant: OptionalNullable[str] = Field(default=UNSET, alias="Participant")
    """The name of the participant (typically team or player) associated with the outcome. NOTE: This is provided by the
    sportsbook. In the case of Player odds, we highly recommend using PlayerID as names of players can be inconsistent
    between sportsbooks."""

    is_available: OptionalNullable[bool] = Field(default=UNSET, alias="IsAvailable")
    """Indicates if this outcome is available for betting as of last update"""

    is_alternate: OptionalNullable[bool] = Field(default=UNSET, alias="IsAlternate")
    """Indicates if this is an alternate value or the core value"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when this betting outcome was created"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The last updated date of the outcome"""

    unlisted: OptionalNullable[str] = Field(default=UNSET, alias="Unlisted")
    """The datetime the outcome was unlisted (no longer available for bets)"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the golfer tied to this outcome"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""

    group_key: OptionalNullable[int] = Field(default=UNSET, alias="GroupKey")
    """A key to identify outcomes which are related and part of the same offering at a sportsbook (for instance, with
    SixShooter markets, this key would identify all the options for a particular group of golfers)"""

    is_in_play_tournament_odd: OptionalNullable[bool] = Field(default=UNSET, alias="IsInPlayTournamentOdd")
    """Indicates if this outcome is considered in-play/live (i.e. was created after the tournament start date)"""

    sportsbook_market_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookMarketID")
    """The market ID of the given sportsbook when available for deep links"""

    sportsbook_outcome_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookOutcomeID")
    """The outcome ID of the given sportsbook when available for deep links"""


class BettingOutcome1Dict(TypedDict):
    betting_outcome_id: NotRequired[int | None]
    betting_market_id: NotRequired[int | None]
    sports_book: NotRequired[Sportsbook | SportsbookDict]
    betting_outcome_type_id: NotRequired[int | None]
    betting_outcome_type: NotRequired[str | None]
    payout_american: NotRequired[int | None]
    payout_decimal: NotRequired[float | None]
    value: NotRequired[float | None]
    participant: NotRequired[str | None]
    is_available: NotRequired[bool | None]
    is_alternate: NotRequired[bool | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    unlisted: NotRequired[str | None]
    player_id: NotRequired[int | None]
    sportsbook_url: NotRequired[str | None]
    group_key: NotRequired[int | None]
    is_in_play_tournament_odd: NotRequired[bool | None]
    sportsbook_market_id: NotRequired[str | None]
    sportsbook_outcome_id: NotRequired[str | None]
