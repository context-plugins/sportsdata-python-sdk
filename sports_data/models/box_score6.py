from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game16 import Game16, Game16Dict
from .player_game7 import PlayerGame7, PlayerGame7Dict
from .quarter import Quarter, QuarterDict
from .team_game7 import TeamGame7, TeamGame7Dict


class BoxScore6(SdkBaseModel):
    game: Optional[Game16] = Field(default=UNSET, alias="Game")
    """Returns the game details for a given game's box score"""

    quarters: Optional[list[Quarter]] = Field(default=UNSET, alias="Quarters")
    """The details of the quarters (including overtime periods) for this game."""

    team_games: Optional[list[TeamGame7]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats associated with this box score"""

    player_games: Optional[list[PlayerGame7]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats associated with this box score"""


class BoxScore6Dict(TypedDict):
    game: NotRequired[Game16 | Game16Dict]
    quarters: NotRequired[list[Quarter | QuarterDict]]
    team_games: NotRequired[list[TeamGame7 | TeamGame7Dict]]
    player_games: NotRequired[list[PlayerGame7 | PlayerGame7Dict]]
