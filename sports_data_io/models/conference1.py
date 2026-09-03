from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .team5 import Team5, Team5Dict


class Conference1(SdkBaseModel):
    conference_id: Optional[int] = Field(default=UNSET, alias="ConferenceID")
    """The ID of the team's conference"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the team's conference (e.g. American Athletic, Big Ten, Conference USA)"""

    teams: Optional[list[Team5]] = Field(default=UNSET, alias="Teams")
    """The college teams within this conference"""


class Conference1Dict(TypedDict):
    conference_id: NotRequired[int]
    name: NotRequired[str | None]
    teams: NotRequired[list[Team5 | Team5Dict]]
