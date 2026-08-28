from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Lineup(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO Note: this ID will stay with the player throughout their
    MLB career"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name"""

    batting_order: OptionalNullable[int] = Field(default=UNSET, alias="BattingOrder")
    """Where the player batted in the lineup for the game (1;2;3; etc.)"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """Player's position in the starting lineup (if started); otherwise the position he substituted for"""

    starting: OptionalNullable[bool] = Field(default=UNSET, alias="Starting")
    """Indicates if this player is starting. Note: started = 1 and non starting= 0"""

    confirmed: OptionalNullable[bool] = Field(default=UNSET, alias="Confirmed")
    """Indicates if batting order has been confirmed (true/false)"""


class LineupDict(TypedDict):
    player_id: NotRequired[int]
    team_id: NotRequired[int]
    team: NotRequired[str | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    batting_order: NotRequired[int | None]
    position: NotRequired[str | None]
    starting: NotRequired[bool | None]
    confirmed: NotRequired[bool | None]
