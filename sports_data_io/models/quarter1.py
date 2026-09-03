from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Quarter1(SdkBaseModel):
    quarter_id: Optional[int] = Field(default=UNSET, alias="QuarterID")
    """Unique identifier for each Quarter."""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game associated with this quarter"""

    number: Optional[int] = Field(default=UNSET, alias="Number")
    """The Number (Order) of the Quarter in the scope of the Game."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The Name of the Quarter (possible values: 1, 2, 3, 4, OT, OT2, OT3, etc)"""

    away_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayScore")
    """The total points scored by the away team in the given period only"""

    home_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeScore")
    """The total points scored by the home team in the given period only"""


class Quarter1Dict(TypedDict):
    quarter_id: NotRequired[int]
    game_id: NotRequired[int]
    number: NotRequired[int]
    name: NotRequired[str | None]
    away_score: NotRequired[int | None]
    home_score: NotRequired[int | None]
