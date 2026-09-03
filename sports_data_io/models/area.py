from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .competition import Competition, CompetitionDict


class Area(SdkBaseModel):
    area_id: Optional[int] = Field(default=UNSET, alias="AreaId")
    """The unique ID of the area"""

    country_code: OptionalNullable[str] = Field(default=UNSET, alias="CountryCode")
    """The 3-digit country or continent code where the area is located"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The display name of the area"""

    competitions: Optional[list[Competition]] = Field(default=UNSET, alias="Competitions")
    """The competitions that are associated with and/or played in the area"""


class AreaDict(TypedDict):
    area_id: NotRequired[int]
    country_code: NotRequired[str | None]
    name: NotRequired[str | None]
    competitions: NotRequired[list[Competition | CompetitionDict]]
