from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Stadium3(SdkBaseModel):
    stadium_id: Optional[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this stadium is active"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the stadium"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city where the stadium is located"""

    state: OptionalNullable[str] = Field(default=UNSET, alias="State")
    """The state where the stadium is located (only US and Canadian stadiums will have values)"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The 3-digit country code where the stadium is located"""

    capacity: OptionalNullable[int] = Field(default=UNSET, alias="Capacity")
    """The estimated seating capacity of the stadium"""

    surface: OptionalNullable[str] = Field(default=UNSET, alias="Surface")
    """The playing surface of the stadium (Grass, Artificial or Dome)"""

    left_field: OptionalNullable[int] = Field(default=UNSET, alias="LeftField")
    """The estimated distance between home plate and the left field wall"""

    mid_left_field: OptionalNullable[int] = Field(default=UNSET, alias="MidLeftField")
    """The estimated distance between home plate and the mid left field wall"""

    left_center_field: OptionalNullable[int] = Field(default=UNSET, alias="LeftCenterField")
    """The estimated distance between home plate and the left center field wall"""

    mid_left_center_field: OptionalNullable[int] = Field(default=UNSET, alias="MidLeftCenterField")
    """The estimated distance between home plate and the mid left center field wall"""

    center_field: OptionalNullable[int] = Field(default=UNSET, alias="CenterField")
    """The estimated distance between home plate and the center field wall"""

    mid_right_center_field: OptionalNullable[int] = Field(default=UNSET, alias="MidRightCenterField")
    """The estimated distance between home plate and the mid right center field wall"""

    right_center_field: OptionalNullable[int] = Field(default=UNSET, alias="RightCenterField")
    """The estimated distance between home plate and the right center field wall"""

    mid_right_field: OptionalNullable[int] = Field(default=UNSET, alias="MidRightField")
    """The estimated distance between home plate and the mid right field wall"""

    right_field: OptionalNullable[int] = Field(default=UNSET, alias="RightField")
    """The estimated distance between home plate and the right field wall"""

    geo_lat: OptionalNullable[float] = Field(default=UNSET, alias="GeoLat")
    """The geographic latitude coordinate of this venue"""

    geo_long: OptionalNullable[float] = Field(default=UNSET, alias="GeoLong")
    """The geographic longitude coordinate of this venue"""

    altitude: OptionalNullable[int] = Field(default=UNSET, alias="Altitude")
    """The altitude of the stadium in feet"""

    home_plate_direction: OptionalNullable[int] = Field(default=UNSET, alias="HomePlateDirection")
    """The direction that the batter is facing while looking at the pitcher's mound. If the home plate is at the north
    of the stadium, the batter is facing south, so the value is given as 180 degrees. If home plate is at the east the
    batter faces west, so it's 270 degrees. If the home plate is at the south the batter faces north, so it's 0 degrees.
    If the home plate is at the west the batter faces east, so it's 90 degrees."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of the stadium (possible values: Outdoor, Dome, RetractableDome)"""


class Stadium3Dict(TypedDict):
    stadium_id: NotRequired[int]
    active: NotRequired[bool]
    name: NotRequired[str | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    country: NotRequired[str | None]
    capacity: NotRequired[int | None]
    surface: NotRequired[str | None]
    left_field: NotRequired[int | None]
    mid_left_field: NotRequired[int | None]
    left_center_field: NotRequired[int | None]
    mid_left_center_field: NotRequired[int | None]
    center_field: NotRequired[int | None]
    mid_right_center_field: NotRequired[int | None]
    right_center_field: NotRequired[int | None]
    mid_right_field: NotRequired[int | None]
    right_field: NotRequired[int | None]
    geo_lat: NotRequired[float | None]
    geo_long: NotRequired[float | None]
    altitude: NotRequired[int | None]
    home_plate_direction: NotRequired[int | None]
    type_: NotRequired[str | None]
