from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DriverRaceBasic(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of this stat record"""

    driver_id: Optional[int] = Field(default=UNSET, alias="DriverID")
    """The unique ID of this driver"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season that this race is associated with"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The driver's full name"""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """The driver's car number"""

    number_display: OptionalNullable[str] = Field(default=UNSET, alias="NumberDisplay")
    """The driver's car number for display purposes (with leading zeros when necessary)"""

    manufacturer: OptionalNullable[str] = Field(default=UNSET, alias="Manufacturer")
    """The manufacturer of the driver's car"""

    start_position: OptionalNullable[float] = Field(default=UNSET, alias="StartPosition")
    """The driver's starting position for the race (typically the same as the PoleFinalPosition)"""

    final_position: OptionalNullable[float] = Field(default=UNSET, alias="FinalPosition")
    """The driver's final position for the race"""

    position_differential: OptionalNullable[float] = Field(default=UNSET, alias="PositionDifferential")
    """The driver's differential between their final position and their starting position"""

    laps: OptionalNullable[float] = Field(default=UNSET, alias="Laps")
    """The total number of laps completed by the driver"""

    laps_led: OptionalNullable[float] = Field(default=UNSET, alias="LapsLed")
    """The total number of laps that this driver completed while in first place"""

    points: OptionalNullable[float] = Field(default=UNSET, alias="Points")
    """The total points scored by this driver"""

    wins: OptionalNullable[float] = Field(default=UNSET, alias="Wins")
    """Indicates whether this driver won the race"""

    poles: OptionalNullable[float] = Field(default=UNSET, alias="Poles")
    """Indicates whether this driver won the qualifying race (pole)"""

    current_position: OptionalNullable[float] = Field(default=UNSET, alias="CurrentPosition")
    """Driver's current position in the race; updated live"""


class DriverRaceBasicDict(TypedDict):
    stat_id: NotRequired[int]
    driver_id: NotRequired[int]
    season: NotRequired[int]
    name: NotRequired[str | None]
    number: NotRequired[int | None]
    number_display: NotRequired[str | None]
    manufacturer: NotRequired[str | None]
    start_position: NotRequired[float | None]
    final_position: NotRequired[float | None]
    position_differential: NotRequired[float | None]
    laps: NotRequired[float | None]
    laps_led: NotRequired[float | None]
    points: NotRequired[float | None]
    wins: NotRequired[float | None]
    poles: NotRequired[float | None]
    current_position: NotRequired[float | None]
