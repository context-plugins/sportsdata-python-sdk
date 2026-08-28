from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .sportsbook1 import Sportsbook1, Sportsbook1Dict


class ConsensusOutcome(SdkBaseModel):
    number_of_sportsbooks: Optional[int] = Field(default=UNSET, alias="NumberOfSportsbooks")
    """The number of sportsbooks' odds that went into creating this consensus outcome"""

    betting_outcome_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeID")
    """The unique ID associated with this specific outcome"""

    betting_market_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    sports_book: Optional[Sportsbook1] = Field(default=UNSET, alias="SportsBook")
    """The name of the sportsbook that is offering this outcome for betting"""

    betting_outcome_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeTypeID")
    """The BettingOutcomeTypeID of this outcome"""

    betting_outcome_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingOutcomeType")
    """The name of betting outcome type (e.g. Home; Away; Under; Over)"""

    payout_american: OptionalNullable[int] = Field(default=UNSET, alias="PayoutAmerican")
    """The payout of the bet, shown in American odds format"""

    payout_decimal: OptionalNullable[float] = Field(default=UNSET, alias="PayoutDecimal")
    """The payout of the bet, shown in Decimal odds format"""

    value: OptionalNullable[float] = Field(default=UNSET, alias="Value")
    """The number associated with the outcome of a market (e.g. the spread, game total, etc.)"""

    participant: OptionalNullable[str] = Field(default=UNSET, alias="Participant")
    """The name of the participant (typically a team or player) associated with a given outcome. Note: This is provided
    by the sportsbook. In the case of Player odds; we highly recommend using PlayerID as names of players can be
    inconsistent between sportsbooks"""

    is_available: OptionalNullable[bool] = Field(default=UNSET, alias="IsAvailable")
    """Indicates whether a BettingOutcome is available for betting or not"""

    is_alternate: OptionalNullable[bool] = Field(default=UNSET, alias="IsAlternate")
    """Is this an alternate value or the core value"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time when this betting outcome was created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of the last time this betting outcome was updated (in US Eastern Time)"""

    unlisted: OptionalNullable[str] = Field(default=UNSET, alias="Unlisted")
    """The timestamp of when these odds were first made unavailable to be bet on any further"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team (if applicable)"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO (if applicable). Note: this ID will stay with the player
    throughout their collegiate career"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues (where
    applicable)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""

    is_in_play: OptionalNullable[bool] = Field(default=UNSET, alias="IsInPlay")
    """Was this outcome created after the start time of the game (only applies when the betting event is of type
    game)"""

    sportsbook_market_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookMarketID")
    """The market ID from the given sportsbook when available"""

    sportsbook_outcome_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookOutcomeID")
    """The outcome ID from the given sportsbook when available"""


class ConsensusOutcomeDict(TypedDict):
    number_of_sportsbooks: NotRequired[int]
    betting_outcome_id: NotRequired[int | None]
    betting_market_id: NotRequired[int | None]
    sports_book: NotRequired[Sportsbook1 | Sportsbook1Dict]
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
    sportsbook_market_id: NotRequired[str | None]
    sportsbook_outcome_id: NotRequired[str | None]
