from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .team7 import Team7, Team7Dict


class Conference2(SdkBaseModel):
    conference_id: Optional[int] = Field(default=UNSET, alias="ConferenceID")
    """The ID of the team's conference"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the team's conference (e.g. American Conference; Big Ten Conference; Conference USA)"""

    teams: Optional[list[Team7]] = Field(default=UNSET, alias="Teams")
    """The list of teams within the conference"""


class Conference2Dict(TypedDict):
    conference_id: NotRequired[int]
    name: NotRequired[str | None]
    teams: NotRequired[list[Team7 | Team7Dict]]
