from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game9 import Game9, Game9Dict
from .player_season7 import PlayerSeason7, PlayerSeason7Dict
from .standing4 import Standing4, Standing4Dict
from .team_season6 import TeamSeason6, TeamSeason6Dict


class Round1(SdkBaseModel):
    round_id: Optional[int] = Field(default=UNSET, alias="RoundId")
    """The unique ID of the round"""

    season_id: Optional[int] = Field(default=UNSET, alias="SeasonId")
    """The unique ID of the season this round is associated with"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The soccer regular season for which these totals apply"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The display name of the round (examples: Regular Season, Semi-finals, Final, etc)"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of this round. Possible values: Cup; Table"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date of the round"""

    end_date: OptionalNullable[str] = Field(default=UNSET, alias="EndDate")
    """The end date of the round"""

    current_week: OptionalNullable[int] = Field(default=UNSET, alias="CurrentWeek")
    """The current week that this round is in"""

    current_round: Optional[bool] = Field(default=UNSET, alias="CurrentRound")
    """Indicates whether or not this round is the current round of the competition/season"""

    games: Optional[list[Game9]] = Field(default=UNSET, alias="Games")
    """The games and their details that are apart of this round"""

    standings: Optional[list[Standing4]] = Field(default=UNSET, alias="Standings")
    """The standings details associated with this round of the competition"""

    team_seasons: Optional[list[TeamSeason6]] = Field(default=UNSET, alias="TeamSeasons")
    """The team stat records associated with this round"""

    player_seasons: Optional[list[PlayerSeason7]] = Field(default=UNSET, alias="PlayerSeasons")
    """Player Season stat records associated with this round"""


class Round1Dict(TypedDict):
    round_id: NotRequired[int]
    season_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    name: NotRequired[str | None]
    type_: NotRequired[str | None]
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
    current_week: NotRequired[int | None]
    current_round: NotRequired[bool]
    games: NotRequired[list[Game9 | Game9Dict]]
    standings: NotRequired[list[Standing4 | Standing4Dict]]
    team_seasons: NotRequired[list[TeamSeason6 | TeamSeason6Dict]]
    player_seasons: NotRequired[list[PlayerSeason7 | PlayerSeason7Dict]]
