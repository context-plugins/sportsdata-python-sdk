from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerRoundScore(SdkBaseModel):
    player_round_id: Optional[int] = Field(default=UNSET, alias="PlayerRoundId")
    """The unique ID of this golfer/round combination"""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """The number of the round associated with this score"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date that this round is being played on"""

    par: OptionalNullable[int] = Field(default=UNSET, alias="Par")
    """The par of the course this round is played on"""

    score: OptionalNullable[int] = Field(default=UNSET, alias="Score")
    """The total strokes this golfer has for this round in the tournament"""

    tee_time: OptionalNullable[str] = Field(default=UNSET, alias="TeeTime")
    """The time that this golfer tees off for the upcoming round (in US Eastern Time)"""

    is_withdrawn: Optional[bool] = Field(default=UNSET, alias="IsWithdrawn")
    """Indicates whether the player has withdrawn from the tournament"""


class PlayerRoundScoreDict(TypedDict):
    player_round_id: NotRequired[int]
    number: NotRequired[int | None]
    day: NotRequired[str | None]
    par: NotRequired[int | None]
    score: NotRequired[int | None]
    tee_time: NotRequired[str | None]
    is_withdrawn: NotRequired[bool]
