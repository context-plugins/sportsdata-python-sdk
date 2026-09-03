from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market import BettingMarket, BettingMarketDict


class BettingEvent(SdkBaseModel):
    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID assocated with the betting event"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the betting event"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the betting event"""

    betting_event_type_id: Optional[int] = Field(default=UNSET, alias="BettingEventTypeID")
    """The ID associated with the type of betting event"""

    betting_event_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingEventType")
    """Indicates the type of betting event - Game or Future"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The furthest forward time any book has a market set to close for this betting event"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time when this betting event was created in US Eastern Time"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time of the last update made to this betting event (in US Eastern Time)"""

    score_id: OptionalNullable[int] = Field(default=UNSET, alias="ScoreID")
    """ScoreID has been superseded by GameID and should not be used in any new integrations. Existing integrations can
    be updated to use GameID instead, so that they are consistent with all other sports."""

    global_score_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalScoreID")
    """A globally unique ID for the game tied to this betting event. This value is guaranteed to be unique across all
    sports/leagues"""

    game_status: OptionalNullable[str] = Field(default=UNSET, alias="GameStatus")
    """The status of the game tied to this betting event"""

    quarter: OptionalNullable[str] = Field(default=UNSET, alias="Quarter")
    """The quarter of the game tied to this event"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the Home Team"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique TeamID of the away team tied to this BettingEvent"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique TeamID of the home team tied to this BettingEvent"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team tied to this BettingEvent This value is guaranteed to be unique across all
    sports/leagues"""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team tied to this BettingEvent. This value is guaranteed to be unique across
    all sports/leagues."""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Score of the away team tied to this betting event (updated after game ends to allow for resolving bets)"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Score of the home team tied to this betting event (updated after game ends to allow for resolving bets)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """The total points scored by both teams in the game tied to this event (updated after game ends to allow for
    resulting bets)"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """Rotation number of away team for this game"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """Rotation number of home team for this game"""

    betting_markets: Optional[list[BettingMarket]] = Field(default=UNSET, alias="BettingMarkets")
    """The list of betting markets for this event"""

    game_start_time: OptionalNullable[str] = Field(default=UNSET, alias="GameStartTime")
    """The date and time the game starts"""


class BettingEventDict(TypedDict):
    betting_event_id: NotRequired[int]
    name: NotRequired[str | None]
    season: NotRequired[int | None]
    betting_event_type_id: NotRequired[int]
    betting_event_type: NotRequired[str | None]
    start_date: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    score_id: NotRequired[int | None]
    global_score_id: NotRequired[int | None]
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
