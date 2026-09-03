from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DepthChart(SdkBaseModel):
    depth_chart_id: Optional[int] = Field(default=UNSET, alias="DepthChartID")
    """Unique ID of Depth Chart Record"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """Unique ID of Team"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """Unique ID of Player"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The category of the player's depth chart position (OFF; DEF; ST)"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's depth chart position"""

    depth_order: OptionalNullable[int] = Field(default=UNSET, alias="DepthOrder")
    """The order this player is at his position (1 = Starter; 2 = Backup; 3 = 3rd String; 4 = 4th String; 5 = 5th
    String)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """Date and time last updated (in US Eastern Time)"""


class DepthChartDict(TypedDict):
    depth_chart_id: NotRequired[int]
    team_id: NotRequired[int]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    position_category: NotRequired[str | None]
    position: NotRequired[str | None]
    depth_order: NotRequired[int | None]
    updated: NotRequired[str | None]
