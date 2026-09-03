from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Transaction(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO tied to this transaction. Note: this ID will stay
    with the player throughout their entire career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    former_team_id: OptionalNullable[int] = Field(default=UNSET, alias="FormerTeamID")
    """ID of Player's former team"""

    former_team: OptionalNullable[str] = Field(default=UNSET, alias="FormerTeam")
    """Player's former team abbreviation [Key] (e.g. LAC; PHI; NE; IND etc.)"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """Type of Transaction. Released, Waived, Signed, Promoted, Elevated, Demoted, and Traded."""

    date: OptionalNullable[str] = Field(default=UNSET, alias="Date")
    """Date & time that the transaction took place (in US Eastern Time)"""

    note: OptionalNullable[str] = Field(default=UNSET, alias="Note")
    """Transaction Summary (e.g. "Harris has signed with the Commanders.")"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """Date and time of the transaction creation (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """Date and time last updated (in US Eastern Time)"""


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
