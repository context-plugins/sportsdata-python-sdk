from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DriverRace(SdkBaseModel):
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

    draft_kings_salary: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsSalary")
    """The DraftKings salary of the driver for this race"""

    race_id: OptionalNullable[int] = Field(default=UNSET, alias="RaceID")
    """The unique ID of this race"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of this race"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date/time of this race"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date/time when this record was last updated"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date/time when this record was created"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """The fantasy points scored by this driver"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """The fantasy points scored by this driver, according to the DraftKings scoring system"""

    qualifying_speed: OptionalNullable[float] = Field(default=UNSET, alias="QualifyingSpeed")
    """The speed of this driver's car during the qualifying race"""

    pole_final_position: OptionalNullable[float] = Field(default=UNSET, alias="PoleFinalPosition")
    """The final position this driver finished in the qualifying race (pole)"""

    start_position: OptionalNullable[float] = Field(default=UNSET, alias="StartPosition")
    """The driver's starting position for the race (typically the same as the PoleFinalPosition)"""

    final_position: OptionalNullable[float] = Field(default=UNSET, alias="FinalPosition")
    """The driver's final position for the race"""

    position_differential: OptionalNullable[float] = Field(default=UNSET, alias="PositionDifferential")
    """The driver's differential between the final position and the starting position"""

    laps: OptionalNullable[float] = Field(default=UNSET, alias="Laps")
    """The total number of laps completed by the driver"""

    laps_led: OptionalNullable[float] = Field(default=UNSET, alias="LapsLed")
    """The total number of laps that this driver finished in first place"""

    fastest_laps: OptionalNullable[float] = Field(default=UNSET, alias="FastestLaps")
    """The total number of laps that this driver finished fastest"""

    points: OptionalNullable[float] = Field(default=UNSET, alias="Points")
    """The total points scored by this driver"""

    bonus: OptionalNullable[float] = Field(default=UNSET, alias="Bonus")
    """The total bonus points scored by this driver"""

    penalty: OptionalNullable[float] = Field(default=UNSET, alias="Penalty")
    """The total penalty points applied to this driver"""

    wins: OptionalNullable[float] = Field(default=UNSET, alias="Wins")
    """Indicates whether this driver won the race"""

    poles: OptionalNullable[float] = Field(default=UNSET, alias="Poles")
    """Indicates whether this driver won the qualifying race (pole)"""

    current_position: OptionalNullable[float] = Field(default=UNSET, alias="CurrentPosition")
    """Driver's current position in the race, updated live."""


class DriverRaceDict(TypedDict):
    stat_id: NotRequired[int]
    driver_id: NotRequired[int]
    season: NotRequired[int]
    name: NotRequired[str | None]
    number: NotRequired[int | None]
    number_display: NotRequired[str | None]
    manufacturer: NotRequired[str | None]
    draft_kings_salary: NotRequired[int | None]
    race_id: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    fantasy_points: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    qualifying_speed: NotRequired[float | None]
    pole_final_position: NotRequired[float | None]
    start_position: NotRequired[float | None]
    final_position: NotRequired[float | None]
    position_differential: NotRequired[float | None]
    laps: NotRequired[float | None]
    laps_led: NotRequired[float | None]
    fastest_laps: NotRequired[float | None]
    points: NotRequired[float | None]
    bonus: NotRequired[float | None]
    penalty: NotRequired[float | None]
    wins: NotRequired[float | None]
    poles: NotRequired[float | None]
    current_position: NotRequired[float | None]
