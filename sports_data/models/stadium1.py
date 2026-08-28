from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Stadium1(SdkBaseModel):
    stadium_id: Optional[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this stadium is the home venue for an active team"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the stadium"""

    dome: Optional[bool] = Field(default=UNSET, alias="Dome")
    """Indicates whether this stadium is a dome"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city where the stadium is located"""

    state: OptionalNullable[str] = Field(default=UNSET, alias="State")
    """The US state where the stadium is located Note: if stadium is outside United States; this value is NULL"""

    geo_lat: OptionalNullable[float] = Field(default=UNSET, alias="GeoLat")
    """The geographic latitude coordinate of this venue"""

    geo_long: OptionalNullable[float] = Field(default=UNSET, alias="GeoLong")
    """The geographic longitude coordinate of this venue"""


class Stadium1Dict(TypedDict):
    stadium_id: NotRequired[int]
    active: NotRequired[bool]
    name: NotRequired[str | None]
    dome: NotRequired[bool]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    geo_lat: NotRequired[float | None]
    geo_long: NotRequired[float | None]
