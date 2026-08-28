from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_split import BettingSplit, BettingSplitDict


class BettingMarketSplit(SdkBaseModel):
    betting_market_id: Optional[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID associated with the betting event"""

    betting_market_type_id: Optional[int] = Field(default=UNSET, alias="BettingMarketTypeID")
    """ID that distinguishes the different types of Market Types"""

    betting_market_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingMarketType")
    """The name of the market type (e.g. Player Prop, Team Prop, Game Prop, etc.)"""

    betting_bet_type_id: Optional[int] = Field(default=UNSET, alias="BettingBetTypeID")
    """The ID associated with the name of the bet type within a market"""

    betting_bet_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingBetType")
    """The name of the bet type within a market (e.g. Total Points, Moneyline, Spread, etc.)"""

    betting_period_type_id: Optional[int] = Field(default=UNSET, alias="BettingPeriodTypeID")
    """The BettingPeriodTypeID of this market"""

    betting_period_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingPeriodType")
    """The BettingPeriodType of this market (e.g. Full Game; 1st Half; 2nd Quarter; Regular Season)"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team (if applicable)"""

    team_key: OptionalNullable[str] = Field(default=UNSET, alias="TeamKey")
    """The abbreviation [Key] of the team tied to this market (if applicable)"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO (if applicable). Note: this ID will stay with the player
    throughout their collegiate career"""

    player_name: OptionalNullable[str] = Field(default=UNSET, alias="PlayerName")
    """The full name of the player associated with this market"""

    betting_splits: Optional[list[BettingSplit]] = Field(default=UNSET, alias="BettingSplits")
    """A list of betting splits for a given game"""


class BettingMarketSplitDict(TypedDict):
    betting_market_id: NotRequired[int]
    betting_event_id: NotRequired[int]
    betting_market_type_id: NotRequired[int]
    betting_market_type: NotRequired[str | None]
    betting_bet_type_id: NotRequired[int]
    betting_bet_type: NotRequired[str | None]
    betting_period_type_id: NotRequired[int]
    betting_period_type: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team_key: NotRequired[str | None]
    player_id: NotRequired[int | None]
    player_name: NotRequired[str | None]
    betting_splits: NotRequired[list[BettingSplit | BettingSplitDict]]
