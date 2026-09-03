from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_outcome import BettingOutcome, BettingOutcomeDict
from .consensus_outcome import ConsensusOutcome, ConsensusOutcomeDict
from .sportsbook import Sportsbook, SportsbookDict


class BettingMarket(SdkBaseModel):
    betting_market_id: Optional[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID assocated with the betting event"""

    betting_market_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingMarketTypeID")
    """The unique ID associated with the market type of the betting market"""

    betting_market_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingMarketType")
    """The name of the market type within a market (e.g. Player Prop, Team Prop, Game Prop, etc.)"""

    betting_bet_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingBetTypeID")
    """The ID associated with the name of the bet type within a market"""

    betting_bet_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingBetType")
    """The name of the bet type within a market (e.g. Total Points, Moneyline, Spread, etc.)"""

    betting_period_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingPeriodTypeID")
    """The BettingPeriodTypeID of this type of market which we can result"""

    betting_period_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingPeriodType")
    """The BettingPeriodType of this market (e.g. Full Game; 1st Period; Overtime; Regular Season)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the betting market"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO tied this market (if applicable)"""

    team_key: OptionalNullable[str] = Field(default=UNSET, alias="TeamKey")
    """The abbreviation [Key] of the team tied to this market (if applicable)"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO tied to this betting market. Note: this ID will
    stay with the player throughout their entire career"""

    player_name: OptionalNullable[str] = Field(default=UNSET, alias="PlayerName")
    """The full name of the player associated with this market"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time when this betting market was created in US Eastern Time"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time of the last update made to this betting market (in US Eastern Time)"""

    available_sportsbooks: Optional[list[Sportsbook]] = Field(default=UNSET, alias="AvailableSportsbooks")
    """The sportsbooks that have had odds in this market"""

    any_bets_available: OptionalNullable[bool] = Field(default=UNSET, alias="AnyBetsAvailable")
    """A field that returns "True" if there are any available bets to make within the market in question. If there are
    no bets available to make, the field returns "False"
    """

    betting_outcomes: Optional[list[BettingOutcome]] = Field(default=UNSET, alias="BettingOutcomes")
    """The list of betting outcomes from each sportsbook in this market"""

    consensus_outcomes: Optional[list[ConsensusOutcome]] = Field(default=UNSET, alias="ConsensusOutcomes")
    """The single set of consensus outcomes of this market"""

    is_archived: Optional[bool] = Field(default=UNSET, alias="IsArchived")
    """Indicates whether a BettingOutcome has been archived or not (true/false)"""

    archive_location: OptionalNullable[str] = Field(default=UNSET, alias="ArchiveLocation")
    """If IsArchived is true, this returns the URL that can be used to retrieve the archived BettingOutcomes. An API Key
    and Sportsbook Grouping will be required to retrieve this information. If IsArchived is false, this returns an emtpy
    string"""


class BettingMarketDict(TypedDict):
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
    betting_outcomes: NotRequired[list[BettingOutcome | BettingOutcomeDict]]
    consensus_outcomes: NotRequired[list[ConsensusOutcome | ConsensusOutcomeDict]]
    is_archived: NotRequired[bool]
    archive_location: NotRequired[str | None]
