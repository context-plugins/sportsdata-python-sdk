from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class GameOdd4(SdkBaseModel):
    game_odd_id: Optional[int] = Field(default=UNSET, alias="GameOddID")
    """The unique ID of this odd"""

    sportsbook: OptionalNullable[str] = Field(default=UNSET, alias="Sportsbook")
    """Name of sportsbook"""

    sportsbook_id: Optional[int] = Field(default=UNSET, alias="SportsbookID")
    """Unique ID of the Sportsbook"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    odd_type: OptionalNullable[str] = Field(default=UNSET, alias="OddType")
    """The market type of the odd (ex: live, pregame, 1st-half, 2nd-quarter)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when these odds were first created in US Eastern Time"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when this record was last updated (in US Eastern time)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for the sportsbook event"""

    home_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeMoneyLine")
    """The sportsbook's money line for the home team"""

    away_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayMoneyLine")
    """The sportsbook's money line for the away team"""

    home_point_spread: OptionalNullable[float] = Field(default=UNSET, alias="HomePointSpread")
    """The sportsbook's point spread for the home team"""

    away_point_spread: OptionalNullable[float] = Field(default=UNSET, alias="AwayPointSpread")
    """The sportsbook's point spread for the away team"""

    home_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="HomePointSpreadPayout")
    """The sportsbook's point spread payout for the home team"""

    away_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="AwayPointSpreadPayout")
    """The sportsbook's point spread payout for the away team"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The sportsbook's total points scored over or under for the game. Note: this is also known as the Total for the
    game."""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for the over"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under"""


class GameOdd4Dict(TypedDict):
    game_odd_id: NotRequired[int]
    sportsbook: NotRequired[str | None]
    sportsbook_id: NotRequired[int]
    game_id: NotRequired[int]
    odd_type: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    sportsbook_url: NotRequired[str | None]
    home_money_line: NotRequired[int | None]
    away_money_line: NotRequired[int | None]
    home_point_spread: NotRequired[float | None]
    away_point_spread: NotRequired[float | None]
    home_point_spread_payout: NotRequired[int | None]
    away_point_spread_payout: NotRequired[int | None]
    over_under: NotRequired[float | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
