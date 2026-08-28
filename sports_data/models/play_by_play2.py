from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .play2 import Play2, Play2Dict
from .quarter1 import Quarter1, Quarter1Dict
from .score4 import Score4, Score4Dict


class PlayByPlay2(SdkBaseModel):
    score: Optional[Score4] = Field(default=UNSET, alias="Score")
    """The score object and other game details of the given game"""

    quarters: Optional[list[Quarter1]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters (including overtime periods) for the given game"""

    plays: Optional[list[Play2]] = Field(default=UNSET, alias="Plays")
    """The list of plays for the given game"""


class PlayByPlay2Dict(TypedDict):
    score: NotRequired[Score4 | Score4Dict]
    quarters: NotRequired[list[Quarter1 | Quarter1Dict]]
    plays: NotRequired[list[Play2 | Play2Dict]]
