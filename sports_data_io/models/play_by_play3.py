from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game52 import Game52, Game52Dict
from .play3 import Play3, Play3Dict


class PlayByPlay3(SdkBaseModel):
    game: Optional[Game52] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this play-by-play"""

    plays: Optional[list[Play3]] = Field(default=UNSET, alias="Plays")
    """List of Plays in the game"""


class PlayByPlay3Dict(TypedDict):
    game: NotRequired[Game52 | Game52Dict]
    plays: NotRequired[list[Play3 | Play3Dict]]
