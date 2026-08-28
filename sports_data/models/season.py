from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Season(SdkBaseModel):
    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season that the game occurs in. Note: season is a single year that the majority of the season occurs in"""

    start_year: Optional[int] = Field(default=UNSET, alias="StartYear")
    """The year in which the season started"""

    end_year: Optional[int] = Field(default=UNSET, alias="EndYear")
    """The year in which the season ended"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of this season for display purposes (e.g. 2024-25; 2025-26; etc)"""

    regular_season_start_date: OptionalNullable[str] = Field(default=UNSET, alias="RegularSeasonStartDate")
    """The start date of the regular season"""

    post_season_start_date: OptionalNullable[str] = Field(default=UNSET, alias="PostSeasonStartDate")
    """The start date of the postseason"""

    api_season: OptionalNullable[str] = Field(default=UNSET, alias="ApiSeason")
    """The string to pass into subsequent API calls in the season parameter (e.g. 2025REG, 2025POST, etc.)"""


class SeasonDict(TypedDict):
    season: NotRequired[int]
    start_year: NotRequired[int]
    end_year: NotRequired[int]
    description: NotRequired[str | None]
    regular_season_start_date: NotRequired[str | None]
    post_season_start_date: NotRequired[str | None]
    api_season: NotRequired[str | None]
