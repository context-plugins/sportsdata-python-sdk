from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ScoringPlay2(SdkBaseModel):
    scoring_play_id: Optional[int] = Field(default=UNSET, alias="ScoringPlayID")
    """The unique ID of the scoring play"""

    period_id: Optional[int] = Field(default=UNSET, alias="PeriodID")
    """The unique ID associated of this period"""

    sequence: OptionalNullable[int] = Field(default=UNSET, alias="Sequence")
    """The sequence/order that this scoring play happened"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """Number of minutes that have passed in the current period. NOTE: this field name might be misleading as it
    actually represents the game clock minutes which are the number of minutes that have already passed in the
    period."""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """Number of seconds that have passed in the current period. NOTE: this field name might be misleading as it
    actually represents the game clock sconds which are the number of minutes that have already passed in the period."""

    scored_by_team_id: OptionalNullable[int] = Field(default=UNSET, alias="ScoredByTeamID")
    """The TeamID of the team that scored the goal"""

    allowed_by_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AllowedByTeamID")
    """The TeamID of the team that allowed the goal"""

    scored_by_player_id: OptionalNullable[int] = Field(default=UNSET, alias="ScoredByPlayerID")
    """The PlayerID of the player who scored the goal"""

    assisted_by_player_id1: OptionalNullable[int] = Field(default=UNSET, alias="AssistedByPlayerID1")
    """The PlayerID of the FIRST player who assisted on the goal"""

    assisted_by_player_id2: OptionalNullable[int] = Field(default=UNSET, alias="AssistedByPlayerID2")
    """The PlayerID of the SECOND player who assisted on the goal"""

    power_play: OptionalNullable[bool] = Field(default=UNSET, alias="PowerPlay")
    """Whether or not the goal was scored on the power play"""

    short_handed: OptionalNullable[bool] = Field(default=UNSET, alias="ShortHanded")
    """Whether the goal was scored shorthanded"""

    empty_net: OptionalNullable[bool] = Field(default=UNSET, alias="EmptyNet")
    """Whether the goal was an empty net goal or not"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """The score of the away team after the conclusion of the scoring play"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """The score of the home team after the conclusion of the scoring play"""


class ScoringPlay2Dict(TypedDict):
    scoring_play_id: NotRequired[int]
    period_id: NotRequired[int]
    sequence: NotRequired[int | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    scored_by_team_id: NotRequired[int | None]
    allowed_by_team_id: NotRequired[int | None]
    scored_by_player_id: NotRequired[int | None]
    assisted_by_player_id1: NotRequired[int | None]
    assisted_by_player_id2: NotRequired[int | None]
    power_play: NotRequired[bool | None]
    short_handed: NotRequired[bool | None]
    empty_net: NotRequired[bool | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
