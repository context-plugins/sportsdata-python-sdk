from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Team7(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team"""

    area_id: OptionalNullable[int] = Field(default=UNSET, alias="AreaId")
    """The unique ID of the team's current home arena"""

    venue_id: OptionalNullable[int] = Field(default=UNSET, alias="VenueId")
    """The unique ID of the team's venue"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """Abbreviation of the team (e.g. LIV; ARS; MNU; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The mascot of the team (e.g. The Reds, The Gunners, etc.)"""

    full_name: OptionalNullable[str] = Field(default=UNSET, alias="FullName")
    """The full name of the team (e.g. Liverpool Football Club, Arsenal Football Club, etc.)"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this team is active (true/false)"""

    area_name: OptionalNullable[str] = Field(default=UNSET, alias="AreaName")
    """The area name of the home team"""

    venue_name: OptionalNullable[str] = Field(default=UNSET, alias="VenueName")
    """The name of the home team's venue"""

    gender: OptionalNullable[str] = Field(default=UNSET, alias="Gender")
    """The gender of the players on the team. Possible Values: Male; Female"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of this team. Possible values: Club, National"""

    address: OptionalNullable[str] = Field(default=UNSET, alias="Address")
    """The address of the home team"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city of the home team"""

    zip: OptionalNullable[str] = Field(default=UNSET, alias="Zip")
    """The zip code of the team's home location"""

    phone: OptionalNullable[str] = Field(default=UNSET, alias="Phone")
    """The phone number of the home team"""

    fax: OptionalNullable[str] = Field(default=UNSET, alias="Fax")
    """The fax number of the home team"""

    website: OptionalNullable[str] = Field(default=UNSET, alias="Website")
    """The website address of the home team"""

    email: OptionalNullable[str] = Field(default=UNSET, alias="Email")
    """The email of the home team"""

    founded: OptionalNullable[int] = Field(default=UNSET, alias="Founded")
    """The calendar year that the team was founded"""

    club_color1: OptionalNullable[str] = Field(default=UNSET, alias="ClubColor1")
    """The primary color of this team's logo/uniform/branding"""

    club_color2: OptionalNullable[str] = Field(default=UNSET, alias="ClubColor2")
    """The secondary color of this team's logo/uniform/branding"""

    club_color3: OptionalNullable[str] = Field(default=UNSET, alias="ClubColor3")
    """The tertiary color of this team's logo/uniform/branding"""

    nickname1: OptionalNullable[str] = Field(default=UNSET, alias="Nickname1")
    """A nickname for this team"""

    nickname2: OptionalNullable[str] = Field(default=UNSET, alias="Nickname2")
    """A nickname for this team"""

    nickname3: OptionalNullable[str] = Field(default=UNSET, alias="Nickname3")
    """A nickname for this team"""

    wikipedia_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaLogoUrl")
    """The link to the team's logo hosted on Wikipedia (This is not licensed for public or commercial use)"""

    wikipedia_word_mark_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaWordMarkUrl")
    """The link to the team's wordmark logo hosted on Wikipedia (This is not licensed for public or commercial use)"""

    global_team_id: Optional[int] = Field(default=UNSET, alias="GlobalTeamId")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    fifa_country_code: OptionalNullable[str] = Field(default=UNSET, alias="FifaCountryCode")
    """The official FIFA country code, for national teams only."""


class Team7Dict(TypedDict):
    team_id: NotRequired[int]
    area_id: NotRequired[int | None]
    venue_id: NotRequired[int | None]
    key: NotRequired[str | None]
    name: NotRequired[str | None]
    full_name: NotRequired[str | None]
    active: NotRequired[bool]
    area_name: NotRequired[str | None]
    venue_name: NotRequired[str | None]
    gender: NotRequired[str | None]
    type_: NotRequired[str | None]
    address: NotRequired[str | None]
    city: NotRequired[str | None]
    zip: NotRequired[str | None]
    phone: NotRequired[str | None]
    fax: NotRequired[str | None]
    website: NotRequired[str | None]
    email: NotRequired[str | None]
    founded: NotRequired[int | None]
    club_color1: NotRequired[str | None]
    club_color2: NotRequired[str | None]
    club_color3: NotRequired[str | None]
    nickname1: NotRequired[str | None]
    nickname2: NotRequired[str | None]
    nickname3: NotRequired[str | None]
    wikipedia_logo_url: NotRequired[str | None]
    wikipedia_word_mark_url: NotRequired[str | None]
    global_team_id: NotRequired[int]
    fifa_country_code: NotRequired[str | None]
