from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class GameOddOutcome(SdkBaseModel):
    game_odd_id: Optional[int] = Field(default=UNSET, alias="GameOddId")
    """The unique ID of this odd"""

    game_odd_result_type_id: OptionalNullable[int] = Field(default=UNSET, alias="GameOddResultTypeId")
    """The unique ID of this GameOddResultType"""

    game_odd_result_type: OptionalNullable[str] = Field(default=UNSET, alias="GameOddResultType")
    """The result/outcome of a bet (e.g. Won; Lost; Push; Not Resulted; Incomplete)"""

    odd_type: OptionalNullable[str] = Field(default=UNSET, alias="OddType")
    """The market type of the odd (ex. live, pregame, 1st-5th ining, etc)"""

    game_odd_type: OptionalNullable[str] = Field(default=UNSET, alias="GameOddType")
    """The GameOddOutcomeType of this outcome as a string"""

    bet_value: OptionalNullable[float] = Field(default=UNSET, alias="BetValue")
    """The value that was bet in this outcome (if applicable)"""

    actual_value: OptionalNullable[float] = Field(default=UNSET, alias="ActualValue")
    """The value of the actual result that occured in game (i.e. If a team won a game by 5 and the spread was -6.5, the
    actual value would be 5 and the bet value would be -6.5)"""


class GameOddOutcomeDict(TypedDict):
    game_odd_id: NotRequired[int]
    game_odd_result_type_id: NotRequired[int | None]
    game_odd_result_type: NotRequired[str | None]
    odd_type: NotRequired[str | None]
    game_odd_type: NotRequired[str | None]
    bet_value: NotRequired[float | None]
    actual_value: NotRequired[float | None]
