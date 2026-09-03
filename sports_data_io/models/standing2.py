from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Standing2(SdkBaseModel):
    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The MLB season for which these totals apply"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """Abbreviation of the team (e.g. LAD; PHI; BOS; CHC; etc.)"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city/location of the team (e.g. Los Angeles; Philadelphia; Boston; Chicago; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Team's full name (city and mascot)"""

    league: OptionalNullable[str] = Field(default=UNSET, alias="League")
    """The league of the team (possible values: AL; NL)"""

    division: OptionalNullable[str] = Field(default=UNSET, alias="Division")
    """The division of the team (e.g. East, Central, West)"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """The total number of wins by a team in the season"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """Total number of losses by the team in the season"""

    percentage: OptionalNullable[float] = Field(default=UNSET, alias="Percentage")
    """Winning percentage of a team"""

    division_wins: OptionalNullable[int] = Field(default=UNSET, alias="DivisionWins")
    """Total number of division wins in the season"""

    division_losses: OptionalNullable[int] = Field(default=UNSET, alias="DivisionLosses")
    """Total number of division losses in a season"""

    games_behind: OptionalNullable[float] = Field(default=UNSET, alias="GamesBehind")
    """Number of games behind the first place team"""

    last_ten_games_wins: OptionalNullable[int] = Field(default=UNSET, alias="LastTenGamesWins")
    """Total number of wins in the last ten games"""

    last_ten_games_losses: OptionalNullable[int] = Field(default=UNSET, alias="LastTenGamesLosses")
    """Total number of losses in the last ten games"""

    streak: OptionalNullable[str] = Field(default=UNSET, alias="Streak")
    """Current streak the team is on (e.g. Win 3, Lost 3)"""

    league_rank: OptionalNullable[int] = Field(default=UNSET, alias="LeagueRank")
    """The ranking in the league"""

    division_rank: OptionalNullable[int] = Field(default=UNSET, alias="DivisionRank")
    """The ranking in the division (e.g. 1, 2, 3, 4, 5)"""

    wild_card_rank: OptionalNullable[int] = Field(default=UNSET, alias="WildCardRank")
    """The rank of the team in terms of Wild Card standings only"""

    wild_card_games_behind: OptionalNullable[float] = Field(default=UNSET, alias="WildCardGamesBehind")
    """The number of games behind a team is of the final Wild Card spot"""

    home_wins: OptionalNullable[int] = Field(default=UNSET, alias="HomeWins")
    """Total number of home wins in the season"""

    home_losses: OptionalNullable[int] = Field(default=UNSET, alias="HomeLosses")
    """Total number of home losses in the season"""

    away_wins: OptionalNullable[int] = Field(default=UNSET, alias="AwayWins")
    """Total number of away wins in the season"""

    away_losses: OptionalNullable[int] = Field(default=UNSET, alias="AwayLosses")
    """Total number of away losses in the season"""

    day_wins: OptionalNullable[int] = Field(default=UNSET, alias="DayWins")
    """Total number of wins in daytime games"""

    day_losses: OptionalNullable[int] = Field(default=UNSET, alias="DayLosses")
    """Total number of losses in daytime games"""

    night_wins: OptionalNullable[int] = Field(default=UNSET, alias="NightWins")
    """Total number of wins in nighttime games"""

    night_losses: OptionalNullable[int] = Field(default=UNSET, alias="NightLosses")
    """Total number of losses in nighttime games"""

    runs_scored: OptionalNullable[int] = Field(default=UNSET, alias="RunsScored")
    """Total runs scored by the team in the season"""

    runs_against: OptionalNullable[int] = Field(default=UNSET, alias="RunsAgainst")
    """Total number of runs scored by the opponents of a specified team"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    clinched_best_league_record: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedBestLeagueRecord")
    """Returns TRUE if team has clinched the best record in their respective league; FALSE if not"""

    clinched_wild_card: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedWildCard")
    """Returns TRUE if team has clinched Wild Card spot; FALSE if not"""

    clinched_division: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedDivision")
    """Returns TRUE if team has clinched their division; FALSE if not"""

    eliminated_from_playoff_contention: OptionalNullable[bool] = Field(
        default=UNSET, alias="EliminatedFromPlayoffContention"
    )
    """Returns TRUE if team has been eliminated from playoff contention; FALSE if not"""


class Standing2Dict(TypedDict):
    season: NotRequired[int]
    season_type: NotRequired[int]
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    city: NotRequired[str | None]
    name: NotRequired[str | None]
    league: NotRequired[str | None]
    division: NotRequired[str | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    percentage: NotRequired[float | None]
    division_wins: NotRequired[int | None]
    division_losses: NotRequired[int | None]
    games_behind: NotRequired[float | None]
    last_ten_games_wins: NotRequired[int | None]
    last_ten_games_losses: NotRequired[int | None]
    streak: NotRequired[str | None]
    league_rank: NotRequired[int | None]
    division_rank: NotRequired[int | None]
    wild_card_rank: NotRequired[int | None]
    wild_card_games_behind: NotRequired[float | None]
    home_wins: NotRequired[int | None]
    home_losses: NotRequired[int | None]
    away_wins: NotRequired[int | None]
    away_losses: NotRequired[int | None]
    day_wins: NotRequired[int | None]
    day_losses: NotRequired[int | None]
    night_wins: NotRequired[int | None]
    night_losses: NotRequired[int | None]
    runs_scored: NotRequired[int | None]
    runs_against: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    clinched_best_league_record: NotRequired[bool | None]
    clinched_wild_card: NotRequired[bool | None]
    clinched_division: NotRequired[bool | None]
    eliminated_from_playoff_contention: NotRequired[bool | None]
