from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayoffAggregateScore(SdkBaseModel):
    team_a_id: Optional[int] = Field(default=UNSET, alias="TeamA_Id")
    """The TeamID of Team A. Note: Team A is determined by the home team in the first leg, and remains set through the
    life of the record"""

    team_a_aggregate_score: Optional[int] = Field(default=UNSET, alias="TeamA_AggregateScore")
    """The score, on aggregate, of Team A in the matchup. Note: Team A is determined by the home team in the first leg,
    and remains set through the life of the record"""

    team_b_id: Optional[int] = Field(default=UNSET, alias="TeamB_Id")
    """The TeamID of Team B. Note: Team B is determined by the away team in the first leg, and remains set through the
    life of the record"""

    team_b_aggregate_score: Optional[int] = Field(default=UNSET, alias="TeamB_AggregateScore")
    """The score, on aggregate, of Team B in the matchup. Note: Team B is determined by the away team in the first leg,
    and remains set through the life of the record"""

    winning_team_id: Optional[int] = Field(default=UNSET, alias="WinningTeamId")
    """The ID of the team that wins the home-and-home matchup"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """Date and time the record was created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (in US Eastern Time)"""


class PlayoffAggregateScoreDict(TypedDict):
    team_a_id: NotRequired[int]
    team_a_aggregate_score: NotRequired[int]
    team_b_id: NotRequired[int]
    team_b_aggregate_score: NotRequired[int]
    winning_team_id: NotRequired[int]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
