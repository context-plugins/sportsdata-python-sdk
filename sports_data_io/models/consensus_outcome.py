from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .sportsbook1 import Sportsbook1, Sportsbook1Dict


class ConsensusOutcome(SdkBaseModel):
    number_of_sportsbooks: Optional[int] = Field(default=UNSET, alias="NumberOfSportsbooks")
    """The number of sportsbooks odds that went into creating this consensus outcome"""

    betting_outcome_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeID")
    """The unique ID associated with the betting outcome"""

    betting_market_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingMarketID")
    """The unique ID associated with the betting market"""

    sports_book: Optional[Sportsbook1] = Field(default=UNSET, alias="SportsBook")
    """Name of sportsbook"""

    betting_outcome_type_id: OptionalNullable[int] = Field(default=UNSET, alias="BettingOutcomeTypeID")
    """The unique ID associated with this BettingOutcomeType"""

    betting_outcome_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingOutcomeType")
    """The name of BettingOutcomeType (e.g. Home; Away; Under; Over)"""

    payout_american: OptionalNullable[int] = Field(default=UNSET, alias="PayoutAmerican")
    """The payout of the bet, shown in American odds format"""

    payout_decimal: OptionalNullable[float] = Field(default=UNSET, alias="PayoutDecimal")
    """The payout of the bet, shown in decimal odds format"""

    value: OptionalNullable[float] = Field(default=UNSET, alias="Value")
    """The number associated with the outcome (spread, total, etc)"""

    participant: OptionalNullable[str] = Field(default=UNSET, alias="Participant")
    """This field is sourced from the related sportsbook and is shown as is; consider it as free-text that can take any
    form. If a BettingOutcome has the PlayerId or TeamId field set; you should use the respective Player or Team record
    to perform actions like displaying a player's name. Note: if a BettingMarket has PlayerId or TeamId set; all the
    child BettingOutcomes will have the field set as well"""

    is_available: OptionalNullable[bool] = Field(default=UNSET, alias="IsAvailable")
    """Indicates whether a BettingOutcome is available for betting or not (true/false)"""

    is_alternate: OptionalNullable[bool] = Field(default=UNSET, alias="IsAlternate")
    """Indicates whether this is an alternate value or the core value (true/false)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time when this betting outcome was created in US Eastern Time."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time of the last update made to this betting outcome (in US Eastern Time)"""

    unlisted: OptionalNullable[str] = Field(default=UNSET, alias="Unlisted")
    """The timestamp of when these odds were first made unavailable to be bet on any further (In US Eastern Time)"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO tied this outcome (if applicable)"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO tied to this betting outcome. Note: this ID will
    stay with the player throughout their entire career"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team tied to this outcome. This value is guaranteed to be unique across all
    sports/leagues (where applicable)"""

    sportsbook_url: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookUrl")
    """The URL for sportsbook event"""

    is_in_play: OptionalNullable[bool] = Field(default=UNSET, alias="IsInPlay")
    """Was this outcome created after the start time of the game (only applies when the betting event is of type game;
    true/false)"""

    sportsbook_market_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookMarketID")
    """The market id on the given sportsbook when available for deep links"""

    sportsbook_outcome_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsbookOutcomeID")
    """The outcome id on the given sportsbook when available for deep links"""


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
