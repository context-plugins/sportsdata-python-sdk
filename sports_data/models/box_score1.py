from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game31 import Game31, Game31Dict
from .period1 import Period1, Period1Dict
from .player_game1 import PlayerGame1, PlayerGame1Dict
from .scoring_play import ScoringPlay, ScoringPlayDict
from .team_game1 import TeamGame1, TeamGame1Dict


class BoxScore1(SdkBaseModel):
    game: Optional[Game31] = Field(default=UNSET, alias="Game")
    """The game details of this box score"""

    periods: Optional[list[Period1]] = Field(default=UNSET, alias="Periods")
    """The details of the periods (quarters & overtime) for this box score"""

    player_games: Optional[list[PlayerGame1]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats of this box score"""

    team_games: Optional[list[TeamGame1]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats of this box score"""

    scoring_plays: Optional[list[ScoringPlay]] = Field(default=UNSET, alias="ScoringPlays")
    """The plays in which either team scoring during the game"""


class BoxScore1Dict(TypedDict):
    game: NotRequired[Game31 | Game31Dict]
    periods: NotRequired[list[Period1 | Period1Dict]]
    player_games: NotRequired[list[PlayerGame1 | PlayerGame1Dict]]
    team_games: NotRequired[list[TeamGame1 | TeamGame1Dict]]
    scoring_plays: NotRequired[list[ScoringPlay | ScoringPlayDict]]
