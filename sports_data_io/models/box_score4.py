from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game34 import Game34, Game34Dict
from .period2 import Period2, Period2Dict
from .player_game5 import PlayerGame5, PlayerGame5Dict
from .team_game5 import TeamGame5, TeamGame5Dict


class BoxScore4(SdkBaseModel):
    game: Optional[Game34] = Field(default=UNSET, alias="Game")
    """Returns the game details for a given game's box score"""

    periods: Optional[list[Period2]] = Field(default=UNSET, alias="Periods")
    """The details of the periods (halves & overtime) for this game. Note: the scores are for that half/period only, not
    total score of game at that point."""

    player_games: Optional[list[PlayerGame5]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats of this box score"""

    team_games: Optional[list[TeamGame5]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats of this box score"""


class BoxScore4Dict(TypedDict):
    game: NotRequired[Game34 | Game34Dict]
    periods: NotRequired[list[Period2 | Period2Dict]]
    player_games: NotRequired[list[PlayerGame5 | PlayerGame5Dict]]
    team_games: NotRequired[list[TeamGame5 | TeamGame5Dict]]
