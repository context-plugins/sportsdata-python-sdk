from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Round1(SdkBaseModel):
    tournament_id: Optional[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament"""

    round_id: Optional[int] = Field(default=UNSET, alias="RoundID")
    """The unique ID of the round of this tournament"""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """The number of the round"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date that this round is being played on"""

    is_round_over: OptionalNullable[bool] = Field(default=UNSET, alias="IsRoundOver")
    """Indicates whether a Round is over"""


class Round1Dict(TypedDict):
    tournament_id: NotRequired[int]
    round_id: NotRequired[int]
    number: NotRequired[int | None]
    day: NotRequired[str | None]
    is_round_over: NotRequired[bool | None]
