from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .fighter1 import Fighter1, Fighter1Dict
from .fighter2 import Fighter2, Fighter2Dict


class FightOdds(SdkBaseModel):
    fight_odd_id: OptionalNullable[int] = Field(default=UNSET, alias="FightOddId")
    """The unique ID of this FIghtOdd"""

    sportsbook_id: OptionalNullable[int] = Field(default=UNSET, alias="SportsbookId")
    """The unique ID of this Sportsbook"""

    sportsbook_name: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookName")
    """The name of Sportsbook"""

    event_id: OptionalNullable[int] = Field(default=UNSET, alias="EventId")
    """The unique ID of this event"""

    fight_id: OptionalNullable[int] = Field(default=UNSET, alias="FightId")
    """The unique ID of this Fight"""

    fighter_a: Optional[Fighter1] = Field(default=UNSET, alias="FighterA")
    """The details of Fighter A"""

    fighter_b: Optional[Fighter2] = Field(default=UNSET, alias="FighterB")
    """The details of Fighter B"""

    fighter_a_moneyline: OptionalNullable[int] = Field(default=UNSET, alias="FighterAMoneyline")
    """The sportsbook's moneyline for Fighter A"""

    fighter_b_moneyline: OptionalNullable[int] = Field(default=UNSET, alias="FighterBMoneyline")
    """The sportsbook's moneyline for Fighter B"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when these odds were first created based on US Eastern Time"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when these odds were last updated (in US Eastern Time)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for the sportsbook event"""


class FightOddsDict(TypedDict):
    fight_odd_id: NotRequired[int | None]
    sportsbook_id: NotRequired[int | None]
    sportsbook_name: NotRequired[str | None]
    event_id: NotRequired[int | None]
    fight_id: NotRequired[int | None]
    fighter_a: NotRequired[Fighter1 | Fighter1Dict]
    fighter_b: NotRequired[Fighter2 | Fighter2Dict]
    fighter_a_moneyline: NotRequired[int | None]
    fighter_b_moneyline: NotRequired[int | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    sportsbook_url: NotRequired[str | None]
