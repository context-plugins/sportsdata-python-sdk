from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .game3 import Game3, Game3Dict
from .period import Period, PeriodDict
from .player_game import PlayerGame, PlayerGameDict
from .team_game import TeamGame, TeamGameDict


class BoxScore(SdkBaseModel):
    game: Optional[Game3] = Field(default=UNSET, alias="Game")
    """Returns the game details for a given game's box score"""

    periods: Optional[list[Period]] = Field(default=UNSET, alias="Periods")
    """The details of the periods (halves & overtime) for this game. Note: the scores are for that half/period only, not
    total score of game at that point."""

    player_games: Optional[list[PlayerGame]] = Field(default=UNSET, alias="PlayerGames")
    """The player game stats of this box score"""

    team_games: Optional[list[TeamGame]] = Field(default=UNSET, alias="TeamGames")
    """The team game stats of this box score"""


class BoxScoreDict(TypedDict):
    game: NotRequired[Game3 | Game3Dict]
    periods: NotRequired[list[Period | PeriodDict]]
    player_games: NotRequired[list[PlayerGame | PlayerGameDict]]
    team_games: NotRequired[list[TeamGame | TeamGameDict]]
