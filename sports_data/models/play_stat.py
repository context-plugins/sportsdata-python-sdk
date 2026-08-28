from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayStat(SdkBaseModel):
    play_stat_id: Optional[int] = Field(default=UNSET, alias="PlayStatID")
    """The unique ID of the PlayStat on the play"""

    play_id: Optional[int] = Field(default=UNSET, alias="PlayID")
    """The unique ID of the play in which the PlayStat occurred"""

    sequence: Optional[int] = Field(default=UNSET, alias="Sequence")
    """The order in which the play stat was registered to the Play."""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player whose stats are tied to the play. Note: this ID will stay with the player
    throughout their entire career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The Name of the Player whose stats this represents."""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team the player belongs to"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team of the player who recorded the stat"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Whether the Player was Home or Away (possible values: HOME, AWAY)"""

    direction: OptionalNullable[str] = Field(default=UNSET, alias="Direction")
    """The Direction this Play occurred (possible values: Left, Middle, Right)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The database generated timestamp of when this PlayStat was last updated (in US Eastern time)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The database generated timestamp of when this PlayStat was first created (in US Eastern Time)"""

    passing_attempts: OptionalNullable[int] = Field(default=UNSET, alias="PassingAttempts")
    """Total passes thrown by the player on the play"""

    passing_completions: OptionalNullable[int] = Field(default=UNSET, alias="PassingCompletions")
    """Total passing completions by the player on the play"""

    passing_yards: OptionalNullable[int] = Field(default=UNSET, alias="PassingYards")
    """Total passing yards by the player on the play"""

    passing_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="PassingTouchdowns")
    """Total passing touchdowns thrown by the player on the play"""

    passing_interceptions: OptionalNullable[int] = Field(default=UNSET, alias="PassingInterceptions")
    """Total interceptions thrown by the player on the play"""

    passing_sacks: OptionalNullable[int] = Field(default=UNSET, alias="PassingSacks")
    """The total number of times the player was sacked on the play"""

    passing_sack_yards: OptionalNullable[int] = Field(default=UNSET, alias="PassingSackYards")
    """Total yards lost by the player as a result of being sacked on the play"""

    rushing_attempts: OptionalNullable[int] = Field(default=UNSET, alias="RushingAttempts")
    """Rushing attempts by the player on the play. Note: this field is expected to be 1 or 0"""

    rushing_yards: OptionalNullable[int] = Field(default=UNSET, alias="RushingYards")
    """Total rushing yards by the player on the play"""

    rushing_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="RushingTouchdowns")
    """Total rushing touchdowns by the player on the play. Note: this field is expected to be 1 or 0"""

    receiving_targets: OptionalNullable[int] = Field(default=UNSET, alias="ReceivingTargets")
    """Total receiving targets by the player on the play. Note: this field is expected to be 1 or 0"""

    receptions: OptionalNullable[int] = Field(default=UNSET, alias="Receptions")
    """Total receptions by the player on the play. Note: this field is expected to be 1 or 0"""

    receiving_yards: OptionalNullable[int] = Field(default=UNSET, alias="ReceivingYards")
    """Total receiving yards by the player on the play"""

    receiving_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="ReceivingTouchdowns")
    """Total receiving touchdowns by the player on the play. Note: this field is expected to be 1 or 0"""

    fumbles: OptionalNullable[int] = Field(default=UNSET, alias="Fumbles")
    """Times the player fumbled on the play"""

    fumbles_lost: OptionalNullable[int] = Field(default=UNSET, alias="FumblesLost")
    """Fumbles lost by the player on the play"""

    two_point_conversion_attempts: OptionalNullable[int] = Field(default=UNSET, alias="TwoPointConversionAttempts")
    """Total two point conversion attempts by the player on the play. Note: this field is expected to be 1 or 0"""

    two_point_conversion_passes: OptionalNullable[int] = Field(default=UNSET, alias="TwoPointConversionPasses")
    """Total successful two point conversion passes by the player on the play. Note: this field is expected to be 1 or
    0"""

    two_point_conversion_runs: OptionalNullable[int] = Field(default=UNSET, alias="TwoPointConversionRuns")
    """Total two point conversion rushes by the player on the play. Note: this field is expected to be 1 or 0"""

    two_point_conversion_receptions: OptionalNullable[int] = Field(default=UNSET, alias="TwoPointConversionReceptions")
    """Total successful two point conversion receptions by the player on the play. Note: this field is expected to be 1
    or 0"""

    two_point_conversion_returns: OptionalNullable[int] = Field(default=UNSET, alias="TwoPointConversionReturns")
    """Total successful two point conversion returns by the player on the play. Note: this field is expected to be 1 or
    0"""

    solo_tackles: OptionalNullable[int] = Field(default=UNSET, alias="SoloTackles")
    """Total defensive solo (unassisted) tackles by the player on the play. Note: this field is expected to be 1 or 0"""

    assisted_tackles: OptionalNullable[int] = Field(default=UNSET, alias="AssistedTackles")
    """Total defensive assisted tackles by the player on the play"""

    tackles_for_loss: OptionalNullable[int] = Field(default=UNSET, alias="TacklesForLoss")
    """Tackles for loss of yards by the player on the play. Note: These are tackles behind the line of scrimmage for
    loss of yards (including sacks) - also this field is expected to be 1 or 0"""

    sacks: OptionalNullable[float] = Field(default=UNSET, alias="Sacks")
    """Total Sacks by this player on the play. Note: this field is expected to be 1 or 0"""

    sack_yards: OptionalNullable[float] = Field(default=UNSET, alias="SackYards")
    """Total sack yards by this player on the play"""

    passes_defended: OptionalNullable[int] = Field(default=UNSET, alias="PassesDefended")
    """Total passes defended by the player on the play"""

    safeties: OptionalNullable[int] = Field(default=UNSET, alias="Safeties")
    """Total defensive safeties by the player on the play. Note: this field is expected to be 1 or 0"""

    fumbles_forced: OptionalNullable[int] = Field(default=UNSET, alias="FumblesForced")
    """Fumbles forced by the player on the play"""

    fumbles_recovered: OptionalNullable[int] = Field(default=UNSET, alias="FumblesRecovered")
    """Defensive fumbles recovered by the player on the play"""

    fumble_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="FumbleReturnYards")
    """Fumble recoveries returned yards by the player on the play"""

    fumble_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="FumbleReturnTouchdowns")
    """Fumble recoveries returned for touchdowns by the player on the play"""

    interceptions: OptionalNullable[int] = Field(default=UNSET, alias="Interceptions")
    """Interceptions by the player on the play"""

    interception_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="InterceptionReturnYards")
    """Interception return yards by the player on the play"""

    interception_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="InterceptionReturnTouchdowns")
    """Interception return touchdowns by the player on the play"""

    punt_returns: OptionalNullable[int] = Field(default=UNSET, alias="PuntReturns")
    """Total punts returned by the player on the play"""

    punt_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="PuntReturnYards")
    """Total punt return yards by the player on the play"""

    punt_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="PuntReturnTouchdowns")
    """Punt returns for touchdowns by the player on the play. Note: this field is expected to be 1 or 0"""

    kick_returns: OptionalNullable[int] = Field(default=UNSET, alias="KickReturns")
    """Kicks returned by the player on the play"""

    kick_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="KickReturnYards")
    """Kicks return yards by the player on the play"""

    kick_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="KickReturnTouchdowns")
    """Kicks returned for touchdowns by the player on the play"""

    blocked_kicks: OptionalNullable[int] = Field(default=UNSET, alias="BlockedKicks")
    """Blocked kicks by the player on the play. Note: BlockedKicks include Field Goals and Punts but NOT Extra Points"""

    blocked_kick_returns: OptionalNullable[int] = Field(default=UNSET, alias="BlockedKickReturns")
    """Blocked kick recovery returns by the player on the play"""

    blocked_kick_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="BlockedKickReturnYards")
    """Blocked kick recovery return yards by the player on the play"""

    blocked_kick_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="BlockedKickReturnTouchdowns")
    """Blocked kick recovery return touchdowns by the player on the play"""

    field_goal_returns: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalReturns")
    """Field goal returns by the player on the play"""

    field_goal_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalReturnYards")
    """Field goal return yards by the player on the play. Note: This field excludes blocked field goals"""

    field_goal_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalReturnTouchdowns")
    """Field goal return touchdowns by the player on the play. Note: This field excludes blocked field goals"""

    kickoffs: OptionalNullable[int] = Field(default=UNSET, alias="Kickoffs")
    """Total kickoffs by this player on the play"""

    kickoff_yards: OptionalNullable[int] = Field(default=UNSET, alias="KickoffYards")
    """Gross kickoff yards by the player on the play"""

    kickoff_touchbacks: OptionalNullable[int] = Field(default=UNSET, alias="KickoffTouchbacks")
    """Kickoff touchbacks by the player on the play"""

    punts: OptionalNullable[int] = Field(default=UNSET, alias="Punts")
    """Total number of punts by the player on the play. Note: this field is expected to be 1 or 0"""

    punt_yards: OptionalNullable[int] = Field(default=UNSET, alias="PuntYards")
    """Total gross punt yards by the player on the play"""

    punt_touchbacks: OptionalNullable[int] = Field(default=UNSET, alias="PuntTouchbacks")
    """Total punt touchbacks by the player on the play. Note: this field is expected to be either 1 or 0"""

    punts_had_blocked: OptionalNullable[int] = Field(default=UNSET, alias="PuntsHadBlocked")
    """Total punts by the player that were blocked on the play. Note: this field is expected to be 1 or 0"""

    field_goals_attempted: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalsAttempted")
    """Field goals attempted by the player on the play"""

    field_goals_made: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalsMade")
    """Field goals made by the player on the play"""

    field_goals_yards: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalsYards")
    """Field goal yards attempted by the player on the play"""

    field_goals_had_blocked: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalsHadBlocked")
    """Field goals attempted by the player that were blocked on the play"""

    extra_points_attempted: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointsAttempted")
    """Extra points attempted by the player on the play"""

    extra_points_made: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointsMade")
    """Extra points made by the player on the play"""

    extra_points_had_blocked: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointsHadBlocked")
    """Extra point attempts by the player that were blocked on the play"""

    penalties: OptionalNullable[int] = Field(default=UNSET, alias="Penalties")
    """Indicates the number of penalties against a player on a play. Note: This serves as a placeholder for data
    intended to be added in the future"""

    penalty_yards: OptionalNullable[int] = Field(default=UNSET, alias="PenaltyYards")
    """Total penalty yards enforced against the player on the play"""


