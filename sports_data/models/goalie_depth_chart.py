from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class GoalieDepthChart(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team this player is employed by"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the goaltender"""

    depth_type: OptionalNullable[str] = Field(default=UNSET, alias="DepthType")
    """Indicates whether it is a goalie tandem or not for a goalie depth chart (returns Tandem; Regular)"""

    display_type: OptionalNullable[str] = Field(default=UNSET, alias="DisplayType")
    """If the goalie depth chart is displayed as a Tandem or as Regular"""

    depth_order: OptionalNullable[int] = Field(default=UNSET, alias="DepthOrder")
    """The order of the goalie in the team's depth chart"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when this depth chart was last edited; based on US Eastern Time (EST/EDT)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (in US Eastern Time)"""


class GoalieDepthChartDict(TypedDict):
    team_id: NotRequired[int]
    team: NotRequired[str | None]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    depth_type: NotRequired[str | None]
    display_type: NotRequired[str | None]
    depth_order: NotRequired[int | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
