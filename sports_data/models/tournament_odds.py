from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .player_tournament_odd import PlayerTournamentOdd, PlayerTournamentOddDict
from .tournament3 import Tournament3, Tournament3Dict


class TournamentOdds(SdkBaseModel):
    tournament: Optional[Tournament3] = Field(default=UNSET, alias="Tournament")
    """The details of the tournament"""

    player_tournament_odds: Optional[list[PlayerTournamentOdd]] = Field(default=UNSET, alias="PlayerTournamentOdds")
    """The tournaments collection of PlayerTournamentOdds"""


class TournamentOddsDict(TypedDict):
    tournament: NotRequired[Tournament3 | Tournament3Dict]
    player_tournament_odds: NotRequired[list[PlayerTournamentOdd | PlayerTournamentOddDict]]
