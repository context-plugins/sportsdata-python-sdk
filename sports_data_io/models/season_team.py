from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .team11 import Team11, Team11Dict


class SeasonTeam(SdkBaseModel):
    season_team_id: Optional[int] = Field(default=UNSET, alias="SeasonTeamId")
    """Unique ID of this season/team combination"""

    season_id: Optional[int] = Field(default=UNSET, alias="SeasonId")
    """The unique ID of the season this record is associated with"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team"""

    team_name: OptionalNullable[str] = Field(default=UNSET, alias="TeamName")
    """The name of the team associated with this record"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether this team is actively associated with this season (true/false)"""

    gender: OptionalNullable[str] = Field(default=UNSET, alias="Gender")
    """The gender of the players on the team. Possible Values: Male; Female"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of season/team. Possible values: Club; National"""

    team: Optional[Team11] = Field(default=UNSET, alias="Team")
    """The details of the team for the given season/team association"""


class SeasonTeamDict(TypedDict):
    season_team_id: NotRequired[int]
    season_id: NotRequired[int]
    team_id: NotRequired[int]
    team_name: NotRequired[str | None]
    active: NotRequired[bool]
    gender: NotRequired[str | None]
    type_: NotRequired[str | None]
    team: NotRequired[Team11Dict]
