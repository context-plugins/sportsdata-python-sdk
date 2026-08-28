from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game52 import Game52, Game52Dict
from .play1 import Play1, Play1Dict
from .quarter import Quarter, QuarterDict


class PlayByPlay1(SdkBaseModel):
    game: Optional[Game52] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this play-by-play"""

    quarters: Optional[list[Quarter]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters associated with this play-by-play"""

    plays: Optional[list[Play1]] = Field(default=UNSET, alias="Plays")
    """The details of the plays associated with this play-by-play"""


class PlayByPlay1Dict(TypedDict):
    game: NotRequired[Game52 | Game52Dict]
    quarters: NotRequired[list[Quarter | QuarterDict]]
    plays: NotRequired[list[Play1 | Play1Dict]]
