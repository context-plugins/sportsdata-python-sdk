from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Driver(SdkBaseModel):
    driver_id: Optional[int] = Field(default=UNSET, alias="DriverID")
    """The unique ID of this driver (assigned by SportsDataIO)"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The driver's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The driver's last name"""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """The driver's car number"""

    number_display: OptionalNullable[str] = Field(default=UNSET, alias="NumberDisplay")
    """The driver's car number for display purposes (with leading zeros when necessary)"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The driver's team name"""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The driver's birthdate"""

    birth_place: OptionalNullable[str] = Field(default=UNSET, alias="BirthPlace")
    """The driver's birthplace"""

    gender: OptionalNullable[str] = Field(default=UNSET, alias="Gender")
    """The driver's gender"""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The driver's height"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The driver's weight"""

    manufacturer: OptionalNullable[str] = Field(default=UNSET, alias="Manufacturer")
    """The manufacturer of the driver's car"""

    engine: OptionalNullable[str] = Field(default=UNSET, alias="Engine")
    """The engine type of the driver's car"""

    chassis: OptionalNullable[str] = Field(default=UNSET, alias="Chassis")
    """The chassis of the driver's car"""

    sponsors: OptionalNullable[str] = Field(default=UNSET, alias="Sponsors")
    """The names of the sponsor(s) of the driver"""

    crew_chief: OptionalNullable[str] = Field(default=UNSET, alias="CrewChief")
    """The name of the crew chief for the driver"""

    photo_url: OptionalNullable[str] = Field(default=UNSET, alias="PhotoUrl")
    """This field is deprecated. Photos are no longer available through it. Headshots are now delivered through IMAGN.
    Please see our Headshots products for further information."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date/time when this driver was last updated"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date/time when this driver was created (in US Eastern Time)"""


class DriverDict(TypedDict):
    driver_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    number: NotRequired[int | None]
    number_display: NotRequired[str | None]
    team: NotRequired[str | None]
    birth_date: NotRequired[str | None]
    birth_place: NotRequired[str | None]
    gender: NotRequired[str | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
    manufacturer: NotRequired[str | None]
    engine: NotRequired[str | None]
    chassis: NotRequired[str | None]
    sponsors: NotRequired[str | None]
    crew_chief: NotRequired[str | None]
    photo_url: NotRequired[str | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
