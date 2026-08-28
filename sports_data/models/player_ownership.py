from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerOwnership(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the ownership info"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's fantasy football position. Possible values: QB; RB; WR; TE; DL; LB; DB; K; P; OL"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that the player is on. Note: If the player is a free agent; this field is NULL"""

    ownership_percentage: OptionalNullable[float] = Field(default=UNSET, alias="OwnershipPercentage")
    """Player's ownership percentage on NFL.com fantasy leagues during this week"""

    delta_ownership_percentage: OptionalNullable[float] = Field(default=UNSET, alias="DeltaOwnershipPercentage")
    """Player's change in ownership percentage on NFL.com fantasy leagues during this week"""

    start_percentage: OptionalNullable[float] = Field(default=UNSET, alias="StartPercentage")
    """Player's starting lineup percentage on NFL.com fantasy leagues during this week"""

    delta_start_percentage: OptionalNullable[float] = Field(default=UNSET, alias="DeltaStartPercentage")
    """Player's change in starting lineup percentage on NFL.com fantasy leagues during this week"""


class PlayerOwnershipDict(TypedDict):
    player_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    week: NotRequired[int]
    name: NotRequired[str | None]
    position: NotRequired[str | None]
    team: NotRequired[str | None]
    team_id: NotRequired[int | None]
    ownership_percentage: NotRequired[float | None]
    delta_ownership_percentage: NotRequired[float | None]
    start_percentage: NotRequired[float | None]
    delta_start_percentage: NotRequired[float | None]
