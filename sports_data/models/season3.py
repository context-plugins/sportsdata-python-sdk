from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Season3(SdkBaseModel):
    season_id: Optional[int] = Field(default=UNSET, alias="SeasonID")
    """The year of the season usable in the API"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The calendar year that the current season is happening"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date of the season"""

    end_date: OptionalNullable[str] = Field(default=UNSET, alias="EndDate")
    """The end date of the season"""


class Season3Dict(TypedDict):
    season_id: NotRequired[int]
    description: NotRequired[str | None]
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
