from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .scoring_detail import ScoringDetail, ScoringDetailDict


class PlayerSeasonThirdDown(SdkBaseModel):
    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this player corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season for which these totals apply"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on. Note: If this player is a free agent; this field is
    NULL"""

    number: Optional[int] = Field(default=UNSET, alias="Number")
    """Player's jersey number"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The primary position of the player. Possible Values: C; CB; DB; DE; DL; DT; FB; FS; G; ILB; K; KR; LB; LS; NT;
    OL; OLB; OT; P; QB; RB; S; SS; T; TE; WR"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The category of the player's position (OFF; DEF; ST)"""

    activated: Optional[int] = Field(default=UNSET, alias="Activated")
    """The total number of games that the player was active for in the season"""

    played: Optional[int] = Field(default=UNSET, alias="Played")
    """The total number of games played by the the player in the season"""

    started: Optional[int] = Field(default=UNSET, alias="Started")
    """Total games started (on offense or defense) by the player in the season"""

    passing_attempts: Optional[float] = Field(default=UNSET, alias="PassingAttempts")
    """Total passes thrown by the player in the season"""

    passing_completions: Optional[float] = Field(default=UNSET, alias="PassingCompletions")
    """Total passes completed by the player in the season"""

    passing_yards: Optional[float] = Field(default=UNSET, alias="PassingYards")
    """Total passing yards by the player in the season"""

    passing_completion_percentage: Optional[float] = Field(default=UNSET, alias="PassingCompletionPercentage")
    """The percentage of passes completed by the player in the season"""

    passing_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="PassingYardsPerAttempt")
    """Total average passing yards per attempt by the player in the season"""

    passing_yards_per_completion: Optional[float] = Field(default=UNSET, alias="PassingYardsPerCompletion")
    """Total average passing yards per completion by the player in the season"""

    passing_touchdowns: Optional[float] = Field(default=UNSET, alias="PassingTouchdowns")
    """Total passing touchdowns by the player in the season"""

    passing_interceptions: Optional[float] = Field(default=UNSET, alias="PassingInterceptions")
    """Total interceptions thrown by the player in the season"""

    passing_rating: Optional[float] = Field(default=UNSET, alias="PassingRating")
    """The passer rating of the player in the season"""

    passing_long: Optional[float] = Field(default=UNSET, alias="PassingLong")
    """Total yards of longest completion by the player in the season"""

    passing_sacks: Optional[float] = Field(default=UNSET, alias="PassingSacks")
    """The total number of times the player was sacked in the season"""

    passing_sack_yards: Optional[float] = Field(default=UNSET, alias="PassingSackYards")
    """Total yards lost by the player in the season as a result of being sacked"""

    rushing_attempts: Optional[float] = Field(default=UNSET, alias="RushingAttempts")
    """Total rushing attempts by the player in the season"""

    rushing_yards: Optional[float] = Field(default=UNSET, alias="RushingYards")
    """Total rushing yards by the player in the season"""

    rushing_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="RushingYardsPerAttempt")
    """Total rushing yards per attempt by the player in the season"""

    rushing_touchdowns: Optional[float] = Field(default=UNSET, alias="RushingTouchdowns")
    """Total rushing touchdowns by the player in the season"""

    rushing_long: Optional[float] = Field(default=UNSET, alias="RushingLong")
    """The longest rush by the player in the season"""

    receiving_targets: OptionalNullable[float] = Field(default=UNSET, alias="ReceivingTargets")
    """Total receiving targets by the player in the season"""

    receptions: Optional[float] = Field(default=UNSET, alias="Receptions")
    """Total receptions by the player in the season"""

    receiving_yards: Optional[float] = Field(default=UNSET, alias="ReceivingYards")
    """Total receiving yards by the player in the season"""

    receiving_yards_per_reception: Optional[float] = Field(default=UNSET, alias="ReceivingYardsPerReception")
    """Average receiving yards per reception by the player in the season"""

    receiving_touchdowns: Optional[float] = Field(default=UNSET, alias="ReceivingTouchdowns")
    """Total receiving touchdowns by the player in the season"""

    receiving_long: Optional[float] = Field(default=UNSET, alias="ReceivingLong")
    """The longest reception by the player in the season"""

    fumbles: Optional[float] = Field(default=UNSET, alias="Fumbles")
    """Total fumbles by the player in the season"""

    fumbles_lost: OptionalNullable[float] = Field(default=UNSET, alias="FumblesLost")
    """Total fumbles lost by the player in the season"""

    punt_returns: Optional[float] = Field(default=UNSET, alias="PuntReturns")
    """Total punt returns by the player in the season"""

    punt_return_yards: Optional[float] = Field(default=UNSET, alias="PuntReturnYards")
    """Total punt return yards by the player in the season"""

    punt_return_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="PuntReturnYardsPerAttempt")
    """Total average yards gained per punt return by the player in the season"""

    punt_return_touchdowns: Optional[float] = Field(default=UNSET, alias="PuntReturnTouchdowns")
    """Total punt return touchdowns by the player in the season"""

    punt_return_long: Optional[float] = Field(default=UNSET, alias="PuntReturnLong")
    """The longest punt return by the player in the season"""

    kick_returns: Optional[float] = Field(default=UNSET, alias="KickReturns")
    """Total kickoff returns by the player in the season"""

    kick_return_yards: Optional[float] = Field(default=UNSET, alias="KickReturnYards")
    """Total kickoff return yards by the player in the season"""

    kick_return_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="KickReturnYardsPerAttempt")
    """Average yards gained per kick return by the player in the season"""

    kick_return_touchdowns: Optional[float] = Field(default=UNSET, alias="KickReturnTouchdowns")
    """Total kickoff return touchdowns by the player in the season"""

    kick_return_long: Optional[float] = Field(default=UNSET, alias="KickReturnLong")
    """Longest kick return by the player in the season"""

    solo_tackles: Optional[float] = Field(default=UNSET, alias="SoloTackles")
    """Total defensive solo (unassisted) tackles by the player in the season"""

    assisted_tackles: Optional[float] = Field(default=UNSET, alias="AssistedTackles")
    """Total defensive assisted tackles by the player in the season"""

    tackles_for_loss: OptionalNullable[float] = Field(default=UNSET, alias="TacklesForLoss")
    """Total tackles for loss by the player in the season. Note: these are tackles behind the line of scrimmage for loss
    of yards (including sacks)"""

    sacks: Optional[float] = Field(default=UNSET, alias="Sacks")
    """Total defensive sacks by the player in the season"""

    sack_yards: Optional[float] = Field(default=UNSET, alias="SackYards")
    """Total defensive safeties scored by the player in the season"""

    quarterback_hits: OptionalNullable[float] = Field(default=UNSET, alias="QuarterbackHits")
    """Total quarterback hits by the player in the season. Note: This is a defensive stat that includes sacks"""

    passes_defended: Optional[float] = Field(default=UNSET, alias="PassesDefended")
    """Total passes defended by the player in the season"""

    fumbles_forced: Optional[float] = Field(default=UNSET, alias="FumblesForced")
    """Total fumbles forced on defense by the player in the season"""

    fumbles_recovered: Optional[float] = Field(default=UNSET, alias="FumblesRecovered")
    """Total defensive fumble recoveries by the player in the season"""

    fumble_return_yards: Optional[float] = Field(default=UNSET, alias="FumbleReturnYards")
    """Total fumble return yards by the player in the season"""

    fumble_return_touchdowns: Optional[float] = Field(default=UNSET, alias="FumbleReturnTouchdowns")
    """Total fumble return touchdowns by the player in the season"""

    interceptions: Optional[float] = Field(default=UNSET, alias="Interceptions")
    """Total defensive interceptions by the player in the season"""

    interception_return_yards: Optional[float] = Field(default=UNSET, alias="InterceptionReturnYards")
    """Total defensive interception return yards by the player in the season"""

    interception_return_touchdowns: Optional[float] = Field(default=UNSET, alias="InterceptionReturnTouchdowns")
    """Total defensive interception return touchdowns by the player in the season"""

    blocked_kicks: Optional[float] = Field(default=UNSET, alias="BlockedKicks")
    """Total blocked kicks by the player in the season. Note: BlockedKicks include Field Goals and Punts but NOT Extra
    Points"""

    special_teams_solo_tackles: Optional[float] = Field(default=UNSET, alias="SpecialTeamsSoloTackles")
    """This field is deprecated"""

    special_teams_assisted_tackles: Optional[float] = Field(default=UNSET, alias="SpecialTeamsAssistedTackles")
    """This field is deprecated"""

    misc_solo_tackles: Optional[float] = Field(default=UNSET, alias="MiscSoloTackles")
    """This field is deprecated"""

    misc_assisted_tackles: Optional[float] = Field(default=UNSET, alias="MiscAssistedTackles")
    """This field is deprecated"""

    punts: Optional[float] = Field(default=UNSET, alias="Punts")
    """Total number of punts by the player in the season"""

    punt_yards: Optional[float] = Field(default=UNSET, alias="PuntYards")
    """Total punt yards by the player in the season"""

    punt_average: Optional[float] = Field(default=UNSET, alias="PuntAverage")
    """The average number of yards per punt by the player in the season"""

    field_goals_attempted: Optional[float] = Field(default=UNSET, alias="FieldGoalsAttempted")
    """Total field goals attempted by the player in the season"""

    field_goals_made: Optional[float] = Field(default=UNSET, alias="FieldGoalsMade")
    """Total field goals made by the player in season"""

    field_goals_longest_made: Optional[float] = Field(default=UNSET, alias="FieldGoalsLongestMade")
    """Longest field goal made by the player in the season"""

    extra_points_made: Optional[float] = Field(default=UNSET, alias="ExtraPointsMade")
    """Total extra points made by the player in the season"""

    two_point_conversion_passes: Optional[float] = Field(default=UNSET, alias="TwoPointConversionPasses")
    """Total successful two point conversion passes by the player in the season"""

    two_point_conversion_runs: Optional[float] = Field(default=UNSET, alias="TwoPointConversionRuns")
    """Total successful two point conversion rushes by the player in the season"""

    two_point_conversion_receptions: Optional[float] = Field(default=UNSET, alias="TwoPointConversionReceptions")
    """Total successful two point conversion receptions by the player in the season"""

    fantasy_points: Optional[float] = Field(default=UNSET, alias="FantasyPoints")
    """Fantasy points scored based on basic fantasy scoring system by the player in the season"""

    fantasy_points_ppr: Optional[float] = Field(default=UNSET, alias="FantasyPointsPPR")
    """Fantasy points scored based on basic PPR fantasy scoring system by the player in the season"""

    reception_percentage: Optional[float] = Field(default=UNSET, alias="ReceptionPercentage")
    """Total percentage of receiving targets that were receptions by the player in the season"""

    receiving_yards_per_target: Optional[float] = Field(default=UNSET, alias="ReceivingYardsPerTarget")
    """Average receiving yards per target by the player in the season"""

    tackles: Optional[float] = Field(default=UNSET, alias="Tackles")
    """Total tackles (solo & assisted) by the player in the season"""

    offensive_touchdowns: Optional[float] = Field(default=UNSET, alias="OffensiveTouchdowns")
    """Total offensive touchdowns scored by the player in the season"""

    defensive_touchdowns: Optional[float] = Field(default=UNSET, alias="DefensiveTouchdowns")
    """Total defensive touchdowns scored by the player in the season"""

    special_teams_touchdowns: Optional[float] = Field(default=UNSET, alias="SpecialTeamsTouchdowns")
    """Total special teams touchdowns scored by the player in the season"""

    touchdowns: Optional[float] = Field(default=UNSET, alias="Touchdowns")
    """Total touchdowns scored by the player in the season"""

    fantasy_position: OptionalNullable[str] = Field(default=UNSET, alias="FantasyPosition")
    """The player's fantasy football position. Possible values: QB, RB, WR, TE, DL, LB, DB, K, P, OL"""

    field_goal_percentage: Optional[float] = Field(default=UNSET, alias="FieldGoalPercentage")
    """Total field goal attempts made by the player in the season"""

    player_season_id: Optional[int] = Field(default=UNSET, alias="PlayerSeasonID")
    """Unique ID of PlayerSeason record (subject to change, although it very rarely does). For a static ID, use a
    combination of SeasonType, Season and PlayerID."""

    fumbles_own_recoveries: OptionalNullable[float] = Field(default=UNSET, alias="FumblesOwnRecoveries")
    """Total own fumble recoveries by the player in the season. Note: this fumble doesn't result in a turnover - the
    fumbling team recovers the fumble"""

    fumbles_out_of_bounds: OptionalNullable[float] = Field(default=UNSET, alias="FumblesOutOfBounds")
    """This field is deprecated"""

    kick_return_fair_catches: OptionalNullable[float] = Field(default=UNSET, alias="KickReturnFairCatches")
    """This field is deprecated"""

    punt_return_fair_catches: OptionalNullable[float] = Field(default=UNSET, alias="PuntReturnFairCatches")
    """This field is deprecated."""

    punt_touchbacks: OptionalNullable[float] = Field(default=UNSET, alias="PuntTouchbacks")
    """Total punts that resulted in touchbacks by the player in the season"""

    punt_inside20: OptionalNullable[float] = Field(default=UNSET, alias="PuntInside20")
    """Total punts downed inside the 20 yard line by the player in the season"""

    punt_net_average: OptionalNullable[float] = Field(default=UNSET, alias="PuntNetAverage")
    """The average net yards per punt by the player in the season"""

    extra_points_attempted: OptionalNullable[float] = Field(default=UNSET, alias="ExtraPointsAttempted")
    """Total extra point kicks attempted by the player in the season"""

    blocked_kick_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="BlockedKickReturnTouchdowns")
    """Total blocked kick recovery return touchdowns for the player in the season"""

    field_goal_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalReturnTouchdowns")
    """Total field goal return touchdowns by the player in the season. Note: This field excludes blocked field goals"""

    safeties: OptionalNullable[float] = Field(default=UNSET, alias="Safeties")
    """Defensive safeties (sacks in end zone, solo tackles in end zone, blocked kicks that went out of bounds in the end
    zone)"""

    field_goals_had_blocked: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsHadBlocked")
    """Total field goals by the player that were blocked in the season"""

    punts_had_blocked: OptionalNullable[float] = Field(default=UNSET, alias="PuntsHadBlocked")
    """Total punts by the player that were blocked in the season"""

    extra_points_had_blocked: OptionalNullable[float] = Field(default=UNSET, alias="ExtraPointsHadBlocked")
    """Total extra point kick attempts by the player that were blocked in the season"""

    punt_long: OptionalNullable[float] = Field(default=UNSET, alias="PuntLong")
    """The longest punt by the player in the season"""

    blocked_kick_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="BlockedKickReturnYards")
    """Total blocked kick recovery return yards for the player in the season"""

    field_goal_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalReturnYards")
    """Total field goal return yards by the player in the season. Note: This field excludes blocked field goals"""

    punt_net_yards: OptionalNullable[float] = Field(default=UNSET, alias="PuntNetYards")
    """The net yards of the punts by the player in the season"""

    special_teams_fumbles_forced: OptionalNullable[float] = Field(default=UNSET, alias="SpecialTeamsFumblesForced")
    """This field is deprecated"""

    special_teams_fumbles_recovered: OptionalNullable[float] = Field(
        default=UNSET, alias="SpecialTeamsFumblesRecovered"
    )
    """This field is deprecated"""

    misc_fumbles_forced: OptionalNullable[float] = Field(default=UNSET, alias="MiscFumblesForced")
    """This field is deprecated"""

    misc_fumbles_recovered: OptionalNullable[float] = Field(default=UNSET, alias="MiscFumblesRecovered")
    """This field is deprecated"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The first initial and last name of the player (J. Doe)"""

    safeties_allowed: OptionalNullable[float] = Field(default=UNSET, alias="SafetiesAllowed")
    """This field is deprecated"""

    temperature: OptionalNullable[int] = Field(default=UNSET, alias="Temperature")
    """Temperature at game start (Fahrenheit)"""

    humidity: OptionalNullable[int] = Field(default=UNSET, alias="Humidity")
    """The humidity percentage at the start of the game"""

    wind_speed: OptionalNullable[int] = Field(default=UNSET, alias="WindSpeed")
    """The wind speed at the start of the game (in MPH)"""

    offensive_snaps_played: OptionalNullable[int] = Field(default=UNSET, alias="OffensiveSnapsPlayed")
    """Total snaps this player played on offensive in the season. Note: Snap counts are available the morning after the
    game."""

    defensive_snaps_played: OptionalNullable[int] = Field(default=UNSET, alias="DefensiveSnapsPlayed")
    """Total snaps this player played on defense in the season. Note: Snap counts are available the morning after the
    game."""

    special_teams_snaps_played: OptionalNullable[int] = Field(default=UNSET, alias="SpecialTeamsSnapsPlayed")
    """Total snaps this player played on special teams in the season. Note: Snap counts are available the morning after
    the game."""

    offensive_team_snaps: OptionalNullable[int] = Field(default=UNSET, alias="OffensiveTeamSnaps")
    """Total offensive snaps this player's team played in the season. Note: Snap counts are available the morning after
    the game."""

    defensive_team_snaps: OptionalNullable[int] = Field(default=UNSET, alias="DefensiveTeamSnaps")
    """Total defensive snaps this player's team played in the season. Note: Snap counts are available the morning after
    the game."""

    special_teams_team_snaps: OptionalNullable[int] = Field(default=UNSET, alias="SpecialTeamsTeamSnaps")
    """Total special teams snaps this player's team played in the season. Note: Snap counts are available the morning
    after the game."""

    auction_value: OptionalNullable[float] = Field(default=UNSET, alias="AuctionValue")
    """Player's dollar value in a $200 salary cap auction draft."""

    auction_value_ppr: OptionalNullable[float] = Field(default=UNSET, alias="AuctionValuePPR")
    """Player's dollar value in a $200 salary cap PPR auction draft."""

    two_point_conversion_returns: OptionalNullable[float] = Field(default=UNSET, alias="TwoPointConversionReturns")
    """Total successful two point conversion returns by the player in the season"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Fantasy points based on FanDuel's scoring system by the player in the season"""

    field_goals_made0to19: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade0to19")
    """Total field goals of 0 to 19 yards made by the player in season"""

    field_goals_made20to29: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade20to29")
    """Total field goals of 20 to 29 yards made by the player in season"""

    field_goals_made30to39: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade30to39")
    """Total field goals of 30 to 39 yards made by the player in season"""

    field_goals_made40to49: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade40to49")
    """Total field goals of 40 to 49 yards made by the player in season"""

    field_goals_made50_plus: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade50Plus")
    """Total field goals of 50+ yards made by the player in season"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Fantasy points based on DraftKings' scoring system by the player in the season"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Fantasy points based on Yahoo's daily fantasy scoring system by the player in the season"""

    average_draft_position: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPosition")
    """The average draft position of the player in re-draft leagues"""

    average_draft_position_ppr: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPositionPPR")
    """The average draft position of this player in Points Per Reception (PPR) leagues."""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that the player is on. Note: If the player is a free agent; this field is NULL"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    fantasy_points_fantasy_draft: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFantasyDraft")
    """Fantasy points based on FantasyDraft's scoring system by the player in the season"""

    scoring_details: Optional[list[ScoringDetail]] = Field(default=UNSET, alias="ScoringDetails")
    """The details of the scoring plays this player recorded in the season"""

    average_draft_position_rookie: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPositionRookie")
    """The average draft position of this rookie in Points Per Reception (PPR) leagues."""

    average_draft_position_dynasty: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPositionDynasty")
    """The average draft position of this player in dynasty drafts leagues"""

    average_draft_position2_qb: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPosition2QB")
    """The average draft position of this player in 2 Quarterback leagues"""

    offensive_fumble_recovery_touchdowns: OptionalNullable[int] = Field(
        default=UNSET, alias="OffensiveFumbleRecoveryTouchdowns"
    )
    """This field is deprecated"""


