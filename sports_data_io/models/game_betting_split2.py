from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market_split import BettingMarketSplit, BettingMarketSplitDict


class GameBettingSplit2(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game tied to this split"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar)."""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The college football season of the game"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The week of the game related to this betting split"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team tied to this split"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    betting_market_splits: Optional[list[BettingMarketSplit]] = Field(default=UNSET, alias="BettingMarketSplits")
    """Shows the Market Types that have splits included for them in a given game"""


class GameBettingSplit2Dict(TypedDict):
    game_id: NotRequired[int]
    season_type: NotRequired[int]
    season: NotRequired[int]
    week: NotRequired[int]
    day: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    betting_market_splits: NotRequired[list[BettingMarketSplit | BettingMarketSplitDict]]
