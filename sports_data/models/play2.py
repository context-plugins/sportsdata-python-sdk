from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .play_stat import PlayStat, PlayStatDict
from .scoring_play11 import ScoringPlay11, ScoringPlay11Dict


class Play2(SdkBaseModel):
    play_id: Optional[int] = Field(default=UNSET, alias="PlayID")
    """The unique ID of the play"""

    quarter_id: Optional[int] = Field(default=UNSET, alias="QuarterID")
    """The unique ID of the quarter in which the play occurred"""

    quarter_name: OptionalNullable[str] = Field(default=UNSET, alias="QuarterName")
    """The name of the quarter in which the play occurred"""

    sequence: OptionalNullable[int] = Field(default=UNSET, alias="Sequence")
    """The order in which this play and/or event happened over the course of the game"""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """The minutes of the time remaining in the Quarter, when this play occurred."""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """The seconds of the time remaining in the Quarter, when this play occurred."""

    play_time: OptionalNullable[str] = Field(default=UNSET, alias="PlayTime")
    """The estimated timestamp of when this Play occurred on the field. Please note that we do not have scouts at the
    venue; so this is an estimate based on our TV feed and estimated TV feed delay"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The database generated timestamp of when this Play was last updated (in US Eastern time)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The database generated timestamp of when this Play was first created (in US Eastern Time)"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that completed the play"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent of the team that this play relates to"""

    down: OptionalNullable[int] = Field(default=UNSET, alias="Down")
    """The Down when this Play occurred."""

    distance: OptionalNullable[int] = Field(default=UNSET, alias="Distance")
    """The yards to go for a first down. Note: this can be any positive number or "Goal"
    """

    yard_line: OptionalNullable[int] = Field(default=UNSET, alias="YardLine")
    """the yard line of the ball's current position on the field when this play occurred"""

    yard_line_territory: OptionalNullable[str] = Field(default=UNSET, alias="YardLineTerritory")
    """The team's side of the field that the ball is on when the play occurred"""

    yards_to_end_zone: OptionalNullable[int] = Field(default=UNSET, alias="YardsToEndZone")
    """The number of yards to go to reach the end zone at the start of the play"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The Type of Play that occurred (possible values: Rush, PassCompleted, PassIncomplete, PassIntercepted,
    TwoPointConversion, Punt, Kickoff, FieldGoal, ExtraPoint, Fumble, Penalty, Sack, Timeout, Period)"""

    yards_gained: OptionalNullable[int] = Field(default=UNSET, alias="YardsGained")
    """The number of yards gained or lost on the play"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of the Play."""

    is_scoring_play: OptionalNullable[bool] = Field(default=UNSET, alias="IsScoringPlay")
    """Indicates whether this Play was a scoring play."""

    scoring_play: Optional[ScoringPlay11] = Field(default=UNSET, alias="ScoringPlay")
    """The details of the scoring play attached to this play (if any)."""

    play_stats: Optional[list[PlayStat]] = Field(default=UNSET, alias="PlayStats")
    """The list of player stats accumulated during the play"""


class Play2Dict(TypedDict):
    play_id: NotRequired[int]
    quarter_id: NotRequired[int]
    quarter_name: NotRequired[str | None]
    sequence: NotRequired[int | None]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    play_time: NotRequired[str | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    team: NotRequired[str | None]
    opponent: NotRequired[str | None]
    down: NotRequired[int | None]
    distance: NotRequired[int | None]
    yard_line: NotRequired[int | None]
    yard_line_territory: NotRequired[str | None]
    yards_to_end_zone: NotRequired[int | None]
    type_: NotRequired[str | None]
    yards_gained: NotRequired[int | None]
    description: NotRequired[str | None]
    is_scoring_play: NotRequired[bool | None]
    scoring_play: NotRequired[ScoringPlay11 | ScoringPlay11Dict]
    play_stats: NotRequired[list[PlayStat | PlayStatDict]]
