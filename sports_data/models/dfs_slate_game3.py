from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game14 import Game14, Game14Dict


class DfsSlateGame3(SdkBaseModel):
    slate_game_id: Optional[int] = Field(default=UNSET, alias="SlateGameID")
    """Unique ID of a SlateGame (assigned by SportsDataIO)."""

    slate_id: Optional[int] = Field(default=UNSET, alias="SlateID")
    """The SlateID that this SlateGame refers to."""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game tied to this SlateGame"""

    game: Optional[Game14] = Field(default=UNSET, alias="Game")
    """The details of the game that this SlateGame refers to"""

    operator_game_id: OptionalNullable[int] = Field(default=UNSET, alias="OperatorGameID")
    """The unique ID of a SlateGame as assigned by the operator"""

    removed_by_operator: OptionalNullable[bool] = Field(default=UNSET, alias="RemovedByOperator")
    """Indicates whether this slate was removed/deleted by the operator"""


class DfsSlateGame3Dict(TypedDict):
    slate_game_id: NotRequired[int]
    slate_id: NotRequired[int]
    game_id: NotRequired[int | None]
    game: NotRequired[Game14 | Game14Dict]
    operator_game_id: NotRequired[int | None]
    removed_by_operator: NotRequired[bool | None]
