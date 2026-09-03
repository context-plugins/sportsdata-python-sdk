from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Booking(SdkBaseModel):
    booking_id: Optional[int] = Field(default=UNSET, alias="BookingId")
    """The unique ID of the booking"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of the game tied to this booking"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of booking. Possible values: Yellow Card, Red Card, Yellow Red Card"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team associated with this booking"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerId")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the player who was booked"""

    game_minute: OptionalNullable[int] = Field(default=UNSET, alias="GameMinute")
    """The minute in the game in which the booking occurred"""

    game_minute_extra: OptionalNullable[int] = Field(default=UNSET, alias="GameMinuteExtra")
    """The extra minute in the game in which the booking occurred"""


class BookingDict(TypedDict):
    booking_id: NotRequired[int]
    game_id: NotRequired[int]
    type_: NotRequired[str | None]
    team_id: NotRequired[int]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    game_minute: NotRequired[int | None]
    game_minute_extra: NotRequired[int | None]
