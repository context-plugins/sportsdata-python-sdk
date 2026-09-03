from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Season(SdkBaseModel):
    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NBA season that these totals apply for"""

    start_year: Optional[int] = Field(default=UNSET, alias="StartYear")
    """The year in which the season started"""

    end_year: Optional[int] = Field(default=UNSET, alias="EndYear")
    """The year in which the season ended"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of the season for display purposes (possible values include: 2017-18, 2018-19, etc)"""

    regular_season_start_date: OptionalNullable[str] = Field(default=UNSET, alias="RegularSeasonStartDate")
    """The start date of the regular season"""

    post_season_start_date: OptionalNullable[str] = Field(default=UNSET, alias="PostSeasonStartDate")
    """The start date of the postseason"""

    season_type: OptionalNullable[str] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar; 6=Exhibition)."""

    api_season: OptionalNullable[str] = Field(default=UNSET, alias="ApiSeason")
    """The string to pass into subsequent API calls in the season parameter (e.g. 2025REG, 2025POST, etc.)"""


class SeasonDict(TypedDict):
    season: NotRequired[int]
    start_year: NotRequired[int]
    end_year: NotRequired[int]
    description: NotRequired[str | None]
    regular_season_start_date: NotRequired[str | None]
    post_season_start_date: NotRequired[str | None]
    season_type: NotRequired[str | None]
    api_season: NotRequired[str | None]
