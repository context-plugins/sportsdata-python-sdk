from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .goaltender1 import Goaltender1, Goaltender1Dict
from .goaltender3 import Goaltender3, Goaltender3Dict


class StartingGoaltenders(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game tied to the StartingGoaltenders"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The end year of season (2021-22 would be 2022)"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 5=AllStar;
    6=Exhibition)."""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game in US Eastern Time"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Final, F/SO, F/OT, Postponed,
    Canceled, NotNecessary"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team tied to these StartingGoaltenders"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team as it relates to the starting goaltenders"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_goaltender: Optional[Goaltender3] = Field(default=UNSET, alias="HomeGoaltender")
    """The information of the home goaltender (PlayerID, TeamID, Team, First & Last Name, Jersey Number, Confirmed)"""

    away_goaltender: Optional[Goaltender1] = Field(default=UNSET, alias="AwayGoaltender")
    """The information of the away goaltender (PlayerID, TeamID, Team, First & Last Name, Jersey Number, Confirmed)"""


class StartingGoaltendersDict(TypedDict):
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
    home_goaltender: NotRequired[Goaltender3Dict]
    away_goaltender: NotRequired[Goaltender1Dict]
