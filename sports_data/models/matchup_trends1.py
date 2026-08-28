from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game6 import Game6, Game6Dict
from .game32 import Game32, Game32Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict
from .team_trends1 import TeamTrends1, TeamTrends1Dict


class MatchupTrends1(SdkBaseModel):
    upcoming_game: Optional[Game32] = Field(default=UNSET, alias="UpcomingGame")
    """Next scheduled game for the team with a specified opposing team"""

    team_trends: Optional[list[TeamTrends1]] = Field(default=UNSET, alias="TeamTrends")
    """The collection of team trends between each team"""

    team_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamMatchupTrends")
    """The collection of team game trends against opponent"""

    opponent_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="OpponentMatchupTrends")
    """The collection of opponent game trends against the team"""

    previous_games: Optional[list[Game6]] = Field(default=UNSET, alias="PreviousGames")
    """The collection of last 10 game scores between each team"""


class MatchupTrends1Dict(TypedDict):
    upcoming_game: NotRequired[Game32 | Game32Dict]
    team_trends: NotRequired[list[TeamTrends1 | TeamTrends1Dict]]
    team_matchup_trends: NotRequired[list[TeamGameTrends | TeamGameTrendsDict]]
    opponent_matchup_trends: NotRequired[list[TeamGameTrends | TeamGameTrendsDict]]
    previous_games: NotRequired[list[Game6 | Game6Dict]]
