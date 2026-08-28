from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Sportsbook(SdkBaseModel):
    sportsbook_id: Optional[int] = Field(default=UNSET, alias="SportsbookID")
    """The unique ID associated with this sportsbook"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the sportsbook"""


class SportsbookDict(TypedDict):
    sportsbook_id: NotRequired[int]
    name: NotRequired[str | None]
