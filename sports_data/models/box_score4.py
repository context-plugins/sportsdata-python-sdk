from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game43 import Game43, Game43Dict
from .period2 import Period2, Period2Dict
from .play3 import Play3, Play3Dict
from .player_game5 import PlayerGame5, PlayerGame5Dict
from .team_game5 import TeamGame5, TeamGame5Dict


class BoxScore4(SdkBaseModel):
    game: Optional[Game43] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this box score"""

    periods: Optional[list[Period2]] = Field(default=UNSET, alias="Periods")
    """The details of the periods associated with this box score"""

    team_games: Optional[list[TeamGame5]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats associated with this box score"""

    player_games: Optional[list[PlayerGame5]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats associated with this box score"""

    shootout_plays: Optional[list[Play3]] = Field(default=UNSET, alias="ShootoutPlays")
    """The details of any shootout plays associated with this box score"""


class BoxScore4Dict(TypedDict):
    game: NotRequired[Game43 | Game43Dict]
    periods: NotRequired[list[Period2 | Period2Dict]]
    team_games: NotRequired[list[TeamGame5 | TeamGame5Dict]]
    player_games: NotRequired[list[PlayerGame5 | PlayerGame5Dict]]
    shootout_plays: NotRequired[list[Play3 | Play3Dict]]
