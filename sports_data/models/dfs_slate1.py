from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dfs_slate_game import DfsSlateGame, DfsSlateGameDict
from .dfs_slate_player1 import DfsSlatePlayer1, DfsSlatePlayer1Dict


class DfsSlate1(SdkBaseModel):
    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """The SlateID that this SlateGame refers to"""

    operator: OptionalNullable[str] = Field(default=UNSET, alias="Operator")
    """The name of the operator who is running contests for this slate Possible values: FanDuel; DraftKings; Yahoo;
    FantasyDraft; etc."""

    operator_slate_id: OptionalNullable[int] = Field(default=UNSET, alias="OperatorSlateID")
    """Unique ID of a slate (assigned by the operator)."""

    operator_name: OptionalNullable[str] = Field(default=UNSET, alias="OperatorName")
    """The name of the slate (assigned by the operator). Possible values: Main, Express, Arcade, Late Night, etc."""

    operator_day: OptionalNullable[str] = Field(default=UNSET, alias="OperatorDay")
    """The day (in EST/EDT) that the slate begins (assigned by the operator)"""

    operator_start_time: OptionalNullable[str] = Field(default=UNSET, alias="OperatorStartTime")
    """The date/time (in EST/EDT) that the slate begins (assigned by the operator)."""

    number_of_games: OptionalNullable[int] = Field(default=UNSET, alias="NumberOfGames")
    """The number of actual games that this slate covers"""

    is_multi_day_slate: OptionalNullable[bool] = Field(default=UNSET, alias="IsMultiDaySlate")
    """Whether or not this slate uses games that take place on different days (true/false)"""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this slate was removed/deleted by the operator."""

    operator_game_type: OptionalNullable[str] = Field(default=UNSET, alias="OperatorGameType")
    """The game type of the slate. Note: Will often be null as most operators only have one game type"""

    dfs_slate_games: Optional[list[DfsSlateGame]] = Field(default=UNSET, alias="DfsSlateGames")
    """The games that are included in this slate"""

    dfs_slate_players: Optional[list[DfsSlatePlayer1]] = Field(default=UNSET, alias="DfsSlatePlayers")
    """The players that are included in this slate"""

    slate_roster_slots: OptionalNullable[list[str]] = Field(default=UNSET, alias="SlateRosterSlots")
    """The positions that need to be filled for this particular slate"""

    salary_cap: OptionalNullable[int] = Field(default=UNSET, alias="SalaryCap")
    """The salary cap for the current slate (is null for slates with no salary cap such a Tiers gametypes)"""


class DfsSlate1Dict(TypedDict):
    slate_id: NotRequired[int]
    operator: NotRequired[str | None]
    operator_slate_id: NotRequired[int | None]
    operator_name: NotRequired[str | None]
    operator_day: NotRequired[str | None]
    operator_start_time: NotRequired[str | None]
    number_of_games: NotRequired[int | None]
    is_multi_day_slate: NotRequired[bool | None]
    removed_by_operator: NotRequired[bool | None]
    operator_game_type: NotRequired[str | None]
    dfs_slate_games: NotRequired[list[DfsSlateGame | DfsSlateGameDict]]
    dfs_slate_players: NotRequired[list[DfsSlatePlayer1 | DfsSlatePlayer1Dict]]
    slate_roster_slots: NotRequired[list[str] | None]
    salary_cap: NotRequired[int | None]
