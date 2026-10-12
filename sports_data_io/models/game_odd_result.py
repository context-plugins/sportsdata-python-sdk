from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game_odd_outcome import GameOddOutcome, GameOddOutcomeDict


class GameOddResult(SdkBaseModel):
    game_odd_id: Optional[int] = Field(default=UNSET, alias="GameOddID")
    """The unique ID of this odd"""

    sportsbook: OptionalNullable[str] = Field(default=UNSET, alias="Sportsbook")
    """Name of sportsbook"""

    score_id: Optional[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the score/game"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when these odds were first created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when these odds were last updated, based on US Eatern Time (EST/EDT). If these are the latest
    odds for this game, and they have not been updated within the last few minutes, then it indicates that there were
    problems connecting to the sportsbook."""

    home_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeMoneyLine")
    """The sportsbook's moneyline for the home team"""

    away_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayMoneyLine")
    """The sportsbook's moneyline for the away team"""

    draw_money_line: OptionalNullable[int] = Field(default=UNSET, alias="DrawMoneyLine")
    """The sportsbook's moneyline for a draw"""

    home_point_spread: OptionalNullable[float] = Field(default=UNSET, alias="HomePointSpread")
    """The sportsbook's point spread for the home team"""

    away_point_spread: OptionalNullable[float] = Field(default=UNSET, alias="AwayPointSpread")
    """The sportsbook's point spread for the away team"""

    home_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="HomePointSpreadPayout")
    """The sportsbook's point spread payout for the home team"""

    away_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="AwayPointSpreadPayout")
    """The sportsbook's point spread payout for the away team"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The sportsbook's total points scored (over/under) for the game"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for over the total points line"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under"""

    sportsbook_id: OptionalNullable[int] = Field(default=UNSET, alias="SportsbookID")
    """Unique ID of the Sportsbook"""

    odd_type: OptionalNullable[str] = Field(default=UNSET, alias="OddType")
    """The market type of this odd (ex: live, pregame, 1st-half, 1st-qtr, etc)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    game_odd_outcome_results: Optional[list[GameOddOutcome]] = Field(default=UNSET, alias="GameOddOutcomeResults")
    """List of outcomes showing results of betting markets that were bet on for the given game"""


class GameOddResultDict(TypedDict):
    game_odd_id: NotRequired[int]
    sportsbook: NotRequired[str | None]
    score_id: NotRequired[int]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    home_money_line: NotRequired[int | None]
    away_money_line: NotRequired[int | None]
    draw_money_line: NotRequired[int | None]
    home_point_spread: NotRequired[float | None]
    away_point_spread: NotRequired[float | None]
    home_point_spread_payout: NotRequired[int | None]
    away_point_spread_payout: NotRequired[int | None]
    over_under: NotRequired[float | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
    sportsbook_id: NotRequired[int | None]
    odd_type: NotRequired[str | None]
    sportsbook_url: NotRequired[str | None]
    game_id: NotRequired[int]
    game_odd_outcome_results: NotRequired[list[GameOddOutcomeDict]]
