from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game9 import Game9, Game9Dict
from .game24 import Game24, Game24Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict
from .team_trends3 import TeamTrends3, TeamTrends3Dict


class MatchupTrends5(SdkBaseModel):
    upcoming_game: Optional[Game24] = Field(default=UNSET, alias="UpcomingGame")
    """Next scheduled game for the team with a specified opposing team"""

    team_trends: Optional[list[TeamTrends3]] = Field(default=UNSET, alias="TeamTrends")
    """The collection of team trends between each team"""

    team_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamMatchupTrends")
    """The collection of team game trends against opponent"""

    opponent_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="OpponentMatchupTrends")
    """The collection of opponent game trends against team"""

    previous_games: Optional[list[Game9]] = Field(default=UNSET, alias="PreviousGames")
    """The collection of last 10 game scores between each team"""


class MatchupTrends5Dict(TypedDict):
    upcoming_game: NotRequired[Game24Dict]
    team_trends: NotRequired[list[TeamTrends3Dict]]
    team_matchup_trends: NotRequired[list[TeamGameTrendsDict]]
    opponent_matchup_trends: NotRequired[list[TeamGameTrendsDict]]
    previous_games: NotRequired[list[Game9Dict]]
