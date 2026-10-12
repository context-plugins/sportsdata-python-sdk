from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .pitch import Pitch, PitchDict


class Play2(SdkBaseModel):
    play_id: Optional[int] = Field(default=UNSET, alias="PlayID")
    """The unique ID of the play assigned by SportsDataIO"""

    inning_id: Optional[int] = Field(default=UNSET, alias="InningID")
    """The unique ID associated with this specific inning in which the play occurred"""

    inning_number: OptionalNullable[int] = Field(default=UNSET, alias="InningNumber")
    """The inning number in which the particular play occurred"""

    inning_half: OptionalNullable[str] = Field(default=UNSET, alias="InningHalf")
    """The inning half that the game is currently in; or the inning half in which the game ended (possible values: T; B;
    E: M: NULL)"""

    play_number: OptionalNullable[int] = Field(default=UNSET, alias="PlayNumber")
    """The order in which plays occurred in a game"""

    inning_batter_number: OptionalNullable[int] = Field(default=UNSET, alias="InningBatterNumber")
    """The batter number in the inning where the play occurred."""

    away_team_runs: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamRuns")
    """Number of runs scored by the away team on this specific play"""

    home_team_runs: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamRuns")
    """Number of runs scored by the home team on this specific play"""

    hitter_id: OptionalNullable[int] = Field(default=UNSET, alias="HitterID")
    """The unique PlayerID of the hitter involved with the play"""

    pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="PitcherID")
    """The PlayerID of the pitcher involved in the play"""

    hitter_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HitterTeamID")
    """The TeamID of the hitter's team."""

    pitcher_team_id: OptionalNullable[int] = Field(default=UNSET, alias="PitcherTeamID")
    """The ID of the pitcher's team"""

    hitter_name: OptionalNullable[str] = Field(default=UNSET, alias="HitterName")
    """The first and last name of the hitter involved in the play"""

    pitcher_name: OptionalNullable[str] = Field(default=UNSET, alias="PitcherName")
    """The full name of the pitcher involved in the play"""

    pitcher_throw_hand: OptionalNullable[str] = Field(default=UNSET, alias="PitcherThrowHand")
    """The throwing hand of the pitcher in which the play occurred. (right or left)"""

    hitter_bat_hand: OptionalNullable[str] = Field(default=UNSET, alias="HitterBatHand")
    """The batter's handedness for which the play occurred. (R; L; S)"""

    hitter_position: OptionalNullable[str] = Field(default=UNSET, alias="HitterPosition")
    """TheÂ position of the player in which the play occrred. (e.g. P;C;1B; SS; OF)"""

    outs: OptionalNullable[int] = Field(default=UNSET, alias="Outs")
    """The number of outs in which the play occurred"""

    balls: OptionalNullable[int] = Field(default=UNSET, alias="Balls")
    """The number of balls in the count in which the play occurred"""

    strikes: OptionalNullable[int] = Field(default=UNSET, alias="Strikes")
    """The number of strikes in the count in which the play occurred"""

    pitch_number_this_at_bat: OptionalNullable[int] = Field(default=UNSET, alias="PitchNumberThisAtBat")
    """The number of pitches in the at bat in which the play occurred"""

    result: OptionalNullable[str] = Field(default=UNSET, alias="Result")
    """The result of the play. Possible values include: Batter's Interference, Bunted into Double Play, Catcher's
    Interference, Double, Error, Fielder's Choice, Fly into Double Play, Fly Out, Foul Out, Fouled into Double Play,
    Ground into Double Play, Ground Out, Hit by Pitch, Home Run, Infield Fly Out, Intentional Walk, Line into Double
    Play, Lineout, Pop Out, Popped into Double Play, Sacrifice, Sacrifice Fly, Single, Strikeout Bunting, Strikeout
    Looking, Strikeout Swinging, Triple, Triple Play, Walk, Stolen Base, Caught Stealing, Passed Ball, Wild Pitch, Pick
    Off, Balk, Error, Fielders Indifference"""

    number_of_outs_on_play: OptionalNullable[int] = Field(default=UNSET, alias="NumberOfOutsOnPlay")
    """The number of outs recorded on the play"""

    runs_batted_in: OptionalNullable[int] = Field(default=UNSET, alias="RunsBattedIn")
    """The number of runs batted in on the play"""

    at_bat: OptionalNullable[bool] = Field(default=UNSET, alias="AtBat")
    """Whether this plate appearance resulted in an at bat"""

    strikeout: OptionalNullable[bool] = Field(default=UNSET, alias="Strikeout")
    """Whether the play resulted with a strikeout (returns true/false)"""

    walk: OptionalNullable[bool] = Field(default=UNSET, alias="Walk")
    """Indicates whether the play resulted in a walk for the hitter (returns true/false)"""

    hit: OptionalNullable[bool] = Field(default=UNSET, alias="Hit")
    """Whether this play resulted in a hit (true/false)"""

    out: OptionalNullable[bool] = Field(default=UNSET, alias="Out")
    """Whether this play resutled in an out (true/false)"""

    sacrifice: OptionalNullable[bool] = Field(default=UNSET, alias="Sacrifice")
    """Whether the play resulted in a sacrifice (returns true/false)"""

    error: OptionalNullable[bool] = Field(default=UNSET, alias="Error")
    """Whether this play resulted in an error (true/false)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The database generated timestamp of when this record was last updated (in US Eastern Time)"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of the play for display purposes"""

    pitches: Optional[list[Pitch]] = Field(default=UNSET, alias="Pitches")
    """The details of the pitches associated with this play"""

    runner1_id: OptionalNullable[int] = Field(default=UNSET, alias="Runner1ID")
    """The PlayerID of the player on first as a result of the play (post-play)"""

    runner2_id: OptionalNullable[int] = Field(default=UNSET, alias="Runner2ID")
    """The PlayerID of the player on second as a result of the play (post-play)"""

    runner3_id: OptionalNullable[int] = Field(default=UNSET, alias="Runner3ID")
    """The PlayerID of the player on third as a result of the play (post-play)"""


