from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Player2(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the golfer"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the golfer"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of the golfer"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The golfer's weight (in pounds)"""

    swings: OptionalNullable[str] = Field(default=UNSET, alias="Swings")
    """Indicates whether this golfer swings right-handed (R) or left-handed (L)"""

    pga_debut: OptionalNullable[int] = Field(default=UNSET, alias="PgaDebut")
    """The year that this golfer made his PGA debut"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The country where this golfer is from"""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The golfer's date of birth"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city where this golfer was born"""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The state where this golfer was born. Note: This field is null for any golfer born outside the US, Canada, and
    Australia"""

    college: OptionalNullable[str] = Field(default=UNSET, alias="College")
    """The college that this golfer attended (if applicable)"""

    photo_url: OptionalNullable[str] = Field(default=UNSET, alias="PhotoUrl")
    """This field is deprecated"""

    sport_radar_player_id: OptionalNullable[str] = Field(default=UNSET, alias="SportRadarPlayerID")
    """The unique ID of this golfer in the SportRadar API"""

    pga_tour_player_id: OptionalNullable[int] = Field(default=UNSET, alias="PgaTourPlayerID")
    """The unique ID of the golfer from PGATour(dot)Com"""

    rotoworld_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoworldPlayerID")
    """The unique ID of this golfer on Rotoworld"""

    roto_wire_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoWirePlayerID")
    """The unique ID of this golfer on RotoWire"""

    fantasy_alarm_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyAlarmPlayerID")
    """The golfer's cross reference Player ID to FantasyAlarm"""

    draft_kings_name: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsName")
    """The golfer's full name in DraftKings' daily fantasy sports platform"""

    fantasy_draft_name: OptionalNullable[str] = Field(default=UNSET, alias="FantasyDraftName")
    """The golfer's full name in FantasyDraft's daily fantasy sports platform"""

    fan_duel_name: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelName")
    """The golfer's full name in Fanduel's daily fantasy sports platform"""

    fantasy_draft_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftPlayerID")
    """The golfer's cross reference PlayerID to FantasyDraft"""

    draft_kings_player_id: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsPlayerID")
    """The golfer's cross reference PlayerID to DraftKings"""

    fan_duel_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelPlayerID")
    """The golfer's cross reference PlayerID to FanDuel"""

    yahoo_player_id: OptionalNullable[int] = Field(default=UNSET, alias="YahooPlayerID")
    """The unique ID of this golfer on Yahoo"""


class Player2Dict(TypedDict):
    player_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    weight: NotRequired[int | None]
    swings: NotRequired[str | None]
    pga_debut: NotRequired[int | None]
    country: NotRequired[str | None]
    birth_date: NotRequired[str | None]
    birth_city: NotRequired[str | None]
    birth_state: NotRequired[str | None]
    college: NotRequired[str | None]
    photo_url: NotRequired[str | None]
    sport_radar_player_id: NotRequired[str | None]
    pga_tour_player_id: NotRequired[int | None]
    rotoworld_player_id: NotRequired[int | None]
    roto_wire_player_id: NotRequired[int | None]
    fantasy_alarm_player_id: NotRequired[int | None]
    draft_kings_name: NotRequired[str | None]
    fantasy_draft_name: NotRequired[str | None]
    fan_duel_name: NotRequired[str | None]
    fantasy_draft_player_id: NotRequired[int | None]
    draft_kings_player_id: NotRequired[int | None]
    fan_duel_player_id: NotRequired[int | None]
    yahoo_player_id: NotRequired[int | None]
