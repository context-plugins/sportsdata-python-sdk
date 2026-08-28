from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Period1(SdkBaseModel):
    period_id: Optional[int] = Field(default=UNSET, alias="PeriodID")
    """Unique ID for each period"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    number: Optional[int] = Field(default=UNSET, alias="Number")
    """The Number (Order) of the Period in the scope of the Game."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the period (possible values: 1; 2; 3; 4; OT; Final, F/OT)"""

    away_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayScore")
    """The total points scored by the away team in this period"""

    home_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeScore")
    """The total points scored by the home team in this period"""


class Period1Dict(TypedDict):
    period_id: NotRequired[int]
    game_id: NotRequired[int]
    number: NotRequired[int]
    name: NotRequired[str | None]
    away_score: NotRequired[int | None]
    home_score: NotRequired[int | None]
