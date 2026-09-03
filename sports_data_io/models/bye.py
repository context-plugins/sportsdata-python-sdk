from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Bye(SdkBaseModel):
    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season during which this bye week occurs."""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week during this bye week (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons
    after 2021 will have only 3 preseason weeks"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team who is on a bye"""


class ByeDict(TypedDict):
    season: NotRequired[int]
    week: NotRequired[int]
    team: NotRequired[str | None]
