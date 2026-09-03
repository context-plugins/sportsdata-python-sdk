from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TeamGameTrends(SdkBaseModel):
    scope: OptionalNullable[str] = Field(default=UNSET, alias="Scope")
    """The type of Trend (e.g. Last 5 games, Last 10 games, Last 5 home games, etc.)"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentID")
    """The unique ID of the opponent team"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team"""

    wins: Optional[int] = Field(default=UNSET, alias="Wins")
    """Total number of wins relating to the scope. Examples of scopes include: Last 3 Games, Last 5 Home Games, Last 10
    Games as Favorite, etc."""

    losses: Optional[int] = Field(default=UNSET, alias="Losses")
    """Losses relating to the scope. Examples of scopes include: Last 3 Games, Last 5 Home Games, Last 10 Games as
    Favorite, etc."""

    ties: Optional[int] = Field(default=UNSET, alias="Ties")
    """Total ties by the team relating to the scope. Examples of scopes include: Last 3 Games, Last 5 Home Games, Last
    10 Games as Favorite, etc."""

    wins_against_the_spread: OptionalNullable[int] = Field(default=UNSET, alias="WinsAgainstTheSpread")
    """Total number of wins against the spread relating to the scope. Examples of scopes include: Last 3 Games, Last 5
    Home Games, Last 10 Games as Favorite, etc."""

    losses_against_the_spread: OptionalNullable[int] = Field(default=UNSET, alias="LossesAgainstTheSpread")
    """Losses against the spread relating to the scope. Examples of scopes include: Last 3 Games, Last 5 Home Games,
    Last 10 Games as Favorite, etc."""

    pushes_against_the_spread: OptionalNullable[int] = Field(default=UNSET, alias="PushesAgainstTheSpread")
    """Pushes against the spread relating to the scope. Examples of scopes include: Last 3 Games, Last 5 Home Games,
    Last 10 Games as Favorite, etc."""

    overs: OptionalNullable[int] = Field(default=UNSET, alias="Overs")
    """Amount of times the total score goes over the total points line (over/under)"""

    unders: OptionalNullable[int] = Field(default=UNSET, alias="Unders")
    """Amount of times the total score goes under the total points line (over/under)"""

    over_under_pushes: OptionalNullable[int] = Field(default=UNSET, alias="OverUnderPushes")
    """Amount of times the total score pushes the total point line (over/under)"""

    average_score: OptionalNullable[float] = Field(default=UNSET, alias="AverageScore")
    """Average score of team"""

    average_opponent_score: OptionalNullable[float] = Field(default=UNSET, alias="AverageOpponentScore")
    """Average score of opponent"""


class TeamGameTrendsDict(TypedDict):
    scope: NotRequired[str | None]
    team_id: NotRequired[int]
    team: NotRequired[str | None]
    opponent_id: NotRequired[int | None]
    opponent: NotRequired[str | None]
    wins: NotRequired[int]
    losses: NotRequired[int]
    ties: NotRequired[int]
    wins_against_the_spread: NotRequired[int | None]
    losses_against_the_spread: NotRequired[int | None]
    pushes_against_the_spread: NotRequired[int | None]
    overs: NotRequired[int | None]
    unders: NotRequired[int | None]
    over_under_pushes: NotRequired[int | None]
    average_score: NotRequired[float | None]
    average_opponent_score: NotRequired[float | None]