class PlayerSeasonThirdDownDict(TypedDict):
    player_id: NotRequired[int | None]
    season_type: NotRequired[int]
    season: NotRequired[int]
    team: NotRequired[str | None]
    number: NotRequired[int]
    name: NotRequired[str | None]
    position: NotRequired[str | None]
    position_category: NotRequired[str | None]
    activated: NotRequired[int]
    played: NotRequired[int]
    started: NotRequired[int]
    passing_attempts: NotRequired[float]
    passing_completions: NotRequired[float]
    passing_yards: NotRequired[float]
    passing_completion_percentage: NotRequired[float]
    passing_yards_per_attempt: NotRequired[float]
    passing_yards_per_completion: NotRequired[float]
    passing_touchdowns: NotRequired[float]
    passing_interceptions: NotRequired[float]
    passing_rating: NotRequired[float]
    passing_long: NotRequired[float]
    passing_sacks: NotRequired[float]
    passing_sack_yards: NotRequired[float]
    rushing_attempts: NotRequired[float]
    rushing_yards: NotRequired[float]
    rushing_yards_per_attempt: NotRequired[float]
    rushing_touchdowns: NotRequired[float]
    rushing_long: NotRequired[float]
    receiving_targets: NotRequired[float | None]
    receptions: NotRequired[float]
    receiving_yards: NotRequired[float]
    receiving_yards_per_reception: NotRequired[float]
    receiving_touchdowns: NotRequired[float]
    receiving_long: NotRequired[float]
    fumbles: NotRequired[float]
    fumbles_lost: NotRequired[float | None]
    punt_returns: NotRequired[float]
    punt_return_yards: NotRequired[float]
    punt_return_yards_per_attempt: NotRequired[float]
    punt_return_touchdowns: NotRequired[float]
    punt_return_long: NotRequired[float]
    kick_returns: NotRequired[float]
    kick_return_yards: NotRequired[float]
    kick_return_yards_per_attempt: NotRequired[float]
    kick_return_touchdowns: NotRequired[float]
    kick_return_long: NotRequired[float]
    solo_tackles: NotRequired[float]
    assisted_tackles: NotRequired[float]
    tackles_for_loss: NotRequired[float | None]
    sacks: NotRequired[float]
    sack_yards: NotRequired[float]
    quarterback_hits: NotRequired[float | None]
    passes_defended: NotRequired[float]
    fumbles_forced: NotRequired[float]
    fumbles_recovered: NotRequired[float]
    fumble_return_yards: NotRequired[float]
    fumble_return_touchdowns: NotRequired[float]
    interceptions: NotRequired[float]
    interception_return_yards: NotRequired[float]
    interception_return_touchdowns: NotRequired[float]
    blocked_kicks: NotRequired[float]
    special_teams_solo_tackles: NotRequired[float]
    special_teams_assisted_tackles: NotRequired[float]
    misc_solo_tackles: NotRequired[float]
    misc_assisted_tackles: NotRequired[float]
    punts: NotRequired[float]
    punt_yards: NotRequired[float]
    punt_average: NotRequired[float]
    field_goals_attempted: NotRequired[float]
    field_goals_made: NotRequired[float]
    field_goals_longest_made: NotRequired[float]
    extra_points_made: NotRequired[float]
    two_point_conversion_passes: NotRequired[float]
    two_point_conversion_runs: NotRequired[float]
    two_point_conversion_receptions: NotRequired[float]
    fantasy_points: NotRequired[float]
    fantasy_points_ppr: NotRequired[float]
    reception_percentage: NotRequired[float]
    receiving_yards_per_target: NotRequired[float]
    tackles: NotRequired[float]
    offensive_touchdowns: NotRequired[float]
    defensive_touchdowns: NotRequired[float]
    special_teams_touchdowns: NotRequired[float]
    touchdowns: NotRequired[float]
    fantasy_position: NotRequired[str | None]
    field_goal_percentage: NotRequired[float]
    player_season_id: NotRequired[int]
    fumbles_own_recoveries: NotRequired[float | None]
    fumbles_out_of_bounds: NotRequired[float | None]
    kick_return_fair_catches: NotRequired[float | None]
    punt_return_fair_catches: NotRequired[float | None]
    punt_touchbacks: NotRequired[float | None]
    punt_inside20: NotRequired[float | None]
    punt_net_average: NotRequired[float | None]
    extra_points_attempted: NotRequired[float | None]
    blocked_kick_return_touchdowns: NotRequired[float | None]
    field_goal_return_touchdowns: NotRequired[float | None]
    safeties: NotRequired[float | None]
    field_goals_had_blocked: NotRequired[float | None]
    punts_had_blocked: NotRequired[float | None]
    extra_points_had_blocked: NotRequired[float | None]
    punt_long: NotRequired[float | None]
    blocked_kick_return_yards: NotRequired[float | None]
    field_goal_return_yards: NotRequired[float | None]
    punt_net_yards: NotRequired[float | None]
    special_teams_fumbles_forced: NotRequired[float | None]
    special_teams_fumbles_recovered: NotRequired[float | None]
    misc_fumbles_forced: NotRequired[float | None]
    misc_fumbles_recovered: NotRequired[float | None]
    short_name: NotRequired[str | None]
    safeties_allowed: NotRequired[float | None]
    temperature: NotRequired[int | None]
    humidity: NotRequired[int | None]
    wind_speed: NotRequired[int | None]
    offensive_snaps_played: NotRequired[int | None]
    defensive_snaps_played: NotRequired[int | None]
    special_teams_snaps_played: NotRequired[int | None]
    offensive_team_snaps: NotRequired[int | None]
    defensive_team_snaps: NotRequired[int | None]
    special_teams_team_snaps: NotRequired[int | None]
    auction_value: NotRequired[float | None]
    auction_value_ppr: NotRequired[float | None]
    two_point_conversion_returns: NotRequired[float | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    field_goals_made0to19: NotRequired[float | None]
    field_goals_made20to29: NotRequired[float | None]
    field_goals_made30to39: NotRequired[float | None]
    field_goals_made40to49: NotRequired[float | None]
    field_goals_made50_plus: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    average_draft_position: NotRequired[float | None]
    average_draft_position_ppr: NotRequired[float | None]
    team_id: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    fantasy_points_fantasy_draft: NotRequired[float | None]
    scoring_details: NotRequired[list[ScoringDetail | ScoringDetailDict]]
    average_draft_position_rookie: NotRequired[float | None]
    average_draft_position_dynasty: NotRequired[float | None]
    average_draft_position2_qb: NotRequired[float | None]
    offensive_fumble_recovery_touchdowns: NotRequired[int | None]
