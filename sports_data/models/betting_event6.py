from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market4 import BettingMarket4, BettingMarket4Dict


class BettingEvent6(SdkBaseModel):
    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID assocated with the betting event"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this betting event"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The soccer regular season for which these totals apply"""

    betting_event_type_id: Optional[int] = Field(default=UNSET, alias="BettingEventTypeID")
    """The ID associated with the type of betting event"""

    betting_event_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingEventType")
    """Indicates the type of betting event - Game or Future"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The last day for betting on this event"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The created date of this betting event (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the betting event record was last updated (US Eastern Time)"""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game tied to this event"""

    game_status: OptionalNullable[str] = Field(default=UNSET, alias="GameStatus")
    """The status of the game tied to this event"""

    quarter: OptionalNullable[str] = Field(default=UNSET, alias="Quarter")
    """The quarter of the game tied to this event"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team tied to this event"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team tied to this event"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team tied to this event"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team tied to this event"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team tied to this event"""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team tied to this event"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """The away team score of the game tied to this event (updated after game ends to allow for resolving bets)"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """The home team score of the game tied to this event (updated after game ends to allow for resolving bets)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """The total combined score of both teams in the game (updated after game ends to allow for resolving bets)"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """The away team rotation number of the game tied to this event"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """The home team rotation number of the game tied to this event"""

    betting_markets: Optional[list[BettingMarket4]] = Field(default=UNSET, alias="BettingMarkets")
    """The list of betting markets for this event"""

    competition_id: OptionalNullable[int] = Field(default=UNSET, alias="CompetitionId")
    """The Id of the competition related to this betting event"""


class BettingEvent6Dict(TypedDict):
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
    betting_markets: NotRequired[list[BettingMarket4 | BettingMarket4Dict]]
    competition_id: NotRequired[int | None]
