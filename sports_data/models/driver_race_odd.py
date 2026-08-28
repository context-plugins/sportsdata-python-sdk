from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DriverRaceOdd(SdkBaseModel):
    driver_race_odd_id: Optional[int] = Field(default=UNSET, alias="DriverRaceOddID")
    """The unique ID of the DriverRaceOdd record"""

    sportsbook_id: OptionalNullable[int] = Field(default=UNSET, alias="SportsbookID")
    """The ID of the Sportsbook associated with this record"""

    sportsbook_name: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookName")
    """The name of the Sportbook"""

    driver_name: OptionalNullable[str] = Field(default=UNSET, alias="DriverName")
    """The driver's full name"""

    driver_id: OptionalNullable[int] = Field(default=UNSET, alias="DriverID")
    """The unique ID of the driver associated with this record"""

    odds_to_win: Optional[int] = Field(default=UNSET, alias="OddsToWin")
    """The odds for this record, in American format i.e. +800, -200, etc."""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date/time when this race was created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time when this record was last seen from the sportsbook"""

    is_available: Optional[bool] = Field(default=UNSET, alias="IsAvailable")
    """Indicates whether the odd is available for wagering at the related Sportsbook (excludes Consensus)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""


class DriverRaceOddDict(TypedDict):
    driver_race_odd_id: NotRequired[int]
    sportsbook_id: NotRequired[int | None]
    sportsbook_name: NotRequired[str | None]
    driver_name: NotRequired[str | None]
    driver_id: NotRequired[int | None]
    odds_to_win: NotRequired[int]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    is_available: NotRequired[bool]
    sportsbook_url: NotRequired[str | None]
