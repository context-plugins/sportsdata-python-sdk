from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Series(SdkBaseModel):
    """Contains relevant series data for playoff series only - HomeTeamWins, AwayTeamWins, GameNumber, and MaxLength"""

    home_team_wins: Optional[int] = Field(default=UNSET, alias="HomeTeamWins")
    """Number of wins by the home team on in the series. Note: this is for postseason series only."""

    away_team_wins: Optional[int] = Field(default=UNSET, alias="AwayTeamWins")
    """Number of wins by the away team in the series. Note: This is for postseason series only."""

    game_number: Optional[int] = Field(default=UNSET, alias="GameNumber")
    """Game number in series. Note: this applies to postseason series only."""

    max_length: Optional[int] = Field(default=UNSET, alias="MaxLength")
    """Maximum number of games in the series. Note: this is for postseason series only."""


class SeriesDict(TypedDict):
    home_team_wins: NotRequired[int]
    away_team_wins: NotRequired[int]
    game_number: NotRequired[int]
    max_length: NotRequired[int]
