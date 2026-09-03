from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .depth_chart import DepthChart, DepthChartDict


class TeamDepthChart(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """Unique ID of Team"""

    offense: Optional[list[DepthChart]] = Field(default=UNSET, alias="Offense")
    """List of Offensive Depth Charts for Team"""

    defense: Optional[list[DepthChart]] = Field(default=UNSET, alias="Defense")
    """List of Defensive Depth Charts for Team"""

    special_teams: Optional[list[DepthChart]] = Field(default=UNSET, alias="SpecialTeams")
    """List of Special Teams Depth Charts for Team"""


class TeamDepthChartDict(TypedDict):
    team_id: NotRequired[int]
    offense: NotRequired[list[DepthChart | DepthChartDict]]
    defense: NotRequired[list[DepthChart | DepthChartDict]]
    special_teams: NotRequired[list[DepthChart | DepthChartDict]]
