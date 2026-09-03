from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class GameOddOutcome1(SdkBaseModel):
    game_odd_id: OptionalNullable[int] = Field(default=UNSET, alias="GameOddId")
    """Unique ID of this odd"""

    game_odd_result_type_id: OptionalNullable[int] = Field(default=UNSET, alias="GameOddResultTypeId")
    """The unique ID of this GameOddResultType"""

    game_odd_result_type: OptionalNullable[str] = Field(default=UNSET, alias="GameOddResultType")
    """The result/outcome of a bet (e.g. Won; Lost; Push; Not Resulted; Incomplete)"""

    odd_type: OptionalNullable[str] = Field(default=UNSET, alias="OddType")
    """The market type of the odd (ex: live; pregame; 1st inning; etc)"""

    game_odd_type: OptionalNullable[str] = Field(default=UNSET, alias="GameOddType")
    """The GameOddResultType of an outcome in the form of a string"""

    bet_value: OptionalNullable[float] = Field(default=UNSET, alias="BetValue")
    """The offered betting line from a sportsbook for a game (i.e. If a team won a game by 2 and the run line was -1.5,
    the actual value would be 2 and the bet value would be -1.5)"""

    actual_value: OptionalNullable[float] = Field(default=UNSET, alias="ActualValue")
    """The value of the actual result that occured in game (i.e. If a team won a game by 2 and the spread was -1.5, the
    actual value would be 2 and the bet value would be -1.5)"""


class GameOddOutcome1Dict(TypedDict):
    game_odd_id: NotRequired[int | None]
    game_odd_result_type_id: NotRequired[int | None]
    game_odd_result_type: NotRequired[str | None]
    odd_type: NotRequired[str | None]
    game_odd_type: NotRequired[str | None]
    bet_value: NotRequired[float | None]
    actual_value: NotRequired[float | None]
