from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DepthChart(SdkBaseModel):
    depth_chart_id: Optional[int] = Field(default=UNSET, alias="DepthChartID")
    """The unique ID of the Depth Chard record"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their MLB career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category. Possible values: DH; IF; OF; P; PH; PR"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """Player's position in the depth chart. Note: a player can be listed in multiple positions of the depth chart"""

    depth_order: OptionalNullable[int] = Field(default=UNSET, alias="DepthOrder")
    """The Depth Chart order of the player and where they are placed in the depth chart"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time of the last update made to this depth chart (in US Eastern Time)"""


class DepthChartDict(TypedDict):
    depth_chart_id: NotRequired[int]
    team_id: NotRequired[int]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    position_category: NotRequired[str | None]
    position: NotRequired[str | None]
    depth_order: NotRequired[int | None]
    updated: NotRequired[str | None]
