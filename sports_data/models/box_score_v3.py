from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fantasy_defense_game import FantasyDefenseGame, FantasyDefenseGameDict
from .player_game4 import PlayerGame4, PlayerGame4Dict
from .quarter1 import Quarter1, Quarter1Dict
from .score3 import Score3, Score3Dict
from .scoring_detail import ScoringDetail, ScoringDetailDict
from .scoring_play1 import ScoringPlay1, ScoringPlay1Dict
from .team_game4 import TeamGame4, TeamGame4Dict


class BoxScoreV3(SdkBaseModel):
    score: Optional[Score3] = Field(default=UNSET, alias="Score")
    """The Score object related to this game"""

    quarters: Optional[list[Quarter1]] = Field(default=UNSET, alias="Quarters")
    """The Quarters objects related to this game"""

    team_games: Optional[list[TeamGame4]] = Field(default=UNSET, alias="TeamGames")
    """The TeamGame objects related to this game"""

    player_games: Optional[list[PlayerGame4]] = Field(default=UNSET, alias="PlayerGames")
    """The PlayerGame objects related to this game"""

    fantasy_defense_games: Optional[list[FantasyDefenseGame]] = Field(default=UNSET, alias="FantasyDefenseGames")
    """The FantasyDefenseGame objects related to this game"""

    scoring_plays: Optional[list[ScoringPlay1]] = Field(default=UNSET, alias="ScoringPlays")
    """The ScoringPlay objects related to this game"""

    scoring_details: Optional[list[ScoringDetail]] = Field(default=UNSET, alias="ScoringDetails")
    """The ScoringDetail objects related to this game"""


class BoxScoreV3Dict(TypedDict):
    score: NotRequired[Score3 | Score3Dict]
    quarters: NotRequired[list[Quarter1 | Quarter1Dict]]
    team_games: NotRequired[list[TeamGame4 | TeamGame4Dict]]
    player_games: NotRequired[list[PlayerGame4 | PlayerGame4Dict]]
    fantasy_defense_games: NotRequired[list[FantasyDefenseGame | FantasyDefenseGameDict]]
    scoring_plays: NotRequired[list[ScoringPlay1 | ScoringPlay1Dict]]
    scoring_details: NotRequired[list[ScoringDetail | ScoringDetailDict]]
