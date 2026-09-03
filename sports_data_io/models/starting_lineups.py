from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .lineup import Lineup, LineupDict


class StartingLineups(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game associated with this lineup"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NBA season of the game that the lineups is associated with"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar; 6=Exhibition)."""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """Date and Time of Game"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled; InProgress; Final; F/OT; Suspended; Postponed;
    Delayed; Canceled; Forfeit; NotNecessary"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """Unique ID of Away Team"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_lineup: Optional[list[Lineup]] = Field(default=UNSET, alias="HomeLineup")
    """The lineup (starters and bench players) of the home team in a given game"""

    away_lineup: Optional[list[Lineup]] = Field(default=UNSET, alias="AwayLineup")
    """The lineup (starters and bench players) of the away team in a given game"""


class StartingLineupsDict(TypedDict):
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
    home_lineup: NotRequired[list[Lineup | LineupDict]]
    away_lineup: NotRequired[list[Lineup | LineupDict]]
