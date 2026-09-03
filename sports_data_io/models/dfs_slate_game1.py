from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game1 import Game1, Game1Dict


class DfsSlateGame1(SdkBaseModel):
    slate_game_id: Optional[int] = Field(default=UNSET, alias="SlateGameID")
    """Unique ID of a SlateGame (assigned by SportsDataIO)."""

    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """The SlateID that this SlateGame refers to."""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game associated with this SlateGame. This points to data in the schedule/game/box score
    feeds."""

    game: Optional[Game1] = Field(default=UNSET, alias="Game")
    """The details of the Game that this SlateGame refers to."""

    operator_game_id: OptionalNullable[int] = Field(default=UNSET, alias="OperatorGameID")
    """Unique ID of a SlateGame (assigned by the operator)."""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this game was removed/deleted by the operator."""


class DfsSlateGame1Dict(TypedDict):
    slate_game_id: NotRequired[int]
    slate_id: NotRequired[int]
    game_id: NotRequired[int | None]
    game: NotRequired[Game1 | Game1Dict]
    operator_game_id: NotRequired[int | None]
    removed_by_operator: NotRequired[bool | None]
