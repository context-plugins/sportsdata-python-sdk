from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .player_round_score import PlayerRoundScore, PlayerRoundScoreDict


class TournamentRound(SdkBaseModel):
    tournament_id: Optional[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament"""

    player_tournament_id: Optional[int] = Field(default=UNSET, alias="PlayerTournamentID")
    """The unique ID of this player/tournament combination"""

    total_score: OptionalNullable[float] = Field(default=UNSET, alias="TotalScore")
    """The total score of the golfer for this tournament as compared to par"""

    total_strokes: OptionalNullable[float] = Field(default=UNSET, alias="TotalStrokes")
    """The total strokes this golfer has for this tournament"""

    player_round_score: Optional[list[PlayerRoundScore]] = Field(default=UNSET, alias="PlayerRoundScore")
    """PlayerRoundScore object"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the golfer"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the golfer"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The last name of this golfer"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The golfer's weight (in pounds)"""

    swings: OptionalNullable[str] = Field(default=UNSET, alias="Swings")
    """Indicates whether this golfer swings right-handed (R) or left-handed (L)"""

    pga_debut: OptionalNullable[int] = Field(default=UNSET, alias="PgaDebut")
    """The year that this golfer made his PGA debut"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The country where this golfer is from"""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The golfer's date of birth"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city where this golfer was born"""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The state where this golfer was born. Note: This field is null for any golfer born outside the US, Canada, and
    Australia"""

    college: OptionalNullable[str] = Field(default=UNSET, alias="College")
    """The college that this golfer attended"""


class TournamentRoundDict(TypedDict):
    tournament_id: NotRequired[int]
    player_tournament_id: NotRequired[int]
    total_score: NotRequired[float | None]
    total_strokes: NotRequired[float | None]
    player_round_score: NotRequired[list[PlayerRoundScore | PlayerRoundScoreDict]]
    player_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    weight: NotRequired[int | None]
    swings: NotRequired[str | None]
    pga_debut: NotRequired[int | None]
    country: NotRequired[str | None]
    birth_date: NotRequired[str | None]
    birth_city: NotRequired[str | None]
    birth_state: NotRequired[str | None]
    college: NotRequired[str | None]
