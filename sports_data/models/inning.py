from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Inning(SdkBaseModel):
    inning_id: Optional[int] = Field(default=UNSET, alias="InningID")
    """The unique ID of this specific inning"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of the game tied to this Inning"""

    inning_number: Optional[int] = Field(default=UNSET, alias="InningNumber")
    """The current inning number of the game"""

    away_team_runs: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamRuns")
    """Number of runs scored by the away team in the specific inning"""

    home_team_runs: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamRuns")
    """Number of runs scored by the home team in the specific inning"""


class InningDict(TypedDict):
    inning_id: NotRequired[int]
    game_id: NotRequired[int]
    inning_number: NotRequired[int]
    away_team_runs: NotRequired[int | None]
    home_team_runs: NotRequired[int | None]
