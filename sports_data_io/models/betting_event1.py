from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market import BettingMarket, BettingMarketDict


class BettingEvent1(SdkBaseModel):
    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID associated with the betting event"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this betting event"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The NBA season of the BettingEvent"""

    betting_event_type_id: Optional[int] = Field(default=UNSET, alias="BettingEventTypeID")
    """The ID associated with the type of betting event"""

    betting_event_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingEventType")
    """Indicates the type of betting event - Game or Future"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The furthest forward time any sportsbook has an event or market set to start for this betting event"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time when this betting event was created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of the last time this betting event was updated (in US Eastern Time)"""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game associated with this BettingEvent"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """The GlobalGameID of the game tied to this event"""

    game_status: OptionalNullable[str] = Field(default=UNSET, alias="GameStatus")
    """The status of the game in tied to this event"""

    quarter: OptionalNullable[str] = Field(default=UNSET, alias="Quarter")
    """The current quarter in the game tied to this betting event. Possible values include: 1; 2; 3; 4; Half; OT;
    NULL"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team tied to the event"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team tied to the event"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team tied to the event"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of points the away team scored in the game tied to the event (post-game)"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total points scored by the home team in the game (post-game)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """The total amount of points scored in the game by both teams. Updated after the game ends to allow for resulting
    bets"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """Rotation number of away team for this event Note: if the betting event is a future this field will be NULL"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """The rotation number of the home team for this event Note: If betting event is a future this field will be NULL"""

    betting_markets: Optional[list[BettingMarket]] = Field(default=UNSET, alias="BettingMarkets")
    """The list of betting markets for this event"""

    game_start_time: OptionalNullable[str] = Field(default=UNSET, alias="GameStartTime")
    """The date and time that the game started (in US Eastern Time)"""


class BettingEvent1Dict(TypedDict):
    betting_event_id: NotRequired[int]
    name: NotRequired[str | None]
    season: NotRequired[int | None]
    betting_event_type_id: NotRequired[int]
    betting_event_type: NotRequired[str | None]
    start_date: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    game_id: NotRequired[int | None]
    global_game_id: NotRequired[int | None]
    game_status: NotRequired[str | None]
    quarter: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    total_score: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    home_rotation_number: NotRequired[int | None]
    betting_markets: NotRequired[list[BettingMarket | BettingMarketDict]]
    game_start_time: NotRequired[str | None]
