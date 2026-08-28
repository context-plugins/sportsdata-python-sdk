from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Quarter1(SdkBaseModel):
    quarter_id: Optional[int] = Field(default=UNSET, alias="QuarterID")
    """The unique ID of the quarter"""

    score_id: Optional[int] = Field(default=UNSET, alias="ScoreID")
    """The unique ID of the score this quarter belongs to"""

    number: Optional[int] = Field(default=UNSET, alias="Number")
    """The Number (Order) of the Quarter in the scope of the Game."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The Name of the Quarter (possible values: 1, 2, 3, 4, OT, OT2, OT3, etc)"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The long description of the quarter"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """The total points scored by the away team in this Quarter."""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """The total points scored by the home team in this Quarter."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The database generated timestamp of when this Quarter was last updated (in US Eastern time)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The database generated timestamp of when this Quarter was first created (in US Eastern Time)"""


class Quarter1Dict(TypedDict):
    quarter_id: NotRequired[int]
    score_id: NotRequired[int]
    number: NotRequired[int]
    name: NotRequired[str | None]
    description: NotRequired[str | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
