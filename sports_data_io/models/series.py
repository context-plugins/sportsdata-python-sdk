from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Series(SdkBaseModel):
    """Contains relevant series data for postseason series only - HomeTeamWins; AwayTeamWins; GameNumber; and MaxLength,
    Contains relevant series data for playoff series only - HomeTeamWins, AwayTeamWins, GameNumber, and MaxLength,
    Contains relevant series data for playoff series only - HomeTeamWins, AwayTeamWins, GameNumber, and MaxLength"""

    home_team_wins: Optional[int] = Field(default=UNSET, alias="HomeTeamWins")
    """Total number of wins by the home team in the series"""

    away_team_wins: Optional[int] = Field(default=UNSET, alias="AwayTeamWins")
    """Total wins in the series by the away team"""

    game_number: Optional[int] = Field(default=UNSET, alias="GameNumber")
    """The game number in the series"""

    max_length: Optional[int] = Field(default=UNSET, alias="MaxLength")
    """The maximum number of games that can be played in a series"""


class SeriesDict(TypedDict):
    home_team_wins: NotRequired[int]
    away_team_wins: NotRequired[int]
    game_number: NotRequired[int]
    max_length: NotRequired[int]
