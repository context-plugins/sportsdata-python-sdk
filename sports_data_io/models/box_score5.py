from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game15 import Game15, Game15Dict
from .player_game6 import PlayerGame6, PlayerGame6Dict
from .quarter1 import Quarter1, Quarter1Dict
from .team_game6 import TeamGame6, TeamGame6Dict


class BoxScore5(SdkBaseModel):
    game: Optional[Game15] = Field(default=UNSET, alias="Game")
    """Returns the game details for a given game's box score"""

    quarters: Optional[list[Quarter1]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters (including overtime periods) for this game."""

    team_games: Optional[list[TeamGame6]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats associated with this box score"""

    player_games: Optional[list[PlayerGame6]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats associated with this box score"""


class BoxScore5Dict(TypedDict):
    game: NotRequired[Game15 | Game15Dict]
    quarters: NotRequired[list[Quarter1 | Quarter1Dict]]
    team_games: NotRequired[list[TeamGame6 | TeamGame6Dict]]
    player_games: NotRequired[list[PlayerGame6 | PlayerGame6Dict]]
