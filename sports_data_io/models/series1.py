from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Series1(SdkBaseModel):
    series_id: Optional[int] = Field(default=UNSET, alias="SeriesID")
    """The unique ID of this series"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this series"""


class Series1Dict(TypedDict):
    series_id: NotRequired[int]
    name: NotRequired[str | None]