class Play2Dict(TypedDict):
    play_id: NotRequired[int]
    inning_id: NotRequired[int]
    inning_number: NotRequired[int | None]
    inning_half: NotRequired[str | None]
    play_number: NotRequired[int | None]
    inning_batter_number: NotRequired[int | None]
    away_team_runs: NotRequired[int | None]
    home_team_runs: NotRequired[int | None]
    hitter_id: NotRequired[int | None]
    pitcher_id: NotRequired[int | None]
    hitter_team_id: NotRequired[int | None]
    pitcher_team_id: NotRequired[int | None]
    hitter_name: NotRequired[str | None]
    pitcher_name: NotRequired[str | None]
    pitcher_throw_hand: NotRequired[str | None]
    hitter_bat_hand: NotRequired[str | None]
    hitter_position: NotRequired[str | None]
    outs: NotRequired[int | None]
    balls: NotRequired[int | None]
    strikes: NotRequired[int | None]
    pitch_number_this_at_bat: NotRequired[int | None]
    result: NotRequired[str | None]
    number_of_outs_on_play: NotRequired[int | None]
    runs_batted_in: NotRequired[int | None]
    at_bat: NotRequired[bool | None]
    strikeout: NotRequired[bool | None]
    walk: NotRequired[bool | None]
    hit: NotRequired[bool | None]
    out: NotRequired[bool | None]
    sacrifice: NotRequired[bool | None]
    error: NotRequired[bool | None]
    updated: NotRequired[str | None]
    description: NotRequired[str | None]
    pitches: NotRequired[list[PitchDict]]
    runner1_id: NotRequired[int | None]
    runner2_id: NotRequired[int | None]
    runner3_id: NotRequired[int | None]
