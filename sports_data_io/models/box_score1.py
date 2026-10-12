from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game41 import Game41, Game41Dict
from .inning import Inning, InningDict
from .player_game2 import PlayerGame2, PlayerGame2Dict
from .team_game2 import TeamGame2, TeamGame2Dict


class BoxScore1(SdkBaseModel):
    game: Optional[Game41] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this box score"""

    innings: Optional[list[Inning]] = Field(default=UNSET, alias="Innings")
    """The inning details associated with the box score"""

    team_games: Optional[list[TeamGame2]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats associated with this box score"""

    player_games: Optional[list[PlayerGame2]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats associated with this box score"""


class BoxScore1Dict(TypedDict):
    game: NotRequired[Game41Dict]
    innings: NotRequired[list[InningDict]]
    team_games: NotRequired[list[TeamGame2Dict]]
    player_games: NotRequired[list[PlayerGame2Dict]]
