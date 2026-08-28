from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DfsSlatePlayer1(SdkBaseModel):
    slate_player_id: Optional[int] = Field(default=UNSET, alias="SlatePlayerID")
    """Unique ID of a SlatePlayer (assigned by SportsDataIO)"""

    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """The SlateID that this SlatePlayer refers to"""

    slate_game_id: OptionalNullable[int] = Field(default=UNSET, alias="SlateGameID")
    """The SlateGameID that this SlatePlayer refers to"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their MLB career"""

    player_game_projection_stat_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerGameProjectionStatID")
    """The SportsDataIO StatID that this SlatePlayer refers to. This points to data in the respective sports' projected
    player game stats feeds."""

    operator_player_id: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPlayerID")
    """Unique ID of the Player (assigned by the operator)"""

    operator_slate_player_id: OptionalNullable[str] = Field(default=UNSET, alias="OperatorSlatePlayerID")
    """Unique ID of the SlatePlayer (assigned by the operator)"""

    operator_player_name: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPlayerName")
    """The player's name (assigned by the operator)"""

    operator_position: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPosition")
    """The player's eligible positions for the contest (assigned by the operator)"""

    operator_salary: OptionalNullable[int] = Field(default=UNSET, alias="OperatorSalary")
    """The player's salary for the contest (assigned by the operator)"""

    operator_roster_slots: OptionalNullable[list[str]] = Field(default=UNSET, alias="OperatorRosterSlots")
    """The player's eligible positions to be played in the contest (assigned by the operator). Note: this would include
    UTIL; etc plays for those that are eligible."""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this player was removed/deleted by the operator"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""


class DfsSlatePlayer1Dict(TypedDict):
    slate_player_id: NotRequired[int]
    slate_id: NotRequired[int]
    slate_game_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    player_game_projection_stat_id: NotRequired[int | None]
    operator_player_id: NotRequired[str | None]
    operator_slate_player_id: NotRequired[str | None]
    operator_player_name: NotRequired[str | None]
    operator_position: NotRequired[str | None]
    operator_salary: NotRequired[int | None]
    operator_roster_slots: NotRequired[list[str] | None]
    removed_by_operator: NotRequired[bool | None]
    team: NotRequired[str | None]
    team_id: NotRequired[int | None]
