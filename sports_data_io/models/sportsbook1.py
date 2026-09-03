from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Sportsbook1(SdkBaseModel):
    """Name of sportsbook"""

    sportsbook_id: Optional[int] = Field(default=UNSET, alias="SportsbookID")
    """Unique ID of the sportsbook"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the sportsbook(s)"""


class Sportsbook1Dict(TypedDict):
    sportsbook_id: NotRequired[int]
    name: NotRequired[str | None]
