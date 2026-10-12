from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .tournament2 import Tournament2, Tournament2Dict


class DfsSlateTournament(SdkBaseModel):
    slate_tournament_id: Optional[int] = Field(default=UNSET, alias="SlateTournamentID")
    """The unique ID of a SlateTournament (assigned by SportsDataIO)."""

    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)."""

    tournament_id: OptionalNullable[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID that this SlateTournament refers to. Note: This points to data in the respective sports'
    schedule/game/box score feeds."""

    tournament: Optional[Tournament2] = Field(default=UNSET, alias="Tournament")
    """The details of the Tournament that this SlateTournament refers to."""

    operator_tournament_id: OptionalNullable[int] = Field(default=UNSET, alias="OperatorTournamentID")
    """The unique ID of the SlateTournament as assigned by the operator"""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this tournament was removed/deleted by the operator"""


class DfsSlateTournamentDict(TypedDict):
    slate_tournament_id: NotRequired[int]
    slate_id: NotRequired[int]
    tournament_id: NotRequired[int | None]
    tournament: NotRequired[Tournament2Dict]
    operator_tournament_id: NotRequired[int | None]
    removed_by_operator: NotRequired[bool | None]
