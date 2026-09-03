from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerSeason5(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of the stats associated with the player in this season"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team associated with this player"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the player as assigned by SportsDataIO. Note: this ID remains with the player their entire
    collegiate career"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The college football season of the game"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """Player's position in the starting lineup (if started), otherwise the position he substituted for"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The category (Offense, Defense or Special Teams) of the players position (OFF, DEF, ST)"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for the player's team. Note: This value is guaranteed to be unique across all
    sports/leagues."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The updated date and time of the stat."""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time of the created stat."""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """Indicates whether or not a player has recorded any stats for a given game."""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points"""

    passing_attempts: OptionalNullable[float] = Field(default=UNSET, alias="PassingAttempts")
    """Total passing attempts"""

    passing_completions: OptionalNullable[float] = Field(default=UNSET, alias="PassingCompletions")
    """Total passing completions"""

    passing_yards: OptionalNullable[float] = Field(default=UNSET, alias="PassingYards")
    """Total passing yards"""

    passing_completion_percentage: OptionalNullable[float] = Field(default=UNSET, alias="PassingCompletionPercentage")
    """Total passing completion percentage"""

    passing_yards_per_attempt: OptionalNullable[float] = Field(default=UNSET, alias="PassingYardsPerAttempt")
    """Total passing yards per attempts"""

    passing_yards_per_completion: OptionalNullable[float] = Field(default=UNSET, alias="PassingYardsPerCompletion")
    """Total passing yards per completion"""

    passing_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="PassingTouchdowns")
    """Total passing touchdowns"""

    passing_interceptions: OptionalNullable[float] = Field(default=UNSET, alias="PassingInterceptions")
    """Total passing interceptions"""

    passing_rating: OptionalNullable[float] = Field(default=UNSET, alias="PassingRating")
    """Total passing rating"""

    rushing_attempts: OptionalNullable[float] = Field(default=UNSET, alias="RushingAttempts")
    """Total rushing attempts"""

    rushing_yards: OptionalNullable[float] = Field(default=UNSET, alias="RushingYards")
    """Total rushing yards"""

    rushing_yards_per_attempt: OptionalNullable[float] = Field(default=UNSET, alias="RushingYardsPerAttempt")
    """Total rushing yards per attempt"""

    rushing_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="RushingTouchdowns")
    """Total rushing touchdowns"""

    rushing_long: OptionalNullable[float] = Field(default=UNSET, alias="RushingLong")
    """Longest rushing attempt"""

    receptions: OptionalNullable[float] = Field(default=UNSET, alias="Receptions")
    """Total receptions"""

    receiving_yards: OptionalNullable[float] = Field(default=UNSET, alias="ReceivingYards")
    """Total receiving yards"""

    receiving_yards_per_reception: OptionalNullable[float] = Field(default=UNSET, alias="ReceivingYardsPerReception")
    """Total receiving yards per reception"""

    receiving_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="ReceivingTouchdowns")
    """Total receiving touchdowns"""

    receiving_long: OptionalNullable[float] = Field(default=UNSET, alias="ReceivingLong")
    """Long receiving reception"""

    punt_returns: OptionalNullable[float] = Field(default=UNSET, alias="PuntReturns")
    """Total punt returns"""

    punt_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="PuntReturnYards")
    """Total punt return yards"""

    punt_return_yards_per_attempt: OptionalNullable[float] = Field(default=UNSET, alias="PuntReturnYardsPerAttempt")
    """Total punt return yards per attempt"""

    punt_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="PuntReturnTouchdowns")
    """Total punt return touchdowns"""

    punt_return_long: OptionalNullable[float] = Field(default=UNSET, alias="PuntReturnLong")
    """Longest punt return"""

    kick_returns: OptionalNullable[float] = Field(default=UNSET, alias="KickReturns")
    """Total kick returns"""

    kick_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="KickReturnYards")
    """Total kick return yards"""

    kick_return_yards_per_attempt: OptionalNullable[float] = Field(default=UNSET, alias="KickReturnYardsPerAttempt")
    """Total kick return yards per attempt"""

    kick_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="KickReturnTouchdowns")
    """Total kick return touchdowns"""

    kick_return_long: OptionalNullable[float] = Field(default=UNSET, alias="KickReturnLong")
    """Longest kick return"""

    punts: OptionalNullable[float] = Field(default=UNSET, alias="Punts")
    """Total punts"""

    punt_yards: OptionalNullable[float] = Field(default=UNSET, alias="PuntYards")
    """Total punt yards"""

    punt_average: OptionalNullable[float] = Field(default=UNSET, alias="PuntAverage")
    """Total punt average"""

    punt_long: OptionalNullable[float] = Field(default=UNSET, alias="PuntLong")
    """Longest punt"""

    field_goals_attempted: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsAttempted")
    """Total field goals attempted"""

    field_goals_made: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade")
    """Total field goals made"""

    field_goal_percentage: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalPercentage")
    """Total field goal percentage"""

    field_goals_longest_made: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsLongestMade")
    """Longest field goal made"""

    extra_points_attempted: OptionalNullable[float] = Field(default=UNSET, alias="ExtraPointsAttempted")
    """Total extra points attempted"""

    extra_points_made: OptionalNullable[float] = Field(default=UNSET, alias="ExtraPointsMade")
    """Total extra points made"""

    interceptions: OptionalNullable[float] = Field(default=UNSET, alias="Interceptions")
    """Total interceptions"""

    interception_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="InterceptionReturnYards")
    """Total interception return yards"""

    interception_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="InterceptionReturnTouchdowns")
    """Total interception return touchdowns"""

    solo_tackles: OptionalNullable[float] = Field(default=UNSET, alias="SoloTackles")
    """Total Solo Tackles"""

    assisted_tackles: OptionalNullable[float] = Field(default=UNSET, alias="AssistedTackles")
    """Total Assisted Tackles"""

    tackles_for_loss: OptionalNullable[float] = Field(default=UNSET, alias="TacklesForLoss")
    """Total Tackles for a loss of yardage"""

    sacks: OptionalNullable[float] = Field(default=UNSET, alias="Sacks")
    """Total Quarterback Sacks"""

    passes_defended: OptionalNullable[float] = Field(default=UNSET, alias="PassesDefended")
    """Total Passes Defended"""

    fumbles_recovered: OptionalNullable[float] = Field(default=UNSET, alias="FumblesRecovered")
    """Total Fumble Recoveries"""

    fumble_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="FumbleReturnTouchdowns")
    """Total Fumbles Recovered and returned for a touchdown"""

    quarterback_hurries: OptionalNullable[float] = Field(default=UNSET, alias="QuarterbackHurries")
    """Total Quarterback Hurries. NOTE: This field is deprecated as of 2021."""

    fumbles: OptionalNullable[float] = Field(default=UNSET, alias="Fumbles")
    """Total Fumbles"""

    fumbles_lost: OptionalNullable[float] = Field(default=UNSET, alias="FumblesLost")
    """Total Fumbles Lost"""


