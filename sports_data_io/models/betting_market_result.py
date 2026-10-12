from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_outcome_result import BettingOutcomeResult, BettingOutcomeResultDict


class BettingMarketResult(SdkBaseModel):
    betting_market_id: Optional[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    betting_market_type_id: Optional[int] = Field(default=UNSET, alias="BettingMarketTypeID")
    """The unique ID associated with the market type of the betting market"""

    betting_market_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingMarketType")
    """The name of the market type within a market (e.g. Player Prop, Team Prop, Game Prop, etc.)"""

    betting_bet_type_id: Optional[int] = Field(default=UNSET, alias="BettingBetTypeID")
    """The ID associated with the name of the bet type within a market"""

    betting_bet_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingBetType")
    """The name of the bet type within a market (e.g. Total Points, Moneyline, Spread, etc.)"""

    betting_period_type_id: Optional[int] = Field(default=UNSET, alias="BettingPeriodTypeID")
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
    """The unique PlayerID of the player as assigned by SportsDataIO tied to this betting market result. Note: this ID
    will stay with the player throughout their entire career"""

    player_name: OptionalNullable[str] = Field(default=UNSET, alias="PlayerName")
    """The full name of the player associated with this market"""

    betting_outcome_results: Optional[list[BettingOutcomeResult]] = Field(default=UNSET, alias="BettingOutcomeResults")
    """The list of outcomes under this market with results"""

    is_market_resulting_supported: Optional[bool] = Field(default=UNSET, alias="IsMarketResultingSupported")
    """Indicates whether resulting is supported for this kind of BettingMarket (true/false)"""


class BettingMarketResultDict(TypedDict):
    betting_market_id: NotRequired[int]
    betting_market_type_id: NotRequired[int]
    betting_market_type: NotRequired[str | None]
    betting_bet_type_id: NotRequired[int]
    betting_bet_type: NotRequired[str | None]
    betting_period_type_id: NotRequired[int]
    betting_period_type: NotRequired[str | None]
    name: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team_key: NotRequired[str | None]
    player_id: NotRequired[int | None]
    player_name: NotRequired[str | None]
    betting_outcome_results: NotRequired[list[BettingOutcomeResultDict]]
    is_market_resulting_supported: NotRequired[bool]
