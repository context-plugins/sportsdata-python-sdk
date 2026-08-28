from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerHole(SdkBaseModel):
    player_round_id: Optional[int] = Field(default=UNSET, alias="PlayerRoundID")
    """The unique ID of this golfer/round combination"""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """The number of the hole associated with these stats"""

    par: OptionalNullable[int] = Field(default=UNSET, alias="Par")
    """The par of this hole"""

    score: OptionalNullable[int] = Field(default=UNSET, alias="Score")
    """The golfer's total strokes on the hole"""

    to_par: OptionalNullable[int] = Field(default=UNSET, alias="ToPar")
    """The player's score on this hole (+/- par)"""

    hole_in_one: Optional[bool] = Field(default=UNSET, alias="HoleInOne")
    """Indicates whether this player shot a hole-in-one on this hole"""

    double_eagle: Optional[bool] = Field(default=UNSET, alias="DoubleEagle")
    """Indicates whether this player shot a double eagle on this hole"""

    eagle: Optional[bool] = Field(default=UNSET, alias="Eagle")
    """Indicates whether this player shot an eagle on this hole"""

    birdie: Optional[bool] = Field(default=UNSET, alias="Birdie")
    """Indicates whether this player shot a birdie on this hole"""

    is_par: Optional[bool] = Field(default=UNSET, alias="IsPar")
    """Indicates whether this player shot par on this hole"""

    bogey: Optional[bool] = Field(default=UNSET, alias="Bogey")
    """Indicates whether this player shot a bogey on this hole"""

    double_bogey: Optional[bool] = Field(default=UNSET, alias="DoubleBogey")
    """Indicates whether this player shot a double bogey on this hole"""

    worse_than_double_bogey: Optional[bool] = Field(default=UNSET, alias="WorseThanDoubleBogey")
    """Indicates whether this player shot worse than a double bogey on this hole"""


class PlayerHoleDict(TypedDict):
    player_round_id: NotRequired[int]
    number: NotRequired[int | None]
    par: NotRequired[int | None]
    score: NotRequired[int | None]
    to_par: NotRequired[int | None]
    hole_in_one: NotRequired[bool]
    double_eagle: NotRequired[bool]
    eagle: NotRequired[bool]
    birdie: NotRequired[bool]
    is_par: NotRequired[bool]
    bogey: NotRequired[bool]
    double_bogey: NotRequired[bool]
    worse_than_double_bogey: NotRequired[bool]
