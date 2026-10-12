from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .fight_stat import FightStat, FightStatDict
from .fighter_info import FighterInfo, FighterInfoDict


class FightDetail(SdkBaseModel):
    fight_stats: Optional[list[FightStat]] = Field(default=UNSET, alias="FightStats")
    """Stats for each fighter in this fight"""

    fight_id: Optional[int] = Field(default=UNSET, alias="FightId")
    """The unique ID of this fight"""

    order: OptionalNullable[int] = Field(default=UNSET, alias="Order")
    """The order of this fight on the fight card"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the event's status. Possible values include: Scheduled; In Progress; Final; Suspended; Postponed;
    Canceled; NULL"""

    weight_class: OptionalNullable[str] = Field(default=UNSET, alias="WeightClass")
    """The weight class this fight is taking place at"""

    card_segment: OptionalNullable[str] = Field(default=UNSET, alias="CardSegment")
    """What segment of the card this fight is on (Main Card, Prelims, Early Prelims)"""

    referee: OptionalNullable[str] = Field(default=UNSET, alias="Referee")
    """The number of referee for this fight"""

    rounds: OptionalNullable[int] = Field(default=UNSET, alias="Rounds")
    """The number of rounds for this fight"""

    result_clock: OptionalNullable[int] = Field(default=UNSET, alias="ResultClock")
    """The time on the clock in seconds when the fight ended"""

    result_round: OptionalNullable[int] = Field(default=UNSET, alias="ResultRound")
    """The round when the fight ended"""

    result_type: OptionalNullable[str] = Field(default=UNSET, alias="ResultType")
    """The way in which this fight ended (Possible values: No Contest; Decision; Submission; KO/TKO; Decision -
    Majority; Decision - Unanimous; Decision - Split; Draw; DQ)"""

    winner_id: OptionalNullable[int] = Field(default=UNSET, alias="WinnerId")
    """The unique ID of the fighter who won the fight"""

    fighters: Optional[list[FighterInfo]] = Field(default=UNSET, alias="Fighters")
    """The fighters competing in this fight and their info (FighterID, FirstName, LastName, PreFightWins,
    PreFightLosses, PreFightDraws, PreFightNoContests, Winner, Moneyline)"""

    active: OptionalNullable[bool] = Field(default=UNSET, alias="Active")
    """Indicates the fight is still active"""


class FightDetailDict(TypedDict):
    fight_stats: NotRequired[list[FightStatDict]]
    fight_id: NotRequired[int]
    order: NotRequired[int | None]
    status: NotRequired[str | None]
    weight_class: NotRequired[str | None]
    card_segment: NotRequired[str | None]
    referee: NotRequired[str | None]
    rounds: NotRequired[int | None]
    result_clock: NotRequired[int | None]
    result_round: NotRequired[int | None]
    result_type: NotRequired[str | None]
    winner_id: NotRequired[int | None]
    fighters: NotRequired[list[FighterInfoDict]]
    active: NotRequired[bool | None]
