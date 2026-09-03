from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .sportsbook import Sportsbook, SportsbookDict


class BettingOutcome1(SdkBaseModel):
    betting_outcome_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeID")
    """The unique ID associated with this specific outcome"""

    betting_market_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID of the betting market"""

    sports_book: Optional[Sportsbook] = Field(default=UNSET, alias="SportsBook")
    """The sportsbook offering this outcome for betting"""

    betting_outcome_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeTypeID")
    """The ID associated with the betting outcome type"""

    betting_outcome_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingOutcomeType")
    """The name of the betting outcome within a betting market (e.g. Home; Away; Under; Over)"""

    payout_american: OptionalNullable[int] = Field(default=UNSET, alias="PayoutAmerican")
    """The american odds payout"""

    payout_decimal: OptionalNullable[float] = Field(default=UNSET, alias="PayoutDecimal")
    """The decimal odds payout"""

    value: OptionalNullable[float] = Field(default=UNSET, alias="Value")
    """The number associated with the outcome of a market (e.g. the spread, game total, etc.)"""

    participant: OptionalNullable[str] = Field(default=UNSET, alias="Participant")
    """The name of the participant (typically team or player) associated with the outcome. NOTE: This is provided by the
    sportsbook. In the case of Player odds, we highly recommend using PlayerID as names of players can be inconsistent
    between sportsbooks."""

    is_available: OptionalNullable[bool] = Field(default=UNSET, alias="IsAvailable")
    """Indicates if this outcome is available for betting as of the last update"""

    is_alternate: OptionalNullable[bool] = Field(default=UNSET, alias="IsAlternate")
    """Indicates if this is an alternate value or the core value"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The created date of the outcome (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the betting outcome was last updated (US Eastern Time)"""

    unlisted: OptionalNullable[str] = Field(default=UNSET, alias="Unlisted")
    """The timestamp of when the outcome was no longer available for betting"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team associated with betting outcome"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team associated with this outcome (where applicable)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""

    is_in_play: OptionalNullable[bool] = Field(default=UNSET, alias="IsInPlay")
    """Was this outcome created after the start time of the game (only applies when the betting event is of type
    game)"""


class BettingOutcome1Dict(TypedDict):
    betting_outcome_id: NotRequired[int | None]
    betting_market_id: NotRequired[int | None]
    sports_book: NotRequired[Sportsbook | SportsbookDict]
    betting_outcome_type_id: NotRequired[int | None]
    betting_outcome_type: NotRequired[str | None]
    payout_american: NotRequired[int | None]
    payout_decimal: NotRequired[float | None]
    value: NotRequired[float | None]
    participant: NotRequired[str | None]
    is_available: NotRequired[bool | None]
    is_alternate: NotRequired[bool | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    unlisted: NotRequired[str | None]
    team_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    sportsbook_url: NotRequired[str | None]
    is_in_play: NotRequired[bool | None]
