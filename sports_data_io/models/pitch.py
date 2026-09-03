from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Pitch(SdkBaseModel):
    pitch_id: Optional[int] = Field(default=UNSET, alias="PitchID")
    """The unique ID of the pitch"""

    play_id: Optional[int] = Field(default=UNSET, alias="PlayID")
    """The unique ID of the play assigned by SportsDataIO"""

    pitch_number_this_at_bat: OptionalNullable[int] = Field(default=UNSET, alias="PitchNumberThisAtBat")
    """The number of pitches in the at bat in which the pitch occurred."""

    pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="PitcherID")
    """The PlayerID of the pitcher who threw the pitch"""

    hitter_id: OptionalNullable[int] = Field(default=UNSET, alias="HitterID")
    """The unique PlayerID of the hitter who represents the play"""

    outs: OptionalNullable[int] = Field(default=UNSET, alias="Outs")
    """The number of outs when the pitch occurred"""

    balls_before_pitch: OptionalNullable[int] = Field(default=UNSET, alias="BallsBeforePitch")
    """The number of balls the pitcher has thrown before the current pitch"""

    strikes_before_pitch: OptionalNullable[int] = Field(default=UNSET, alias="StrikesBeforePitch")
    """The number of strikes the pitcher has thrown before the current pitch"""

    strike: OptionalNullable[bool] = Field(default=UNSET, alias="Strike")
    """Whether the pitch was a strike (true/false)"""

    ball: OptionalNullable[bool] = Field(default=UNSET, alias="Ball")
    """Whether the pitch was a ball (true/false)"""

    foul: OptionalNullable[bool] = Field(default=UNSET, alias="Foul")
    """Whether the pitch was hit foul (true/false)"""

    swinging: OptionalNullable[bool] = Field(default=UNSET, alias="Swinging")
    """Whether the hitter struck out swinging (true/false)"""

    looking: OptionalNullable[bool] = Field(default=UNSET, alias="Looking")
    """Whether or not the hitter struck out looking (returns true/false)"""


class PitchDict(TypedDict):
    pitch_id: NotRequired[int]
    play_id: NotRequired[int]
    pitch_number_this_at_bat: NotRequired[int | None]
    pitcher_id: NotRequired[int | None]
    hitter_id: NotRequired[int | None]
    outs: NotRequired[int | None]
    balls_before_pitch: NotRequired[int | None]
    strikes_before_pitch: NotRequired[int | None]
    strike: NotRequired[bool | None]
    ball: NotRequired[bool | None]
    foul: NotRequired[bool | None]
    swinging: NotRequired[bool | None]
    looking: NotRequired[bool | None]
