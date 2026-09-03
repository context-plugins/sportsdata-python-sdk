from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game17 import Game17, Game17Dict
from .season6 import Season6, Season6Dict
from .season11 import Season11, Season11Dict
from .team_detail import TeamDetail, TeamDetailDict


class CompetitionDetail(SdkBaseModel):
    current_season: Optional[Season11] = Field(default=UNSET, alias="CurrentSeason")
    """The current active season for this competition/league"""

    teams: Optional[list[TeamDetail]] = Field(default=UNSET, alias="Teams")
    """The list of active teams associated with this competition"""

    games: Optional[list[Game17]] = Field(default=UNSET, alias="Games")
    """The complete schedule for the current season of this competition/league"""

    competition_id: Optional[int] = Field(default=UNSET, alias="CompetitionId")
    """The unique ID of the competition/league"""

    area_id: Optional[int] = Field(default=UNSET, alias="AreaId")
    """The unique ID of the area where this competition/league is played"""

    area_name: OptionalNullable[str] = Field(default=UNSET, alias="AreaName")
    """The display name of the area where this competition/league is played"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The display name of the competition/league"""

    gender: OptionalNullable[str] = Field(default=UNSET, alias="Gender")
    """The gender of the players on the team Possible Values: Male; Female"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of this competition/league Possible values: Club; International"""

    format: OptionalNullable[str] = Field(default=UNSET, alias="Format")
    """The format of the competition/league. Possible values: Domestic League; International Cup"""

    seasons: Optional[list[Season6]] = Field(default=UNSET, alias="Seasons")
    """The seasons associated with this competition/league"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """The unique string key of the competition/league"""


class CompetitionDetailDict(TypedDict):
    current_season: NotRequired[Season11 | Season11Dict]
    teams: NotRequired[list[TeamDetail | TeamDetailDict]]
    games: NotRequired[list[Game17 | Game17Dict]]
    competition_id: NotRequired[int]
    area_id: NotRequired[int]
    area_name: NotRequired[str | None]
    name: NotRequired[str | None]
    gender: NotRequired[str | None]
    type_: NotRequired[str | None]
    format: NotRequired[str | None]
    seasons: NotRequired[list[Season6 | Season6Dict]]
    key: NotRequired[str | None]
