from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .driver_race_basic import DriverRaceBasic, DriverRaceBasicDict
from .race_basic2 import RaceBasic2, RaceBasic2Dict


class RaceResultBasic(SdkBaseModel):
    race: Optional[RaceBasic2] = Field(default=UNSET, alias="Race")
    """RaceBasic object (Includes basic information such as RaceID, Day, DateTime, Updated, and Created)"""

    driver_races: Optional[list[DriverRaceBasic]] = Field(default=UNSET, alias="DriverRaces")
    """StatBasic object (includes basic information on the drivers race performance such as DriveID, Season, Driver's
    Name, Start and Final positions, Lap information, etc.)"""


class RaceResultBasicDict(TypedDict):
    race: NotRequired[RaceBasic2 | RaceBasic2Dict]
    driver_races: NotRequired[list[DriverRaceBasic | DriverRaceBasicDict]]
