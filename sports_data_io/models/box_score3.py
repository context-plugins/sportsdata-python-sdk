from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game33 import Game33, Game33Dict
from .period1 import Period1, Period1Dict
from .player_game4 import PlayerGame4, PlayerGame4Dict
from .scoring_play3 import ScoringPlay3, ScoringPlay3Dict
from .team_game4 import TeamGame4, TeamGame4Dict


class BoxScore3(SdkBaseModel):
    game: Optional[Game33] = Field(default=UNSET, alias="Game")
    """The game details of this box score"""

    periods: Optional[list[Period1]] = Field(default=UNSET, alias="Periods")
    """The details of the periods (quarters & overtime) for this box score"""

    player_games: Optional[list[PlayerGame4]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats of this box score"""

    team_games: Optional[list[TeamGame4]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats of this box score"""

    scoring_plays: Optional[list[ScoringPlay3]] = Field(default=UNSET, alias="ScoringPlays")
    """The plays in which either team scoring during the game"""


class BoxScore3Dict(TypedDict):
    game: NotRequired[Game33Dict]
    periods: NotRequired[list[Period1Dict]]
    player_games: NotRequired[list[PlayerGame4Dict]]
    team_games: NotRequired[list[TeamGame4Dict]]
    scoring_plays: NotRequired[list[ScoringPlay3Dict]]
