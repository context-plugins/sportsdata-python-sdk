from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dfs_slate_player2 import DfsSlatePlayer2, DfsSlatePlayer2Dict
from .dfs_slate_tournament import DfsSlateTournament, DfsSlateTournamentDict


class DfsSlate2(SdkBaseModel):
    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)."""

    operator: OptionalNullable[str] = Field(default=UNSET, alias="Operator")
    """The name of the operator who is running contests for this slate. Possible values: FanDuel, DraftKings, Yahoo,
    FantasyDraft, etc."""

    operator_slate_id: OptionalNullable[int] = Field(default=UNSET, alias="OperatorSlateID")
    """The unique ID of a slate as assigned by the operator"""

    operator_name: OptionalNullable[str] = Field(default=UNSET, alias="OperatorName")
    """The name of the slate as assigned by the operator. Possible values: Main; Express; Arcade; Late Night; etc."""

    operator_day: OptionalNullable[str] = Field(default=UNSET, alias="OperatorDay")
    """The day (in EST/EDT) that the slate begins, as assigned by the operator"""

    operator_start_time: OptionalNullable[str] = Field(default=UNSET, alias="OperatorStartTime")
    """The date/time (in EST/EDT) that the slate begins as assigned by the operator)"""

    number_of_tournaments: OptionalNullable[int] = Field(default=UNSET, alias="NumberOfTournaments")
    """The total number of actual tournaments that this slate covers"""

    is_multi_day_slate: OptionalNullable[bool] = Field(default=UNSET, alias="IsMultiDaySlate")
    """Indicates if this slate uses tournaments that take place on different days"""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this slate was removed/deleted by the operator"""

    operator_game_type: OptionalNullable[str] = Field(default=UNSET, alias="OperatorGameType")
    """The game type of the slate as assigned by the operator. Note: will often be null as most operators only have one
    game type"""

    dfs_slate_tournaments: Optional[list[DfsSlateTournament]] = Field(default=UNSET, alias="DfsSlateTournaments")
    """The tournament(s) included in this slate"""

    dfs_slate_players: Optional[list[DfsSlatePlayer2]] = Field(default=UNSET, alias="DfsSlatePlayers")
    """The list of players that are included in this slate"""

    slate_roster_slots: Optional[list[str | None]] = Field(default=UNSET, alias="SlateRosterSlots")
    """The positions that need to be filled for this particular slate"""


class DfsSlate2Dict(TypedDict):
    slate_id: NotRequired[int]
    operator: NotRequired[str | None]
    operator_slate_id: NotRequired[int | None]
    operator_name: NotRequired[str | None]
    operator_day: NotRequired[str | None]
    operator_start_time: NotRequired[str | None]
    number_of_tournaments: NotRequired[int | None]
    is_multi_day_slate: NotRequired[bool | None]
    removed_by_operator: NotRequired[bool | None]
    operator_game_type: NotRequired[str | None]
    dfs_slate_tournaments: NotRequired[list[DfsSlateTournamentDict]]
    dfs_slate_players: NotRequired[list[DfsSlatePlayer2Dict]]
    slate_roster_slots: NotRequired[list[str | None]]
