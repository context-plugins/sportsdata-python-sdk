from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .depth_chart import DepthChart, DepthChartDict


class TeamDepthChart1(SdkBaseModel):
    depth_charts: Optional[list[DepthChart]] = Field(default=UNSET, alias="DepthCharts")
    """List of Depth Chart Records for Team"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""


class TeamDepthChart1Dict(TypedDict):
    depth_charts: NotRequired[list[DepthChart | DepthChartDict]]
    team_id: NotRequired[int]
