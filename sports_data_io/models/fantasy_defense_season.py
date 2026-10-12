from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .scoring_detail import ScoringDetail, ScoringDetailDict


class FantasyDefenseSeason(SdkBaseModel):
    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this team corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL regular season for which these totals apply"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    points_allowed: Optional[float] = Field(default=UNSET, alias="PointsAllowed")
    """Total points allowed by the team during the season"""

    touchdowns_scored: Optional[float] = Field(default=UNSET, alias="TouchdownsScored")
    """Total defensive and special teams touchdowns scored by the team in the season"""

    solo_tackles: Optional[float] = Field(default=UNSET, alias="SoloTackles")
    """Total defensive solo (unassisted) tackles by the team in the season"""

    assisted_tackles: Optional[float] = Field(default=UNSET, alias="AssistedTackles")
    """Total defensive assisted tackles by the team in the season"""

    sacks: Optional[float] = Field(default=UNSET, alias="Sacks")
    """Total defensive sacks by the team in the season"""

    sack_yards: Optional[float] = Field(default=UNSET, alias="SackYards")
    """Total defensive sack yards by the team in the season"""

    passes_defended: Optional[float] = Field(default=UNSET, alias="PassesDefended")
    """Total passes defended by the team in the season"""

    fumbles_forced: Optional[float] = Field(default=UNSET, alias="FumblesForced")
    """Total fumbles forced on defense by the team in the season"""

    fumbles_recovered: Optional[float] = Field(default=UNSET, alias="FumblesRecovered")
    """Total defensive fumble recoveries by the team in the season"""

    fumble_return_yards: Optional[float] = Field(default=UNSET, alias="FumbleReturnYards")
    """Total fumble return yards by the team in the season"""

    fumble_return_touchdowns: Optional[float] = Field(default=UNSET, alias="FumbleReturnTouchdowns")
    """Total fumble return touchdowns by the team in the season"""

    interceptions: Optional[float] = Field(default=UNSET, alias="Interceptions")
    """Total defensive interceptions by the team in the season"""

    interception_return_yards: Optional[float] = Field(default=UNSET, alias="InterceptionReturnYards")
    """Total defensive interception return yards by the team in the season"""

    interception_return_touchdowns: Optional[float] = Field(default=UNSET, alias="InterceptionReturnTouchdowns")
    """Total defensive interception return touchdowns by the team in the season"""

    blocked_kicks: Optional[float] = Field(default=UNSET, alias="BlockedKicks")
    """Total blocked kicks by the team in the season. Note: BlockedKicks include Field Goals and Punts but NOT Extra
    Points"""

    safeties: Optional[float] = Field(default=UNSET, alias="Safeties")
    """Total defensive safeties scored by the team in the season"""

    punt_returns: Optional[float] = Field(default=UNSET, alias="PuntReturns")
    """Total punt returns by the team in the season"""

    punt_return_yards: Optional[float] = Field(default=UNSET, alias="PuntReturnYards")
    """Total punt return yards by the team in the season"""

    punt_return_touchdowns: Optional[float] = Field(default=UNSET, alias="PuntReturnTouchdowns")
    """Total punt return touchdowns by the team in the season"""

    punt_return_long: Optional[float] = Field(default=UNSET, alias="PuntReturnLong")
    """The longest punt return by the team in the season"""

    kick_returns: Optional[float] = Field(default=UNSET, alias="KickReturns")
    """Total kickoff returns by the team in the season"""

    kick_return_yards: Optional[float] = Field(default=UNSET, alias="KickReturnYards")
    """Total kickoff return yards by the team in the season"""

    kick_return_touchdowns: Optional[float] = Field(default=UNSET, alias="KickReturnTouchdowns")
    """Total kickoff return touchdowns by the team in the season"""

    kick_return_long: Optional[float] = Field(default=UNSET, alias="KickReturnLong")
    """Longest kick return by the team in the season"""

    blocked_kick_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="BlockedKickReturnTouchdowns")
    """Total blocked kick recovery return touchdowns for the team in the season"""

    field_goal_return_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalReturnTouchdowns")
    """Total field goal return touchdowns by the team in the season. Note: This field excludes blocked field goals"""

    fantasy_points_allowed: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsAllowed")
    """Fantasy points allowed to opposing offensive players in the season. Note: positions include: QB; RB; WR; TE"""

    quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="QuarterbackFantasyPointsAllowed"
    )
    """Fantasy points allowed to opposing quarterbacks by the team in the season"""

    runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="RunningbackFantasyPointsAllowed"
    )
    """Total fantasy points allowed to opposing running backs by the team in the season"""

    wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="WideReceiverFantasyPointsAllowed"
    )
    """Fantasy points allowed to opposing wide receivers"""

    tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="TightEndFantasyPointsAllowed"
    )
    """Fantasy points allowed to opposing tight ends by the team in the season"""

    kicker_fantasy_points_allowed: OptionalNullable[float] = Field(default=UNSET, alias="KickerFantasyPointsAllowed")
    """Fantasy points allowed to opponent kickers by the team in the season"""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The total number of games played by the team in the season"""

    blocked_kick_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="BlockedKickReturnYards")
    """Total blocked kick recovery return yards for the team in the season"""

    field_goal_return_yards: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalReturnYards")
    """Total field goal return yards by the team in the season. Note: This field excludes blocked field goals"""

    quarterback_hits: OptionalNullable[float] = Field(default=UNSET, alias="QuarterbackHits")
    """Total quarterback hits by the team in the season. Note: This is a defensive stat that includes sacks"""

    tackles_for_loss: OptionalNullable[float] = Field(default=UNSET, alias="TacklesForLoss")
    """Total tackles for loss by the team in the season. Note: these are tackles behind the line of scrimmage for loss
    of yards (including sacks)"""

    defensive_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="DefensiveTouchdowns")
    """Total defensive touchdowns scored by the team in the season"""

    special_teams_touchdowns: OptionalNullable[float] = Field(default=UNSET, alias="SpecialTeamsTouchdowns")
    """Total special teams touchdowns scored by the team in the season"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Fantasy points scored based on basic fantasy scoring system by the team in the season"""

    temperature: OptionalNullable[int] = Field(default=UNSET, alias="Temperature")
    """Temperature at game start (Fahrenheit)"""

    humidity: OptionalNullable[int] = Field(default=UNSET, alias="Humidity")
    """The humidity percentage at the start of the game"""

    wind_speed: OptionalNullable[int] = Field(default=UNSET, alias="WindSpeed")
    """The wind speed at the start of the game (in MPH)"""

    third_down_attempts: OptionalNullable[float] = Field(default=UNSET, alias="ThirdDownAttempts")
    """Total third down attempts against the team in the season"""

    third_down_conversions: OptionalNullable[float] = Field(default=UNSET, alias="ThirdDownConversions")
    """Total third down conversions against the team in the season"""

    fourth_down_attempts: OptionalNullable[float] = Field(default=UNSET, alias="FourthDownAttempts")
    """Opponent's fourth down attempts against the team in the season"""

    fourth_down_conversions: OptionalNullable[float] = Field(default=UNSET, alias="FourthDownConversions")
    """Opponent's fourth down conversions against the team in the season"""

    points_allowed_by_defense_special_teams: OptionalNullable[float] = Field(
        default=UNSET, alias="PointsAllowedByDefenseSpecialTeams"
    )
    """Total number of points allowed by the team in the season to the opposing offense and special teams. Note: This
    field excludes points scored by the opponent's defense"""

    auction_value: OptionalNullable[float] = Field(default=UNSET, alias="AuctionValue")
    """Player's dollar value in a $200 salary cap auction draft."""

    auction_value_ppr: OptionalNullable[float] = Field(default=UNSET, alias="AuctionValuePPR")
    """Player's dollar value in a $200 salary cap PPR auction draft."""

    two_point_conversion_returns: OptionalNullable[float] = Field(default=UNSET, alias="TwoPointConversionReturns")
    """Total successful two point conversion returns by the team in the season"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Fantasy points based on FanDuel's scoring system by the team in the season"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Fantasy points based on DraftKings' scoring system by the team in the season"""

    offensive_yards_allowed: OptionalNullable[float] = Field(default=UNSET, alias="OffensiveYardsAllowed")
    """Offensive yards allowed by the team's defense in the season"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO for use when combining with player feeds. Note:
    this ID will stay with the player throughout their entire career"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Fantasy points based on Yahoo's daily fantasy scoring system by the team in the season"""

    average_draft_position: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPosition")
    """The average draft position of the team's fantasy defense (DST) in re-draft leagues"""

    average_draft_position_ppr: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPositionPPR")
    """The average draft position of the team (DST) in Points Per Reception (PPR) leagues"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    fan_duel_fantasy_points_allowed: OptionalNullable[float] = Field(default=UNSET, alias="FanDuelFantasyPointsAllowed")
    """FanDuel fantasy points allowed to opposing offensive players in the season. Note: positions include: QB; RB; WR;
    TE"""

    fan_duel_quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelQuarterbackFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing quarterbacks in the season"""

    fan_duel_runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelRunningbackFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing running backs in the season"""

    fan_duel_wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelWideReceiverFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing wide receivers in the season"""

    fan_duel_tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelTightEndFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing tight ends in the season"""

    fan_duel_kicker_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FanDuelKickerFantasyPointsAllowed"
    )
    """FanDuel fantasy points allowed by the team to opposing kickers in the season"""

    draft_kings_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed to opposing offensive players in the season. Note: positions include: QB; RB;
    WR; TE"""

    draft_kings_quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsQuarterbackFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent quarterbacks in the season"""

    draft_kings_runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsRunningbackFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent running backs in the season"""

    draft_kings_wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsWideReceiverFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent wide receivers in the season"""

    draft_kings_tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsTightEndFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent tight ends in the season"""

    draft_kings_kicker_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="DraftKingsKickerFantasyPointsAllowed"
    )
    """DraftKings fantasy points allowed by the team to opponent kickers in the season"""

    yahoo_fantasy_points_allowed: OptionalNullable[float] = Field(default=UNSET, alias="YahooFantasyPointsAllowed")
    """Total Yahoo fantasy points allowed to opposing offensive players by the team in the season. Note: Offensive
    players include: QB, RB, WR, & TE"""

    yahoo_quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooQuarterbackFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing quarterbacks by the team in the season"""

    yahoo_runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooRunningbackFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing running backs by the team in the season"""

    yahoo_wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooWideReceiverFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing wide receivers by the team in the season"""

    yahoo_tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooTightEndFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing tight ends by the team in the season"""

    yahoo_kicker_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="YahooKickerFantasyPointsAllowed"
    )
    """Total Yahoo fantasy points allowed to opposing kickers by the team in the season"""

    fantasy_points_fantasy_draft: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFantasyDraft")
    """Fantasy points based on FanDraft's scoring system by the team in the season"""

    fantasy_draft_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed to opposing offensive players in the season. Note: positions include: QB; RB;
    WR; TE"""

    fantasy_draft_quarterback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftQuarterbackFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing quarterbacks in the season"""

    fantasy_draft_runningback_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftRunningbackFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing running backs in the season"""

    fantasy_draft_wide_receiver_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftWideReceiverFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing wide receivers in the season"""

    fantasy_draft_tight_end_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftTightEndFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing tight ends in the season"""

    fantasy_draft_kicker_fantasy_points_allowed: OptionalNullable[float] = Field(
        default=UNSET, alias="FantasyDraftKickerFantasyPointsAllowed"
    )
    """FantasyDraft fantasy points allowed by the team to opposing kickers in the season"""

    scoring_details: Optional[list[ScoringDetail]] = Field(default=UNSET, alias="ScoringDetails")
    """The details of the scoring plays this team DST recorded in the season"""

    average_draft_position_dynasty: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPositionDynasty")
    """The average draft position of this team (DST) in dynasty drafts leagues"""

    average_draft_position2_qb: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPosition2QB")
    """The average draft position of the team (DST) in 2 Quarterback leagues"""


class FantasyDefenseSeasonDict(TypedDict):
    season_type: NotRequired[int]
    season: NotRequired[int]
    team: NotRequired[str | None]
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
    games: NotRequired[int | None]
    blocked_kick_return_yards: NotRequired[float | None]
    field_goal_return_yards: NotRequired[float | None]
    quarterback_hits: NotRequired[float | None]
    tackles_for_loss: NotRequired[float | None]
    defensive_touchdowns: NotRequired[float | None]
    special_teams_touchdowns: NotRequired[float | None]
    fantasy_points: NotRequired[float | None]
    temperature: NotRequired[int | None]
    humidity: NotRequired[int | None]
    wind_speed: NotRequired[int | None]
    third_down_attempts: NotRequired[float | None]
    third_down_conversions: NotRequired[float | None]
    fourth_down_attempts: NotRequired[float | None]
    fourth_down_conversions: NotRequired[float | None]
    points_allowed_by_defense_special_teams: NotRequired[float | None]
    auction_value: NotRequired[float | None]
    auction_value_ppr: NotRequired[float | None]
    two_point_conversion_returns: NotRequired[float | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    offensive_yards_allowed: NotRequired[float | None]
    player_id: NotRequired[int | None]
    fantasy_points_yahoo: NotRequired[float | None]
    average_draft_position: NotRequired[float | None]
    average_draft_position_ppr: NotRequired[float | None]
    team_id: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
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
    average_draft_position_dynasty: NotRequired[float | None]
    average_draft_position2_qb: NotRequired[float | None]
