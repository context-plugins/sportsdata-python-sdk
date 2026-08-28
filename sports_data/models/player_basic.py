from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerBasic(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their collegiate career"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the player's team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the player's team"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number (0-99)"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's eligible position(s). Possible values: C; F; F-C; G; G-F, PG, SG, SF, PF"""

    class_: OptionalNullable[str] = Field(default=UNSET, alias="Class")
    """The class of the year (e.g. Freshman; Sophomore; Junior; Senior; Graduate Student). Note: Redshirt classes
    available for Freshman, Sophomore, Junior, Senior"""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The player's height in inches"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The player's weight in pounds (lbs)"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city in which the player was born"""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The state in which the player was born (two letter abbreviation)"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""


class PlayerBasicDict(TypedDict):
    player_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    jersey: NotRequired[int | None]
    position: NotRequired[str | None]
    class_: NotRequired[str | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
    birth_city: NotRequired[str | None]
    birth_state: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
