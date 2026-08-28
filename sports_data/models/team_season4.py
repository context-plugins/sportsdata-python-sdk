from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TeamSeason4(SdkBaseModel):
    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this team corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL regular season for which these totals apply"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    score: Optional[int] = Field(default=UNSET, alias="Score")
    """Total points scored by the team in the season"""

    opponent_score: Optional[int] = Field(default=UNSET, alias="OpponentScore")
    """Total points scored by opponent teams in the season"""

    total_score: Optional[int] = Field(default=UNSET, alias="TotalScore")
    """The total points scored and allowed by the team in the season"""

    temperature: OptionalNullable[int] = Field(default=UNSET, alias="Temperature")
    """Temperature at game start (Fahrenheit)"""

    humidity: OptionalNullable[int] = Field(default=UNSET, alias="Humidity")
    """The humidity percentage at the start of the game"""

    wind_speed: OptionalNullable[int] = Field(default=UNSET, alias="WindSpeed")
    """The wind speed at the start of the game (in MPH)"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The average total points line (over/under) for the team in the season"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """The average point spread from the perspecive of the team for the season (negative numbers indicate the HomeTeam
    is favored; positive numbers indicate the AwayTeam is favored)"""

    score_quarter1: OptionalNullable[int] = Field(default=UNSET, alias="ScoreQuarter1")
    """Points scored during Quarter 1 for the team in the season"""

    score_quarter2: OptionalNullable[int] = Field(default=UNSET, alias="ScoreQuarter2")
    """Points scored during Quarter 2 for the team in the season"""

    score_quarter3: OptionalNullable[int] = Field(default=UNSET, alias="ScoreQuarter3")
    """Points scored during Quarter 3 for the team in the season"""

    score_quarter4: OptionalNullable[int] = Field(default=UNSET, alias="ScoreQuarter4")
    """Points scored during Quarter 4 for the team in the season"""

    score_overtime: Optional[int] = Field(default=UNSET, alias="ScoreOvertime")
    """Points scored during overtime for the team in the season"""

    time_of_possession: OptionalNullable[str] = Field(default=UNSET, alias="TimeOfPossession")
    """Total average time of possession by the team in the season"""

    first_downs: OptionalNullable[int] = Field(default=UNSET, alias="FirstDowns")
    """Total first downs by the team in the season"""

    first_downs_by_rushing: OptionalNullable[int] = Field(default=UNSET, alias="FirstDownsByRushing")
    """Total rushing first downs by the team in the season"""

    first_downs_by_passing: OptionalNullable[int] = Field(default=UNSET, alias="FirstDownsByPassing")
    """Total passing first downs team in the season"""

    first_downs_by_penalty: OptionalNullable[int] = Field(default=UNSET, alias="FirstDownsByPenalty")
    """Total first downs by opponent's penalty by the team in the season"""

    offensive_plays: Optional[int] = Field(default=UNSET, alias="OffensivePlays")
    """Number of offensive plays run by the season in the game"""

    offensive_yards: Optional[int] = Field(default=UNSET, alias="OffensiveYards")
    """Total offensive yards gained by the team in the season"""

    offensive_yards_per_play: Optional[float] = Field(default=UNSET, alias="OffensiveYardsPerPlay")
    """Average yards gained per offensive play by the team in the season"""

    touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="Touchdowns")
    """Total touchdowns scored by the team in the season"""

    rushing_attempts: OptionalNullable[int] = Field(default=UNSET, alias="RushingAttempts")
    """Total rushing attempts by the team in the season"""

    rushing_yards: OptionalNullable[int] = Field(default=UNSET, alias="RushingYards")
    """Total rushing yards by the team in the season"""

    rushing_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="RushingYardsPerAttempt")
    """Total rushing yards per attempt by the team in the season"""

    rushing_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="RushingTouchdowns")
    """Total rushing touchdowns by the team in the season"""

    passing_attempts: OptionalNullable[int] = Field(default=UNSET, alias="PassingAttempts")
    """Total passes thrown by the team in the season"""

    passing_completions: OptionalNullable[int] = Field(default=UNSET, alias="PassingCompletions")
    """Total passes completed by the team in the season"""

    passing_yards: OptionalNullable[int] = Field(default=UNSET, alias="PassingYards")
    """Total passing yards by the team in the season"""

    passing_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="PassingTouchdowns")
    """Total passing touchdowns by the team in the season"""

    passing_interceptions: OptionalNullable[int] = Field(default=UNSET, alias="PassingInterceptions")
    """Total interceptions thrown by the team in the season"""

    passing_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="PassingYardsPerAttempt")
    """Total average passing yards per attempt by the team in the season"""

    passing_yards_per_completion: Optional[float] = Field(default=UNSET, alias="PassingYardsPerCompletion")
    """Total average passing yards per completion by the team in the season"""

    completion_percentage: Optional[float] = Field(default=UNSET, alias="CompletionPercentage")
    """Percentage of passes that were completed by the team in the season"""

    passer_rating: OptionalNullable[float] = Field(default=UNSET, alias="PasserRating")
    """The team's passer rating in the season"""

    third_down_attempts: OptionalNullable[int] = Field(default=UNSET, alias="ThirdDownAttempts")
    """Total third down attempts by the team in the season"""

    third_down_conversions: OptionalNullable[int] = Field(default=UNSET, alias="ThirdDownConversions")
    """Total third down conversions by the team in the season"""

    third_down_percentage: OptionalNullable[float] = Field(default=UNSET, alias="ThirdDownPercentage")
    """Total percentage of third downs converted by the team in the season"""

    fourth_down_attempts: OptionalNullable[int] = Field(default=UNSET, alias="FourthDownAttempts")
    """Total fourth down attempts by the team in the season"""

    fourth_down_conversions: OptionalNullable[int] = Field(default=UNSET, alias="FourthDownConversions")
    """Total fourth down conversions by the team in the season"""

    fourth_down_percentage: OptionalNullable[float] = Field(default=UNSET, alias="FourthDownPercentage")
    """Percentage of fourth downs converted by the team in the season"""

    red_zone_attempts: OptionalNullable[int] = Field(default=UNSET, alias="RedZoneAttempts")
    """Total red zone opportunities by the team in the season"""

    red_zone_conversions: OptionalNullable[int] = Field(default=UNSET, alias="RedZoneConversions")
    """Total red zone opportunities converted into touchdowns by the team in the season"""

    goal_to_go_attempts: OptionalNullable[int] = Field(default=UNSET, alias="GoalToGoAttempts")
    """This field is deprecated"""

    goal_to_go_conversions: OptionalNullable[int] = Field(default=UNSET, alias="GoalToGoConversions")
    """This field is deprecated"""

    return_yards: OptionalNullable[int] = Field(default=UNSET, alias="ReturnYards")
    """Total punt and defensive return yards by the team in the season"""

    penalties: OptionalNullable[int] = Field(default=UNSET, alias="Penalties")
    """Total penalties committed by the team in the season"""

    penalty_yards: OptionalNullable[int] = Field(default=UNSET, alias="PenaltyYards")
    """Total penalty yards enforced against the team"""

    fumbles: OptionalNullable[int] = Field(default=UNSET, alias="Fumbles")
    """Total fumbles by the team in the season"""

    fumbles_lost: OptionalNullable[int] = Field(default=UNSET, alias="FumblesLost")
    """Total fumbles lost by the team in the season"""

    times_sacked: OptionalNullable[int] = Field(default=UNSET, alias="TimesSacked")
    """Total number of sacks allowed by the team in the season"""

    times_sacked_yards: OptionalNullable[int] = Field(default=UNSET, alias="TimesSackedYards")
    """Total sack yards allowed by the team in the season"""

    quarterback_hits: OptionalNullable[int] = Field(default=UNSET, alias="QuarterbackHits")
    """Total quarterback hits by the team in the season. Note: This is a defensive stat that includes sacks"""

    tackles_for_loss: OptionalNullable[int] = Field(default=UNSET, alias="TacklesForLoss")
    """Total tackles for loss by the team in the season. Note: These are tackles behind the line of scrimmage for loss
    of yards (including sacks)"""

    safeties: OptionalNullable[int] = Field(default=UNSET, alias="Safeties")
    """Total defensive safeties scored by the team in the season"""

    punts: OptionalNullable[int] = Field(default=UNSET, alias="Punts")
    """Total number of punts by the team in the game"""

    punt_yards: OptionalNullable[int] = Field(default=UNSET, alias="PuntYards")
    """Total punt yards by the team in the season"""

    punt_average: Optional[float] = Field(default=UNSET, alias="PuntAverage")
    """The average number of yards per punt by the team in the season"""

    giveaways: Optional[int] = Field(default=UNSET, alias="Giveaways")
    """Total number of giveaways by the team in the season"""

    takeaways: Optional[int] = Field(default=UNSET, alias="Takeaways")
    """Total takeaways by the team in the season"""

    turnover_differential: Optional[int] = Field(default=UNSET, alias="TurnoverDifferential")
    """Total turnover differential (takeaways minus giveaways) by the team in the season"""

    opponent_score_quarter1: OptionalNullable[int] = Field(default=UNSET, alias="OpponentScoreQuarter1")
    """Points scored during Quarter 1 for the opponent teams in the season"""

    opponent_score_quarter2: OptionalNullable[int] = Field(default=UNSET, alias="OpponentScoreQuarter2")
    """Points scored during Quarter 2 for the opponent teams in the season"""

    opponent_score_quarter3: OptionalNullable[int] = Field(default=UNSET, alias="OpponentScoreQuarter3")
    """Points scored during Quarter 3 for the opponent teams in the season"""

    opponent_score_quarter4: OptionalNullable[int] = Field(default=UNSET, alias="OpponentScoreQuarter4")
    """Points scored during Quarter 4 for the opponent teams in the season"""

    opponent_score_overtime: Optional[int] = Field(default=UNSET, alias="OpponentScoreOvertime")
    """Points scored during overtime for the opponent teams in the season"""

    opponent_time_of_possession: OptionalNullable[str] = Field(default=UNSET, alias="OpponentTimeOfPossession")
    """Total average time of possession for the opponent teams in the season"""

    opponent_first_downs: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFirstDowns")
    """Total first downs converted the opponent teams in the season"""

    opponent_first_downs_by_rushing: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFirstDownsByRushing")
    """Total rushing first downs by the opponent teams in the season"""

    opponent_first_downs_by_passing: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFirstDownsByPassing")
    """Total passing first downs converted the opponent teams in the season"""

    opponent_first_downs_by_penalty: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFirstDownsByPenalty")
    """Total first downs by penalty for the opponent teams in the season"""

    opponent_offensive_plays: Optional[int] = Field(default=UNSET, alias="OpponentOffensivePlays")
    """Total offensive plays by the opponent teams in the season"""

    opponent_offensive_yards: Optional[int] = Field(default=UNSET, alias="OpponentOffensiveYards")
    """Total offensive yards gained by the opponent teams in the season"""

    opponent_offensive_yards_per_play: Optional[float] = Field(default=UNSET, alias="OpponentOffensiveYardsPerPlay")
    """Average yards gained per offensive play by the opponent teams in the season"""

    opponent_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="OpponentTouchdowns")
    """Total touchdowns scored by the opponent teams in the season"""

    opponent_rushing_attempts: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRushingAttempts")
    """Total rushing attempts by the opponent teams in the season"""

    opponent_rushing_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRushingYards")
    """Total rushing yards by the opponent teams in the season"""

    opponent_rushing_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="OpponentRushingYardsPerAttempt")
    """Average rushing yards gained per attempt by the opponent teams in the season"""

    opponent_rushing_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRushingTouchdowns")
    """Total rushing touchdowns by the opponent teams in the season"""

    opponent_passing_attempts: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPassingAttempts")
    """Total passes thrown by the opponent teams in the season"""

    opponent_passing_completions: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPassingCompletions")
    """Total passing completions by the opponent teams in the season"""

    opponent_passing_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPassingYards")
    """Total passing yards by the opponent teams in the season"""

    opponent_passing_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPassingTouchdowns")
    """Total passing touchdowns by the opponent teams in the season"""

    opponent_passing_interceptions: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPassingInterceptions")
    """Total interception thrown by the opponent teams in the season"""

    opponent_passing_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="OpponentPassingYardsPerAttempt")
    """Average passing yards gained per attempt by the opponent teams in the season"""

    opponent_passing_yards_per_completion: Optional[float] = Field(
        default=UNSET, alias="OpponentPassingYardsPerCompletion"
    )
    """Average passing yards gained per completion by the opponent teams in the season"""

    opponent_completion_percentage: Optional[float] = Field(default=UNSET, alias="OpponentCompletionPercentage")
    """Total completion percentage of the opponent teams in the season"""

    opponent_passer_rating: OptionalNullable[float] = Field(default=UNSET, alias="OpponentPasserRating")
    """Total passer rating by the opponent teams in the season"""

    opponent_third_down_attempts: OptionalNullable[int] = Field(default=UNSET, alias="OpponentThirdDownAttempts")
    """Total third down attempts by the opponent teams in the season"""

    opponent_third_down_conversions: OptionalNullable[int] = Field(default=UNSET, alias="OpponentThirdDownConversions")
    """Total third down conversions by the opponent teams in the season"""

    opponent_third_down_percentage: OptionalNullable[float] = Field(default=UNSET, alias="OpponentThirdDownPercentage")
    """Total third down percentage by the opponent teams in the season"""

    opponent_fourth_down_attempts: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFourthDownAttempts")
    """Total fourth downs attempted by the opponent teams in the season"""

    opponent_fourth_down_conversions: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentFourthDownConversions"
    )
    """Total fourth downs converted by the opponent teams in the season"""

    opponent_fourth_down_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="OpponentFourthDownPercentage"
    )
    """Total fourth down conversion percentage by the opponent teams in the season"""

    opponent_red_zone_attempts: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRedZoneAttempts")
    """Total red zone opportunities by the opponents in the season"""

    opponent_red_zone_conversions: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRedZoneConversions")
    """Total red zone opportunities converted to touchdowns by the opponents in the season"""

    opponent_goal_to_go_attempts: OptionalNullable[int] = Field(default=UNSET, alias="OpponentGoalToGoAttempts")
    """This field is deprecated"""

    opponent_goal_to_go_conversions: OptionalNullable[int] = Field(default=UNSET, alias="OpponentGoalToGoConversions")
    """This field is deprecated"""

    opponent_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentReturnYards")
    """Total punt and defensive return yards by the opponent teams in the season"""

    opponent_penalties: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPenalties")
    """Total penalty yards enforced against the opponent teams in the season"""

    opponent_penalty_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPenaltyYards")
    """Total penalty yards enforced against the opponent teams in the season"""

    opponent_fumbles: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFumbles")
    """Total offensive fumbles by the opponent teams in the season"""

    opponent_fumbles_lost: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFumblesLost")
    """Total fumbles lost by the opponent teams in the season"""

    opponent_times_sacked: OptionalNullable[int] = Field(default=UNSET, alias="OpponentTimesSacked")
    """Total sacks allowed by the opponent teams in the season"""

    opponent_times_sacked_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentTimesSackedYards")
    """Total yards as a result of a sack allowed by the opponent teams in the season"""

    opponent_quarterback_hits: OptionalNullable[int] = Field(default=UNSET, alias="OpponentQuarterbackHits")
    """Total quarterback hits by the opponent teams in the season"""

    opponent_tackles_for_loss: OptionalNullable[int] = Field(default=UNSET, alias="OpponentTacklesForLoss")
    """Total tackles for loss by the opponent teams in the season"""

    opponent_safeties: OptionalNullable[int] = Field(default=UNSET, alias="OpponentSafeties")
    """Total safeties recorded by the opponent teams in the season"""

    opponent_punts: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPunts")
    """Total punts by the opponent teams in the season"""

    opponent_punt_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPuntYards")
    """Total punt yards by the opponent teams in the season"""

    opponent_punt_average: Optional[float] = Field(default=UNSET, alias="OpponentPuntAverage")
    """Average number of yards per punt by the opponent team in the season"""

    opponent_giveaways: Optional[int] = Field(default=UNSET, alias="OpponentGiveaways")
    """Total giveaways by the opponent teams in the season"""

    opponent_takeaways: Optional[int] = Field(default=UNSET, alias="OpponentTakeaways")
    """Total takeaways by the opponent teams in the season"""

    opponent_turnover_differential: Optional[int] = Field(default=UNSET, alias="OpponentTurnoverDifferential")
    """Total turnover differential by the opponent teams in the season (takeaways minus giveaways)"""

    red_zone_percentage: OptionalNullable[float] = Field(default=UNSET, alias="RedZonePercentage")
    """Total percentage of red zone opportunities converted into touchdowns by the team in the season"""

    goal_to_go_percentage: OptionalNullable[float] = Field(default=UNSET, alias="GoalToGoPercentage")
    """This field is deprecated"""

    quarterback_hits_differential: OptionalNullable[int] = Field(default=UNSET, alias="QuarterbackHitsDifferential")
    """The quarterback hits differential of the team in the season. Note: Determined by hits on opposing quarterback
    minus hits on own quarterback"""

    tackles_for_loss_differential: OptionalNullable[int] = Field(default=UNSET, alias="TacklesForLossDifferential")
    """Total tackles for loss differential by the team in the season"""

    quarterback_sacks_differential: Optional[int] = Field(default=UNSET, alias="QuarterbackSacksDifferential")
    """Total sack differential of the team in the season"""

    tackles_for_loss_percentage: OptionalNullable[float] = Field(default=UNSET, alias="TacklesForLossPercentage")
    """Total percentage of plays defended that resulted in a tackle for loss by the team in the season"""

    quarterback_hits_percentage: OptionalNullable[float] = Field(default=UNSET, alias="QuarterbackHitsPercentage")
    """Total percentage of opposing quarterback dropbacks that resulted in a quarterback hit by the team in the
    season"""

    times_sacked_percentage: Optional[float] = Field(default=UNSET, alias="TimesSackedPercentage")
    """Total percentage of drop backs that resulted in a sack by the team in the season"""

    opponent_red_zone_percentage: OptionalNullable[float] = Field(default=UNSET, alias="OpponentRedZonePercentage")
    """Percentage of opponent's red zone opportunities converted into touchdowns in the season"""

    opponent_goal_to_go_percentage: OptionalNullable[float] = Field(default=UNSET, alias="OpponentGoalToGoPercentage")
    """This field is deprecated"""

    opponent_quarterback_hits_differential: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentQuarterbackHitsDifferential"
    )
    """Total quarterback hits differential by the opponent teams in the season"""

    opponent_tackles_for_loss_differential: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentTacklesForLossDifferential"
    )
    """Total tackles for loss differential by the opponent teams in the season"""

    opponent_quarterback_sacks_differential: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentQuarterbackSacksDifferential"
    )
    """Total quarterback sacks differential by the opponent teams in the season"""

    opponent_tackles_for_loss_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="OpponentTacklesForLossPercentage"
    )
    """Total percentage of tackles for loss by the opponent teams in the season"""

    opponent_quarterback_hits_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="OpponentQuarterbackHitsPercentage"
    )
    """Percentage of own team's quarterback drop backs that resulted in our quarterback getting hit"""

    opponent_times_sacked_percentage: Optional[float] = Field(default=UNSET, alias="OpponentTimesSackedPercentage")
    """Total percentage of dropbacks that resulted in a sack allowed by the opponent teams in the season"""

    kickoffs: OptionalNullable[int] = Field(default=UNSET, alias="Kickoffs")
    """Total number of kickoffs by the team in the season"""

    kickoffs_in_end_zone: OptionalNullable[int] = Field(default=UNSET, alias="KickoffsInEndZone")
    """Total kickoffs that went into the end zone by the team in the season"""

    kickoff_touchbacks: OptionalNullable[int] = Field(default=UNSET, alias="KickoffTouchbacks")
    """Total kickoffs that resulted in touchbacks by the team in the season"""

    punts_had_blocked: OptionalNullable[int] = Field(default=UNSET, alias="PuntsHadBlocked")
    """Total punts by the team that were blocked in the season"""

    punt_net_average: OptionalNullable[float] = Field(default=UNSET, alias="PuntNetAverage")
    """The average net yards per punt by the team in the season"""

    extra_point_kicking_attempts: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointKickingAttempts")
    """Total extra point kick attempts by the team in the season"""

    extra_point_kicking_conversions: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointKickingConversions")
    """Total extra point kicks made by the team in the season"""

    extra_points_had_blocked: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointsHadBlocked")
    """Total extra point kick attempts by the team that were blocked in the season"""

    extra_point_passing_attempts: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointPassingAttempts")
    """Total two point conversion passing attempts by the team in the season"""

    extra_point_passing_conversions: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointPassingConversions")
    """Total two point conversion passing conversions by the team in the season"""

    extra_point_rushing_attempts: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointRushingAttempts")
    """Total two point conversion rushing attempts by the team in the season"""

    extra_point_rushing_conversions: OptionalNullable[int] = Field(default=UNSET, alias="ExtraPointRushingConversions")
    """Total two point conversion rushing conversions in the season"""

    field_goal_attempts: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalAttempts")
    """Total field goal attempts by the team in the season"""

    field_goals_made: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalsMade")
    """Total field goals made by the team in season"""

    field_goals_had_blocked: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalsHadBlocked")
    """Total field goals by the team that were blocked in the season"""

    punt_returns: OptionalNullable[int] = Field(default=UNSET, alias="PuntReturns")
    """Total punt returns by the team in the season"""

    punt_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="PuntReturnYards")
    """Total punt return yards by the team in the season"""

    kick_returns: OptionalNullable[int] = Field(default=UNSET, alias="KickReturns")
    """Total kickoff returns by the team in the season"""

    kick_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="KickReturnYards")
    """Total kickoff return yards by the team in the season"""

    interception_returns: OptionalNullable[int] = Field(default=UNSET, alias="InterceptionReturns")
    """Total defensive interception returns by the team in the season"""

    interception_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="InterceptionReturnYards")
    """Total defensive interception return yards by the team in the season"""

    opponent_kickoffs: OptionalNullable[int] = Field(default=UNSET, alias="OpponentKickoffs")
    """Total kickoffs by the opponent teams in the season"""

    opponent_kickoffs_in_end_zone: OptionalNullable[int] = Field(default=UNSET, alias="OpponentKickoffsInEndZone")
    """Total kickoffs that went into the end zone by the opponent teams in the season"""

    opponent_kickoff_touchbacks: OptionalNullable[int] = Field(default=UNSET, alias="OpponentKickoffTouchbacks")
    """Total kickoffs that resulted in touchbacks by the opponent teams in the season"""

    opponent_punts_had_blocked: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPuntsHadBlocked")
    """Total punt yard that were blocked for the opponent teams in the season"""

    opponent_punt_net_average: OptionalNullable[float] = Field(default=UNSET, alias="OpponentPuntNetAverage")
    """Average net punt yards by the opponent team in the season"""

    opponent_extra_point_kicking_attempts: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentExtraPointKickingAttempts"
    )
    """Total extra point kick attempts by the opponent teams in the season"""

    opponent_extra_point_kicking_conversions: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentExtraPointKickingConversions"
    )
    """Total extra point kicks made by the opponent teams in the season"""

    opponent_extra_points_had_blocked: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentExtraPointsHadBlocked"
    )
    """Total extra point kick attempts that were blocked against the opponent teams in the season"""

    opponent_extra_point_passing_attempts: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentExtraPointPassingAttempts"
    )
    """Total two point conversion passing attempts by the opponent teams in the season"""

    opponent_extra_point_passing_conversions: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentExtraPointPassingConversions"
    )
    """Total two point conversion passing conversions by the opponent teams in the season"""

    opponent_extra_point_rushing_attempts: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentExtraPointRushingAttempts"
    )
    """Total two point conversion rushing attempts by the opponent teams in the season"""

    opponent_extra_point_rushing_conversions: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentExtraPointRushingConversions"
    )
    """Total two point conversion rushing conversions by the opponent teams in the season"""

    opponent_field_goal_attempts: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFieldGoalAttempts")
    """Total field goal attempts by the opponent teams in the season"""

    opponent_field_goals_made: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFieldGoalsMade")
    """Total field goals made the opponent teams in the season"""

    opponent_field_goals_had_blocked: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFieldGoalsHadBlocked")
    """Total blocked field goals against the opponent teams in the season"""

    opponent_punt_returns: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPuntReturns")
    """Total punt returns by the opponent teams in the season"""

    opponent_punt_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPuntReturnYards")
    """Total punt return yards the opponent teams in the season"""

    opponent_kick_returns: OptionalNullable[int] = Field(default=UNSET, alias="OpponentKickReturns")
    """Total kickoff returns by the opponent teams in the season"""

    opponent_kick_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentKickReturnYards")
    """Total kickoff return yards by the opponent teams in the season"""

    opponent_interception_returns: OptionalNullable[int] = Field(default=UNSET, alias="OpponentInterceptionReturns")
    """Total defensive interceptions by the opponent teams in the seasons"""

    opponent_interception_return_yards: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentInterceptionReturnYards"
    )
    """Total defensive interception return yards by the opponent teams in the seasons"""

    solo_tackles: OptionalNullable[int] = Field(default=UNSET, alias="SoloTackles")
    """Total defensive solo (unassisted) tackles by the team in the season"""

    assisted_tackles: OptionalNullable[int] = Field(default=UNSET, alias="AssistedTackles")
    """Total defensive assisted tackles by the team in the season"""

    sacks: OptionalNullable[int] = Field(default=UNSET, alias="Sacks")
    """Total defensive sacks by the team in the season"""

    sack_yards: OptionalNullable[int] = Field(default=UNSET, alias="SackYards")
    """Total defensive sack yards by the team in the season"""

    passes_defended: OptionalNullable[int] = Field(default=UNSET, alias="PassesDefended")
    """Total passes defended by the team's defense in the season"""

    fumbles_forced: OptionalNullable[int] = Field(default=UNSET, alias="FumblesForced")
    """Total fumbles forced on defense by the team in the season"""

    fumbles_recovered: OptionalNullable[int] = Field(default=UNSET, alias="FumblesRecovered")
    """Total defensive fumble recoveries by the team in the season"""

    fumble_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="FumbleReturnYards")
    """Total fumble return yards by the team in the season"""

    fumble_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="FumbleReturnTouchdowns")
    """Total fumble return touchdowns by the team in the season"""

    interception_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="InterceptionReturnTouchdowns")
    """Total defensive interception return touchdowns by the team in the season"""

    blocked_kicks: OptionalNullable[int] = Field(default=UNSET, alias="BlockedKicks")
    """Total blocked kicks by the team in the season. Note: BlockedKicks include Field Goals and Punts but NOT Extra
    Points"""

    punt_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="PuntReturnTouchdowns")
    """Total punt return touchdowns by the team in the season"""

    punt_return_long: OptionalNullable[int] = Field(default=UNSET, alias="PuntReturnLong")
    """The longest punt return by the team in the season"""

    kick_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="KickReturnTouchdowns")
    """Total kickoff return touchdowns by the team in the season"""

    kick_return_long: OptionalNullable[int] = Field(default=UNSET, alias="KickReturnLong")
    """Longest kick return by the team in the season"""

    blocked_kick_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="BlockedKickReturnYards")
    """Total blocked kick recovery return yards for the team in the season"""

    blocked_kick_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="BlockedKickReturnTouchdowns")
    """Total blocked kick recovery return touchdowns for the team in the season"""

    field_goal_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalReturnYards")
    """Total field goal return yards by the team in the season. Note: This field excludes blocked field goals"""

    field_goal_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalReturnTouchdowns")
    """Total field goal return touchdowns by the team in the season. Note: This field excludes blocked field goals"""

    punt_net_yards: OptionalNullable[int] = Field(default=UNSET, alias="PuntNetYards")
    """The net yards of the punts by the team in the season"""

    opponent_solo_tackles: OptionalNullable[int] = Field(default=UNSET, alias="OpponentSoloTackles")
    """Total defensive solo tackles by the opponent teams in the season"""

    opponent_assisted_tackles: OptionalNullable[int] = Field(default=UNSET, alias="OpponentAssistedTackles")
    """Total defensive assisted tackles by the opponent teams in the season"""

    opponent_sacks: OptionalNullable[int] = Field(default=UNSET, alias="OpponentSacks")
    """Total defensive sacks by the opponent teams in the season"""

    opponent_sack_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentSackYards")
    """Total defensive sack yards by the opponent teams in the season"""

    opponent_passes_defended: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPassesDefended")
    """Total passes defended by the opponent teams in the season"""

    opponent_fumbles_forced: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFumblesForced")
    """Total defensive fumbles forced by the opponent teams in the season"""

    opponent_fumbles_recovered: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFumblesRecovered")
    """Total defensive fumble recoveries by the opponent teams in the season"""

    opponent_fumble_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFumbleReturnYards")
    """Total defensive fumbles return yards by the opponent teams in the season"""

    opponent_fumble_return_touchdowns: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentFumbleReturnTouchdowns"
    )
    """Total defensive fumbles return touchdowns by the opponent teams in the season"""

    opponent_interception_return_touchdowns: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentInterceptionReturnTouchdowns"
    )
    """Total defensive interception touchdowns by the opponent teams in the seasons"""

    opponent_blocked_kicks: OptionalNullable[int] = Field(default=UNSET, alias="OpponentBlockedKicks")
    """Total blocked kicks against the opponent teams in the season"""

    opponent_punt_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPuntReturnTouchdowns")
    """Total punt return touchdowns the opponent teams in the season"""

    opponent_punt_return_long: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPuntReturnLong")
    """Longest punt return by the opponent teams in the season"""

    opponent_kick_return_touchdowns: OptionalNullable[int] = Field(default=UNSET, alias="OpponentKickReturnTouchdowns")
    """Total kickoff return touchdowns by the opponent teams in the season"""

    opponent_kick_return_long: OptionalNullable[int] = Field(default=UNSET, alias="OpponentKickReturnLong")
    """Longest kick return by the opponent teams in the season"""

    opponent_blocked_kick_return_yards: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentBlockedKickReturnYards"
    )
    """Total blocked kick return yards by the opponent teams in the season"""

    opponent_blocked_kick_return_touchdowns: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentBlockedKickReturnTouchdowns"
    )
    """Total blocked kick return touchdowns by the opponent teams in the season"""

    opponent_field_goal_return_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentFieldGoalReturnYards")
    """Total field goal return yards by the opponent teams in the season. Note: Excludes blocked field goals (only for
    straight misses that are returned)"""

    opponent_field_goal_return_touchdowns: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentFieldGoalReturnTouchdowns"
    )
    """Total field goal return touchdowns by the opponent teams in the season. Note: Excludes blocked field goals (only
    for straight misses that are returned)"""

    opponent_punt_net_yards: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPuntNetYards")
    """Total net punt yards by the opponent team in the season"""

    team_name: OptionalNullable[str] = Field(default=UNSET, alias="TeamName")
    """The full name of the team (e.g. New England Patriots; Los Angeles Chargers)"""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The total number of games played by the team in the season"""

    passing_dropbacks: OptionalNullable[int] = Field(default=UNSET, alias="PassingDropbacks")
    """Total number of times the team dropped back to pass in the season"""

    opponent_passing_dropbacks: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPassingDropbacks")
    """Total passing dropbacks by the opponent teams in the season"""

    team_season_id: Optional[int] = Field(default=UNSET, alias="TeamSeasonID")
    """The unique identifier for this TeamSeason record (subject to change; although it very rarely does). For a static
    ID; use a combination of SeasonType; Season and Team."""

    point_differential: OptionalNullable[int] = Field(default=UNSET, alias="PointDifferential")
    """The team's total point differential in the season"""

    passing_interception_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="PassingInterceptionPercentage"
    )
    """The team's percentage of passes that were intercepted by the defense in the season. Note: This refers to the
    offensive team's passes that were intercepted"""

    punt_return_average: OptionalNullable[float] = Field(default=UNSET, alias="PuntReturnAverage")
    """The average punt return yardage for the team in the season"""

    kick_return_average: OptionalNullable[float] = Field(default=UNSET, alias="KickReturnAverage")
    """Average kick return yard by the team in the season"""

    extra_point_percentage: OptionalNullable[float] = Field(default=UNSET, alias="ExtraPointPercentage")
    """Team's percentage of extra points made in the season"""

    field_goal_percentage: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalPercentage")
    """Team's percentage of field goals made in the season"""

    opponent_passing_interception_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="OpponentPassingInterceptionPercentage"
    )
    """Percentage of passes that were intercepted against the opponent teams in the season"""

    opponent_punt_return_average: OptionalNullable[float] = Field(default=UNSET, alias="OpponentPuntReturnAverage")
    """Punt return average of the opponent team in the seasons"""

    opponent_kick_return_average: OptionalNullable[float] = Field(default=UNSET, alias="OpponentKickReturnAverage")
    """Kick return average of the opponent teams in the season"""

    opponent_extra_point_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="OpponentExtraPointPercentage"
    )
    """Total extra point percentage by the opponent teams in the season"""

    opponent_field_goal_percentage: OptionalNullable[float] = Field(default=UNSET, alias="OpponentFieldGoalPercentage")
    """Total field goal percentage by the opponent teams in the season"""

    penalty_yard_differential: OptionalNullable[int] = Field(default=UNSET, alias="PenaltyYardDifferential")
    """The team's penalty yard differential in the season"""

    punt_return_yard_differential: OptionalNullable[int] = Field(default=UNSET, alias="PuntReturnYardDifferential")
    """Punt return yard differential for the team in the season"""

    kick_return_yard_differential: OptionalNullable[int] = Field(default=UNSET, alias="KickReturnYardDifferential")
    """Total kick return yard differential by the team in the season"""

    two_point_conversion_returns: OptionalNullable[int] = Field(default=UNSET, alias="TwoPointConversionReturns")
    """Total successful two point conversion returns by the team in the season"""

    opponent_two_point_conversion_returns: OptionalNullable[int] = Field(
        default=UNSET, alias="OpponentTwoPointConversionReturns"
    )
    """Total two point attempt returns converted by the defense for the opponent teams in the season"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    team_stat_id: Optional[int] = Field(default=UNSET, alias="TeamStatID")
    """Unique ID of this TeamStatID record."""


class TeamSeason4Dict(TypedDict):
    season_type: NotRequired[int]
    season: NotRequired[int]
    team: NotRequired[str | None]
    score: NotRequired[int]
    opponent_score: NotRequired[int]
    total_score: NotRequired[int]
    temperature: NotRequired[int | None]
    humidity: NotRequired[int | None]
    wind_speed: NotRequired[int | None]
    over_under: NotRequired[float | None]
    point_spread: NotRequired[float | None]
    score_quarter1: NotRequired[int | None]
    score_quarter2: NotRequired[int | None]
    score_quarter3: NotRequired[int | None]
    score_quarter4: NotRequired[int | None]
    score_overtime: NotRequired[int]
    time_of_possession: NotRequired[str | None]
    first_downs: NotRequired[int | None]
    first_downs_by_rushing: NotRequired[int | None]
    first_downs_by_passing: NotRequired[int | None]
    first_downs_by_penalty: NotRequired[int | None]
    offensive_plays: NotRequired[int]
    offensive_yards: NotRequired[int]
    offensive_yards_per_play: NotRequired[float]
    touchdowns: NotRequired[int | None]
    rushing_attempts: NotRequired[int | None]
    rushing_yards: NotRequired[int | None]
    rushing_yards_per_attempt: NotRequired[float]
    rushing_touchdowns: NotRequired[int | None]
    passing_attempts: NotRequired[int | None]
    passing_completions: NotRequired[int | None]
    passing_yards: NotRequired[int | None]
    passing_touchdowns: NotRequired[int | None]
    passing_interceptions: NotRequired[int | None]
    passing_yards_per_attempt: NotRequired[float]
    passing_yards_per_completion: NotRequired[float]
    completion_percentage: NotRequired[float]
    passer_rating: NotRequired[float | None]
    third_down_attempts: NotRequired[int | None]
    third_down_conversions: NotRequired[int | None]
    third_down_percentage: NotRequired[float | None]
    fourth_down_attempts: NotRequired[int | None]
    fourth_down_conversions: NotRequired[int | None]
    fourth_down_percentage: NotRequired[float | None]
    red_zone_attempts: NotRequired[int | None]
    red_zone_conversions: NotRequired[int | None]
    goal_to_go_attempts: NotRequired[int | None]
    goal_to_go_conversions: NotRequired[int | None]
    return_yards: NotRequired[int | None]
    penalties: NotRequired[int | None]
    penalty_yards: NotRequired[int | None]
    fumbles: NotRequired[int | None]
    fumbles_lost: NotRequired[int | None]
    times_sacked: NotRequired[int | None]
    times_sacked_yards: NotRequired[int | None]
    quarterback_hits: NotRequired[int | None]
    tackles_for_loss: NotRequired[int | None]
    safeties: NotRequired[int | None]
    punts: NotRequired[int | None]
    punt_yards: NotRequired[int | None]
    punt_average: NotRequired[float]
    giveaways: NotRequired[int]
    takeaways: NotRequired[int]
    turnover_differential: NotRequired[int]
    opponent_score_quarter1: NotRequired[int | None]
    opponent_score_quarter2: NotRequired[int | None]
    opponent_score_quarter3: NotRequired[int | None]
    opponent_score_quarter4: NotRequired[int | None]
    opponent_score_overtime: NotRequired[int]
    opponent_time_of_possession: NotRequired[str | None]
    opponent_first_downs: NotRequired[int | None]
    opponent_first_downs_by_rushing: NotRequired[int | None]
    opponent_first_downs_by_passing: NotRequired[int | None]
    opponent_first_downs_by_penalty: NotRequired[int | None]
    opponent_offensive_plays: NotRequired[int]
    opponent_offensive_yards: NotRequired[int]
    opponent_offensive_yards_per_play: NotRequired[float]
    opponent_touchdowns: NotRequired[int | None]
    opponent_rushing_attempts: NotRequired[int | None]
    opponent_rushing_yards: NotRequired[int | None]
    opponent_rushing_yards_per_attempt: NotRequired[float]
    opponent_rushing_touchdowns: NotRequired[int | None]
    opponent_passing_attempts: NotRequired[int | None]
    opponent_passing_completions: NotRequired[int | None]
    opponent_passing_yards: NotRequired[int | None]
    opponent_passing_touchdowns: NotRequired[int | None]
    opponent_passing_interceptions: NotRequired[int | None]
    opponent_passing_yards_per_attempt: NotRequired[float]
    opponent_passing_yards_per_completion: NotRequired[float]
    opponent_completion_percentage: NotRequired[float]
    opponent_passer_rating: NotRequired[float | None]
    opponent_third_down_attempts: NotRequired[int | None]
    opponent_third_down_conversions: NotRequired[int | None]
    opponent_third_down_percentage: NotRequired[float | None]
    opponent_fourth_down_attempts: NotRequired[int | None]
    opponent_fourth_down_conversions: NotRequired[int | None]
    opponent_fourth_down_percentage: NotRequired[float | None]
    opponent_red_zone_attempts: NotRequired[int | None]
    opponent_red_zone_conversions: NotRequired[int | None]
    opponent_goal_to_go_attempts: NotRequired[int | None]
    opponent_goal_to_go_conversions: NotRequired[int | None]
    opponent_return_yards: NotRequired[int | None]
    opponent_penalties: NotRequired[int | None]
    opponent_penalty_yards: NotRequired[int | None]
    opponent_fumbles: NotRequired[int | None]
    opponent_fumbles_lost: NotRequired[int | None]
    opponent_times_sacked: NotRequired[int | None]
    opponent_times_sacked_yards: NotRequired[int | None]
    opponent_quarterback_hits: NotRequired[int | None]
    opponent_tackles_for_loss: NotRequired[int | None]
    opponent_safeties: NotRequired[int | None]
    opponent_punts: NotRequired[int | None]
    opponent_punt_yards: NotRequired[int | None]
    opponent_punt_average: NotRequired[float]
    opponent_giveaways: NotRequired[int]
    opponent_takeaways: NotRequired[int]
    opponent_turnover_differential: NotRequired[int]
    red_zone_percentage: NotRequired[float | None]
    goal_to_go_percentage: NotRequired[float | None]
    quarterback_hits_differential: NotRequired[int | None]
    tackles_for_loss_differential: NotRequired[int | None]
    quarterback_sacks_differential: NotRequired[int]
    tackles_for_loss_percentage: NotRequired[float | None]
    quarterback_hits_percentage: NotRequired[float | None]
    times_sacked_percentage: NotRequired[float]
    opponent_red_zone_percentage: NotRequired[float | None]
    opponent_goal_to_go_percentage: NotRequired[float | None]
    opponent_quarterback_hits_differential: NotRequired[int | None]
    opponent_tackles_for_loss_differential: NotRequired[int | None]
    opponent_quarterback_sacks_differential: NotRequired[int | None]
    opponent_tackles_for_loss_percentage: NotRequired[float | None]
    opponent_quarterback_hits_percentage: NotRequired[float | None]
    opponent_times_sacked_percentage: NotRequired[float]
    kickoffs: NotRequired[int | None]
    kickoffs_in_end_zone: NotRequired[int | None]
    kickoff_touchbacks: NotRequired[int | None]
    punts_had_blocked: NotRequired[int | None]
    punt_net_average: NotRequired[float | None]
    extra_point_kicking_attempts: NotRequired[int | None]
    extra_point_kicking_conversions: NotRequired[int | None]
    extra_points_had_blocked: NotRequired[int | None]
    extra_point_passing_attempts: NotRequired[int | None]
    extra_point_passing_conversions: NotRequired[int | None]
    extra_point_rushing_attempts: NotRequired[int | None]
    extra_point_rushing_conversions: NotRequired[int | None]
    field_goal_attempts: NotRequired[int | None]
    field_goals_made: NotRequired[int | None]
    field_goals_had_blocked: NotRequired[int | None]
    punt_returns: NotRequired[int | None]
    punt_return_yards: NotRequired[int | None]
    kick_returns: NotRequired[int | None]
    kick_return_yards: NotRequired[int | None]
    interception_returns: NotRequired[int | None]
    interception_return_yards: NotRequired[int | None]
    opponent_kickoffs: NotRequired[int | None]
    opponent_kickoffs_in_end_zone: NotRequired[int | None]
    opponent_kickoff_touchbacks: NotRequired[int | None]
    opponent_punts_had_blocked: NotRequired[int | None]
    opponent_punt_net_average: NotRequired[float | None]
    opponent_extra_point_kicking_attempts: NotRequired[int | None]
    opponent_extra_point_kicking_conversions: NotRequired[int | None]
    opponent_extra_points_had_blocked: NotRequired[int | None]
    opponent_extra_point_passing_attempts: NotRequired[int | None]
    opponent_extra_point_passing_conversions: NotRequired[int | None]
    opponent_extra_point_rushing_attempts: NotRequired[int | None]
    opponent_extra_point_rushing_conversions: NotRequired[int | None]
    opponent_field_goal_attempts: NotRequired[int | None]
    opponent_field_goals_made: NotRequired[int | None]
    opponent_field_goals_had_blocked: NotRequired[int | None]
    opponent_punt_returns: NotRequired[int | None]
    opponent_punt_return_yards: NotRequired[int | None]
    opponent_kick_returns: NotRequired[int | None]
    opponent_kick_return_yards: NotRequired[int | None]
    opponent_interception_returns: NotRequired[int | None]
    opponent_interception_return_yards: NotRequired[int | None]
    solo_tackles: NotRequired[int | None]
    assisted_tackles: NotRequired[int | None]
    sacks: NotRequired[int | None]
    sack_yards: NotRequired[int | None]
    passes_defended: NotRequired[int | None]
    fumbles_forced: NotRequired[int | None]
    fumbles_recovered: NotRequired[int | None]
    fumble_return_yards: NotRequired[int | None]
    fumble_return_touchdowns: NotRequired[int | None]
    interception_return_touchdowns: NotRequired[int | None]
    blocked_kicks: NotRequired[int | None]
    punt_return_touchdowns: NotRequired[int | None]
    punt_return_long: NotRequired[int | None]
    kick_return_touchdowns: NotRequired[int | None]
    kick_return_long: NotRequired[int | None]
    blocked_kick_return_yards: NotRequired[int | None]
    blocked_kick_return_touchdowns: NotRequired[int | None]
    field_goal_return_yards: NotRequired[int | None]
    field_goal_return_touchdowns: NotRequired[int | None]
    punt_net_yards: NotRequired[int | None]
    opponent_solo_tackles: NotRequired[int | None]
    opponent_assisted_tackles: NotRequired[int | None]
    opponent_sacks: NotRequired[int | None]
    opponent_sack_yards: NotRequired[int | None]
    opponent_passes_defended: NotRequired[int | None]
    opponent_fumbles_forced: NotRequired[int | None]
    opponent_fumbles_recovered: NotRequired[int | None]
    opponent_fumble_return_yards: NotRequired[int | None]
    opponent_fumble_return_touchdowns: NotRequired[int | None]
    opponent_interception_return_touchdowns: NotRequired[int | None]
    opponent_blocked_kicks: NotRequired[int | None]
    opponent_punt_return_touchdowns: NotRequired[int | None]
    opponent_punt_return_long: NotRequired[int | None]
    opponent_kick_return_touchdowns: NotRequired[int | None]
    opponent_kick_return_long: NotRequired[int | None]
    opponent_blocked_kick_return_yards: NotRequired[int | None]
    opponent_blocked_kick_return_touchdowns: NotRequired[int | None]
    opponent_field_goal_return_yards: NotRequired[int | None]
    opponent_field_goal_return_touchdowns: NotRequired[int | None]
    opponent_punt_net_yards: NotRequired[int | None]
    team_name: NotRequired[str | None]
    games: NotRequired[int | None]
    passing_dropbacks: NotRequired[int | None]
    opponent_passing_dropbacks: NotRequired[int | None]
    team_season_id: NotRequired[int]
    point_differential: NotRequired[int | None]
    passing_interception_percentage: NotRequired[float | None]
    punt_return_average: NotRequired[float | None]
    kick_return_average: NotRequired[float | None]
    extra_point_percentage: NotRequired[float | None]
    field_goal_percentage: NotRequired[float | None]
    opponent_passing_interception_percentage: NotRequired[float | None]
    opponent_punt_return_average: NotRequired[float | None]
    opponent_kick_return_average: NotRequired[float | None]
    opponent_extra_point_percentage: NotRequired[float | None]
    opponent_field_goal_percentage: NotRequired[float | None]
    penalty_yard_differential: NotRequired[int | None]
    punt_return_yard_differential: NotRequired[int | None]
    kick_return_yard_differential: NotRequired[int | None]
    two_point_conversion_returns: NotRequired[int | None]
    opponent_two_point_conversion_returns: NotRequired[int | None]
    team_id: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    team_stat_id: NotRequired[int]
