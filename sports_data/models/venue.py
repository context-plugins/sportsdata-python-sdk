from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Venue(SdkBaseModel):
    venue_id: Optional[int] = Field(default=UNSET, alias="VenueId")
    """The unique ID of the venue"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the venue"""

    address: OptionalNullable[str] = Field(default=UNSET, alias="Address")
    """The address where the venue is located"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city where the venue is located"""

    zip: OptionalNullable[str] = Field(default=UNSET, alias="Zip")
    """The zip code of where the venue is located"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The country name of where the venue is located"""

    open: Optional[bool] = Field(default=UNSET, alias="Open")
    """Indicates whether this venue is actively used"""

    opened: OptionalNullable[int] = Field(default=UNSET, alias="Opened")
    """The year the venue opened (e.g. 1950; 1960; etc)"""

    nickname1: OptionalNullable[str] = Field(default=UNSET, alias="Nickname1")
    """A nickname for this venue"""

    nickname2: OptionalNullable[str] = Field(default=UNSET, alias="Nickname2")
    """A nickname for this venue"""

    capacity: OptionalNullable[int] = Field(default=UNSET, alias="Capacity")
    """The estimated seating capacity of the venue"""

    surface: OptionalNullable[str] = Field(default=UNSET, alias="Surface")
    """The playing surface of the stadium. Possible values: Grass; Artificial"""

    geo_lat: OptionalNullable[float] = Field(default=UNSET, alias="GeoLat")
    """The geographic latitude coordinate of this venue"""

    geo_long: OptionalNullable[float] = Field(default=UNSET, alias="GeoLong")
    """The geographic latitude coordinate of this venue"""


class VenueDict(TypedDict):
    venue_id: NotRequired[int]
    name: NotRequired[str | None]
    address: NotRequired[str | None]
    city: NotRequired[str | None]
    zip: NotRequired[str | None]
    country: NotRequired[str | None]
    open: NotRequired[bool]
    opened: NotRequired[int | None]
    nickname1: NotRequired[str | None]
    nickname2: NotRequired[str | None]
    capacity: NotRequired[int | None]
    surface: NotRequired[str | None]
    geo_lat: NotRequired[float | None]
    geo_long: NotRequired[float | None]
