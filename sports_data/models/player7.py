from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Player7(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerId")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career."""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of the player"""

    common_name: OptionalNullable[str] = Field(default=UNSET, alias="CommonName")
    """The player's common name"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The short name of the player"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The position of the player. Possible values include: A (Attacker); M (Midfielder); D (Defender); GK
    (Goalkeeper)."""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number"""

    foot: OptionalNullable[str] = Field(default=UNSET, alias="Foot")
    """The primary foot of the player. Possible values: left or right."""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The height of the player in centimeters (cm)"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The player's weight in kilograms (kg)"""

    gender: OptionalNullable[str] = Field(default=UNSET, alias="Gender")
    """The gender of this player on the team. Possible Values: Male; Female."""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The player's date of birth"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city in which the player was born"""

    birth_country: OptionalNullable[str] = Field(default=UNSET, alias="BirthCountry")
    """The country in which the player was born"""

    nationality: OptionalNullable[str] = Field(default=UNSET, alias="Nationality")
    """The nationality of the player"""

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """Indicates the player's injury status. Possible values: Questionable; Out."""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """The body part of the player that is injured (Knee; Groin; Calf; Hamstring; etc.)"""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """Not yet supported; will be null"""

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The date that the injury started or was first discovered"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)"""

    photo_url: OptionalNullable[str] = Field(default=UNSET, alias="PhotoUrl")
    """This field is deprecated. Note: Photos are no longer available through this field. Headshots are now delivered
    through IMAGN. Please see our Headshots products for further information."""

    roto_wire_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoWirePlayerID")
    """The player's cross reference PlayerID to the RotoWire news feed."""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The position of the player according to DraftKings"""

    usa_today_player_id: OptionalNullable[int] = Field(default=UNSET, alias="UsaTodayPlayerID")
    """The player's cross reference PlayerID to USA Today headshot data feeds"""

    usa_today_headshot_url: OptionalNullable[str] = Field(default=UNSET, alias="UsaTodayHeadshotUrl")
    """The player's headshot URL as provided by USA Today. License from USA Today is required."""

    usa_today_headshot_no_background_url: OptionalNullable[str] = Field(
        default=UNSET, alias="UsaTodayHeadshotNoBackgroundUrl"
    )
    """The player's transparent background headshot URL as provided by USA Today. License from USA Today is required."""

    usa_today_headshot_updated: OptionalNullable[str] = Field(default=UNSET, alias="UsaTodayHeadshotUpdated")
    """The last updated timestamp of the player's headshot as provided by USA Today. License from USA Today is
    required."""

    usa_today_headshot_no_background_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="UsaTodayHeadshotNoBackgroundUpdated"
    )
    """The last updated timestamp of the player's transparent background headshot as provided by USA Today. License from
    USA Today is required."""


class Player7Dict(TypedDict):
    player_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    common_name: NotRequired[str | None]
    short_name: NotRequired[str | None]
    position: NotRequired[str | None]
    position_category: NotRequired[str | None]
    jersey: NotRequired[int | None]
    foot: NotRequired[str | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
    gender: NotRequired[str | None]
    birth_date: NotRequired[str | None]
    birth_city: NotRequired[str | None]
    birth_country: NotRequired[str | None]
    nationality: NotRequired[str | None]
    injury_status: NotRequired[str | None]
    injury_body_part: NotRequired[str | None]
    injury_notes: NotRequired[str | None]
    injury_start_date: NotRequired[str | None]
    updated: NotRequired[str | None]
    photo_url: NotRequired[str | None]
    roto_wire_player_id: NotRequired[int | None]
    draft_kings_position: NotRequired[str | None]
    usa_today_player_id: NotRequired[int | None]
    usa_today_headshot_url: NotRequired[str | None]
    usa_today_headshot_no_background_url: NotRequired[str | None]
    usa_today_headshot_updated: NotRequired[str | None]
    usa_today_headshot_no_background_updated: NotRequired[str | None]
