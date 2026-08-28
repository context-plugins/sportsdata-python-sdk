from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TeamSeason1(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of the stats associated with the team in this season"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The college football season of the game"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The team's full name"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """Total number of wins by the team in the season"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """The total number of losses by the team in the season"""

    points_for: OptionalNullable[int] = Field(default=UNSET, alias="PointsFor")
    """Total points scored by the team in the season"""

    points_against: OptionalNullable[int] = Field(default=UNSET, alias="PointsAgainst")
    """Total points scored against the team in the season"""

    conference_wins: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceWins")
    """The total number of conference wins by the team"""

    conference_losses: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceLosses")
    """The total number of conference losses by the team"""

    conference_points_for: OptionalNullable[int] = Field(default=UNSET, alias="ConferencePointsFor")
    """Total conference points scored by the team"""

    conference_points_against: OptionalNullable[int] = Field(default=UNSET, alias="ConferencePointsAgainst")
    """Total conference points against the team"""

    home_wins: OptionalNullable[int] = Field(default=UNSET, alias="HomeWins")
    """Total home wins by the team in the season"""

    home_losses: OptionalNullable[int] = Field(default=UNSET, alias="HomeLosses")
    """Total home losses by the team in the season"""

    road_wins: OptionalNullable[int] = Field(default=UNSET, alias="RoadWins")
    """Total road wins by the team in the season"""

    road_losses: OptionalNullable[int] = Field(default=UNSET, alias="RoadLosses")
    """Total road losses by the team in the season"""

    streak: OptionalNullable[int] = Field(default=UNSET, alias="Streak")
    """The current winning or losing streak of the team in the season. A positive number indicates a winning streak, and
    a negative number indicates a losing streak."""

    score: OptionalNullable[int] = Field(default=UNSET, alias="Score")
    """Total points scored by the team in the season"""

    opponent_score: OptionalNullable[int] = Field(default=UNSET, alias="OpponentScore")
    """Total points scored by the opponent team"""

    first_downs: OptionalNullable[int] = Field(default=UNSET, alias="FirstDowns")
    """Total first downs converted by the team in the season"""

    third_down_conversions: OptionalNullable[int] = Field(default=UNSET, alias="ThirdDownConversions")
    """Total third down conversions by the team in the season"""

    third_down_attempts: OptionalNullable[int] = Field(default=UNSET, alias="ThirdDownAttempts")
    """Total third down attempts by the team in the season"""

    fourth_down_conversions: OptionalNullable[int] = Field(default=UNSET, alias="FourthDownConversions")
    """Total fourth down conversions by the team in the season"""

    fourth_down_attempts: OptionalNullable[int] = Field(default=UNSET, alias="FourthDownAttempts")
    """Total fourth down attempts by the team in the season"""

    penalties: OptionalNullable[int] = Field(default=UNSET, alias="Penalties")
    """Total penalties committed by the team in the season"""

    penalty_yards: OptionalNullable[int] = Field(default=UNSET, alias="PenaltyYards")
    """Total penalties yards enforced against the team in the season"""

    time_of_possession_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeOfPossessionMinutes")
    """Total number of minutes the team possessed the ball for in the season"""

    time_of_possession_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeOfPossessionSeconds")
    """Total number of seconds the team possessed the ball for in the season"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for the team. Note: This value is guaranteed to be unique across all sports/leagues."""

    conference_rank: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceRank")
    """This field is deprecated."""

    division_rank: OptionalNullable[int] = Field(default=UNSET, alias="DivisionRank")
    """This field is deprecated."""

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


class TeamSeason1Dict(TypedDict):
    stat_id: NotRequired[int]
    team_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    points_for: NotRequired[int | None]
    points_against: NotRequired[int | None]
    conference_wins: NotRequired[int | None]
    conference_losses: NotRequired[int | None]
    conference_points_for: NotRequired[int | None]
    conference_points_against: NotRequired[int | None]
    home_wins: NotRequired[int | None]
    home_losses: NotRequired[int | None]
    road_wins: NotRequired[int | None]
    road_losses: NotRequired[int | None]
    streak: NotRequired[int | None]
    score: NotRequired[int | None]
    opponent_score: NotRequired[int | None]
    first_downs: NotRequired[int | None]
    third_down_conversions: NotRequired[int | None]
    third_down_attempts: NotRequired[int | None]
    fourth_down_conversions: NotRequired[int | None]
    fourth_down_attempts: NotRequired[int | None]
    penalties: NotRequired[int | None]
    penalty_yards: NotRequired[int | None]
    time_of_possession_minutes: NotRequired[int | None]
    time_of_possession_seconds: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    conference_rank: NotRequired[int | None]
    division_rank: NotRequired[int | None]
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
