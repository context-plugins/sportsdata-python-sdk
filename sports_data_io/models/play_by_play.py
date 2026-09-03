from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .play import Play, PlayDict
from .quarter import Quarter, QuarterDict
from .score4 import Score4, Score4Dict


class PlayByPlay(SdkBaseModel):
    score: Optional[Score4] = Field(default=UNSET, alias="Score")
    """The score object and other game details of the given game"""

    quarters: Optional[list[Quarter]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters (including overtime periods) for the given game"""

    plays: Optional[list[Play]] = Field(default=UNSET, alias="Plays")
    """The list of plays for the given game"""


class PlayByPlayDict(TypedDict):
    score: NotRequired[Score4 | Score4Dict]
    quarters: NotRequired[list[Quarter | QuarterDict]]
    plays: NotRequired[list[Play | PlayDict]]
