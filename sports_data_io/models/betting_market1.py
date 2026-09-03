from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_outcome1 import BettingOutcome1, BettingOutcome1Dict
from .consensus_outcome1 import ConsensusOutcome1, ConsensusOutcome1Dict
from .sportsbook import Sportsbook, SportsbookDict


class BettingMarket1(SdkBaseModel):
    betting_market_id: Optional[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID of the betting market"""

    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID assocated with the betting event"""

    betting_market_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingMarketTypeID")
    """The unique ID associated with the name of the market type"""

    betting_market_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingMarketType")
    """The name of the market type within a betting market (e.g. Player Prop, Team Prop, Game Prop, etc.)"""

    betting_bet_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingBetTypeID")
    """The ID associated with the name of the bet type within a market"""

    betting_bet_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingBetType")
    """The name of the bet type within a market (e.g. Spread, Moneyline, Total Goals, etc.)"""

    betting_period_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingPeriodTypeID")
    """The ID associated with the betting period type which we can result"""

    betting_period_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingPeriodType")
    """The name of the period type of a market (e.g. Regular Season; 1st half; 90 Minutes and Stoppage Time; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this betting market"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team associated with betting market"""

    team_key: OptionalNullable[str] = Field(default=UNSET, alias="TeamKey")
    """The abbreviation [Key] of the team associated with this betting market"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career"""

    player_name: OptionalNullable[str] = Field(default=UNSET, alias="PlayerName")
    """The player's full name tied to this betting market"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The created date of this market (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the betting market record was last updated (US Eastern Time)"""

    available_sportsbooks: Optional[list[Sportsbook]] = Field(default=UNSET, alias="AvailableSportsbooks")
    """The sportsbooks that have had odds in this market"""

    any_bets_available: OptionalNullable[bool] = Field(default=UNSET, alias="AnyBetsAvailable")
    """Shows if any bets are currently available for betting in this market"""

    betting_outcomes: Optional[list[BettingOutcome1]] = Field(default=UNSET, alias="BettingOutcomes")
    """The list of betting outcomes from each sportsbook in this market"""

    consensus_outcomes: Optional[list[ConsensusOutcome1]] = Field(default=UNSET, alias="ConsensusOutcomes")
    """The single set of consesnus outcomes of this market"""


class BettingMarket1Dict(TypedDict):
    betting_market_id: NotRequired[int]
    betting_event_id: NotRequired[int]
    betting_market_type_id: NotRequired[int | None]
    betting_market_type: NotRequired[str | None]
    betting_bet_type_id: NotRequired[int | None]
    betting_bet_type: NotRequired[str | None]
    betting_period_type_id: NotRequired[int | None]
    betting_period_type: NotRequired[str | None]
    name: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team_key: NotRequired[str | None]
    player_id: NotRequired[int | None]
    player_name: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    available_sportsbooks: NotRequired[list[Sportsbook | SportsbookDict]]
    any_bets_available: NotRequired[bool | None]
    betting_outcomes: NotRequired[list[BettingOutcome1 | BettingOutcome1Dict]]
    consensus_outcomes: NotRequired[list[ConsensusOutcome1 | ConsensusOutcome1Dict]]
