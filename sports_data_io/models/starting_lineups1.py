from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .lineup1 import Lineup1, Lineup1Dict
from .lineup2 import Lineup2, Lineup2Dict
from .lineup3 import Lineup3, Lineup3Dict


class StartingLineups1(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game tied to the StartingLineups"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The MLB season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar)"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game in US Eastern Time"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled; InProgress; Final; Suspended; Delayed;
    Postponed; Canceled; Forfeit; NotNecessary"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team tied to these StartingLineups"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the Home Team"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique TeamID of the away team"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_starting_pitcher: Optional[Lineup3] = Field(default=UNSET, alias="HomeStartingPitcher")
    """Home team starting pitcher. Note: this is a probable pitcher until confirmed field = TRUE."""

    home_batting_lineup: Optional[list[Lineup1]] = Field(default=UNSET, alias="HomeBattingLineup")
    """The batting lineup of the home team"""

    away_starting_pitcher: Optional[Lineup2] = Field(default=UNSET, alias="AwayStartingPitcher")
    """Away team starting pitcher. Note: this is a probable pitcher until confirmed field = TRUE."""

    away_batting_lineup: Optional[list[Lineup1]] = Field(default=UNSET, alias="AwayBattingLineup")
    """Away team batting lineup for the game"""

    home_team_opener: OptionalNullable[bool] = Field(default=UNSET, alias="HomeTeamOpener")
    """Indicates whether the home team will use an Opener as the starting pitcher. NOTE: An opener is a pitcher
    (typically a relief pitcher) that is only scheduled to pitch the first 1-3 innings of the game."""

    away_team_opener: OptionalNullable[bool] = Field(default=UNSET, alias="AwayTeamOpener")
    """Indicates whether the away team will use an Opener as the starting pitcher. NOTE: An opener is a pitcher
    (typically a relief pitcher) that is only scheduled to pitch the first 1-3 innings of the game."""


class StartingLineups1Dict(TypedDict):
    game_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    status: NotRequired[str | None]
    home_team_id: NotRequired[int | None]
    home_team: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    away_team: NotRequired[str | None]
    home_starting_pitcher: NotRequired[Lineup3 | Lineup3Dict]
    home_batting_lineup: NotRequired[list[Lineup1 | Lineup1Dict]]
    away_starting_pitcher: NotRequired[Lineup2 | Lineup2Dict]
    away_batting_lineup: NotRequired[list[Lineup1 | Lineup1Dict]]
    home_team_opener: NotRequired[bool | None]
    away_team_opener: NotRequired[bool | None]
