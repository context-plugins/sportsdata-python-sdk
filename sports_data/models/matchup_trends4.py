from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game8 import Game8, Game8Dict
from .game34 import Game34, Game34Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict
from .team_trends4 import TeamTrends4, TeamTrends4Dict


class MatchupTrends4(SdkBaseModel):
    upcoming_game: Optional[Game34] = Field(default=UNSET, alias="UpcomingGame")
    """Upcoming game between the team and the opponent"""

    team_trends: Optional[list[TeamTrends4]] = Field(default=UNSET, alias="TeamTrends")
    """The collection of team trends between each team"""

    team_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamMatchupTrends")
    """The collection of team game trends against opponent"""

    opponent_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="OpponentMatchupTrends")
    """The collection of opponent game trends against a specific team"""

    previous_games: Optional[list[Game8]] = Field(default=UNSET, alias="PreviousGames")
    """The collection of last 10 game scores between each team"""


class MatchupTrends4Dict(TypedDict):
    upcoming_game: NotRequired[Game34 | Game34Dict]
    team_trends: NotRequired[list[TeamTrends4 | TeamTrends4Dict]]
    team_matchup_trends: NotRequired[list[TeamGameTrends | TeamGameTrendsDict]]
    opponent_matchup_trends: NotRequired[list[TeamGameTrends | TeamGameTrendsDict]]
    previous_games: NotRequired[list[Game8 | Game8Dict]]
