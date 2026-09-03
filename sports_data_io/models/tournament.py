from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game9 import Game9, Game9Dict


class Tournament(SdkBaseModel):
    tournament_id: Optional[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament. Note: this field is specific to March Madness tournament & does not include
    other tournaments"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season that the tournament occurs in. Note: season is a single year that the majority of the season occurs
    in"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the tournament"""

    location: OptionalNullable[str] = Field(default=UNSET, alias="Location")
    """Where the tournament in question is located/being played"""

    games: Optional[list[Game9]] = Field(default=UNSET, alias="Games")
    """Shows a list of games that are held within a tournament for a given season"""

    left_top_bracket_conference: OptionalNullable[str] = Field(default=UNSET, alias="LeftTopBracketConference")
    """The region that is designated to be in the top-left of the NCAA Tournament bracket"""

    left_bottom_bracket_conference: OptionalNullable[str] = Field(default=UNSET, alias="LeftBottomBracketConference")
    """The region that is designated to be in the bottom-left of the NCAA Tournament bracket"""

    right_top_bracket_conference: OptionalNullable[str] = Field(default=UNSET, alias="RightTopBracketConference")
    """The region that is designated to be in the top-right of the NCAA Tournament bracket"""

    right_bottom_bracket_conference: OptionalNullable[str] = Field(default=UNSET, alias="RightBottomBracketConference")
    """The region that is designated to be in the bottom-right of the NCAA Tournament bracket"""


class TournamentDict(TypedDict):
    tournament_id: NotRequired[int]
    season: NotRequired[int]
    name: NotRequired[str | None]
    location: NotRequired[str | None]
    games: NotRequired[list[Game9 | Game9Dict]]
    left_top_bracket_conference: NotRequired[str | None]
    left_bottom_bracket_conference: NotRequired[str | None]
    right_top_bracket_conference: NotRequired[str | None]
    right_bottom_bracket_conference: NotRequired[str | None]
