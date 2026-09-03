from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerTournamentOdd(SdkBaseModel):
    player_tournament_odd_id: Optional[int] = Field(default=UNSET, alias="PlayerTournamentOddId")
    """The unique ID of this player/tournament odd record"""

    sportsbook_id: Optional[int] = Field(default=UNSET, alias="SportsbookId")
    """The Id of the Sportsbook associated with this record."""

    sportbook_name: OptionalNullable[str] = Field(default=UNSET, alias="SportbookName")
    """The name of the sportsbook"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the golfer"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerId")
    """The unique ID of the golfer associated with this record"""

    odds_to_win: Optional[int] = Field(default=UNSET, alias="OddsToWin")
    """The odds for this record; in American format (i.e. +800; -200; etc.)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when this odds record was created"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time when this record was updated."""

    is_available: Optional[bool] = Field(default=UNSET, alias="IsAvailable")
    """Indicates whether the odd is available for wagering at the related sportsbook (excludes Consensus)"""

    odd_type: OptionalNullable[str] = Field(default=UNSET, alias="OddType")
    """The market type of the odd (e.g. live; pregame; Round 1; Thru Round 4)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""


class PlayerTournamentOddDict(TypedDict):
    player_tournament_odd_id: NotRequired[int]
    sportsbook_id: NotRequired[int]
    sportbook_name: NotRequired[str | None]
    name: NotRequired[str | None]
    player_id: NotRequired[int]
    odds_to_win: NotRequired[int]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    is_available: NotRequired[bool]
    odd_type: NotRequired[str | None]
    sportsbook_url: NotRequired[str | None]
