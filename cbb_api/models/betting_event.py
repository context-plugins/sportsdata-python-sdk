from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market import BettingMarket, BettingMarketDict


class BettingEvent(SdkBaseModel):
    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID associated with the betting event"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this betting event"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The season that this betting event occurs in. Note: season is a single year that the majority of the season
    occurs in"""

    betting_event_type_id: Optional[int] = Field(default=UNSET, alias="BettingEventTypeID")
    """The ID associated with the type of betting event"""

    betting_event_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingEventType")
    """Indicates the type of betting event (Game or Future)"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The date and time a specified event is scheduled to begin. Note: For Futures, this will be the furthest forward
    time a book has a market set to close"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time when this betting event was created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of the last time this betting event was updated (in US Eastern Time)"""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game tied to this event"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    game_status: OptionalNullable[str] = Field(default=UNSET, alias="GameStatus")
    """The status of the game in tied to this event. A list of CBB game statuses can be found here"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team tied to the event"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team tied to this event"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team tied to the event"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team tied to this event"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team tied to this event This value is guaranteed to be unique across all
    sports/leagues"""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team tied to this event. This value is guaranteed to be unique across all
    sports/leagues"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of points the away team scored in the game tied to the event (post-game)"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total number of points the home team scored in this game (post-game)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """The total amount of points scored in the game by both teams, posted after the conclusion of the game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """Rotation number of away team in the game tied to this event."""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """Rotation number of home team for this game for this event"""

    betting_markets: Optional[list[BettingMarket]] = Field(default=UNSET, alias="BettingMarkets")
    """The list of betting markets for this event"""

    game_start_time: OptionalNullable[str] = Field(default=UNSET, alias="GameStartTime")
    """The date and time that the game started. Note: Time is in US Eastern Time"""


class BettingEventDict(TypedDict):
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
