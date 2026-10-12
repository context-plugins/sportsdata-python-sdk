from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market_split import BettingMarketSplit, BettingMarketSplitDict


class GameBettingSplit(SdkBaseModel):
    score_id: Optional[int] = Field(default=UNSET, alias="ScoreId")
    """Unique ID of the score/game"""

    game_key: OptionalNullable[str] = Field(default=UNSET, alias="GameKey")
    """A 9 digit unique code identifying the game that this record corresponds to. The GameID is composed of Season;
    SeasonType; Week and HomeTeam. Note: This value will be NULL for bye weeks"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this game corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)."""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season of the score"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week associated with this betting split (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4).
    Note: seasons after 2021 will have 3 preseason weeks"""

    date: OptionalNullable[str] = Field(default=UNSET, alias="Date")
    """The date and time of the game (in US Eastern Time)"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key} of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    betting_market_splits: Optional[list[BettingMarketSplit]] = Field(default=UNSET, alias="BettingMarketSplits")
    """Shows the Market Types that have splits included for them in a given game"""


class GameBettingSplitDict(TypedDict):
    score_id: NotRequired[int]
    game_key: NotRequired[str | None]
    season_type: NotRequired[int]
    season: NotRequired[int]
    week: NotRequired[int]
    date: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    betting_market_splits: NotRequired[list[BettingMarketSplitDict]]
