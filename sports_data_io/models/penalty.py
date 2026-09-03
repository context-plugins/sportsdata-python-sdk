from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Penalty(SdkBaseModel):
    penalty_id: Optional[int] = Field(default=UNSET, alias="PenaltyID")
    """The unique ID of this penalty"""

    period_id: Optional[int] = Field(default=UNSET, alias="PeriodID")
    """The unique ID of the period during which this penalty occurred"""

    sequence: OptionalNullable[int] = Field(default=UNSET, alias="Sequence")
    """The sequence/order that this penalty happened"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """Number of minutes that have passed in the current period. NOTE: this field name might be misleading as it
    actually represents the game clock minutes which are the number of minutes that have already passed in the
    period."""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """Number of seconds that have passed in the current period. NOTE: this field name might be misleading as it
    actually represents the game clock seconds which are the number of minutes that have already passed in the
    period."""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of the penalty"""

    penalty_minutes: OptionalNullable[int] = Field(default=UNSET, alias="PenaltyMinutes")
    """Total minutes the penalty lasts"""

    penalized_team_id: OptionalNullable[int] = Field(default=UNSET, alias="PenalizedTeamID")
    """The TeamID of the team who committed the penalty"""

    penalized_player_id: OptionalNullable[int] = Field(default=UNSET, alias="PenalizedPlayerID")
    """The PlayerID of the player who committed the penalty"""

    drawn_by_team_id: OptionalNullable[int] = Field(default=UNSET, alias="DrawnByTeamID")
    """The TeamID of the player/team that drew the penalty"""

    drawn_by_player_id: OptionalNullable[int] = Field(default=UNSET, alias="DrawnByPlayerID")
    """The PlayerID of the player who drew the penalty"""

    is_bench_penalty: OptionalNullable[bool] = Field(default=UNSET, alias="IsBenchPenalty")
    """Whether or not the penalty is a bench penalty"""

    bench_penalty_served_by_player_id: OptionalNullable[int] = Field(
        default=UNSET, alias="BenchPenaltyServedByPlayerID"
    )
    """The PlayerID of the player who served the bench penalty"""


class PenaltyDict(TypedDict):
    penalty_id: NotRequired[int]
    period_id: NotRequired[int]
    sequence: NotRequired[int | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    description: NotRequired[str | None]
    penalty_minutes: NotRequired[int | None]
    penalized_team_id: NotRequired[int | None]
    penalized_player_id: NotRequired[int | None]
    drawn_by_team_id: NotRequired[int | None]
    drawn_by_player_id: NotRequired[int | None]
    is_bench_penalty: NotRequired[bool | None]
    bench_penalty_served_by_player_id: NotRequired[int | None]
