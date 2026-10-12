from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .penalty import Penalty, PenaltyDict
from .scoring_play2 import ScoringPlay2, ScoringPlay2Dict


class Period(SdkBaseModel):
    period_id: Optional[int] = Field(default=UNSET, alias="PeriodID")
    """The unique ID associated of this period"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game tied to this period"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the period (possible values: 1; 2; 3; SO; OT; OT2; OT3; OT4; etc)"""

    away_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayScore")
    """Total goals scored by the away team in a given period"""

    home_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeScore")
    """Total goals scored by the home team in the period"""

    scoring_plays: Optional[list[ScoringPlay2]] = Field(default=UNSET, alias="ScoringPlays")
    """The details of the scoring plays that occurred during this period"""

    penalties: Optional[list[Penalty]] = Field(default=UNSET, alias="Penalties")
    """The details of the penalties that occurred during this period"""


class PeriodDict(TypedDict):
    period_id: NotRequired[int]
    game_id: NotRequired[int]
    name: NotRequired[str | None]
    away_score: NotRequired[int | None]
    home_score: NotRequired[int | None]
    scoring_plays: NotRequired[list[ScoringPlay2Dict]]
    penalties: NotRequired[list[PenaltyDict]]
