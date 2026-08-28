from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Standing4(SdkBaseModel):
    standing_id: Optional[int] = Field(default=UNSET, alias="StandingId")
    """The unique ID of the standing"""

    round_id: Optional[int] = Field(default=UNSET, alias="RoundId")
    """The unique ID of the round that this team is associated with"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The team's full name"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The short name of the team"""

    scope: OptionalNullable[str] = Field(default=UNSET, alias="Scope")
    """The scope of the standing (possible values: Total, Away, Home)"""

    order: OptionalNullable[int] = Field(default=UNSET, alias="Order")
    """The order of the teams in the standing (e.g 1; 2; 3; 4; etc.)"""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """Total number of games played by the team in the season"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """Number of wins by the team in the season"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """The number of losses for the team"""

    draws: OptionalNullable[int] = Field(default=UNSET, alias="Draws")
    """Number of draws by the team in the season"""

    goals_scored: OptionalNullable[int] = Field(default=UNSET, alias="GoalsScored")
    """Total number of goals scored by the team in the season"""

    goals_against: OptionalNullable[int] = Field(default=UNSET, alias="GoalsAgainst")
    """Total number of goals against by the team in the season"""

    goals_differential: OptionalNullable[int] = Field(default=UNSET, alias="GoalsDifferential")
    """The goal differential of the team in the season. Note: GoalDifferential = GoalsScored - GoalsAgainst"""

    points: OptionalNullable[int] = Field(default=UNSET, alias="Points")
    """Total points accumulated by the team"""

    group: OptionalNullable[str] = Field(default=UNSET, alias="Group")
    """The name of the group (when applicable)"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""


class Standing4Dict(TypedDict):
    standing_id: NotRequired[int]
    round_id: NotRequired[int]
    team_id: NotRequired[int]
    name: NotRequired[str | None]
    short_name: NotRequired[str | None]
    scope: NotRequired[str | None]
    order: NotRequired[int | None]
    games: NotRequired[int | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    draws: NotRequired[int | None]
    goals_scored: NotRequired[int | None]
    goals_against: NotRequired[int | None]
    goals_differential: NotRequired[int | None]
    points: NotRequired[int | None]
    group: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
