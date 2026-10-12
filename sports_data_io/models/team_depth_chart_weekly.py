from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .depth_chart_weekly import DepthChartWeekly, DepthChartWeeklyDict


class TeamDepthChartWeekly(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """Unique ID of Team"""

    offense: Optional[list[DepthChartWeekly]] = Field(default=UNSET, alias="Offense")
    """List of Offensive Depth Charts for Team"""

    defense: Optional[list[DepthChartWeekly]] = Field(default=UNSET, alias="Defense")
    """List of Defensive Depth Charts for Team"""

    special_teams: Optional[list[DepthChartWeekly]] = Field(default=UNSET, alias="SpecialTeams")
    """List of Special Teams Depth Charts for Team"""


class TeamDepthChartWeeklyDict(TypedDict):
    team_id: NotRequired[int]
    offense: NotRequired[list[DepthChartWeeklyDict]]
    defense: NotRequired[list[DepthChartWeeklyDict]]
    special_teams: NotRequired[list[DepthChartWeeklyDict]]
