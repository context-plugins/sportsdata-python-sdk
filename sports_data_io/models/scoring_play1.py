from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ScoringPlay1(SdkBaseModel):
    """The details of the scoring play attached to this play (if any)."""

    game_key: OptionalNullable[str] = Field(default=UNSET, alias="GameKey")
    """A 9 digit unique code identifying the game that this record corresponds to. The GameID is composed of Season;
    SeasonType; Week and HomeTeam. Note: This value will be NULL for bye weeks"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this game corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    scoring_play_id: Optional[int] = Field(default=UNSET, alias="ScoringPlayID")
    """Unique ID of the scoring play"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the game"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key} of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    date: OptionalNullable[str] = Field(default=UNSET, alias="Date")
    """The date and time of the game (in US Eastern Time)"""

    sequence: OptionalNullable[int] = Field(default=UNSET, alias="Sequence")
    """The order in which the scoring play happened"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    quarter: OptionalNullable[str] = Field(default=UNSET, alias="Quarter")
    """The quarter of the scoring play (1; 2; 3; 4; OT)"""

    time_remaining: OptionalNullable[str] = Field(default=UNSET, alias="TimeRemaining")
    """The amount of time remaining in the current quarter when the scoring play occurred (e.g. 11:23; 5:34; NULL if
    game is not in progress or at halftime)"""

    play_description: OptionalNullable[str] = Field(default=UNSET, alias="PlayDescription")
    """The detailed description of the play for display purposes"""

    away_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayScore")
    """The away team's score as a result of the scoring play (includes point after)"""

    home_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeScore")
    """The home team's score as a result of the scoring play (includes point after)"""

    score_id: Optional[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the score/game"""


class ScoringPlay1Dict(TypedDict):
    game_key: NotRequired[str | None]
    season_type: NotRequired[int]
    scoring_play_id: NotRequired[int]
    season: NotRequired[int]
    week: NotRequired[int]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    date: NotRequired[str | None]
    sequence: NotRequired[int | None]
    team: NotRequired[str | None]
    quarter: NotRequired[str | None]
    time_remaining: NotRequired[str | None]
    play_description: NotRequired[str | None]
    away_score: NotRequired[int | None]
    home_score: NotRequired[int | None]
    score_id: NotRequired[int]
