from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Referee(SdkBaseModel):
    referee_id: Optional[int] = Field(default=UNSET, alias="RefereeID")
    """The unique ID of the referee"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the referee"""

    number: Optional[int] = Field(default=UNSET, alias="Number")
    """The referee's number"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The referee's position"""

    college: OptionalNullable[str] = Field(default=UNSET, alias="College")
    """The referee's college"""

    experience: Optional[int] = Field(default=UNSET, alias="Experience")
    """The referee's years of experience"""


class RefereeDict(TypedDict):
    referee_id: NotRequired[int]
    name: NotRequired[str | None]
    number: NotRequired[int]
    position: NotRequired[str | None]
    college: NotRequired[str | None]
    experience: NotRequired[int]
