from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Stadium6(SdkBaseModel):
    stadium_id: Optional[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this team is active. Note: Active = True & Inactive = False"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the stadium"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city in which the stadium is located"""

    state: OptionalNullable[str] = Field(default=UNSET, alias="State")
    """The state where the stadium is located (only US and Canadian stadiums will have values)"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The 2-digit country code where the stadium is located"""


class Stadium6Dict(TypedDict):
    stadium_id: NotRequired[int]
    active: NotRequired[bool]
    name: NotRequired[str | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    country: NotRequired[str | None]