class PlayerSeason5Dict(TypedDict):
    stat_id: NotRequired[int]
    team_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
    position_category: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    games: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    passing_attempts: NotRequired[float | None]
    passing_completions: NotRequired[float | None]
    passing_yards: NotRequired[float | None]
    passing_completion_percentage: NotRequired[float | None]
    passing_yards_per_attempt: NotRequired[float | None]
    passing_yards_per_completion: NotRequired[float | None]
    passing_touchdowns: NotRequired[float | None]
    passing_interceptions: NotRequired[float | None]
    passing_rating: NotRequired[float | None]
    rushing_attempts: NotRequired[float | None]
    rushing_yards: NotRequired[float | None]
    rushing_yards_per_attempt: NotRequired[float | None]
    rushing_touchdowns: NotRequired[float | None]
    rushing_long: NotRequired[float | None]
    receptions: NotRequired[float | None]
    receiving_yards: NotRequired[float | None]
    receiving_yards_per_reception: NotRequired[float | None]
    receiving_touchdowns: NotRequired[float | None]
    receiving_long: NotRequired[float | None]
    punt_returns: NotRequired[float | None]
    punt_return_yards: NotRequired[float | None]
    punt_return_yards_per_attempt: NotRequired[float | None]
    punt_return_touchdowns: NotRequired[float | None]
    punt_return_long: NotRequired[float | None]
    kick_returns: NotRequired[float | None]
    kick_return_yards: NotRequired[float | None]
    kick_return_yards_per_attempt: NotRequired[float | None]
    kick_return_touchdowns: NotRequired[float | None]
    kick_return_long: NotRequired[float | None]
    punts: NotRequired[float | None]
    punt_yards: NotRequired[float | None]
    punt_average: NotRequired[float | None]
    punt_long: NotRequired[float | None]
    field_goals_attempted: NotRequired[float | None]
    field_goals_made: NotRequired[float | None]
    field_goal_percentage: NotRequired[float | None]
    field_goals_longest_made: NotRequired[float | None]
    extra_points_attempted: NotRequired[float | None]
    extra_points_made: NotRequired[float | None]
    interceptions: NotRequired[float | None]
    interception_return_yards: NotRequired[float | None]
    interception_return_touchdowns: NotRequired[float | None]
    solo_tackles: NotRequired[float | None]
    assisted_tackles: NotRequired[float | None]
    tackles_for_loss: NotRequired[float | None]
    sacks: NotRequired[float | None]
    passes_defended: NotRequired[float | None]
    fumbles_recovered: NotRequired[float | None]
    fumble_return_touchdowns: NotRequired[float | None]
    quarterback_hurries: NotRequired[float | None]
    fumbles: NotRequired[float | None]
    fumbles_lost: NotRequired[float | None]
