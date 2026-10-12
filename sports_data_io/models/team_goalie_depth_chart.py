from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .goalie_depth_chart import GoalieDepthChart, GoalieDepthChartDict


class TeamGoalieDepthChart(SdkBaseModel):
    goalie_depth_charts: Optional[list[GoalieDepthChart]] = Field(default=UNSET, alias="GoalieDepthCharts")
    """List of players that make up the goalie depth chart for each team"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""


class TeamGoalieDepthChartDict(TypedDict):
    goalie_depth_charts: NotRequired[list[GoalieDepthChartDict]]
    team_id: NotRequired[int]
