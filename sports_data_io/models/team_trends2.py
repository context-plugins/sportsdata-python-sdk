from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game13 import Game13, Game13Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict


class TeamTrends2(SdkBaseModel):
    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    upcoming_game: Optional[Game13] = Field(default=UNSET, alias="UpcomingGame")
    """The most recent future game for the team"""

    team_game_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamGameTrends")
    """The collection of Game Trends for this team"""


class TeamTrends2Dict(TypedDict):
    team: NotRequired[str | None]
    team_id: NotRequired[int | None]
    upcoming_game: NotRequired[Game13Dict]
    team_game_trends: NotRequired[list[TeamGameTrendsDict]]
