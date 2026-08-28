from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DepthChartWeekly(SdkBaseModel):
    depth_chart_weekly_id: Optional[int] = Field(default=UNSET, alias="DepthChartWeeklyID")
    """Unique ID of Depth Chart Weekly Record"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """Unique ID of Team"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """Unique ID of Player"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player Name"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """Player Position Category (OFF, DEF, ST)"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """Player Position"""

    depth_order: OptionalNullable[int] = Field(default=UNSET, alias="DepthOrder")
    """Depth Chart Order"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """Date and Time Last Updated"""


class DepthChartWeeklyDict(TypedDict):
    depth_chart_weekly_id: NotRequired[int]
    team_id: NotRequired[int]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    position_category: NotRequired[str | None]
    position: NotRequired[str | None]
    depth_order: NotRequired[int | None]
    updated: NotRequired[str | None]
