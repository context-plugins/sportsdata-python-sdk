from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Referee5(SdkBaseModel):
    """The second additional assistant referee"""

    referee_id: Optional[int] = Field(default=UNSET, alias="RefereeId")
    """The last name of the referee"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the referee"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of the referee"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The short name of the referee"""

    nationality: OptionalNullable[str] = Field(default=UNSET, alias="Nationality")
    """The nationality of the referee"""


class Referee5Dict(TypedDict):
    referee_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    short_name: NotRequired[str | None]
    nationality: NotRequired[str | None]
