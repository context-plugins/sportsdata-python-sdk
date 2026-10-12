from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_outcome3 import BettingOutcome3, BettingOutcome3Dict
from .sportsbook import Sportsbook, SportsbookDict


class BettingMarket3(SdkBaseModel):
    betting_market_id: Optional[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID associated with the betting market within the betting event"""

    betting_market_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingMarketTypeID")
    """The ID that distinguishes the different types of Market Types"""

    betting_market_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingMarketType")
    """The name of the market type within a market (e.g. Race Prop, Driver Future, Race Line, etc.)"""

    betting_bet_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingBetTypeID")
    """The ID associated with the name of the bet type within a market"""

    betting_bet_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingBetType")
    """The name of the bet type within a market (e.g. Tournament Winner, Best Score, etc.)"""

    betting_period_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingPeriodTypeID")
    """The BettingPeriodTypeID of this type of market which we can result"""

    betting_period_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingPeriodType")
    """The name of the period type of this market"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this betting market"""

    driver_id: OptionalNullable[int] = Field(default=UNSET, alias="DriverID")
    """The unique ID of the driver tied to this market (if applicable)"""

    driver_name: OptionalNullable[str] = Field(default=UNSET, alias="DriverName")
    """The name of the driver tied to this market (if applicable)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date/time when this betting market was created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The last updated date of this market"""

    available_sportsbooks: Optional[list[Sportsbook]] = Field(default=UNSET, alias="AvailableSportsbooks")
    """The sportsbooks that have had odds in this market"""

    any_bets_available: OptionalNullable[bool] = Field(default=UNSET, alias="AnyBetsAvailable")
    """Shows if any bets are currently available for betting in this market"""

    betting_outcomes: Optional[list[BettingOutcome3]] = Field(default=UNSET, alias="BettingOutcomes")
    """A list of the possible betting outcomes from each sportsbook in this market"""


class BettingMarket3Dict(TypedDict):
    betting_market_id: NotRequired[int]
    betting_event_id: NotRequired[int]
    betting_market_type_id: NotRequired[int | None]
    betting_market_type: NotRequired[str | None]
    betting_bet_type_id: NotRequired[int | None]
    betting_bet_type: NotRequired[str | None]
    betting_period_type_id: NotRequired[int | None]
    betting_period_type: NotRequired[str | None]
    name: NotRequired[str | None]
    driver_id: NotRequired[int | None]
    driver_name: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    available_sportsbooks: NotRequired[list[SportsbookDict]]
    any_bets_available: NotRequired[bool | None]
    betting_outcomes: NotRequired[list[BettingOutcome3Dict]]
