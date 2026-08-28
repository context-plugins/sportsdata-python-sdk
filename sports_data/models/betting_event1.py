from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market1 import BettingMarket1, BettingMarket1Dict


class BettingEvent1(SdkBaseModel):
    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID associated with the betting event"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this betting event"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The PGA season of this betting event"""

    betting_event_type_id: Optional[int] = Field(default=UNSET, alias="BettingEventTypeID")
    """The ID associated with the type of betting event"""

    betting_event_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingEventType")
    """Indicates the type of betting event. Note: golf does not have the concept of a future type betting event"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The last day for betting on this event"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when this betting event was created"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The last updated date of this betting event"""

    tournament_id: OptionalNullable[int] = Field(default=UNSET, alias="TournamentId")
    """The unique ID of the tournament tied to this event"""

    betting_markets: Optional[list[BettingMarket1]] = Field(default=UNSET, alias="BettingMarkets")
    """A list of the possible betting markets within a betting event"""


class BettingEvent1Dict(TypedDict):
    betting_event_id: NotRequired[int]
    name: NotRequired[str | None]
    season: NotRequired[int | None]
    betting_event_type_id: NotRequired[int]
    betting_event_type: NotRequired[str | None]
    start_date: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    tournament_id: NotRequired[int | None]
    betting_markets: NotRequired[list[BettingMarket1 | BettingMarket1Dict]]
