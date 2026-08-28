from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Referee(SdkBaseModel):
    referee_id: Optional[int] = Field(default=UNSET, alias="RefereeID")
    """Unique ID of Referee"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The referee's full name"""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """The number of the referee"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The position of the referee in the crew"""

    college: OptionalNullable[str] = Field(default=UNSET, alias="College")
    """The college of the referee"""

    experience: OptionalNullable[int] = Field(default=UNSET, alias="Experience")
    """The number of years of experience the referee has in the NBA"""


class RefereeDict(TypedDict):
    referee_id: NotRequired[int]
    name: NotRequired[str | None]
    number: NotRequired[int | None]
    position: NotRequired[str | None]
    college: NotRequired[str | None]
    experience: NotRequired[int | None]
