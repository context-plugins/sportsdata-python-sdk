from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Season4(SdkBaseModel):
    year: Optional[int] = Field(default=UNSET, alias="Year")
    """The WNBA season for which these totals apply"""

    preseason_start_date: OptionalNullable[str] = Field(default=UNSET, alias="PreseasonStartDate")
    """The start date of the preseason"""

    regular_season_start_date: OptionalNullable[str] = Field(default=UNSET, alias="RegularSeasonStartDate")
    """The start date of the regular season"""

    post_season_start_date: OptionalNullable[str] = Field(default=UNSET, alias="PostSeasonStartDate")
    """The start date of the postseason"""

    current_season_type: OptionalNullable[str] = Field(default=UNSET, alias="CurrentSeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar)"""

    api_season: OptionalNullable[str] = Field(default=UNSET, alias="ApiSeason")
    """The string to pass into subsequent API calls in the season parameter (e.g. 2025REG, 2025POST, etc.)."""


class Season4Dict(TypedDict):
    year: NotRequired[int]
    preseason_start_date: NotRequired[str | None]
    regular_season_start_date: NotRequired[str | None]
    post_season_start_date: NotRequired[str | None]
    current_season_type: NotRequired[str | None]
    api_season: NotRequired[str | None]
