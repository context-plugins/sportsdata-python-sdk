from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ScoringPlay(SdkBaseModel):
    scoring_play_id: Optional[int] = Field(default=UNSET, alias="ScoringPlayID")
    """The unique id of the scoring play"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    period: OptionalNullable[str] = Field(default=UNSET, alias="Period")
    """The period of the score"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """Total number of minutes remaining in the quarter when the scoring play happened"""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """Total number of seconds remaining in the quarter when the scoring play happened"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of the play"""

    drive_summary: OptionalNullable[str] = Field(default=UNSET, alias="DriveSummary")
    """The summary of the drive in plays, yards and time elapsed"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """The score of the home team after the play"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of points of the away team after the play"""

    scoring_team_id: OptionalNullable[int] = Field(default=UNSET, alias="ScoringTeamID")
    """The ID of the team who scord on the play"""

    scoring_type: OptionalNullable[str] = Field(default=UNSET, alias="ScoringType")
    """The type of score on the play (ex. TD; FG; SF; D2P for Touchdown; Field Goal; Safety; Defensive 2pt conversion
    respectively)"""

    sequence: Optional[int] = Field(default=UNSET, alias="Sequence")
    """The order in which the scoring plays happened"""


class ScoringPlayDict(TypedDict):
    scoring_play_id: NotRequired[int]
    game_id: NotRequired[int]
    period: NotRequired[str | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    description: NotRequired[str | None]
    drive_summary: NotRequired[str | None]
    home_team_score: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    scoring_team_id: NotRequired[int | None]
    scoring_type: NotRequired[str | None]
    sequence: NotRequired[int]
