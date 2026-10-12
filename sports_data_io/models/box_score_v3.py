from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fantasy_defense_game import FantasyDefenseGame, FantasyDefenseGameDict
from .player_game import PlayerGame, PlayerGameDict
from .quarter import Quarter, QuarterDict
from .score3 import Score3, Score3Dict
from .scoring_detail import ScoringDetail, ScoringDetailDict
from .scoring_play import ScoringPlay, ScoringPlayDict
from .team_game import TeamGame, TeamGameDict


class BoxScoreV3(SdkBaseModel):
    score: Optional[Score3] = Field(default=UNSET, alias="Score")
    """The Score object related to this game"""

    quarters: Optional[list[Quarter]] = Field(default=UNSET, alias="Quarters")
    """The Quarters objects related to this game"""

    team_games: Optional[list[TeamGame]] = Field(default=UNSET, alias="TeamGames")
    """The TeamGame objects related to this game"""

    player_games: Optional[list[PlayerGame]] = Field(default=UNSET, alias="PlayerGames")
    """The PlayerGame objects related to this game"""

    fantasy_defense_games: Optional[list[FantasyDefenseGame]] = Field(default=UNSET, alias="FantasyDefenseGames")
    """The FantasyDefenseGame objects related to this game"""

    scoring_plays: Optional[list[ScoringPlay]] = Field(default=UNSET, alias="ScoringPlays")
    """The ScoringPlay objects related to this game"""

    scoring_details: Optional[list[ScoringDetail]] = Field(default=UNSET, alias="ScoringDetails")
    """The ScoringDetail objects related to this game"""


class BoxScoreV3Dict(TypedDict):
    score: NotRequired[Score3Dict]
    quarters: NotRequired[list[QuarterDict]]
    team_games: NotRequired[list[TeamGameDict]]
    player_games: NotRequired[list[PlayerGameDict]]
    fantasy_defense_games: NotRequired[list[FantasyDefenseGameDict]]
    scoring_plays: NotRequired[list[ScoringPlayDict]]
    scoring_details: NotRequired[list[ScoringDetailDict]]
