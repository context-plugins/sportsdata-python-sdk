from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerSeason2(SdkBaseModel):
    player_season_id: Optional[int] = Field(default=UNSET, alias="PlayerSeasonID")
    """The unique ID of the golfer season record"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The PGA season for which this record applies"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the golfer"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the golfer"""

    world_golf_rank: OptionalNullable[int] = Field(default=UNSET, alias="WorldGolfRank")
    """The player's latest World Golf Ranking"""

    world_golf_rank_last_week: OptionalNullable[int] = Field(default=UNSET, alias="WorldGolfRankLastWeek")
    """The player's World Golf Ranking from the previous week"""

    events: OptionalNullable[int] = Field(default=UNSET, alias="Events")
    """The total number of tournaments the player competed in during the season"""

    average_points: OptionalNullable[float] = Field(default=UNSET, alias="AveragePoints")
    """The total Average World Golf Ranking points scored on tournaments during this season"""

    total_points: OptionalNullable[float] = Field(default=UNSET, alias="TotalPoints")
    """Total World Golf Ranking points scored on tournaments during this season"""

    points_lost: OptionalNullable[float] = Field(default=UNSET, alias="PointsLost")
    """Total World Golf Ranking points lost after the golfers most recent performance"""

    points_gained: OptionalNullable[float] = Field(default=UNSET, alias="PointsGained")
    """Total World Golf Ranking points gained after the golfers most recent performance"""


class PlayerSeason2Dict(TypedDict):
    player_season_id: NotRequired[int]
    season: NotRequired[int]
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    world_golf_rank: NotRequired[int | None]
    world_golf_rank_last_week: NotRequired[int | None]
    events: NotRequired[int | None]
    average_points: NotRequired[float | None]
    total_points: NotRequired[float | None]
    points_lost: NotRequired[float | None]
    points_gained: NotRequired[float | None]
