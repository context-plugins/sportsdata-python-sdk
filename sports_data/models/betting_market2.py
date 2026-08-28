from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_outcome2 import BettingOutcome2, BettingOutcome2Dict
from .consensus_outcome2 import ConsensusOutcome2, ConsensusOutcome2Dict
from .sportsbook import Sportsbook, SportsbookDict


class BettingMarket2(SdkBaseModel):
    betting_market_id: Optional[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID associated with the betting event"""

    betting_market_type_id: Optional[int] = Field(default=UNSET, alias="BettingMarketTypeID")
    """ID that distinguishes the different types of Market Types"""

    betting_market_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingMarketType")
    """The name of the Market Type (e.g. Fighter Prop, Fight Prop, etc.)"""

    betting_bet_type_id: Optional[int] = Field(default=UNSET, alias="BettingBetTypeID")
    """The ID associated with the name of the bet type within a market"""

    betting_bet_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingBetType")
    """The name of the bet type within a market"""

    betting_period_type_id: Optional[int] = Field(default=UNSET, alias="BettingPeriodTypeID")
    """The BettingPeriodTypeID of this type of market which we can result"""

    betting_period_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingPeriodType")
    """The BettingPeriodType of this market (e.g. Full Fight; 1st Round, etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the betting market"""

    fighter_id: OptionalNullable[int] = Field(default=UNSET, alias="FighterId")
    """The unique ID of the fighter tied to this market (where applicable)"""

    fighter_name: OptionalNullable[str] = Field(default=UNSET, alias="FighterName")
    """The full name of the fighter tied to this market (where applicable)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when this market was created"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The updated timestamp of this market (in US Eastern Time)"""

    available_sportsbooks: Optional[list[Sportsbook]] = Field(default=UNSET, alias="AvailableSportsbooks")
    """The sportsbooks which have had odds in this market"""

    any_bets_available: Optional[bool] = Field(default=UNSET, alias="AnyBetsAvailable")
    """A field that returns "True" if there are any available bets to make within the market in question. If there are
    no bets available to make, the field returns "False"
    """

    betting_outcomes: Optional[list[BettingOutcome2]] = Field(default=UNSET, alias="BettingOutcomes")
    """The list of betting outcomes from each sportsbook in the market"""

    consensus_outcomes: Optional[list[ConsensusOutcome2]] = Field(default=UNSET, alias="ConsensusOutcomes")
    """The single set of consensus outcomes of this market"""


class BettingMarket2Dict(TypedDict):
    betting_market_id: NotRequired[int]
    betting_event_id: NotRequired[int]
    betting_market_type_id: NotRequired[int]
    betting_market_type: NotRequired[str | None]
    betting_bet_type_id: NotRequired[int]
    betting_bet_type: NotRequired[str | None]
    betting_period_type_id: NotRequired[int]
    betting_period_type: NotRequired[str | None]
    name: NotRequired[str | None]
    fighter_id: NotRequired[int | None]
    fighter_name: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    available_sportsbooks: NotRequired[list[Sportsbook | SportsbookDict]]
    any_bets_available: NotRequired[bool]
    betting_outcomes: NotRequired[list[BettingOutcome2 | BettingOutcome2Dict]]
    consensus_outcomes: NotRequired[list[ConsensusOutcome2 | ConsensusOutcome2Dict]]
