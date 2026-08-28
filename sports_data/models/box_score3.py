from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game42 import Game42, Game42Dict
from .player_game3 import PlayerGame3, PlayerGame3Dict
from .quarter import Quarter, QuarterDict
from .team_game3 import TeamGame3, TeamGame3Dict


class BoxScore3(SdkBaseModel):
    game: Optional[Game42] = Field(default=UNSET, alias="Game")
    """The details of the game associated with this box score"""

    quarters: Optional[list[Quarter]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters associated with this box score"""

    team_games: Optional[list[TeamGame3]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats associated with this box score"""

    player_games: Optional[list[PlayerGame3]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats associated with this box score"""


class BoxScore3Dict(TypedDict):
    game: NotRequired[Game42 | Game42Dict]
    quarters: NotRequired[list[Quarter | QuarterDict]]
    team_games: NotRequired[list[TeamGame3 | TeamGame3Dict]]
    player_games: NotRequired[list[PlayerGame3 | PlayerGame3Dict]]
