from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event1 import Event1, Event1Dict
from .fight_odds import FightOdds, FightOddsDict


class EventOdds(SdkBaseModel):
    event: Optional[Event1] = Field(default=UNSET, alias="Event")
    """The Event as an object - including the EventID, LeagueID, Name (and ShortName)of the Event, Season, Day,
    DateTime, & Status"""

    fight_odds: Optional[list[FightOdds]] = Field(default=UNSET, alias="FightOdds")
    """The Event's collection of FightOdds"""


class EventOddsDict(TypedDict):
    event: NotRequired[Event1 | Event1Dict]
    fight_odds: NotRequired[list[FightOdds | FightOddsDict]]
