from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DfsSlatePlayer2(SdkBaseModel):
    slate_player_id: Optional[int] = Field(default=UNSET, alias="SlatePlayerID")
    """Unique ID of a SlatePlayer (assigned by SportsDataIO)."""

    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)."""

    slate_tournament_id: OptionalNullable[int] = Field(default=UNSET, alias="SlateTournamentID")
    """The unique ID of a SlateTournament (assigned by SportsDataIO)."""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique SportsDataIO ID of the golfer that this slate refers to"""

    player_tournament_projection_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerTournamentProjectionID")
    """The unique ID for the player tournament projection that this SlatePlayer refers to. Note: This points to data in
    the respective sports' projected player game stats feeds."""

    operator_player_id: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPlayerID")
    """The unique ID of the golfer as assigned by the operator"""

    operator_slate_player_id: OptionalNullable[str] = Field(default=UNSET, alias="OperatorSlatePlayerID")
    """The unique ID of the SlatePlayer as assigned by the operator"""

    operator_player_name: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPlayerName")
    """The golfer's name as assigned by the operator"""

    operator_position: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPosition")
    """The golfer's eligible positions for the contest as assigned by the operator"""

    operator_salary: OptionalNullable[int] = Field(default=UNSET, alias="OperatorSalary")
    """The golfer's salary for the contest as assigned by the operator"""

    operator_roster_slots: OptionalNullable[list[str]] = Field(default=UNSET, alias="OperatorRosterSlots")
    """The golfer's eligible positions for the contest as assigned by the operator; This would include UTIL, etc. plays
    for those that are eligible"""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this player was removed/deleted by the operator"""


class DfsSlatePlayer2Dict(TypedDict):
    slate_player_id: NotRequired[int]
    slate_id: NotRequired[int]
    slate_tournament_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    player_tournament_projection_id: NotRequired[int | None]
    operator_player_id: NotRequired[str | None]
    operator_slate_player_id: NotRequired[str | None]
    operator_player_name: NotRequired[str | None]
    operator_position: NotRequired[str | None]
    operator_salary: NotRequired[int | None]
    operator_roster_slots: NotRequired[list[str] | None]
    removed_by_operator: NotRequired[bool | None]
