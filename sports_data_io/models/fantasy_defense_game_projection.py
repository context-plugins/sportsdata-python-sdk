from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .scoring_detail import ScoringDetail, ScoringDetailDict


class FantasyDefenseGameProjection(SdkBaseModel):
    game_key: OptionalNullable[str] = Field(default=UNSET, alias="GameKey")
    """A 9 digit unique code identifying the game that this record corresponds to. The GameID is composed of Season;
    SeasonType; Week and HomeTeam. Note: This value will be NULL for bye weeks"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this player corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the game"""

    week: OptionalNullable[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    date: OptionalNullable[str] = Field(default=UNSET, alias="Date")
    """The date and time of the game (in US Eastern Time)"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team"""

    points_allowed: Optional[float] = Field(default=UNSET, alias="PointsAllowed")
    """Total points allowed by the team during the game"""

    touchdowns_scored: Optional[float] = Field(default=UNSET, alias="TouchdownsScored")
    """Total defensive and special teams touchdowns scored by the team in the game"""

    solo_tackles: Optional[float] = Field(default=UNSET, alias="SoloTackles")
    """Total defensive solo (unassisted) tackles by the team in the game"""

    assisted_tackles: Optional[float] = Field(default=UNSET, alias="AssistedTackles")
    """Total defensive assisted tackles by the team in the game"""

    sacks: Optional[float] = Field(default=UNSET, alias="Sacks")
    """Total defensive sacks by the team in the game"""

    sack_yards: Optional[float] = Field(default=UNSET, alias="SackYards")
    """Total defensive sack yards by the team in the game"""

    passes_defended: Optional[float] = Field(default=UNSET, alias="PassesDefended")
    """Total passes defended by the team in the game"""

    fumbles_forced: Optional[float] = Field(default=UNSET, alias="FumblesForced")
    """Total fumbles forced on defense by the team in the game"""

    fumbles_recovered: Optional[float] = Field(default=UNSET, alias="FumblesRecovered")
    """Total defensive fumble recoveries by the team in the game"""

    fumble_return_yards: Optional[float] = Field(default=UNSET, alias="FumbleReturnYards")
    """Total fumble return yards by the team in the game"""

    fumble_return_touchdowns: Optional[float] = Field(default=UNSET, alias="FumbleReturnTouchdowns")
    """Total fumble return touchdowns by the team in the game"""

    interceptions: Optional[float] = Field(default=UNSET, alias="Interceptions")
    """Total defensive interceptions by the team in the game"""

    interception_return_yards: Optional[float] = Field(default=UNSET, alias="InterceptionReturnYards")
    """Total defensive interception return yards by the team in the game"""

    interception_return_touchdowns: Optional[float] = Field(default=UNSET, alias="InterceptionReturnTouchdowns")
    """Total defensive interception return touchdowns by the team in the game"""

    blocked_kicks: Optional[float] = Field(default=UNSET, alias="BlockedKicks")
    """Total blocked kicks by team in the game. Note: BlockedKicks include Field Goals and Punts but NOT Extra Points"""

    safeties: Optional[float] = Field(default=UNSET, alias="Safeties")
    """Total defensive safeties scored by the team in the game"""

    punt_returns: Optional[float] = Field(default=UNSET, alias="PuntReturns")
    """Total punt returns by the team in the game"""

    punt_return_yards: Optional[float] = Field(default=UNSET, alias="PuntReturnYards")
    """Total punt return yards by the team in the game"""

    punt_return_touchdowns: Optional[float] = Field(default=UNSET, alias="PuntReturnTouchdowns")
    """Total punt return touchdowns by the team in the game"""

    punt_return_long: Optional[float] = Field(default=UNSET, alias="PuntReturnLong")
    """The longest punt return by the team in the game"""

    kick_returns: Optional[float] = Field(default=UNSET, alias="KickReturns")
    """Total kickoff returns by the team in the game"""

    kick_return_yards: Optional[float] = Field(default=UNSET, alias="KickReturnYards")
    """Total kickoff return yards by the team in the game"""

    kick_return_touchdowns: Optional[float] = Field(default=UNSET, alias="KickReturnTouchdowns")
    """Total kickoff return touchdowns by the team in the game"""

    kick_return_long: Optional[float] = Field(default=UNSET, alias="KickReturnLong")
    """Longest kick return by the team in the game"""

    blocked_kick_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="BlockedKickReturnTouchdowns")
    """Total blocked kick recovery return touchdowns for the team in the game"""

    field_goal_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalReturnTouchdowns")
    """Total field goal return touchdowns by the team in the game. Note: This field excludes blocked field goals"""

    fantasy_points_allowed: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsAllowed")
    """Fantasy points allowed to opposing offensive players in the season. Note: positions include: QB; RB; WR; TE"""

    quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="QuarterbackFantasyPointsAllowed"
    )
    """Fantasy points allowed to opposing quarterbacks by the team in the game"""

    runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="RunningbackFantasyPointsAllowed"
    )
    """Total fantasy points allowed to opposing running backs by the team in the game"""

    wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="WideReceiverFantasyPointsAllowed"
    )
    """Fantasy points allowed to opposing wide receivers"""

    tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="TightEndFantasyPointsAllowed"
    )
    """Fantasy points allowed to opposing tight ends by the team in the game"""

    kicker_fantasy_points_allowed: OptionalNullable[float] = Field(default=UNSET, alias="KickerFantasyPointsAllowed")
    """Fantasy points allowed to opponent kickers by the team in the game"""

    blocked_kick_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="BlockedKickReturnYards")
    """Total blocked kick recovery return yards for the team in the game"""

    field_goal_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalReturnYards")
    """Total field goal return yards by the team in the game. Note: This field excludes blocked field goals"""

    quarterback_hits: OptionalNullable[float] = Field(default=UNSET, alias="QuarterbackHits")
    """Total quarterback hits by the team in the game. Note: This is a defensive stat that includes sacks"""

    tackles_for_loss: OptionalNullable[float] = Field(default=UNSET, alias="TacklesForLoss")
    """Total tackles for loss by the team in the game. Note: These are tackles behind the line of scrimmage for loss of
    yards (including sacks)"""

    defensive_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="DefensiveTouchdowns")
    """Total touchdowns scored by the defense"""

    special_teams_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="SpecialTeamsTouchdowns")
    """Total special teams touchdowns scored by the team in the game"""

    is_game_over: OptionalNullable[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether the game is over (true/false)"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Fantasy points scored based on basic fantasy scoring system by the team's D/ST in the game"""

    stadium: OptionalNullable[str] = Field(default=UNSET, alias="Stadium")
    """Stadium of the event"""

    temperature: OptionalNullable[int] = Field(default=UNSET, alias="Temperature")
    """Temperature at game start (Fahrenheit)"""

    humidity: OptionalNullable[int] = Field(default=UNSET, alias="Humidity")
    """The humidity percentage at the start of the game"""

    wind_speed: OptionalNullable[int] = Field(default=UNSET, alias="WindSpeed")
    """The wind speed at the start of the game (in MPH)"""

    third_down_attempts: OptionalNullable[float] = Field(default=UNSET, alias="ThirdDownAttempts")
    """Total third down attempts against the team in the game"""

    third_down_conversions: OptionalNullable[float] = Field(default=UNSET, alias="ThirdDownConversions")
    """Total third down conversions against the team in the game"""

    fourth_down_attempts: OptionalNullable[float] = Field(default=UNSET, alias="FourthDownAttempts")
    """Opponent's fourth down attempts against the team in the game"""

    fourth_down_conversions: OptionalNullable[float] = Field(default=UNSET, alias="FourthDownConversions")
    """Opponent's fourth down conversions against the team in the game"""

    points_allowed_by_defense_special_teams: OptionalNullable[float] = Field(
        default=UNSET, alias="PointsAllowedByDefenseSpecialTeams"
    )
    """Total number of points allowed by the team in the game to the opposing offense and special teams. Note: This
    field excludes points scored by the opponent's defense"""

    fan_duel_salary: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelSalary")
    """The team's D/ST salary for FanDuel daily fantasy contests"""

    draft_kings_salary: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsSalary")
    """The team's D/ST salary for DraftKings daily fantasy contests."""

    fantasy_data_salary: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDataSalary")
    """The team's D/ST salary as calculated by SportsDataIO (formerly known as FantasyData). Based on the same salary
    cap as DraftKings contests ($50,000)"""

    victiv_salary: OptionalNullable[int] = Field(default=UNSET, alias="VictivSalary")
    """The player's salary for Victiv daily fantasy contests."""

    two_point_conversion_returns: OptionalNullable[float] = Field(default=UNSET, alias="TwoPointConversionReturns")
    """Total successful two point conversion returns by the team in the game"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Fantasy points based on FanDuel's scoring system by the team in the game"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Fantasy points based on DraftKings' scoring system by the team in the game"""

    offensive_yards_allowed: OptionalNullable[float] = Field(default=UNSET, alias="OffensiveYardsAllowed")
    """Offensive yards allowed by the team's defense in the game"""

    yahoo_salary: OptionalNullable[int] = Field(default=UNSET, alias="YahooSalary")
    """The player's salary for Yahoo daily fantasy contests"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO for use when combining with player feeds. Note:
    this ID will stay with the player throughout their entire career"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Fantasy points based on Yahoo's daily fantasy scoring system by the team in the game"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Whether the team is home or away"""

    opponent_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRank")
    """The ranking of the opposing team's offense with regards to fantasy points allowed to fantasy DST"""

    opponent_position_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPositionRank")
    """The ranking of the opposing team's offense with regards to fantasy points allowed to fantasy DST"""

    fantasy_draft_salary: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftSalary")
    """The team's D/ST salary for FantasyDraft daily fantasy contests."""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

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
    """A globally unique ID for this team's opponent. This value is guaranteed to be unique across all sports/leagues"""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The position of this team's D/ST; as listed by DraftKings."""

    fan_duel_position: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelPosition")
    """The position of this team's D/ST; as listed by FanDuel."""

    fantasy_draft_position: OptionalNullable[str] = Field(default=UNSET, alias="FantasyDraftPosition")
    """The position of this team's D/ST; as listed by FantasyDraft"""

    yahoo_position: OptionalNullable[str] = Field(default=UNSET, alias="YahooPosition")
    """The position of the team's defense/special teams unit, as listed on Yahoo's daily fantasy sports platform"""

    fantasy_defense_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDefenseID")
    """"Unique ID of FantasyDefense record (subject to change; although it very rarely does). Note: For a guaranteed
    static ID; use a combination of GameKey and Team"
    """

    score_id: Optional[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the score/game"""

    fan_duel_fantasy_points_allowed: OptionalNullable[float] = Field(default=UNSET, alias="FanDuelFantasyPointsAllowed")
    """FanDuel fantasy points allowed to opposing offensive players in the game. Note: positions include: QB; RB; WR;
    TE"""

    fan_duel_quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelQuarterbackFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing quarterbacks in the game"""

    fan_duel_runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelRunningbackFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing running backs in the game"""

    fan_duel_wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelWideReceiverFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing wide receivers in the game"""

    fan_duel_tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelTightEndFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing tight ends in the game"""

    fan_duel_kicker_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelKickerFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing kickers in the game"""

    draft_kings_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed to opposing offensive players in the game. Note: positions include: QB; RB; WR;
    TE"""

    draft_kings_quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsQuarterbackFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent quarterbacks in the game"""

    draft_kings_runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsRunningbackFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent running backs in the game"""

    draft_kings_wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsWideReceiverFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent wide receivers in the game"""

    draft_kings_tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsTightEndFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent tight ends in the game"""

    draft_kings_kicker_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsKickerFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed to opposing kickers"""

    yahoo_fantasy_points_allowed: OptionalNullable[float] = Field(default=UNSET, alias="YahooFantasyPointsAllowed")
    """Total Yahoo fantasy points allowed to opposing offensive players by the team in the game. Note: Offensive players
    include: QB, RB, WR, & TE"""

    yahoo_quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooQuarterbackFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing quarterbacks by the team in the game"""

    yahoo_runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooRunningbackFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing running backs by the team in the game"""

    yahoo_wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooWideReceiverFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing wide receivers by the team in the game"""

    yahoo_tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooTightEndFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing tight ends by the team in the game"""

    yahoo_kicker_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooKickerFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing kickers by the team in the game"""

    fantasy_points_fantasy_draft: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFantasyDraft")
    """Fantasy points based on FantasyDraft's scoring system by the team in the game"""

    fantasy_draft_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed to opposing offensive players in the game. Note: positions include: QB; RB;
    WR; TE"""

    fantasy_draft_quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftQuarterbackFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing quarterbacks in the game"""

    fantasy_draft_runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftRunningbackFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing running backs in the game"""

    fantasy_draft_wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftWideReceiverFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing wide receivers in the game"""

    fantasy_draft_tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftTightEndFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing tight ends in the game"""

    fantasy_draft_kicker_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftKickerFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing kickers in the game"""

    scoring_details: Optional[list[ScoringDetail]] = Field(default=UNSET, alias="ScoringDetails")
    """The details of the scoring plays this team DST recorded in the game"""


class FantasyDefenseGameProjectionDict(TypedDict):
    game_key: NotRequired[str | None]
    season_type: NotRequired[int]
    season: NotRequired[int]
    week: NotRequired[int | None]
    date: NotRequired[str | None]
    team: NotRequired[str | None]
    opponent: NotRequired[str | None]
    points_allowed: NotRequired[float]
    touchdowns_scored: NotRequired[float]
    solo_tackles: NotRequired[float]
    assisted_tackles: NotRequired[float]
    sacks: NotRequired[float]
    sack_yards: NotRequired[float]
    passes_defended: NotRequired[float]
    fumbles_forced: NotRequired[float]
    fumbles_recovered: NotRequired[float]
    fumble_return_yards: NotRequired[float]
    fumble_return_touchdowns: NotRequired[float]
    interceptions: NotRequired[float]
    interception_return_yards: NotRequired[float]
    interception_return_touchdowns: NotRequired[float]
    blocked_kicks: NotRequired[float]
    safeties: NotRequired[float]
    punt_returns: NotRequired[float]
    punt_return_yards: NotRequired[float]
    punt_return_touchdowns: NotRequired[float]
    punt_return_long: NotRequired[float]
    kick_returns: NotRequired[float]
    kick_return_yards: NotRequired[float]
    kick_return_touchdowns: NotRequired[float]
    kick_return_long: NotRequired[float]
    blocked_kick_return_touchdowns: NotRequired[float | None]
    field_goal_return_touchdowns: NotRequired[float | None]
    fantasy_points_allowed: NotRequired[float | None]
    quarterback_fantasy_points_allowed: NotRequired[float | None]
    runningback_fantasy_points_allowed: NotRequired[float | None]
    wide_receiver_fantasy_points_allowed: NotRequired[float | None]
    tight_end_fantasy_points_allowed: NotRequired[float | None]
    kicker_fantasy_points_allowed: NotRequired[float | None]
    blocked_kick_return_yards: NotRequired[float | None]
    field_goal_return_yards: NotRequired[float | None]
    quarterback_hits: NotRequired[float | None]
    tackles_for_loss: NotRequired[float | None]
    defensive_touchdowns: NotRequired[float | None]
    special_teams_touchdowns: NotRequired[float | None]
    is_game_over: NotRequired[bool | None]
    fantasy_points: NotRequired[float | None]
    stadium: NotRequired[str | None]
    temperature: NotRequired[int | None]
    humidity: NotRequired[int | None]
    wind_speed: NotRequired[int | None]
    third_down_attempts: NotRequired[float | None]
    third_down_conversions: NotRequired[float | None]
    fourth_down_attempts: NotRequired[float | None]
    fourth_down_conversions: NotRequired[float | None]
    points_allowed_by_defense_special_teams: NotRequired[float | None]
    fan_duel_salary: NotRequired[int | None]
    draft_kings_salary: NotRequired[int | None]
    fantasy_data_salary: NotRequired[int | None]
    victiv_salary: NotRequired[int | None]
    two_point_conversion_returns: NotRequired[float | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    offensive_yards_allowed: NotRequired[float | None]
    yahoo_salary: NotRequired[int | None]
    player_id: NotRequired[int | None]
    fantasy_points_yahoo: NotRequired[float | None]
    home_or_away: NotRequired[str | None]
    opponent_rank: NotRequired[int | None]
    opponent_position_rank: NotRequired[int | None]
    fantasy_draft_salary: NotRequired[int | None]
    team_id: NotRequired[int | None]
    opponent_id: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    global_game_id: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    global_opponent_id: NotRequired[int | None]
    draft_kings_position: NotRequired[str | None]
    fan_duel_position: NotRequired[str | None]
    fantasy_draft_position: NotRequired[str | None]
    yahoo_position: NotRequired[str | None]
    fantasy_defense_id: NotRequired[int | None]
    score_id: NotRequired[int]
    fan_duel_fantasy_points_allowed: NotRequired[float | None]
    fan_duel_quarterback_fantasy_points_allowed: NotRequired[float | None]
    fan_duel_runningback_fantasy_points_allowed: NotRequired[float | None]
    fan_duel_wide_receiver_fantasy_points_allowed: NotRequired[float | None]
    fan_duel_tight_end_fantasy_points_allowed: NotRequired[float | None]
    fan_duel_kicker_fantasy_points_allowed: NotRequired[float | None]
    draft_kings_fantasy_points_allowed: NotRequired[float | None]
    draft_kings_quarterback_fantasy_points_allowed: NotRequired[float | None]
    draft_kings_runningback_fantasy_points_allowed: NotRequired[float | None]
    draft_kings_wide_receiver_fantasy_points_allowed: NotRequired[float | None]
    draft_kings_tight_end_fantasy_points_allowed: NotRequired[float | None]
    draft_kings_kicker_fantasy_points_allowed: NotRequired[float | None]
    yahoo_fantasy_points_allowed: NotRequired[float | None]
    yahoo_quarterback_fantasy_points_allowed: NotRequired[float | None]
    yahoo_runningback_fantasy_points_allowed: NotRequired[float | None]
    yahoo_wide_receiver_fantasy_points_allowed: NotRequired[float | None]
    yahoo_tight_end_fantasy_points_allowed: NotRequired[float | None]
    yahoo_kicker_fantasy_points_allowed: NotRequired[float | None]
    fantasy_points_fantasy_draft: NotRequired[float | None]
    fantasy_draft_fantasy_points_allowed: NotRequired[float | None]
    fantasy_draft_quarterback_fantasy_points_allowed: NotRequired[float | None]
    fantasy_draft_runningback_fantasy_points_allowed: NotRequired[float | None]
    fantasy_draft_wide_receiver_fantasy_points_allowed: NotRequired[float | None]
    fantasy_draft_tight_end_fantasy_points_allowed: NotRequired[float | None]
    fantasy_draft_kicker_fantasy_points_allowed: NotRequired[float | None]
    scoring_details: NotRequired[list[ScoringDetailDict]]
