from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Standing(SdkBaseModel):
    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this game corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)."""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season for which these totals apply"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The conference of the team (e.g. AFC or NFC)"""

    division: OptionalNullable[str] = Field(default=UNSET, alias="Division")
    """The division of the team (e.g. East; North; South; West)"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the team"""

    wins: Optional[int] = Field(default=UNSET, alias="Wins")
    """Total number of wins by the team in the season"""

    losses: Optional[int] = Field(default=UNSET, alias="Losses")
    """Regular season losses by the team"""

    ties: Optional[int] = Field(default=UNSET, alias="Ties")
    """Total ties by the team"""

    percentage: Optional[float] = Field(default=UNSET, alias="Percentage")
    """The winning percentage of the team in the season"""

    points_for: Optional[int] = Field(default=UNSET, alias="PointsFor")
    """Total points scored by the team in the season"""

    points_against: Optional[int] = Field(default=UNSET, alias="PointsAgainst")
    """Total points allowed by the team during the season"""

    net_points: Optional[int] = Field(default=UNSET, alias="NetPoints")
    """Difference between PointsFor and PointsAgainst for the team"""

    touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="Touchdowns")
    """Total touchdowns scored by the team"""

    division_wins: Optional[int] = Field(default=UNSET, alias="DivisionWins")
    """Regular season wins within the division by the team"""

    division_losses: Optional[int] = Field(default=UNSET, alias="DivisionLosses")
    """Regular season losses within the division by the team"""

    conference_wins: Optional[int] = Field(default=UNSET, alias="ConferenceWins")
    """Regular season wins within the conference by the team"""

    conference_losses: Optional[int] = Field(default=UNSET, alias="ConferenceLosses")
    """Regular season losses within the conference by the team"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    division_ties: Optional[int] = Field(default=UNSET, alias="DivisionTies")
    """Regular season ties within the division by the team"""

    conference_ties: Optional[int] = Field(default=UNSET, alias="ConferenceTies")
    """Regular season ties within the conference by the team"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    division_rank: Optional[int] = Field(default=UNSET, alias="DivisionRank")
    """Team's rank within the division"""

    conference_rank: Optional[int] = Field(default=UNSET, alias="ConferenceRank")
    """Team's rank within the conference"""

    home_wins: OptionalNullable[int] = Field(default=UNSET, alias="HomeWins")
    """Home wins for the team"""

    home_losses: OptionalNullable[int] = Field(default=UNSET, alias="HomeLosses")
    """Home losses for the team"""

    home_ties: OptionalNullable[int] = Field(default=UNSET, alias="HomeTies")
    """Home ties for the team"""

    away_wins: OptionalNullable[int] = Field(default=UNSET, alias="AwayWins")
    """Away wins for the team"""

    away_losses: OptionalNullable[int] = Field(default=UNSET, alias="AwayLosses")
    """Away losses for the team"""

    away_ties: OptionalNullable[int] = Field(default=UNSET, alias="AwayTies")
    """Away ties for the team"""

    streak: OptionalNullable[int] = Field(default=UNSET, alias="Streak")
    """The current winning or losing streak for this team (negative numbers represent losing streaks)."""

    clinched_division: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedDivision")
    """Returns TRUE if team has clinched their division; FALSE if not"""

    clinched_wild_card: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedWildCard")
    """Returns TRUE if team has clinched a Wild Card spot; FALSE if not"""

    clinched_bye: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedBye")
    """Returns TRUE if team has clinched a first-round bye in the playoffs; FALSE if not"""

    eliminated_from_playoff_contention: OptionalNullable[bool] = Field(
        default=UNSET, alias="EliminatedFromPlayoffContention"
    )
    """Returns TRUE if team has been eliminated from playoff contention; FALSE if not"""


class StandingDict(TypedDict):
    season_type: NotRequired[int]
    season: NotRequired[int]
    conference: NotRequired[str | None]
    division: NotRequired[str | None]
    team: NotRequired[str | None]
    name: NotRequired[str | None]
    wins: NotRequired[int]
    losses: NotRequired[int]
    ties: NotRequired[int]
    percentage: NotRequired[float]
    points_for: NotRequired[int]
    points_against: NotRequired[int]
    net_points: NotRequired[int]
    touchdowns: NotRequired[int | None]
    division_wins: NotRequired[int]
    division_losses: NotRequired[int]
    conference_wins: NotRequired[int]
    conference_losses: NotRequired[int]
    team_id: NotRequired[int]
    division_ties: NotRequired[int]
    conference_ties: NotRequired[int]
    global_team_id: NotRequired[int | None]
    division_rank: NotRequired[int]
    conference_rank: NotRequired[int]
    home_wins: NotRequired[int | None]
    home_losses: NotRequired[int | None]
    home_ties: NotRequired[int | None]
    away_wins: NotRequired[int | None]
    away_losses: NotRequired[int | None]
    away_ties: NotRequired[int | None]
    streak: NotRequired[int | None]
    clinched_division: NotRequired[bool | None]
    clinched_wild_card: NotRequired[bool | None]
    clinched_bye: NotRequired[bool | None]
    eliminated_from_playoff_contention: NotRequired[bool | None]
