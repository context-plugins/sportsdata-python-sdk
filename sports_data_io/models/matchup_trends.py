from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .score import Score, ScoreDict
from .score2 import Score2, Score2Dict
from .team_game_trends import TeamGameTrends, TeamGameTrendsDict
from .team_trends import TeamTrends, TeamTrendsDict


class MatchupTrends(SdkBaseModel):
    upcoming_game: Optional[Score2] = Field(default=UNSET, alias="UpcomingGame")
    """Upcoming game between the team and the opponent"""

    team_trends: Optional[list[TeamTrends]] = Field(default=UNSET, alias="TeamTrends")
    """The collection of team trends between each team"""

    team_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="TeamMatchupTrends")
    """The collection of team game trends against opponent"""

    opponent_matchup_trends: Optional[list[TeamGameTrends]] = Field(default=UNSET, alias="OpponentMatchupTrends")
    """The collection of opponent game trends against team"""

    previous_games: Optional[list[Score]] = Field(default=UNSET, alias="PreviousGames")
    """The collection of last 10 game scores between each team"""


class MatchupTrendsDict(TypedDict):
    upcoming_game: NotRequired[Score2Dict]
    team_trends: NotRequired[list[TeamTrendsDict]]
    team_matchup_trends: NotRequired[list[TeamGameTrendsDict]]
    opponent_matchup_trends: NotRequired[list[TeamGameTrendsDict]]
    previous_games: NotRequired[list[ScoreDict]]
