from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Season1(SdkBaseModel):
    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The MLB season for which these totals apply"""

    regular_season_start_date: OptionalNullable[str] = Field(default=UNSET, alias="RegularSeasonStartDate")
    """The start date of the regular season"""

    post_season_start_date: OptionalNullable[str] = Field(default=UNSET, alias="PostSeasonStartDate")
    """The start date of the postseason"""

    season_type: OptionalNullable[str] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    api_season: OptionalNullable[str] = Field(default=UNSET, alias="ApiSeason")
    """The string to pass into subsequent API calls in the season parameter (e.g. 2025REG, 2025POST, etc.)."""


class Season1Dict(TypedDict):
    season: NotRequired[int]
    regular_season_start_date: NotRequired[str | None]
    post_season_start_date: NotRequired[str | None]
    season_type: NotRequired[str | None]
    api_season: NotRequired[str | None]
