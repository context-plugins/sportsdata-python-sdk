from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Standing1(SdkBaseModel):
    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NBA season that these totals apply for"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar; 6=Exhibition)."""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID for the team"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """The key (short team name) of the team"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city/location of the team (e.g. Los Angeles; Philadelphia; Boston; Chicago; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The team's full name"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The conference of the team (can either be Eastern or Western)"""

    division: OptionalNullable[str] = Field(default=UNSET, alias="Division")
    """The division of the team (e.g. Atlantic, Central, Southeast, etc.)"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """Total wins by the team"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """Total losses by the team"""

    percentage: OptionalNullable[float] = Field(default=UNSET, alias="Percentage")
    """The team's winning percentage"""

    conference_wins: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceWins")
    """Total conference wins"""

    conference_losses: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceLosses")
    """Total conference losses"""

    division_wins: OptionalNullable[int] = Field(default=UNSET, alias="DivisionWins")
    """Total number of division wins"""

    division_losses: OptionalNullable[int] = Field(default=UNSET, alias="DivisionLosses")
    """Total number of division losses"""

    home_wins: OptionalNullable[int] = Field(default=UNSET, alias="HomeWins")
    """Total number of home game wins"""

    home_losses: OptionalNullable[int] = Field(default=UNSET, alias="HomeLosses")
    """Total number of home game losses"""

    away_wins: OptionalNullable[int] = Field(default=UNSET, alias="AwayWins")
    """Total number of away game wins"""

    away_losses: OptionalNullable[int] = Field(default=UNSET, alias="AwayLosses")
    """Total number of away game losses"""

    last_ten_wins: OptionalNullable[int] = Field(default=UNSET, alias="LastTenWins")
    """Total wins in the last 10 games"""

    last_ten_losses: OptionalNullable[int] = Field(default=UNSET, alias="LastTenLosses")
    """Total losses in the last 10 games"""

    points_per_game_for: OptionalNullable[float] = Field(default=UNSET, alias="PointsPerGameFor")
    """Average points scored by the team per game"""

    points_per_game_against: OptionalNullable[float] = Field(default=UNSET, alias="PointsPerGameAgainst")
    """Average points scored against the team per game"""

    streak: OptionalNullable[int] = Field(default=UNSET, alias="Streak")
    """Total games that the streak (winning or losing) has lasted"""

    games_back: OptionalNullable[float] = Field(default=UNSET, alias="GamesBack")
    """Total number of games behind the top ranked team for a given team"""

    streak_description: OptionalNullable[str] = Field(default=UNSET, alias="StreakDescription")
    """The winning or losing streak written in the form W5 or L1"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    conference_rank: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceRank")
    """Team rank at the conference level"""

    division_rank: OptionalNullable[int] = Field(default=UNSET, alias="DivisionRank")
    """Team rank at the division level"""

    clinched_division: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedDivision")
    """Returns TRUE if a team has clinched their division; FALSE if not"""

    clinched_playoff_berth: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedPlayoffBerth")
    """Returns TRUE if a team has clinched a playoff spot; FALSE if not"""

    won_play_in_tournament: OptionalNullable[bool] = Field(default=UNSET, alias="WonPlayInTournament")
    """Returns TRUE if a team has clinched a playoff spot through the play-in; FALSE if not"""

    clinched_play_in_tournament_berth: OptionalNullable[bool] = Field(
        default=UNSET, alias="ClinchedPlayInTournamentBerth"
    )
    """Returns TRUE if a team has clinched a spot in the play-in; FALSE if not"""

    eliminated_from_playoff_contention: OptionalNullable[bool] = Field(
        default=UNSET, alias="EliminatedFromPlayoffContention"
    )
    """Returns TRUE if a team has been eliminated from playoff contention; FALSE if not"""

    clinched_conference: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedConference")
    """Returns TRUE if a team has clinched their conference; FALSE if not"""


class Standing1Dict(TypedDict):
    season: NotRequired[int]
    season_type: NotRequired[int]
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    city: NotRequired[str | None]
    name: NotRequired[str | None]
    conference: NotRequired[str | None]
    division: NotRequired[str | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    percentage: NotRequired[float | None]
    conference_wins: NotRequired[int | None]
    conference_losses: NotRequired[int | None]
    division_wins: NotRequired[int | None]
    division_losses: NotRequired[int | None]
    home_wins: NotRequired[int | None]
    home_losses: NotRequired[int | None]
    away_wins: NotRequired[int | None]
    away_losses: NotRequired[int | None]
    last_ten_wins: NotRequired[int | None]
    last_ten_losses: NotRequired[int | None]
    points_per_game_for: NotRequired[float | None]
    points_per_game_against: NotRequired[float | None]
    streak: NotRequired[int | None]
    games_back: NotRequired[float | None]
    streak_description: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    conference_rank: NotRequired[int | None]
    division_rank: NotRequired[int | None]
    clinched_division: NotRequired[bool | None]
    clinched_playoff_berth: NotRequired[bool | None]
    won_play_in_tournament: NotRequired[bool | None]
    clinched_play_in_tournament_berth: NotRequired[bool | None]
    eliminated_from_playoff_contention: NotRequired[bool | None]
    clinched_conference: NotRequired[bool | None]
