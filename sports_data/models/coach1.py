from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Coach1(SdkBaseModel):
    """The coach of the home team"""

    coach_id: Optional[int] = Field(default=UNSET, alias="CoachId")
    """The unique ID of the coach"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """Coach's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of the coach"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The short name of the coach"""

    nationality: OptionalNullable[str] = Field(default=UNSET, alias="Nationality")
    """Coach's nationality"""


class Coach1Dict(TypedDict):
    coach_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    short_name: NotRequired[str | None]
    nationality: NotRequired[str | None]
