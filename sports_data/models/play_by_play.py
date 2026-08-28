from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game51 import Game51, Game51Dict
from .play import Play, PlayDict


class PlayByPlay(SdkBaseModel):
    game: Optional[Game51] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this play-by-play"""

    plays: Optional[list[Play]] = Field(default=UNSET, alias="Plays")
    """The details of the plays associated with this play-by-play"""


class PlayByPlayDict(TypedDict):
    game: NotRequired[Game51 | Game51Dict]
    plays: NotRequired[list[Play | PlayDict]]
