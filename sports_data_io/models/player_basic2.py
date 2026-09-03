from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerBasic2(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their MLB career"""

    sports_data_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsDataID")
    """Deprecated. Use SportRadarPlayerID instead."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the player's status of being on an Major League Active Roster. Possible values include: Active, 40 Man
    Active, Non-Roster Invitee, Minors, Inactive, 7 Day Injury List, 10 Day Injury List, 15 Day Injury List, 60 Day
    Injury List, Restricted List, Paternity List, Bereavement List, Military List"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category. Possible values: DH, IF, OF, P, PH, PR"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's position associated with the given game or season. Possible values: 1B; 2B; 3B; C; CF; DH; IF; LF;
    OF; P; PH; PR; RF; RP; SP; SS"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name"""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The player's date of birth"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city in which the player was born"""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The state in which the player was born. Note: State will be NULL for all countries outside of North America and
    Australia"""

    birth_country: OptionalNullable[str] = Field(default=UNSET, alias="BirthCountry")
    """The country in which the player was born"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    bat_hand: OptionalNullable[str] = Field(default=UNSET, alias="BatHand")
    """The player's batting hand. Possible values: R, L, S"""

    throw_hand: OptionalNullable[str] = Field(default=UNSET, alias="ThrowHand")
    """The player's throwing hand. Possible values: R, L, S"""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The player's height in inches"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The weight of the player in pounds (lbs.)"""


class PlayerBasic2Dict(TypedDict):
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
    bat_hand: NotRequired[str | None]
    throw_hand: NotRequired[str | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
