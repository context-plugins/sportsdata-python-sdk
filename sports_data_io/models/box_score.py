from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game4 import Game4, Game4Dict
from .player_game1 import PlayerGame1, PlayerGame1Dict
from .quarter1 import Quarter1, Quarter1Dict
from .team_game1 import TeamGame1, TeamGame1Dict


class BoxScore(SdkBaseModel):
    game: Optional[Game4] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this box score"""

    quarters: Optional[list[Quarter1]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters associated with this box score"""

    team_games: Optional[list[TeamGame1]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats associated with this box score"""

    player_games: Optional[list[PlayerGame1]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats associated with this box score"""


class BoxScoreDict(TypedDict):
    game: NotRequired[Game4 | Game4Dict]
    quarters: NotRequired[list[Quarter1 | Quarter1Dict]]
    team_games: NotRequired[list[TeamGame1 | TeamGame1Dict]]
    player_games: NotRequired[list[PlayerGame1 | PlayerGame1Dict]]
