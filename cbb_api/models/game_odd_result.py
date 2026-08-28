from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game_odd_outcome import GameOddOutcome, GameOddOutcomeDict


class GameOddResult(SdkBaseModel):
    game_odd_id: Optional[int] = Field(default=UNSET, alias="GameOddID")
    """Unique ID of this odd"""

    sportsbook: OptionalNullable[str] = Field(default=UNSET, alias="Sportsbook")
    """The name of the sportsbook"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when these odds were first created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when these odds were last updated; based on US Eastern Time. If these are the latest odds for
    this game; and they have not been updated within the last few minutes; then it indicates that there were problems
    connecting to the sportsbook."""

    home_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeMoneyLine")
    """The sportsbook's moneyline for the home team"""

    away_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayMoneyLine")
    """The sportsbook's moneyline for the away team"""

    home_point_spread: OptionalNullable[float] = Field(default=UNSET, alias="HomePointSpread")
    """The sportsbook's point spread for the home team"""

    away_point_spread: OptionalNullable[float] = Field(default=UNSET, alias="AwayPointSpread")
    """The sportsbook's point spread for the away team"""

    home_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="HomePointSpreadPayout")
    """The sportsbook's point spread payout for the home team"""

    away_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="AwayPointSpreadPayout")
    """The sportsbook's point spread payout for the away team. Note: this line is a consensus."""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The total points line (over/under) as given by the sportsbook"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The odds at which the sportsbook will pay out winning Over bets at"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under"""

    sportsbook_id: OptionalNullable[int] = Field(default=UNSET, alias="SportsbookID")
    """The unique ID associated with this sportsbook"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""

    odd_type: OptionalNullable[str] = Field(default=UNSET, alias="OddType")
    """The market type of the odd (ex: live; pregame; 1st-half; etc.)"""

    game_odd_outcome_results: Optional[list[GameOddOutcome]] = Field(default=UNSET, alias="GameOddOutcomeResults")
    """List of outcomes showing results of betting markets that were bet on for the given game"""


class GameOddResultDict(TypedDict):
    game_odd_id: NotRequired[int]
    sportsbook: NotRequired[str | None]
    game_id: NotRequired[int]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    home_money_line: NotRequired[int | None]
    away_money_line: NotRequired[int | None]
    home_point_spread: NotRequired[float | None]
    away_point_spread: NotRequired[float | None]
    home_point_spread_payout: NotRequired[int | None]
    away_point_spread_payout: NotRequired[int | None]
    over_under: NotRequired[float | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
    sportsbook_id: NotRequired[int | None]
    sportsbook_url: NotRequired[str | None]
    odd_type: NotRequired[str | None]
    game_odd_outcome_results: NotRequired[list[GameOddOutcome | GameOddOutcomeDict]]
