from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FighterInfo(SdkBaseModel):
    fighter_id: OptionalNullable[int] = Field(default=UNSET, alias="FighterId")
    """The unique ID of this fighter"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the fighter"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of the fighter"""

    pre_fight_wins: OptionalNullable[int] = Field(default=UNSET, alias="PreFightWins")
    """The fighter's win total prior to the fight"""

    pre_fight_losses: OptionalNullable[int] = Field(default=UNSET, alias="PreFightLosses")
    """The fighter's loss total prior to the fight"""

    pre_fight_draws: OptionalNullable[int] = Field(default=UNSET, alias="PreFightDraws")
    """The fighter's draw total prior to the fight"""

    pre_fight_no_contests: OptionalNullable[int] = Field(default=UNSET, alias="PreFightNoContests")
    """The fighter's no contest total prior to the fight"""

    winner: OptionalNullable[bool] = Field(default=UNSET, alias="Winner")
    """Indicates if this fighter won the fight"""

    moneyline: OptionalNullable[int] = Field(default=UNSET, alias="Moneyline")
    """Moneyline for the fighter's odds to win the fight"""

    active: OptionalNullable[bool] = Field(default=UNSET, alias="Active")
    """Indicates the fighter is still listed for this fight"""


class FighterInfoDict(TypedDict):
    fighter_id: NotRequired[int | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    pre_fight_wins: NotRequired[int | None]
    pre_fight_losses: NotRequired[int | None]
    pre_fight_draws: NotRequired[int | None]
    pre_fight_no_contests: NotRequired[int | None]
    winner: NotRequired[bool | None]
    moneyline: NotRequired[int | None]
    active: NotRequired[bool | None]
