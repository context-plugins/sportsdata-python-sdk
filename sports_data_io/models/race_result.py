from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .driver_race import DriverRace, DriverRaceDict
from .race1 import Race1, Race1Dict


class RaceResult(SdkBaseModel):
    race: Optional[Race1] = Field(default=UNSET, alias="Race")
    """The details of the race including general information about the race itself (Ex: Name; DateTime; Track; WinnerID;
    IsInProgress; Scheduled Laps; etc.)"""

    driver_races: Optional[list[DriverRace]] = Field(default=UNSET, alias="DriverRaces")
    """The details of the drivers in this race"""


class RaceResultDict(TypedDict):
    race: NotRequired[Race1 | Race1Dict]
    driver_races: NotRequired[list[DriverRace | DriverRaceDict]]
