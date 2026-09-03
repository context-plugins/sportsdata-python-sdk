from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CareerStat2(SdkBaseModel):
    """The fighter's overall career stats"""

    fighter_id: OptionalNullable[int] = Field(default=UNSET, alias="FighterId")
    """The unique ID of this fighter"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the fighter"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of the fighter"""

    sig_strikes_landed_per_minute: OptionalNullable[float] = Field(default=UNSET, alias="SigStrikesLandedPerMinute")
    """Significant strikes landed per minute over the fighter's career"""

    sig_strike_accuracy: OptionalNullable[float] = Field(default=UNSET, alias="SigStrikeAccuracy")
    """Significant strikes landed divided by strikes attempted over the fighter's career"""

    takedown_average: OptionalNullable[float] = Field(default=UNSET, alias="TakedownAverage")
    """Average takedowns landed per 15 minutes in the fighter's career"""

    submission_average: OptionalNullable[float] = Field(default=UNSET, alias="SubmissionAverage")
    """Average number of submissions attempted per 15 minutes in the fighter's career"""

    knockout_percentage: OptionalNullable[float] = Field(default=UNSET, alias="KnockoutPercentage")
    """The percentage of wins ending in a knockout by the fighter"""

    technical_knockout_percentage: OptionalNullable[float] = Field(default=UNSET, alias="TechnicalKnockoutPercentage")
    """Percentage of wins ending by TKO in the fighter's career"""

    decision_percentage: OptionalNullable[float] = Field(default=UNSET, alias="DecisionPercentage")
    """The percentage of wins ending in a decision by the fighter in their career"""


class CareerStat2Dict(TypedDict):
    fighter_id: NotRequired[int | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    sig_strikes_landed_per_minute: NotRequired[float | None]
    sig_strike_accuracy: NotRequired[float | None]
    takedown_average: NotRequired[float | None]
    submission_average: NotRequired[float | None]
    knockout_percentage: NotRequired[float | None]
    technical_knockout_percentage: NotRequired[float | None]
    decision_percentage: NotRequired[float | None]
