from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .career_stat2 import CareerStat2, CareerStat2Dict


class Fighter(SdkBaseModel):
    fighter_id: Optional[int] = Field(default=UNSET, alias="FighterId")
    """The unique ID of this fighter"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the fighter"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of the fighter"""

    nickname: OptionalNullable[str] = Field(default=UNSET, alias="Nickname")
    """The nickname of the fighter"""

    weight_class: OptionalNullable[str] = Field(default=UNSET, alias="WeightClass")
    """The fighter's weight class"""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The fighter's date of birth"""

    height: OptionalNullable[float] = Field(default=UNSET, alias="Height")
    """The height of the fighter"""

    weight: OptionalNullable[float] = Field(default=UNSET, alias="Weight")
    """The fighter's weight in pounds (lbs.)"""

    reach: OptionalNullable[float] = Field(default=UNSET, alias="Reach")
    """The fighter's reach"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """The total number of wins the fighter has in their career"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """Total number of losses by the fighter in their career"""

    draws: OptionalNullable[int] = Field(default=UNSET, alias="Draws")
    """The total number of fights in the fighter's career that ended in a draw"""

    no_contests: OptionalNullable[int] = Field(default=UNSET, alias="NoContests")
    """The total number of fights in the fighter's career that ended in a no contest"""

    technical_knockouts: OptionalNullable[int] = Field(default=UNSET, alias="TechnicalKnockouts")
    """Total technical knockout (TKO) wins by the fighter in their career"""

    technical_knockout_losses: OptionalNullable[int] = Field(default=UNSET, alias="TechnicalKnockoutLosses")
    """Total technical knockout (TKO) losses by the fighter in their career"""

    submissions: OptionalNullable[int] = Field(default=UNSET, alias="Submissions")
    """Total submission wins by the fighter in their career"""

    submission_losses: OptionalNullable[int] = Field(default=UNSET, alias="SubmissionLosses")
    """Total submission losses by the fighter in their career"""

    title_wins: OptionalNullable[int] = Field(default=UNSET, alias="TitleWins")
    """Total title fight wins by the fighter in their career"""

    title_losses: OptionalNullable[int] = Field(default=UNSET, alias="TitleLosses")
    """Total title fight losses by the fighter in their career"""

    title_draws: OptionalNullable[int] = Field(default=UNSET, alias="TitleDraws")
    """The fighter's title draws"""

    career_stats: Optional[CareerStat2] = Field(default=UNSET, alias="CareerStats")
    """The fighter's overall career stats"""


class FighterDict(TypedDict):
    fighter_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    nickname: NotRequired[str | None]
    weight_class: NotRequired[str | None]
    birth_date: NotRequired[str | None]
    height: NotRequired[float | None]
    weight: NotRequired[float | None]
    reach: NotRequired[float | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    draws: NotRequired[int | None]
    no_contests: NotRequired[int | None]
    technical_knockouts: NotRequired[int | None]
    technical_knockout_losses: NotRequired[int | None]
    submissions: NotRequired[int | None]
    submission_losses: NotRequired[int | None]
    title_wins: NotRequired[int | None]
    title_losses: NotRequired[int | None]
    title_draws: NotRequired[int | None]
    career_stats: NotRequired[CareerStat2Dict]
