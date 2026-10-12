from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .score1 import Score1, Score1Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict


class TeamTrends(SdkBaseModel):
    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    upcoming_game: Optional[Score1] = Field(default=UNSET, alias="UpcomingGame")
    """Upcoming game for this team"""

    team_game_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamGameTrends")
    """The collection of Game Trends for this team"""


class TeamTrendsDict(TypedDict):
    team: NotRequired[str | None]
    team_id: NotRequired[int | None]
    upcoming_game: NotRequired[Score1Dict]
    team_game_trends: NotRequired[list[TeamGameTrendsDict]]
