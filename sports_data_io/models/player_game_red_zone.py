from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .scoring_detail import ScoringDetail, ScoringDetailDict


class PlayerGameRedZone(SdkBaseModel):
    game_key: OptionalNullable[str] = Field(default=UNSET, alias="GameKey")
    """A 9 digit unique code identifying the game that this record corresponds to. The GameID is composed of Season;
    SeasonType; Week and HomeTeam.. Note: This value will be NULL for bye weeks"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this player corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the game"""

    game_date: OptionalNullable[str] = Field(default=UNSET, alias="GameDate")
    """The date and time the game is scheduled to start"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on. Note: if this player is a free agent; this field is
    NULL"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Whether the team is home or away"""

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
    """Whether or not the player was active for the game"""

    played: Optional[int] = Field(default=UNSET, alias="Played")
    """Whether the player played at least one snap in the game Note: Will return "1" if player played at least one snap
    and "0" if they did not"""

    started: Optional[int] = Field(default=UNSET, alias="Started")
    """Whether the player started the game (on offensive or defense). Note: Started = 1 / Did Not Start = 0"""

    passing_attempts: Optional[float] = Field(default=UNSET, alias="PassingAttempts")
    """Total passes thrown by the player in the game"""

    passing_completions: Optional[float] = Field(default=UNSET, alias="PassingCompletions")
    """Total passes completed by the player in the game"""

    passing_yards: Optional[float] = Field(default=UNSET, alias="PassingYards")
    """Total passing yards by the player in the game"""

    passing_completion_percentage: Optional[float] = Field(default=UNSET, alias="PassingCompletionPercentage")
    """The percentage of passes completed by the player in the game"""

    passing_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="PassingYardsPerAttempt")
    """Total average passing yards per attempt by the player in the game"""

    passing_yards_per_completion: Optional[float] = Field(default=UNSET, alias="PassingYardsPerCompletion")
    """Total average passing yards per completion by the player in the game"""

    passing_touchdowns: Optional[float] = Field(default=UNSET, alias="PassingTouchdowns")
    """Total passing touchdowns by the player in the game"""

    passing_interceptions: Optional[float] = Field(default=UNSET, alias="PassingInterceptions")
    """Total interceptions thrown by the player in the game"""

    passing_rating: Optional[float] = Field(default=UNSET, alias="PassingRating")
    """The passer rating of the player in the game"""

    passing_long: Optional[float] = Field(default=UNSET, alias="PassingLong")
    """Total yards of longest completion by the player in the game"""

    passing_sacks: Optional[float] = Field(default=UNSET, alias="PassingSacks")
    """The total number of times the player was sacked in the game"""

    passing_sack_yards: Optional[float] = Field(default=UNSET, alias="PassingSackYards")
    """Total yards lost by the player in the game as a result of being sacked"""

    rushing_attempts: Optional[float] = Field(default=UNSET, alias="RushingAttempts")
    """Total rushing attempts by the player in the game"""

    rushing_yards: Optional[float] = Field(default=UNSET, alias="RushingYards")
    """Total rushing yards by the player in the game"""

    rushing_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="RushingYardsPerAttempt")
    """Total rushing yards per attempt by the player in the game"""

    rushing_touchdowns: Optional[float] = Field(default=UNSET, alias="RushingTouchdowns")
    """Total rushing touchdowns by the player in the game"""

    rushing_long: Optional[float] = Field(default=UNSET, alias="RushingLong")
    """The longest rush by the player in the game"""

    receiving_targets: OptionalNullable[float] = Field(default=UNSET, alias="ReceivingTargets")
    """Total receiving targets by the player in the game"""

    receptions: Optional[float] = Field(default=UNSET, alias="Receptions")
    """Total receptions by the player in the game"""

    receiving_yards: Optional[float] = Field(default=UNSET, alias="ReceivingYards")
    """Total receiving yards by the player in the game"""

    receiving_yards_per_reception: Optional[float] = Field(default=UNSET, alias="ReceivingYardsPerReception")
    """Average receiving yards per reception by the player in the game"""

    receiving_touchdowns: Optional[float] = Field(default=UNSET, alias="ReceivingTouchdowns")
    """Total receiving touchdowns by the player in the game"""

    receiving_long: Optional[float] = Field(default=UNSET, alias="ReceivingLong")
    """The longest reception by the player in the game"""

    fumbles: Optional[float] = Field(default=UNSET, alias="Fumbles")
    """Total fumbles by the player in the game"""

    fumbles_lost: OptionalNullable[float] = Field(default=UNSET, alias="FumblesLost")
    """Total fumbles lost by the player in the game"""

    punt_returns: Optional[float] = Field(default=UNSET, alias="PuntReturns")
    """Total punt returns by the player in the game"""

    punt_return_yards: Optional[float] = Field(default=UNSET, alias="PuntReturnYards")
    """Total punt return yards by the player in the game"""

    punt_return_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="PuntReturnYardsPerAttempt")
    """Total average yards gained per punt return by the player in the game"""

    punt_return_touchdowns: Optional[float] = Field(default=UNSET, alias="PuntReturnTouchdowns")
    """Total punt return touchdowns by the player in the game"""

    punt_return_long: Optional[float] = Field(default=UNSET, alias="PuntReturnLong")
    """The longest punt return by the player in the game"""

    kick_returns: Optional[float] = Field(default=UNSET, alias="KickReturns")
    """Total kickoff returns by the player in the game"""

    kick_return_yards: Optional[float] = Field(default=UNSET, alias="KickReturnYards")
    """Total kickoff return yards by the player in the game"""

    kick_return_yards_per_attempt: Optional[float] = Field(default=UNSET, alias="KickReturnYardsPerAttempt")
    """Average yards gained per kick return by the player in the game"""

    kick_return_touchdowns: Optional[float] = Field(default=UNSET, alias="KickReturnTouchdowns")
    """Total kickoff return touchdowns by the player in the game"""

    kick_return_long: Optional[float] = Field(default=UNSET, alias="KickReturnLong")
    """Longest kick return by the player in the game"""

    solo_tackles: Optional[float] = Field(default=UNSET, alias="SoloTackles")
    """Total defensive solo (unassisted) tackles by the player in the game"""

    assisted_tackles: Optional[float] = Field(default=UNSET, alias="AssistedTackles")
    """Total defensive assisted tackles by the player in the game"""

    tackles_for_loss: OptionalNullable[float] = Field(default=UNSET, alias="TacklesForLoss")
    """Total tackles for loss by the player in the game. Note: these are tackles behind the line of scrimmage for loss
    of yards (including sacks)"""

    sacks: Optional[float] = Field(default=UNSET, alias="Sacks")
    """Total defensive sacks by the player in the game"""

    sack_yards: Optional[float] = Field(default=UNSET, alias="SackYards")
    """Total defensive sacks yards by the player in the game"""

    quarterback_hits: OptionalNullable[float] = Field(default=UNSET, alias="QuarterbackHits")
    """Total quarterback hits by the player in the game. Note: This is a defensive stat that includes sacks"""

    passes_defended: Optional[float] = Field(default=UNSET, alias="PassesDefended")
    """Total passes defended by the player in the game"""

    fumbles_forced: Optional[float] = Field(default=UNSET, alias="FumblesForced")
    """Total fumbles forced on defense by the player in the game"""

    fumbles_recovered: Optional[float] = Field(default=UNSET, alias="FumblesRecovered")
    """Total defensive fumble recoveries by the player in the game"""

    fumble_return_yards: Optional[float] = Field(default=UNSET, alias="FumbleReturnYards")
    """Total fumble return yards by the player in the game"""

    fumble_return_touchdowns: Optional[float] = Field(default=UNSET, alias="FumbleReturnTouchdowns")
    """Total fumble return touchdowns by the player in the game"""

    interceptions: Optional[float] = Field(default=UNSET, alias="Interceptions")
    """Total defensive interceptions by the player in the game"""

    interception_return_yards: Optional[float] = Field(default=UNSET, alias="InterceptionReturnYards")
    """Total defensive interception return yards by the player in the game"""

    interception_return_touchdowns: Optional[float] = Field(default=UNSET, alias="InterceptionReturnTouchdowns")
    """Total defensive interception return touchdowns by the player in the game"""

    blocked_kicks: Optional[float] = Field(default=UNSET, alias="BlockedKicks")
    """Total blocked kicks by the player in the game. Note: BlockedKicks include Field Goals and Punts but NOT Extra
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
    """Total number of punts by the player in the game"""

    punt_yards: Optional[float] = Field(default=UNSET, alias="PuntYards")
    """Total punt yards by the player in the game"""

    punt_average: Optional[float] = Field(default=UNSET, alias="PuntAverage")
    """The average number of yards per punt by the player in the game"""

    field_goals_attempted: Optional[float] = Field(default=UNSET, alias="FieldGoalsAttempted")
    """Total field goals attempted by the player in the game"""

    field_goals_made: Optional[float] = Field(default=UNSET, alias="FieldGoalsMade")
    """Total field goals made by the player in game"""

    field_goals_longest_made: Optional[float] = Field(default=UNSET, alias="FieldGoalsLongestMade")
    """Longest field goal made by the player in the game"""

    extra_points_made: Optional[float] = Field(default=UNSET, alias="ExtraPointsMade")
    """Total extra points made by the player in the game"""

    two_point_conversion_passes: Optional[float] = Field(default=UNSET, alias="TwoPointConversionPasses")
    """Total successful two point conversion passes by the player in the game"""

    two_point_conversion_runs: Optional[float] = Field(default=UNSET, alias="TwoPointConversionRuns")
    """Total successful two point conversion rushes by the player in the game"""

    two_point_conversion_receptions: Optional[float] = Field(default=UNSET, alias="TwoPointConversionReceptions")
    """Total successful two point conversion receptions by the player in the game"""

    fantasy_points: Optional[float] = Field(default=UNSET, alias="FantasyPoints")
    """Fantasy points scored based on basic fantasy scoring system by the player in the game"""

    fantasy_points_ppr: Optional[float] = Field(default=UNSET, alias="FantasyPointsPPR")
    """This field is expected to be NULL"""

    reception_percentage: Optional[float] = Field(default=UNSET, alias="ReceptionPercentage")
    """Total percentage of receiving targets that were receptions by the player in the game"""

    receiving_yards_per_target: Optional[float] = Field(default=UNSET, alias="ReceivingYardsPerTarget")
    """Average receiving yards per target by the player in the game"""

    tackles: Optional[float] = Field(default=UNSET, alias="Tackles")
    """Total tackles (solo & assisted) by the player in the game"""

    offensive_touchdowns: Optional[float] = Field(default=UNSET, alias="OffensiveTouchdowns")
    """Total offensive touchdowns scored by the player in the game"""

    defensive_touchdowns: Optional[float] = Field(default=UNSET, alias="DefensiveTouchdowns")
    """Total defensive touchdowns scored by the player in the game"""

    special_teams_touchdowns: Optional[float] = Field(default=UNSET, alias="SpecialTeamsTouchdowns")
    """Total special teams touchdowns scored by the player in the game"""

    touchdowns: Optional[float] = Field(default=UNSET, alias="Touchdowns")
    """Total touchdowns scored by the player in the game (excludes passing touchdowns)"""

    fantasy_position: OptionalNullable[str] = Field(default=UNSET, alias="FantasyPosition")
    """The player's fantasy football position. Possible values: QB; RB; WR; TE; DL; LB; DB; K; P; OL"""

    field_goal_percentage: Optional[float] = Field(default=UNSET, alias="FieldGoalPercentage")
    """Total field goal attempts made by the player in the game"""

    player_game_id: Optional[int] = Field(default=UNSET, alias="PlayerGameID")
    """Unique ID of PlayerGame record (subject to change, although it very rarely does). For a static ID, use a
    combination of GameKey and PlayerID."""

    fumbles_own_recoveries: OptionalNullable[float] = Field(default=UNSET, alias="FumblesOwnRecoveries")
    """Total own fumble recoveries by the player in the game. Note: this fumble doesn't result in a turnover - the
    fumbling team recovers the fumble"""

    fumbles_out_of_bounds: OptionalNullable[float] = Field(default=UNSET, alias="FumblesOutOfBounds")
    """This field is deprecated"""

    kick_return_fair_catches: OptionalNullable[float] = Field(default=UNSET, alias="KickReturnFairCatches")
    """This field is deprecated"""

    punt_return_fair_catches: OptionalNullable[float] = Field(default=UNSET, alias="PuntReturnFairCatches")
    """This field is deprecated"""

    punt_touchbacks: OptionalNullable[float] = Field(default=UNSET, alias="PuntTouchbacks")
    """Total punts that resulted in touchbacks by the player in the game"""

    punt_inside20: OptionalNullable[float] = Field(default=UNSET, alias="PuntInside20")
    """Total punts downed inside the 20 yard line by the player in the game"""

    punt_net_average: OptionalNullable[float] = Field(default=UNSET, alias="PuntNetAverage")
    """The average net yards per punt by the player in the game"""

    extra_points_attempted: OptionalNullable[float] = Field(default=UNSET, alias="ExtraPointsAttempted")
    """Total extra point kicks attempted by the player in the game"""

    blocked_kick_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="BlockedKickReturnTouchdowns")
    """Total blocked kick recovery return touchdowns for the player in the game"""

    field_goal_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalReturnTouchdowns")
    """Total field goal return touchdowns by the player in the game. Note: This field excludes blocked field goals"""

    safeties: OptionalNullable[float] = Field(default=UNSET, alias="Safeties")
    """Total defensive safeties scored by the player in the game"""

    field_goals_had_blocked: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsHadBlocked")
    """Total field goals by the player that were blocked in the game"""

    punts_had_blocked: OptionalNullable[float] = Field(default=UNSET, alias="PuntsHadBlocked")
    """Total punts by the player that were blocked in the game"""

    extra_points_had_blocked: OptionalNullable[float] = Field(default=UNSET, alias="ExtraPointsHadBlocked")
    """Total extra point kick attempts by the player that were blocked in the game"""

    punt_long: OptionalNullable[float] = Field(default=UNSET, alias="PuntLong")
    """The longest punt by the player in the game"""

    blocked_kick_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="BlockedKickReturnYards")
    """Total blocked kick recovery return yards for the player in the game"""

    field_goal_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalReturnYards")
    """Total field goal return yards by the player in the game. Note: This field excludes blocked field goals"""

    punt_net_yards: OptionalNullable[float] = Field(default=UNSET, alias="PuntNetYards")
    """The net yards of the punts by the player in the game"""

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

    playing_surface: OptionalNullable[str] = Field(default=UNSET, alias="PlayingSurface")
    """The playing surface of the stadium"""

    is_game_over: OptionalNullable[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether the game is over (true/false)"""

    safeties_allowed: OptionalNullable[float] = Field(default=UNSET, alias="SafetiesAllowed")
    """This field is deprecated"""

    stadium: OptionalNullable[str] = Field(default=UNSET, alias="Stadium")
    """Stadium of the event"""

    temperature: OptionalNullable[int] = Field(default=UNSET, alias="Temperature")
    """Temperature at game start (Fahrenheit)"""

    humidity: OptionalNullable[int] = Field(default=UNSET, alias="Humidity")
    """The humidity percentage at the start of the game"""

    wind_speed: OptionalNullable[int] = Field(default=UNSET, alias="WindSpeed")
    """The wind speed at the start of the game (in MPH)"""

    fan_duel_salary: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelSalary")
    """The player's salary for FanDuel daily fantasy contests."""

    draft_kings_salary: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsSalary")
    """The player's salary for DraftKings daily fantasy contests."""

    fantasy_data_salary: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDataSalary")
    """The player's salary as calculated by SportsDataIO (formerly known as FantasyData). Based on the same salary cap
    as DraftKings contests ($50,000)."""

    offensive_snaps_played: OptionalNullable[int] = Field(default=UNSET, alias="OffensiveSnapsPlayed")
    """Total snaps this player played on offense in the game. Note: Snap counts are available the morning after the
    game."""

    defensive_snaps_played: OptionalNullable[int] = Field(default=UNSET, alias="DefensiveSnapsPlayed")
    """Total snaps this player played on defense in the game. Note: Snap counts are available the morning after the
    game."""

    special_teams_snaps_played: OptionalNullable[int] = Field(default=UNSET, alias="SpecialTeamsSnapsPlayed")
    """Total snaps this player played on special teams in the game. Note: Snap counts are available the morning after
    the game."""

    offensive_team_snaps: OptionalNullable[int] = Field(default=UNSET, alias="OffensiveTeamSnaps")
    """Total offensive snaps this player's team played in the game. Note: Snap counts are available the morning after
    the game."""

    defensive_team_snaps: OptionalNullable[int] = Field(default=UNSET, alias="DefensiveTeamSnaps")
    """Total defensive snaps this player's team played in the game. Note: Snap counts are available the morning after
    the game."""

    special_teams_team_snaps: OptionalNullable[int] = Field(default=UNSET, alias="SpecialTeamsTeamSnaps")
    """Total special teams snaps this player's team played in the game. Note: Snap counts are available the morning
    after the game."""

    victiv_salary: OptionalNullable[int] = Field(default=UNSET, alias="VictivSalary")
    """The player's salary for Victiv daily fantasy contests."""

    two_point_conversion_returns: OptionalNullable[float] = Field(default=UNSET, alias="TwoPointConversionReturns")
    """Total successful two point conversion returns by the player in the game"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Fantasy points based on FanDuel's scoring system by the player in the game"""

    field_goals_made0to19: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade0to19")
    """Total field goals of 0 to 19 yards made by the player in game"""

    field_goals_made20to29: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade20to29")
    """Total field goals of 20 to 29 yards made by the player in game"""

    field_goals_made30to39: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade30to39")
    """Total field goals of 30 to 39 yards made by the player in game"""

    field_goals_made40to49: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade40to49")
    """Total field goals of 40 to 49 yards made by the player in game"""

    field_goals_made50_plus: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade50Plus")
    """Total field goals of 50+ yards made by the player in game"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Fantasy points based on DraftKings' scoring system by the player in the game"""

    yahoo_salary: OptionalNullable[int] = Field(default=UNSET, alias="YahooSalary")
    """The player's salary for Yahoo daily fantasy contests"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Fantasy points based on Yahoo's daily fantasy scoring system by the player in the game"""

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """The player's current injury status; in the form of likelihood that player plays (Probable; Questionable;
    Doubtful; Out)"""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """The body part that is injured for the player (Knee; Groin; Calf; Hamstring; etc.)"""

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The day that the player's injury started or was first discovered"""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """A brief description of the player's injury and expected availability"""

    fan_duel_position: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelPosition")
    """The player's eligible position in FanDuel's daily fantasy sports platform."""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The player's eligible position in DraftKings' daily fantasy sports platform."""

    yahoo_position: OptionalNullable[str] = Field(default=UNSET, alias="YahooPosition")
    """The player's eligible position in Yahoo's daily fantasy sports platform"""

    opponent_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRank")
    """The ranking of the player's opponent with regards to fantasy points allowed."""

    opponent_position_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPositionRank")
    """The ranking of the player's opponent by position with regards to fantasy points allowed."""

    injury_practice: OptionalNullable[str] = Field(default=UNSET, alias="InjuryPractice")
    """This field is deprecated"""

    injury_practice_description: OptionalNullable[str] = Field(default=UNSET, alias="InjuryPracticeDescription")
    """This field is deprecated"""

    declared_inactive: Optional[bool] = Field(default=UNSET, alias="DeclaredInactive")
    """Whether the player has been declared inactive. This value is updated in the hours leading up to game start time;
    as teams announce their inactive players. Note: This is only updated for offensive skill position players (QB; RB;
    WR; TE)"""

    fantasy_draft_salary: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftSalary")
    """The player's salary for FantasyDraft daily fantasy contests."""

    fantasy_draft_position: OptionalNullable[str] = Field(default=UNSET, alias="FantasyDraftPosition")
    """The player's eligible position in FantasyDraft's daily fantasy sports platform."""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that the player is on. Note: if the player is a free agent; this field is NULL"""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentID")
    """The unique ID of this opponent team"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game (in US Eastern Time)"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    global_opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalOpponentID")
    """A globally unique ID for this opposing team. This value is guaranteed to be unique across all sports/leagues."""

    score_id: Optional[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the score/game"""

    fantasy_points_fantasy_draft: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFantasyDraft")
    """This field is no longer in use and will return null."""

    scoring_details: Optional[list[ScoringDetail]] = Field(default=UNSET, alias="ScoringDetails")
    """The details of the scoring plays this player recorded in the game"""

    offensive_fumble_recovery_touchdowns: OptionalNullable[float] = Field(
        default=UNSET, alias="OffensiveFumbleRecoveryTouchdowns"
    )
    """This field is deprecated"""

    snap_counts_confirmed: OptionalNullable[bool] = Field(default=UNSET, alias="SnapCountsConfirmed")
    """Whether snap count fields are confirmed (true/false). Note: This takes place the morning after the game."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """Time of last update (in US Eastern time). Note: this does not indicate that stats changed."""


class PlayerGameRedZoneDict(TypedDict):
    game_key: NotRequired[str | None]
    player_id: NotRequired[int | None]
    season_type: NotRequired[int]
    season: NotRequired[int]
    game_date: NotRequired[str | None]
    week: NotRequired[int]
    team: NotRequired[str | None]
    opponent: NotRequired[str | None]
    home_or_away: NotRequired[str | None]
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
    player_game_id: NotRequired[int]
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
    playing_surface: NotRequired[str | None]
    is_game_over: NotRequired[bool | None]
    safeties_allowed: NotRequired[float | None]
    stadium: NotRequired[str | None]
    temperature: NotRequired[int | None]
    humidity: NotRequired[int | None]
    wind_speed: NotRequired[int | None]
    fan_duel_salary: NotRequired[int | None]
    draft_kings_salary: NotRequired[int | None]
    fantasy_data_salary: NotRequired[int | None]
    offensive_snaps_played: NotRequired[int | None]
    defensive_snaps_played: NotRequired[int | None]
    special_teams_snaps_played: NotRequired[int | None]
    offensive_team_snaps: NotRequired[int | None]
    defensive_team_snaps: NotRequired[int | None]
    special_teams_team_snaps: NotRequired[int | None]
    victiv_salary: NotRequired[int | None]
    two_point_conversion_returns: NotRequired[float | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    field_goals_made0to19: NotRequired[float | None]
    field_goals_made20to29: NotRequired[float | None]
    field_goals_made30to39: NotRequired[float | None]
    field_goals_made40to49: NotRequired[float | None]
    field_goals_made50_plus: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    yahoo_salary: NotRequired[int | None]
    fantasy_points_yahoo: NotRequired[float | None]
    injury_status: NotRequired[str | None]
    injury_body_part: NotRequired[str | None]
    injury_start_date: NotRequired[str | None]
    injury_notes: NotRequired[str | None]
    fan_duel_position: NotRequired[str | None]
    draft_kings_position: NotRequired[str | None]
    yahoo_position: NotRequired[str | None]
    opponent_rank: NotRequired[int | None]
    opponent_position_rank: NotRequired[int | None]
    injury_practice: NotRequired[str | None]
    injury_practice_description: NotRequired[str | None]
    declared_inactive: NotRequired[bool]
    fantasy_draft_salary: NotRequired[int | None]
    fantasy_draft_position: NotRequired[str | None]
    team_id: NotRequired[int | None]
    opponent_id: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    global_game_id: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    global_opponent_id: NotRequired[int | None]
    score_id: NotRequired[int]
    fantasy_points_fantasy_draft: NotRequired[float | None]
    scoring_details: NotRequired[list[ScoringDetail | ScoringDetailDict]]
    offensive_fumble_recovery_touchdowns: NotRequired[float | None]
    snap_counts_confirmed: NotRequired[bool | None]
    updated: NotRequired[str | None]
