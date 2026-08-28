from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .team1 import Team1, Team1Dict


class Conference1(SdkBaseModel):
    conference_id: Optional[int] = Field(default=UNSET, alias="ConferenceID")
    """The unique ID of the team's conference"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the team's conference"""

    teams: Optional[list[Team1]] = Field(default=UNSET, alias="Teams")
    """The teams that play within this conference"""

    conference_name: OptionalNullable[str] = Field(default=UNSET, alias="ConferenceName")
    """The name of the team's parent conference (e.g. SEC, Big Ten, etc)"""

    division_name: OptionalNullable[str] = Field(default=UNSET, alias="DivisionName")
    """The name of the team's division (e.g. East; West; Atlantic; etc). Note: Not all conferences have divisons"""


class Conference1Dict(TypedDict):
    conference_id: NotRequired[int]
    name: NotRequired[str | None]
    teams: NotRequired[list[Team1 | Team1Dict]]
    conference_name: NotRequired[str | None]
    division_name: NotRequired[str | None]
