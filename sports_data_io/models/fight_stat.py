from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FightStat(SdkBaseModel):
    fighter_id: OptionalNullable[int] = Field(default=UNSET, alias="FighterId")
    """The unique ID of this fighter"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the fighter"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of the fighter"""

    winner: OptionalNullable[bool] = Field(default=UNSET, alias="Winner")
    """Indicates if this fighter won the fight"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points scored by the fighter in the fight"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total DraftKings fantasy points scored by the fighter in the fight"""

    knockdowns: OptionalNullable[float] = Field(default=UNSET, alias="Knockdowns")
    """The total number of official knockdowns by the fighter to the opponent"""

    total_strikes_attempted: OptionalNullable[float] = Field(default=UNSET, alias="TotalStrikesAttempted")
    """Total number of all strikes attempted by the fighter in this fight"""

    total_strikes_landed: OptionalNullable[float] = Field(default=UNSET, alias="TotalStrikesLanded")
    """Total number of all strikes landed by the fighter in this fight"""

    sig_strikes_attempted: OptionalNullable[float] = Field(default=UNSET, alias="SigStrikesAttempted")
    """Total number of strikes attempted that officials deem significant strikes by the fighter in this fight"""

    sig_strikes_landed: OptionalNullable[float] = Field(default=UNSET, alias="SigStrikesLanded")
    """Total number of strikes landed that officials deem significant strikes by the fighter in this fight"""

    takedowns_attempted: OptionalNullable[float] = Field(default=UNSET, alias="TakedownsAttempted")
    """Total number of takedowns attempted by the fighter in this fight"""

    takedowns_landed: OptionalNullable[float] = Field(default=UNSET, alias="TakedownsLanded")
    """Total number of takedowns landed by the fighter in this fight"""

    takedowns_slams: OptionalNullable[float] = Field(default=UNSET, alias="TakedownsSlams")
    """Total number of takedowns that were a result of forcefully slamming opponent to ground by the fighter in this
    fight"""

    takedown_accuracy: OptionalNullable[float] = Field(default=UNSET, alias="TakedownAccuracy")
    """Total number of takedowns landed divided by number of takedowns attempted"""

    advances: OptionalNullable[float] = Field(default=UNSET, alias="Advances")
    """Total number of advances to half guard, side control, mount, or back control"""

    reversals: OptionalNullable[float] = Field(default=UNSET, alias="Reversals")
    """Transitions performed by countering your opponents transition and giving fighter the offensive advantage."""

    submissions: OptionalNullable[float] = Field(default=UNSET, alias="Submissions")
    """Total number of submissions or technical submissions attempted"""

    slam_rate: OptionalNullable[float] = Field(default=UNSET, alias="SlamRate")
    """Number of takedown slams landed divided by number of takedowns attempted"""

    time_in_control: OptionalNullable[float] = Field(default=UNSET, alias="TimeInControl")
    """Number of seconds fighter deemed in control by officials"""

    first_round_win: OptionalNullable[bool] = Field(default=UNSET, alias="FirstRoundWin")
    """Indicates if this fighter won the fight in the first round"""

    second_round_win: OptionalNullable[bool] = Field(default=UNSET, alias="SecondRoundWin")
    """Indicates if this fighter won the fight in the second round"""

    third_round_win: OptionalNullable[bool] = Field(default=UNSET, alias="ThirdRoundWin")
    """Indicates if this fighter won the fight in the third round"""

    fourth_round_win: OptionalNullable[bool] = Field(default=UNSET, alias="FourthRoundWin")
    """Indicates if this fighter won the fight in the fourth round"""

    fifth_round_win: OptionalNullable[bool] = Field(default=UNSET, alias="FifthRoundWin")
    """Indicates if this fighter won the fight in the fifth round"""

    decision_win: OptionalNullable[bool] = Field(default=UNSET, alias="DecisionWin")
    """Indicates if this fighter won the fight by decision"""


class FightStatDict(TypedDict):
    fighter_id: NotRequired[int | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    winner: NotRequired[bool | None]
    fantasy_points: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    knockdowns: NotRequired[float | None]
    total_strikes_attempted: NotRequired[float | None]
    total_strikes_landed: NotRequired[float | None]
    sig_strikes_attempted: NotRequired[float | None]
    sig_strikes_landed: NotRequired[float | None]
    takedowns_attempted: NotRequired[float | None]
    takedowns_landed: NotRequired[float | None]
    takedowns_slams: NotRequired[float | None]
    takedown_accuracy: NotRequired[float | None]
    advances: NotRequired[float | None]
    reversals: NotRequired[float | None]
    submissions: NotRequired[float | None]
    slam_rate: NotRequired[float | None]
    time_in_control: NotRequired[float | None]
    first_round_win: NotRequired[bool | None]
    second_round_win: NotRequired[bool | None]
    third_round_win: NotRequired[bool | None]
    fourth_round_win: NotRequired[bool | None]
    fifth_round_win: NotRequired[bool | None]
    decision_win: NotRequired[bool | None]
