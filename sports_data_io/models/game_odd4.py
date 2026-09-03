from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class GameOdd4(SdkBaseModel):
    game_odd_id: Optional[int] = Field(default=UNSET, alias="GameOddId")
    """The unique ID of this odd"""

    sportsbook: OptionalNullable[str] = Field(default=UNSET, alias="Sportsbook")
    """The name of the sportsbook"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of the game"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when these odds were first created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when these odds were last updated, based on US Eatern Time (EST/EDT). If these are the latest
    odds for this game, and they have not been updated within the last few minutes, then it indicates that there were
    problems connecting to the sportsbook."""

    home_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeMoneyLine")
    """The sportsbook's moneyline for the home team"""

    away_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayMoneyLine")
    """The sportsbook's money line for the away team"""

    draw_money_line: OptionalNullable[int] = Field(default=UNSET, alias="DrawMoneyLine")
    """The sportsbook's money line for a draw"""

    home_point_spread: OptionalNullable[float] = Field(default=UNSET, alias="HomePointSpread")
    """The sportsbook's point spread for the home team"""

    away_point_spread: OptionalNullable[float] = Field(default=UNSET, alias="AwayPointSpread")
    """The sportsbook's point spread for the away team"""

    home_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="HomePointSpreadPayout")
    """The sportsbook's point spread payout for the home team"""

    away_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="AwayPointSpreadPayout")
    """The sportsbook's point spread payout for the away team"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The sportsbook's total goals line (over/under) for the game"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for the over bet on the total goals line"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under bet on the total goals line"""

    sportsbook_id: OptionalNullable[int] = Field(default=UNSET, alias="SportsbookId")
    """The unique ID of the sportsbook"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""

    home_team_asian_handicap: OptionalNullable[float] = Field(default=UNSET, alias="HomeTeamAsianHandicap")
    """The sportsbook's asian handicap for the home team"""

    away_team_asian_handicap: OptionalNullable[float] = Field(default=UNSET, alias="AwayTeamAsianHandicap")
    """The sportsbook's asian handicap for the away team"""

    home_team_asian_handicap_payout: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamAsianHandicapPayout")
    """The sportsbook's Asian handicap payout for the home team"""

    away_team_asian_handicap_payout: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamAsianHandicapPayout")
    """The sportsbook's asian handicap payout for the away team covering"""

    asian_total: OptionalNullable[float] = Field(default=UNSET, alias="AsianTotal")
    """The sportsbook's asian total for the game"""

    asian_total_over_payout: OptionalNullable[int] = Field(default=UNSET, alias="AsianTotalOverPayout")
    """The sportsbook's payout for a result over the asian total"""

    asian_total_under_payout: OptionalNullable[int] = Field(default=UNSET, alias="AsianTotalUnderPayout")
    """The sportsbook's payout for a result under the asian total"""

    odd_type: OptionalNullable[str] = Field(default=UNSET, alias="OddType")
    """The market type of the odd (ex: live; pregame; 90 minutes + stoppage time; etc.)"""


class GameOdd4Dict(TypedDict):
    game_odd_id: NotRequired[int]
    sportsbook: NotRequired[str | None]
    game_id: NotRequired[int]
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
    sportsbook_url: NotRequired[str | None]
    home_team_asian_handicap: NotRequired[float | None]
    away_team_asian_handicap: NotRequired[float | None]
    home_team_asian_handicap_payout: NotRequired[int | None]
    away_team_asian_handicap_payout: NotRequired[int | None]
    asian_total: NotRequired[float | None]
    asian_total_over_payout: NotRequired[int | None]
    asian_total_under_payout: NotRequired[int | None]
    odd_type: NotRequired[str | None]
