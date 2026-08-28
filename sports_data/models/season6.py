from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .round1 import Round1, Round1Dict


class Season6(SdkBaseModel):
    season_id: Optional[int] = Field(default=UNSET, alias="SeasonId")
    """The unique ID of the season"""

    competition_id: Optional[int] = Field(default=UNSET, alias="CompetitionId")
    """The unique ID of the competition"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The soccer regular season for which these totals apply"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The display name of the season (e.g. 2017/2018; 2018/19; etc)"""

    competition_name: OptionalNullable[str] = Field(default=UNSET, alias="CompetitionName")
    """The display name of the competition associated with this season"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date of the season"""

    end_date: OptionalNullable[str] = Field(default=UNSET, alias="EndDate")
    """The end date of the season (UTC)"""

    current_season: Optional[bool] = Field(default=UNSET, alias="CurrentSeason")
    """Indicates whether or not this season is the current season of the competition"""

    rounds: Optional[list[Round1]] = Field(default=UNSET, alias="Rounds")
    """The unique ID of the round that this season is associated with"""


class Season6Dict(TypedDict):
    season_id: NotRequired[int]
    competition_id: NotRequired[int]
    season: NotRequired[int]
    name: NotRequired[str | None]
    competition_name: NotRequired[str | None]
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
    current_season: NotRequired[bool]
    rounds: NotRequired[list[Round1 | Round1Dict]]
