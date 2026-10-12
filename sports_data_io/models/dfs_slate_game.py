from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .schedule1 import Schedule1, Schedule1Dict


class DfsSlateGame(SdkBaseModel):
    slate_game_id: Optional[int] = Field(default=UNSET, alias="SlateGameID")
    """Unique ID of a SlateGame (assigned by SportsDataIO)."""

    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """Unique ID of a Slate (assigned by SportsDataIO)."""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game tied to this SlateGame"""

    operator_game_id: OptionalNullable[int] = Field(default=UNSET, alias="OperatorGameID")
    """Unique ID of a SlateGame (assigned by the operator)"""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this game was removed/deleted by the operator."""

    score_id: OptionalNullable[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the Score/Game"""

    game: Optional[Schedule1] = Field(default=UNSET, alias="Game")
    """The details of the Score/Game that this SlateGame refers to"""


class DfsSlateGameDict(TypedDict):
    slate_game_id: NotRequired[int]
    slate_id: NotRequired[int]
    game_id: NotRequired[int | None]
    operator_game_id: NotRequired[int | None]
    removed_by_operator: NotRequired[bool | None]
    score_id: NotRequired[int | None]
    game: NotRequired[Schedule1Dict]
