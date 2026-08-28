from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game22 import Game22, Game22Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict


class TeamTrends1(SdkBaseModel):
    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    upcoming_game: Optional[Game22] = Field(default=UNSET, alias="UpcomingGame")
    """Next scheduled game for the team"""

    team_game_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamGameTrends")
    """The collection of Game Trends for this team"""


class TeamTrends1Dict(TypedDict):
    team: NotRequired[str | None]
    team_id: NotRequired[int | None]
    upcoming_game: NotRequired[Game22 | Game22Dict]
    team_game_trends: NotRequired[list[TeamGameTrends | TeamGameTrendsDict]]
