from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game24 import Game24, Game24Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict


class TeamTrends4(SdkBaseModel):
    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    upcoming_game: Optional[Game24] = Field(default=UNSET, alias="UpcomingGame")
    """Upcoming game for this team"""

    team_game_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamGameTrends")
    """The collection of Game Trends for this team"""


class TeamTrends4Dict(TypedDict):
    team: NotRequired[str | None]
    team_id: NotRequired[int | None]
    upcoming_game: NotRequired[Game24 | Game24Dict]
    team_game_trends: NotRequired[list[TeamGameTrends | TeamGameTrendsDict]]
