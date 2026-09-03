from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game42 import Game42, Game42Dict
from .period import Period, PeriodDict
from .play3 import Play3, Play3Dict
from .player_game3 import PlayerGame3, PlayerGame3Dict
from .team_game3 import TeamGame3, TeamGame3Dict


class BoxScore2(SdkBaseModel):
    game: Optional[Game42] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this box score"""

    periods: Optional[list[Period]] = Field(default=UNSET, alias="Periods")
    """The details of the periods associated with this box score"""

    team_games: Optional[list[TeamGame3]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats associated with this box score"""

    player_games: Optional[list[PlayerGame3]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats associated with this box score"""

    shootout_plays: Optional[list[Play3]] = Field(default=UNSET, alias="ShootoutPlays")
    """The details of any shootout plays associated with this box score"""


class BoxScore2Dict(TypedDict):
    game: NotRequired[Game42 | Game42Dict]
    periods: NotRequired[list[Period | PeriodDict]]
    team_games: NotRequired[list[TeamGame3 | TeamGame3Dict]]
    player_games: NotRequired[list[PlayerGame3 | PlayerGame3Dict]]
    shootout_plays: NotRequired[list[Play3 | Play3Dict]]
