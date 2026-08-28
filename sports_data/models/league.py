from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class League(SdkBaseModel):
    league_id: Optional[int] = Field(default=UNSET, alias="LeagueId")
    """The unique ID of the MMA league"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this MMA league"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """The league abbreviation of the MMA league"""


class LeagueDict(TypedDict):
    league_id: NotRequired[int]
    name: NotRequired[str | None]
    key: NotRequired[str | None]
