from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Transaction(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their MLB career."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    former_team_id: OptionalNullable[int] = Field(default=UNSET, alias="FormerTeamID")
    """TeamID of player's former team"""

    former_team: OptionalNullable[str] = Field(default=UNSET, alias="FormerTeam")
    """Player's former team in abbreviated format [Key] (e.g. SD; PHI; LAD; ATL etc.)"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """Type of Transaction. Released, Waived, Signed, Promoted, Elevated, Demoted, and Traded."""

    date: OptionalNullable[str] = Field(default=UNSET, alias="Date")
    """The date that this transaction took place"""

    note: OptionalNullable[str] = Field(default=UNSET, alias="Note")
    """A summary of the transaction (e.g. "Harris has signed with the Diamondbacks.")"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time this transaction was created in US Eastern Time"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time of the last update made to this transaction (in US Eastern Time)"""


class TransactionDict(TypedDict):
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    former_team_id: NotRequired[int | None]
    former_team: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    type_: NotRequired[str | None]
    date: NotRequired[str | None]
    note: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
