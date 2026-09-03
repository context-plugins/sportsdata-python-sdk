from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Sportsbook(SdkBaseModel):
    """The sportsbook offering this outcome for betting, Name of sportsbook, The sportsbook offering this outcome for
    betting, The sportsbook offering this outcome for betting, The name of the sportsbook that is offering this outcome
    for betting, The sportsbook offering this outcome for betting, The sportsbook offering this outcome for betting, The
    sportsbook offering this outcome for betting, The sportsbook offering this outcome for betting, The sportsbook
    offering this outcome for betting"""

    sportsbook_id: Optional[int] = Field(default=UNSET, alias="SportsbookID")
    """Unique ID of the sportsbook"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the sportsbook(s)"""


class SportsbookDict(TypedDict):
    sportsbook_id: NotRequired[int]
    name: NotRequired[str | None]
