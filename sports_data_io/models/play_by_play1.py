from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game5 import Game5, Game5Dict
from .play1 import Play1, Play1Dict
from .quarter1 import Quarter1, Quarter1Dict


class PlayByPlay1(SdkBaseModel):
    game: Optional[Game5] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this play-by-play"""

    quarters: Optional[list[Quarter1]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters associated with this play-by-play"""

    plays: Optional[list[Play1]] = Field(default=UNSET, alias="Plays")
    """The details of the plays associated with this play-by-play"""


class PlayByPlay1Dict(TypedDict):
    game: NotRequired[Game5 | Game5Dict]
    quarters: NotRequired[list[Quarter1 | Quarter1Dict]]
    plays: NotRequired[list[Play1 | Play1Dict]]
