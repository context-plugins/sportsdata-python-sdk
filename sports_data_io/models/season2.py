from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Season2(SdkBaseModel):
    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NCAA football season"""

    start_year: Optional[int] = Field(default=UNSET, alias="StartYear")
    """The year in which the season started"""

    end_year: Optional[int] = Field(default=UNSET, alias="EndYear")
    """The year in which the season ended"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of this season for display purposes"""

    api_season: OptionalNullable[str] = Field(default=UNSET, alias="ApiSeason")
    """The string to pass into subsequent API calls in the season parameter"""

    api_week: OptionalNullable[int] = Field(default=UNSET, alias="ApiWeek")
    """The current week which can be passed into subsequent API calls in the week parameter"""


class Season2Dict(TypedDict):
    season: NotRequired[int]
    start_year: NotRequired[int]
    end_year: NotRequired[int]
    description: NotRequired[str | None]
    api_season: NotRequired[str | None]
    api_week: NotRequired[int | None]
