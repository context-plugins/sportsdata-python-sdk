from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TeamGameTrends(SdkBaseModel):
    scope: OptionalNullable[str] = Field(default=UNSET, alias="Scope")
    """The range in which the trend shows data for (e.g. Last 5 games; Last 10 games; Last 5 home games; etc.)"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentID")
    """The unique ID of the opponent team"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team"""

    wins: Optional[int] = Field(default=UNSET, alias="Wins")
    """The total number of wins by the team relating to the scope (conference & non-conference)"""

    losses: Optional[int] = Field(default=UNSET, alias="Losses")
    """The total number of losses by the team relating to the scope (conference & non-conference)"""

    ties: Optional[int] = Field(default=UNSET, alias="Ties")
    """The total number of ties by the team relating to the scope (conference & non-conference)"""

    wins_against_the_spread: OptionalNullable[int] = Field(default=UNSET, alias="WinsAgainstTheSpread")
    """How many games the given team has covered the spread in relating to the scope of the search"""

    losses_against_the_spread: OptionalNullable[int] = Field(default=UNSET, alias="LossesAgainstTheSpread")
    """The total number of losses against the point spread by the team relating to the scope (conference &
    non-conference"""

    pushes_against_the_spread: OptionalNullable[int] = Field(default=UNSET, alias="PushesAgainstTheSpread")
    """The amount of times a given team's final score of their game has pushed the point spread (a push is neither a win
    nor a loss)"""

    overs: OptionalNullable[int] = Field(default=UNSET, alias="Overs")
    """The amount of times a given team's final score of their game has gone over the point total (Over/Under) relating
    to the scope"""

    unders: OptionalNullable[int] = Field(default=UNSET, alias="Unders")
    """Amount of times the total score goes under the OverUnder"""

    over_under_pushes: OptionalNullable[int] = Field(default=UNSET, alias="OverUnderPushes")
    """The amount of times a given team's final score of their game has pushed the total points line (a push is neither
    a win nor a loss)"""

    average_score: OptionalNullable[float] = Field(default=UNSET, alias="AverageScore")
    """The average points per game scored by the given team over a certain scope (Last 3 Games, Last 5 Games, Last 10
    Games, etc.)"""

    average_opponent_score: OptionalNullable[float] = Field(default=UNSET, alias="AverageOpponentScore")
    """The average points per game scored by the opposing teams of a given team over a certain scope (Last 3 Games, Last
    5 Games, Last 10 Games, etc.)"""


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
