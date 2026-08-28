from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Stadium41(SdkBaseModel):
    """The details of this team's home stadium"""

    stadium_id: Optional[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the stadium"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city where the stadium is located"""

    state: OptionalNullable[str] = Field(default=UNSET, alias="State")
    """The city where the venue is located"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The 3-digit country code where the stadium is located"""

    capacity: OptionalNullable[int] = Field(default=UNSET, alias="Capacity")
    """The estimated seating capacity of the stadium"""

    playing_surface: OptionalNullable[str] = Field(default=UNSET, alias="PlayingSurface")
    """The playing surface of the stadium (Grass, Artificial or Dome)"""

    geo_lat: OptionalNullable[float] = Field(default=UNSET, alias="GeoLat")
    """The geographic latitude coordinate of this venue"""

    geo_long: OptionalNullable[float] = Field(default=UNSET, alias="GeoLong")
    """The geographic longitude coordinate of this venue."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of the stadium (possible values: Outdoor, Dome, RetractableDome)"""


class Stadium41Dict(TypedDict):
    stadium_id: NotRequired[int]
    name: NotRequired[str | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    country: NotRequired[str | None]
    capacity: NotRequired[int | None]
    playing_surface: NotRequired[str | None]
    geo_lat: NotRequired[float | None]
    geo_long: NotRequired[float | None]
    type_: NotRequired[str | None]
