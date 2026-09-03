from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Player6(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player through their
    career"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name."""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the player's status of being on an active roster. Possible values include: Active; Inactive; Suspended;
    Maternity; Bereavement"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when this record was last updated (in US Eastern time)"""

    available: OptionalNullable[bool] = Field(default=UNSET, alias="Available")
    """Designates whether or not the player is available (returns true/false)"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the player's team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The jersey number of the player"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: PG; SG; SF; PF; C"""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The height of the player in inches"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The weight of the player in pounds (lbs.)"""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The date (MM/DD/YYYY) the player was born"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city in which the player was born"""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The state in which the player was born (2-letter abbreviation). Note: If the player was born outside of North
    America or Australia, this field will be blank"""

    birth_country: OptionalNullable[str] = Field(default=UNSET, alias="BirthCountry")
    """The country in which the player was born"""

    college: OptionalNullable[str] = Field(default=UNSET, alias="College")
    """The last college attened by the player. Note: If the player did not attend a college, this field will be "None"
    """

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """Injury status used to project availability Statuses: Probable; Questionable; Doubtful; Out. If a player has a
    NULL injury status, they are healthy/available to play"""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """The player's body part(s) that are injured (e.g. Knee; Groin; Calf; Hamstring; etc.) Note: if a player has
    multiple injured body parts they will appear as such - Hamstring/Ankle"""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """Short description of injury involving injured body part(s), game status, player name, team name, and other extra
    news necessary. Notes are custom and can be unique"""

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The date that the injury occurred, was first discovered, or was freshly updated"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""


class Player6Dict(TypedDict):
    player_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    status: NotRequired[str | None]
    updated: NotRequired[str | None]
    available: NotRequired[bool | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    jersey: NotRequired[int | None]
    position: NotRequired[str | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
    birth_date: NotRequired[str | None]
    birth_city: NotRequired[str | None]
    birth_state: NotRequired[str | None]
    birth_country: NotRequired[str | None]
    college: NotRequired[str | None]
    injury_status: NotRequired[str | None]
    injury_body_part: NotRequired[str | None]
    injury_notes: NotRequired[str | None]
    injury_start_date: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
