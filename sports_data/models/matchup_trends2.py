from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game7 import Game7, Game7Dict
from .game33 import Game33, Game33Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict
from .team_trends2 import TeamTrends2, TeamTrends2Dict


class MatchupTrends2(SdkBaseModel):
    upcoming_game: Optional[Game33] = Field(default=UNSET, alias="UpcomingGame")
    """Next scheduled game for the team with a specified opposing team"""

    team_trends: Optional[list[TeamTrends2]] = Field(default=UNSET, alias="TeamTrends")
    """The collection of team trends between each team"""

    team_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamMatchupTrends")
    """The collection of team game trends against opponent"""

    opponent_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="OpponentMatchupTrends")
    """The collection of opponent game trends against team"""

    previous_games: Optional[list[Game7]] = Field(default=UNSET, alias="PreviousGames")
    """The collection of last 10 game scores between each team"""


class MatchupTrends2Dict(TypedDict):
    upcoming_game: NotRequired[Game33 | Game33Dict]
    team_trends: NotRequired[list[TeamTrends2 | TeamTrends2Dict]]
    team_matchup_trends: NotRequired[list[TeamGameTrends | TeamGameTrendsDict]]
    opponent_matchup_trends: NotRequired[list[TeamGameTrends | TeamGameTrendsDict]]
    previous_games: NotRequired[list[Game7 | Game7Dict]]
