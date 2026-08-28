from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Stadium3(SdkBaseModel):
    """The active home stadium of the team"""

    stadium_id: Optional[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this stadium is the home venue for an active team. Note: Active = True & Inactive = False"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the stadium"""

    address: OptionalNullable[str] = Field(default=UNSET, alias="Address")
    """The address where the stadium is located (street name). Note: some stadiums will not have an address field"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city where the stadium is located"""

    state: OptionalNullable[str] = Field(default=UNSET, alias="State")
    """The US state where the stadium is located. Note: if Stadium is outside US; this value is NULL"""

    zip: OptionalNullable[str] = Field(default=UNSET, alias="Zip")
    """The zip code of the stadium"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The 3-letter country abbreviation where the stadium is located"""

    capacity: OptionalNullable[int] = Field(default=UNSET, alias="Capacity")
    """The estimated seating capacity of the stadium"""

    geo_lat: OptionalNullable[float] = Field(default=UNSET, alias="GeoLat")
    """The geographic latitude coordinate of this venue."""

    geo_long: OptionalNullable[float] = Field(default=UNSET, alias="GeoLong")
    """The geographic longitude coordinate of this venue."""


class Stadium3Dict(TypedDict):
    stadium_id: NotRequired[int]
    active: NotRequired[bool]
    name: NotRequired[str | None]
    address: NotRequired[str | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    zip: NotRequired[str | None]
    country: NotRequired[str | None]
    capacity: NotRequired[int | None]
    geo_lat: NotRequired[float | None]
    geo_long: NotRequired[float | None]
