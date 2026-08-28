from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Goal(SdkBaseModel):
    goal_id: Optional[int] = Field(default=UNSET, alias="GoalId")
    """The unique ID of the goal"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of the game tied to this goal"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team associated with this goal"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerId")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the player who scored the goal"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of goal scored"""

    assisted_by_player_id1: OptionalNullable[int] = Field(default=UNSET, alias="AssistedByPlayerId1")
    """The unique ID of the first assisted player"""

    assisted_by_player_name1: OptionalNullable[str] = Field(default=UNSET, alias="AssistedByPlayerName1")
    """The player's name of the first assisted player"""

    assisted_by_player_id2: OptionalNullable[int] = Field(default=UNSET, alias="AssistedByPlayerId2")
    """The unique ID of the second assisted player"""

    assisted_by_player_name2: OptionalNullable[str] = Field(default=UNSET, alias="AssistedByPlayerName2")
    """The player's name of the second assisted player"""

    game_minute: OptionalNullable[int] = Field(default=UNSET, alias="GameMinute")
    """The minute in the game in which the goal was scored"""

    game_minute_extra: OptionalNullable[int] = Field(default=UNSET, alias="GameMinuteExtra")
    """The extra minute in the game in which the goal was scored"""


class GoalDict(TypedDict):
    goal_id: NotRequired[int]
    game_id: NotRequired[int]
    team_id: NotRequired[int]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    type_: NotRequired[str | None]
    assisted_by_player_id1: NotRequired[int | None]
    assisted_by_player_name1: NotRequired[str | None]
    assisted_by_player_id2: NotRequired[int | None]
    assisted_by_player_name2: NotRequired[str | None]
    game_minute: NotRequired[int | None]
    game_minute_extra: NotRequired[int | None]
