from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FantasyTournament(SdkBaseModel):
    tournament_id: Optional[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the golfer"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The PGA season for which this record applies"""

    tee_time: OptionalNullable[str] = Field(default=UNSET, alias="TeeTime")
    """The time that this golfer tees off for the upcoming round (in US Eastern Time)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the golfer"""

    rank: OptionalNullable[int] = Field(default=UNSET, alias="Rank")
    """The rank of this golfer in the tournament"""

    tournament_status: OptionalNullable[str] = Field(default=UNSET, alias="TournamentStatus")
    """Indicates whether a golfer is not playing in this tournament. Note: If golfer is not playing; this will be out"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Total fantasy points scored by the golfer in the tournament using FanDuel's scoring system"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total fantasy points scored by the golfer in the tournament using Yahoo's scoring system"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time when this record was updated."""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points scored by the golfer in the tournament using the default SportsDataIO scoring system"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total fantasy points scored by the golfer in the tournament using DraftKings' scoring system"""


class FantasyTournamentDict(TypedDict):
    tournament_id: NotRequired[int]
    player_id: NotRequired[int]
    season: NotRequired[int | None]
    tee_time: NotRequired[str | None]
    name: NotRequired[str | None]
    rank: NotRequired[int | None]
    tournament_status: NotRequired[str | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    updated: NotRequired[str | None]
    fantasy_points: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
