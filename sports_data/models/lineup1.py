from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Lineup1(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: C; PF; PG; SF; SG"""

    starting: OptionalNullable[bool] = Field(default=UNSET, alias="Starting")
    """Indicates whether this player is in the starting lineup or on the bench"""

    confirmed: OptionalNullable[bool] = Field(default=UNSET, alias="Confirmed")
    """Indicated whether the 'Starting' field has been confirmed for a player"""

    lineup_status: OptionalNullable[str] = Field(default=UNSET, alias="LineupStatus")
    """Indicates whether player is starting, active, or inactive"""


class Lineup1Dict(TypedDict):
    player_id: NotRequired[int]
    team_id: NotRequired[int]
    team: NotRequired[str | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    position: NotRequired[str | None]
    starting: NotRequired[bool | None]
    confirmed: NotRequired[bool | None]
    lineup_status: NotRequired[str | None]