class PlayStatDict(TypedDict):
    play_stat_id: NotRequired[int]
    play_id: NotRequired[int]
    sequence: NotRequired[int]
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    opponent: NotRequired[str | None]
    home_or_away: NotRequired[str | None]
    direction: NotRequired[str | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    passing_attempts: NotRequired[int | None]
    passing_completions: NotRequired[int | None]
    passing_yards: NotRequired[int | None]
    passing_touchdowns: NotRequired[int | None]
    passing_interceptions: NotRequired[int | None]
    passing_sacks: NotRequired[int | None]
    passing_sack_yards: NotRequired[int | None]
    rushing_attempts: NotRequired[int | None]
    rushing_yards: NotRequired[int | None]
    rushing_touchdowns: NotRequired[int | None]
    receiving_targets: NotRequired[int | None]
    receptions: NotRequired[int | None]
    receiving_yards: NotRequired[int | None]
    receiving_touchdowns: NotRequired[int | None]
    fumbles: NotRequired[int | None]
    fumbles_lost: NotRequired[int | None]
    two_point_conversion_attempts: NotRequired[int | None]
    two_point_conversion_passes: NotRequired[int | None]
    two_point_conversion_runs: NotRequired[int | None]
    two_point_conversion_receptions: NotRequired[int | None]
    two_point_conversion_returns: NotRequired[int | None]
    solo_tackles: NotRequired[int | None]
    assisted_tackles: NotRequired[int | None]
    tackles_for_loss: NotRequired[int | None]
    sacks: NotRequired[float | None]
    sack_yards: NotRequired[float | None]
    passes_defended: NotRequired[int | None]
    safeties: NotRequired[int | None]
    fumbles_forced: NotRequired[int | None]
    fumbles_recovered: NotRequired[int | None]
    fumble_return_yards: NotRequired[int | None]
    fumble_return_touchdowns: NotRequired[int | None]
    interceptions: NotRequired[int | None]
    interception_return_yards: NotRequired[int | None]
    interception_return_touchdowns: NotRequired[int | None]
    punt_returns: NotRequired[int | None]
    punt_return_yards: NotRequired[int | None]
    punt_return_touchdowns: NotRequired[int | None]
    kick_returns: NotRequired[int | None]
    kick_return_yards: NotRequired[int | None]
    kick_return_touchdowns: NotRequired[int | None]
    blocked_kicks: NotRequired[int | None]
    blocked_kick_returns: NotRequired[int | None]
    blocked_kick_return_yards: NotRequired[int | None]
    blocked_kick_return_touchdowns: NotRequired[int | None]
    field_goal_returns: NotRequired[int | None]
    field_goal_return_yards: NotRequired[int | None]
    field_goal_return_touchdowns: NotRequired[int | None]
    kickoffs: NotRequired[int | None]
    kickoff_yards: NotRequired[int | None]
    kickoff_touchbacks: NotRequired[int | None]
    punts: NotRequired[int | None]
    punt_yards: NotRequired[int | None]
    punt_touchbacks: NotRequired[int | None]
    punts_had_blocked: NotRequired[int | None]
    field_goals_attempted: NotRequired[int | None]
    field_goals_made: NotRequired[int | None]
    field_goals_yards: NotRequired[int | None]
    field_goals_had_blocked: NotRequired[int | None]
    extra_points_attempted: NotRequired[int | None]
    extra_points_made: NotRequired[int | None]
    extra_points_had_blocked: NotRequired[int | None]
    penalties: NotRequired[int | None]
    penalty_yards: NotRequired[int | None]
