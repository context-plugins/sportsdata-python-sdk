from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Period(SdkBaseModel):
    period_id: Optional[int] = Field(default=UNSET, alias="PeriodID")
    """The unique ID for the period"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    number: Optional[int] = Field(default=UNSET, alias="Number")
    """The Number (Order) of the Period in the scope of the Game."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the period in the game (e.g. 1, 2, OT, OT2, etc.)"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """Indicates whether this period is the first/second half or overtime (possible values: Half, Overtime)"""

    away_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayScore")
    """The total points scored by the away team in this period only"""

    home_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeScore")
    """The total points scored by the home team in this period only"""


class PeriodDict(TypedDict):
    period_id: NotRequired[int]
    game_id: NotRequired[int]
    number: NotRequired[int]
    name: NotRequired[str | None]
    type_: NotRequired[str | None]
    away_score: NotRequired[int | None]
    home_score: NotRequired[int | None]
