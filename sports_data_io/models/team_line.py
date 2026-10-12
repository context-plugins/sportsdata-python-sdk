from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .player_line import PlayerLine, PlayerLineDict


class TeamLine(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """"The abbreviation [Key] of the team associated with this market (Ex. BOS, EDM, LAK)"
    """

    full_name: OptionalNullable[str] = Field(default=UNSET, alias="FullName")
    """The team's full name (ex. Minnesota Wild; New York Islanders)"""

    even_strength_lines: Optional[list[PlayerLine]] = Field(default=UNSET, alias="EvenStrengthLines")
    """The even strength lines for this team"""

    power_play_lines: Optional[list[PlayerLine]] = Field(default=UNSET, alias="PowerPlayLines")
    """The power play lines for a given team"""

    short_handed_lines: Optional[list[PlayerLine]] = Field(default=UNSET, alias="ShortHandedLines")
    """The short-handed/penalty-kill lines for this team"""


class TeamLineDict(TypedDict):
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    full_name: NotRequired[str | None]
    even_strength_lines: NotRequired[list[PlayerLineDict]]
    power_play_lines: NotRequired[list[PlayerLineDict]]
    short_handed_lines: NotRequired[list[PlayerLineDict]]
