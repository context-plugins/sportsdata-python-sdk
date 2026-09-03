from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BettingOutcomeResult(SdkBaseModel):
    betting_outcome_id: Optional[int] = Field(default=UNSET, alias="BettingOutcomeID")
    """The unique ID associated with the betting outcome"""

    betting_result_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingResultTypeID")
    """The BettingResultTypeID of this outcome"""

    betting_result_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingResultType")
    """The string identifier of the BettingResultType of this outcome (e.g. Win; Loss; Push; Not Resulted;
    Incomplete)"""

    betting_outcome_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeTypeID")
    """The unique ID associated with this BettingOutcomeType"""

    betting_outcome_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingOutcomeType")
    """The name of BettingOutcomeType (e.g. Home; Away; Under; Over)"""

    bet_value: OptionalNullable[float] = Field(default=UNSET, alias="BetValue")
    """The offered betting line from a sportsbook for a game (i.e. If a team won a game by 5 and the spread was -6.5,
    the actual value would be 5 and the bet value would be -6.5)"""

    actual_value: OptionalNullable[float] = Field(default=UNSET, alias="ActualValue")
    """The value of the actual result that occured in game (i.e. If a team won a game by 5 and the spread was -6.5, the
    actual value would be 5 and the bet value would be -6.5)"""


class BettingOutcomeResultDict(TypedDict):
    betting_outcome_id: NotRequired[int]
    betting_result_type_id: NotRequired[int | None]
    betting_result_type: NotRequired[str | None]
    betting_outcome_type_id: NotRequired[int | None]
    betting_outcome_type: NotRequired[str | None]
    bet_value: NotRequired[float | None]
    actual_value: NotRequired[float | None]
