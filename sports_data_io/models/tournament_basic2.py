from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TournamentBasic2(SdkBaseModel):
    """The details of the tournament for this event"""

    tournament_id: Optional[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the tournament"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date of this tournament"""

    end_date: OptionalNullable[str] = Field(default=UNSET, alias="EndDate")
    """The end date of this tournament"""

    is_over: Optional[bool] = Field(default=UNSET, alias="IsOver")
    """Indicates whether this tournament is over"""


class TournamentBasic2Dict(TypedDict):
    tournament_id: NotRequired[int]
    name: NotRequired[str | None]
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
    is_over: NotRequired[bool]
