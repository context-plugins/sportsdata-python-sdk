from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Goaltender1(SdkBaseModel):
    """The information of the away goaltender (PlayerID, TeamID, Team, First & Last Name, Jersey Number, Confirmed)"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team the goaltender belongs to"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the goaltender"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The goaltender's last name"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The goaltender's jersey number"""

    confirmed: Optional[bool] = Field(default=UNSET, alias="Confirmed")
    """Indicates whether the starting goaltender is projected or confirmed"""


class Goaltender1Dict(TypedDict):
    player_id: NotRequired[int]
    team_id: NotRequired[int]
    team: NotRequired[str | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    jersey: NotRequired[int | None]
    confirmed: NotRequired[bool]
