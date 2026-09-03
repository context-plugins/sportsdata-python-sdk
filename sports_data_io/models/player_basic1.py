from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerBasic1(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    sports_data_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsDataID")
    """Deprecated. Use SportRadarPlayerID instead."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the player's status of being on an active roster. Possible values include: Active, Inactive"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the player's team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the player's team"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number."""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category. Possible values: C, F, G"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: PG; SG; SF; PF; C"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name."""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name."""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The player's date of birth."""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city in which the player was born."""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The state in which the player was born."""

    birth_country: OptionalNullable[str] = Field(default=UNSET, alias="BirthCountry")
    """The country in which the player was born."""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The player's height in inches."""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The player's weight in pounds (lbs)."""


class PlayerBasic1Dict(TypedDict):
    player_id: NotRequired[int]
    sports_data_id: NotRequired[str | None]
    status: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    jersey: NotRequired[int | None]
    position_category: NotRequired[str | None]
    position: NotRequired[str | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    birth_date: NotRequired[str | None]
    birth_city: NotRequired[str | None]
    birth_state: NotRequired[str | None]
    birth_country: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
