from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DfsSlatePlayer(SdkBaseModel):
    slate_player_id: Optional[int] = Field(default=UNSET, alias="SlatePlayerID")
    """Unique ID of a SlatePlayer (assigned by SportsDataIO)"""

    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)"""

    slate_game_id: OptionalNullable[int] = Field(default=UNSET, alias="SlateGameID")
    """Unique ID of a SlateGame (assigned by SportsDataIO)"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO tied to this SlatePlayer. This points to data in
    the respective sports' player feeds Note: this ID will stay with the player throughout their entire career"""

    player_game_projection_stat_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerGameProjectionStatID")
    """The SportsDataIO StatID that this SlatePlayer refers to. This points to data in the respective sports' projected
    player game stats feeds. This field is only filled for Players. For the NFL feeds; this is the
    PlayerGameProjection.PlayerGameID"""

    fantasy_defense_projection_stat_id: OptionalNullable[int] = Field(
        default=UNSET, alias="FantasyDefenseProjectionStatID"
    )
    """The SportsDataIO StatID that this SlatePlayer refers to. This field is only filled for Defense/Special Teams. For
    the NFL feeds, this is the FantasyDefenseGameProjection.FantasyDefenseID."""

    operator_player_id: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPlayerID")
    """Unique ID of the Player (assigned by the operator)"""

    operator_slate_player_id: OptionalNullable[str] = Field(default=UNSET, alias="OperatorSlatePlayerID")
    """Unique ID of the SlatePlayer (assigned by the operator)"""

    operator_player_name: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPlayerName")
    """The player's name (assigned by the operator)"""

    operator_position: OptionalNullable[str] = Field(default=UNSET, alias="OperatorPosition")
    """The player's eligible positions (assigned by the operator)"""

    operator_roster_slots: Optional[list[str | None]] = Field(default=UNSET, alias="OperatorRosterSlots")
    """The player's eligible positions to be played in the contest (assigned by the operator). Note: This would include
    FLEX; etc plays for those that are eligible"""

    operator_salary: OptionalNullable[int] = Field(default=UNSET, alias="OperatorSalary")
    """The player's salary for the contest (assigned by the operator)."""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that the player is on. Note: If the player is a free agent; this field is NULL"""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this player was removed/deleted by the operator."""


class DfsSlatePlayerDict(TypedDict):
    slate_player_id: NotRequired[int]
    slate_id: NotRequired[int]
    slate_game_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    player_game_projection_stat_id: NotRequired[int | None]
    fantasy_defense_projection_stat_id: NotRequired[int | None]
    operator_player_id: NotRequired[str | None]
    operator_slate_player_id: NotRequired[str | None]
    operator_player_name: NotRequired[str | None]
    operator_position: NotRequired[str | None]
    operator_roster_slots: NotRequired[list[str | None]]
    operator_salary: NotRequired[int | None]
    team: NotRequired[str | None]
    team_id: NotRequired[int | None]
    removed_by_operator: NotRequired[bool | None]
