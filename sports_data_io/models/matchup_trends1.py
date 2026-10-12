from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game import Game, GameDict
from .game3 import Game3, Game3Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict
from .team_trends1 import TeamTrends1, TeamTrends1Dict


class MatchupTrends1(SdkBaseModel):
    upcoming_game: Optional[Game3] = Field(default=UNSET, alias="UpcomingGame")
    """Next scheduled game for the team with a specified opposing team"""

    team_trends: Optional[list[TeamTrends1]] = Field(default=UNSET, alias="TeamTrends")
    """The collection of team trends between each team"""

    team_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamMatchupTrends")
    """The collection of team game trends against opponent"""

    opponent_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="OpponentMatchupTrends")
    """The collection of opponent game trends against team"""

    previous_games: Optional[list[Game]] = Field(default=UNSET, alias="PreviousGames")
    """The collection of last 10 game scores between each team"""


class MatchupTrends1Dict(TypedDict):
    upcoming_game: NotRequired[Game3Dict]
    team_trends: NotRequired[list[TeamTrends1Dict]]
    team_matchup_trends: NotRequired[list[TeamGameTrendsDict]]
    opponent_matchup_trends: NotRequired[list[TeamGameTrendsDict]]
    previous_games: NotRequired[list[GameDict]]
