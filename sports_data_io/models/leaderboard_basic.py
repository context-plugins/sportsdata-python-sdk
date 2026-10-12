from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .player_tournament_basic import PlayerTournamentBasic, PlayerTournamentBasicDict
from .tournament_basic2 import TournamentBasic2, TournamentBasic2Dict


class LeaderboardBasic(SdkBaseModel):
    tournament: Optional[TournamentBasic2] = Field(default=UNSET, alias="Tournament")
    """The details of the tournament for this event"""

    players: Optional[list[PlayerTournamentBasic]] = Field(default=UNSET, alias="Players")
    """The details of the golfers who competed in this tournament"""


class LeaderboardBasicDict(TypedDict):
    tournament: NotRequired[TournamentBasic2Dict]
    players: NotRequired[list[PlayerTournamentBasicDict]]
