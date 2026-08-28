from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .player_tournament import PlayerTournament, PlayerTournamentDict
from .tournament11 import Tournament11, Tournament11Dict


class Leaderboard(SdkBaseModel):
    tournament: Optional[Tournament11] = Field(default=UNSET, alias="Tournament")
    """The details of the tournament for this leaderboard"""

    players: Optional[list[PlayerTournament]] = Field(default=UNSET, alias="Players")
    """The details of the golfers who competed in this tournament"""


class LeaderboardDict(TypedDict):
    tournament: NotRequired[Tournament11 | Tournament11Dict]
    players: NotRequired[list[PlayerTournament | PlayerTournamentDict]]
