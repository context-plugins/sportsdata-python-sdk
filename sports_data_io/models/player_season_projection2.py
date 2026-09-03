from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerSeasonProjection2(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of the stat"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their MLB career"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar)"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The MLB season for which these totals apply"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's position associated with the given game or season. Possible values: 1B; 2B; 3B; C; CF; DH; IF; LF;
    OF; P; PH; PR; RF; RP; SP; SS"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category. Possible values: DH; IF; OF; P; PH; PR"""

    started: OptionalNullable[int] = Field(default=UNSET, alias="Started")
    """Number of games started in the season"""

    batting_order: OptionalNullable[int] = Field(default=UNSET, alias="BattingOrder")
    """This field is expected to be NULL"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    average_draft_position: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPosition")
    """The auction value for this player as it pertains to auction-style drafts for season-long fantasy baseball"""

    auction_value: OptionalNullable[int] = Field(default=UNSET, alias="AuctionValue")
    """The auction value for this player as it pertains to auction-style drafts for season-long fantasy baseball"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)."""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The number of games played."""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points"""

    at_bats: OptionalNullable[float] = Field(default=UNSET, alias="AtBats")
    """At bats while hitting"""

    runs: OptionalNullable[float] = Field(default=UNSET, alias="Runs")
    """Total runs scored."""

    hits: OptionalNullable[float] = Field(default=UNSET, alias="Hits")
    """Total hits"""

    singles: OptionalNullable[float] = Field(default=UNSET, alias="Singles")
    """Total singles"""

    doubles: OptionalNullable[float] = Field(default=UNSET, alias="Doubles")
    """Total doubles"""

    triples: OptionalNullable[float] = Field(default=UNSET, alias="Triples")
    """Total triples"""

    home_runs: OptionalNullable[float] = Field(default=UNSET, alias="HomeRuns")
    """Total home runs"""

    runs_batted_in: OptionalNullable[float] = Field(default=UNSET, alias="RunsBattedIn")
    """Total runs batted in"""

    batting_average: OptionalNullable[float] = Field(default=UNSET, alias="BattingAverage")
    """Total batting average"""

    outs: OptionalNullable[float] = Field(default=UNSET, alias="Outs")
    """Total outs"""

    strikeouts: OptionalNullable[float] = Field(default=UNSET, alias="Strikeouts")
    """Total strikeouts"""

    walks: OptionalNullable[float] = Field(default=UNSET, alias="Walks")
    """Total walks"""

    hit_by_pitch: OptionalNullable[float] = Field(default=UNSET, alias="HitByPitch")
    """Total times hit by pitch"""

    sacrifices: OptionalNullable[float] = Field(default=UNSET, alias="Sacrifices")
    """Total sacrifices"""

    sacrifice_flies: OptionalNullable[float] = Field(default=UNSET, alias="SacrificeFlies")
    """Total sacrifice flies"""

    ground_into_double_play: OptionalNullable[float] = Field(default=UNSET, alias="GroundIntoDoublePlay")
    """Total times grounded into double play"""

    stolen_bases: OptionalNullable[float] = Field(default=UNSET, alias="StolenBases")
    """Total stolen bases"""

    caught_stealing: OptionalNullable[float] = Field(default=UNSET, alias="CaughtStealing")
    """Total caught stealing"""

    pitches_seen: OptionalNullable[float] = Field(default=UNSET, alias="PitchesSeen")
    """Total pitches seen"""

    on_base_percentage: OptionalNullable[float] = Field(default=UNSET, alias="OnBasePercentage")
    """Total on base percentage"""

    slugging_percentage: OptionalNullable[float] = Field(default=UNSET, alias="SluggingPercentage")
    """Total slugging percentage"""

    on_base_plus_slugging: OptionalNullable[float] = Field(default=UNSET, alias="OnBasePlusSlugging")
    """Total on base plus percentage"""

    errors: OptionalNullable[float] = Field(default=UNSET, alias="Errors")
    """Total errors"""

    wins: OptionalNullable[float] = Field(default=UNSET, alias="Wins")
    """Total wins by the team/player"""

    losses: OptionalNullable[float] = Field(default=UNSET, alias="Losses")
    """Total losses by the team/player"""

    saves: OptionalNullable[float] = Field(default=UNSET, alias="Saves")
    """Total saves by team/player"""

    innings_pitched_decimal: OptionalNullable[float] = Field(default=UNSET, alias="InningsPitchedDecimal")
    """Decimal representation of total innings pitched (e.g. 1.33, 7.66, etc)"""

    total_outs_pitched: OptionalNullable[float] = Field(default=UNSET, alias="TotalOutsPitched")
    """Total outs pitched by team/player"""

    innings_pitched_full: OptionalNullable[float] = Field(default=UNSET, alias="InningsPitchedFull")
    """Total full innings pitched (e.g. 6, 71, 89, etc)"""

    innings_pitched_outs: OptionalNullable[float] = Field(default=UNSET, alias="InningsPitchedOuts")
    """Outs pitched beyond InningsPitchedFull (possible values: 0, 1, 2)"""

    earned_run_average: OptionalNullable[float] = Field(default=UNSET, alias="EarnedRunAverage")
    """Total earned run average by team/player"""

    pitching_hits: OptionalNullable[float] = Field(default=UNSET, alias="PitchingHits")
    """Hits allowed while pitching"""

    pitching_runs: OptionalNullable[float] = Field(default=UNSET, alias="PitchingRuns")
    """Runs allowed while pitching"""

    pitching_earned_runs: OptionalNullable[float] = Field(default=UNSET, alias="PitchingEarnedRuns")
    """Earned runs allowed while pitching"""

    pitching_walks: OptionalNullable[float] = Field(default=UNSET, alias="PitchingWalks")
    """Walks allowed while pitching"""

    pitching_strikeouts: OptionalNullable[float] = Field(default=UNSET, alias="PitchingStrikeouts")
    """Strikeouts allowed while pitching"""

    pitching_home_runs: OptionalNullable[float] = Field(default=UNSET, alias="PitchingHomeRuns")
    """Home runs allowed while pitching"""

    pitches_thrown: OptionalNullable[float] = Field(default=UNSET, alias="PitchesThrown")
    """Total pitches thrown while pitching"""

    pitches_thrown_strikes: OptionalNullable[float] = Field(default=UNSET, alias="PitchesThrownStrikes")
    """Total pitches thrown for strikes while pitching"""

    walks_hits_per_innings_pitched: OptionalNullable[float] = Field(default=UNSET, alias="WalksHitsPerInningsPitched")
    """Walks plus hits per innings pitched (WHIP) while pitching"""

    pitching_batting_average_against: OptionalNullable[float] = Field(
        default=UNSET, alias="PitchingBattingAverageAgainst"
    )
    """Total batting average against (BAA) while pitching"""

    grand_slams: OptionalNullable[float] = Field(default=UNSET, alias="GrandSlams")
    """Total grand slams"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Total FanDuel fantasy points"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total DraftKings fantasy points"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total Yahoo fantasy points"""

    plate_appearances: OptionalNullable[float] = Field(default=UNSET, alias="PlateAppearances")
    """Total plate appearances"""

    total_bases: OptionalNullable[float] = Field(default=UNSET, alias="TotalBases")
    """Number of total bases"""

    fly_outs: OptionalNullable[float] = Field(default=UNSET, alias="FlyOuts")
    """Total fly outs"""

    ground_outs: OptionalNullable[float] = Field(default=UNSET, alias="GroundOuts")
    """Total ground outs"""

    line_outs: OptionalNullable[float] = Field(default=UNSET, alias="LineOuts")
    """Total line outs"""

    pop_outs: OptionalNullable[float] = Field(default=UNSET, alias="PopOuts")
    """Total pop outs"""

    intentional_walks: OptionalNullable[float] = Field(default=UNSET, alias="IntentionalWalks")
    """Total intentional walks"""

    reached_on_error: OptionalNullable[float] = Field(default=UNSET, alias="ReachedOnError")
    """Total times reached on error"""

    balls_in_play: OptionalNullable[float] = Field(default=UNSET, alias="BallsInPlay")
    """Total balls in play"""

    batting_average_on_balls_in_play: OptionalNullable[float] = Field(
        default=UNSET, alias="BattingAverageOnBallsInPlay"
    )
    """Total batting average on balls in play (BABIP)"""

    weighted_on_base_percentage: OptionalNullable[float] = Field(default=UNSET, alias="WeightedOnBasePercentage")
    """Total weight on base percentage"""

    pitching_singles: OptionalNullable[float] = Field(default=UNSET, alias="PitchingSingles")
    """Total singles allowed while pitching"""

    pitching_doubles: OptionalNullable[float] = Field(default=UNSET, alias="PitchingDoubles")
    """Total doubles allowed while pitching"""

    pitching_triples: OptionalNullable[float] = Field(default=UNSET, alias="PitchingTriples")
    """Total triples allowed while pitching"""

    pitching_grand_slams: OptionalNullable[float] = Field(default=UNSET, alias="PitchingGrandSlams")
    """Total grand slams allowed while pitching"""

    pitching_hit_by_pitch: OptionalNullable[float] = Field(default=UNSET, alias="PitchingHitByPitch")
    """Total batters hit by pitch while pitching"""

    pitching_sacrifices: OptionalNullable[float] = Field(default=UNSET, alias="PitchingSacrifices")
    """Total sacrifices while pitching"""

    pitching_sacrifice_flies: OptionalNullable[float] = Field(default=UNSET, alias="PitchingSacrificeFlies")
    """Total sacrifice flies while pitching"""

    pitching_ground_into_double_play: OptionalNullable[float] = Field(
        default=UNSET, alias="PitchingGroundIntoDoublePlay"
    )
    """Total grounded into double plays while pitching"""

    pitching_complete_games: OptionalNullable[float] = Field(default=UNSET, alias="PitchingCompleteGames")
    """Total complete games while pitching"""

    pitching_shut_outs: OptionalNullable[float] = Field(default=UNSET, alias="PitchingShutOuts")
    """Total shuouts while pitching"""

    pitching_no_hitters: OptionalNullable[float] = Field(default=UNSET, alias="PitchingNoHitters")
    """Total no hitters while pitching"""

    pitching_perfect_games: OptionalNullable[float] = Field(default=UNSET, alias="PitchingPerfectGames")
    """Total perfect games while pitching"""

    pitching_plate_appearances: OptionalNullable[float] = Field(default=UNSET, alias="PitchingPlateAppearances")
    """Total plate appearances while pitching"""

    pitching_total_bases: OptionalNullable[float] = Field(default=UNSET, alias="PitchingTotalBases")
    """Total bases while pitching"""

    pitching_fly_outs: OptionalNullable[float] = Field(default=UNSET, alias="PitchingFlyOuts")
    """Total fly outs while pitching"""

    pitching_ground_outs: OptionalNullable[float] = Field(default=UNSET, alias="PitchingGroundOuts")
    """Total ground outs while pitching"""

    pitching_line_outs: OptionalNullable[float] = Field(default=UNSET, alias="PitchingLineOuts")
    """Total line outs while pitching"""

    pitching_pop_outs: OptionalNullable[float] = Field(default=UNSET, alias="PitchingPopOuts")
    """Total pop outs while pitching"""

    pitching_intentional_walks: OptionalNullable[float] = Field(default=UNSET, alias="PitchingIntentionalWalks")
    """Total intentional walks while pitching"""

    pitching_reached_on_error: OptionalNullable[float] = Field(default=UNSET, alias="PitchingReachedOnError")
    """Total times reached on error while pitching"""

    pitching_catchers_interference: OptionalNullable[float] = Field(default=UNSET, alias="PitchingCatchersInterference")
    """Total catchers interference while pitching"""

    pitching_balls_in_play: OptionalNullable[float] = Field(default=UNSET, alias="PitchingBallsInPlay")
    """Total balls in play while pitching"""

    pitching_on_base_percentage: OptionalNullable[float] = Field(default=UNSET, alias="PitchingOnBasePercentage")
    """Total on base percentage (OBP) while pitching"""

    pitching_slugging_percentage: OptionalNullable[float] = Field(default=UNSET, alias="PitchingSluggingPercentage")
    """Total slugging percentage (SLG) while pitching"""

    pitching_on_base_plus_slugging: OptionalNullable[float] = Field(default=UNSET, alias="PitchingOnBasePlusSlugging")
    """Total on base plus slugging (OPS) while pitching"""

    pitching_strikeouts_per_nine_innings: OptionalNullable[float] = Field(
        default=UNSET, alias="PitchingStrikeoutsPerNineInnings"
    )
    """Total strikeouts per nine innings (K/9) while pitching"""

    pitching_walks_per_nine_innings: OptionalNullable[float] = Field(default=UNSET, alias="PitchingWalksPerNineInnings")
    """Total walks per nine innings (BB/9) while pitching"""

    pitching_batting_average_on_balls_in_play: OptionalNullable[float] = Field(
        default=UNSET, alias="PitchingBattingAverageOnBallsInPlay"
    )
    """Total batting average on balls in play (BABIP) while pitching"""

    pitching_weighted_on_base_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="PitchingWeightedOnBasePercentage"
    )
    """Total weighted on base percentage while pitching"""

    double_plays: OptionalNullable[float] = Field(default=UNSET, alias="DoublePlays")
    """Total double plays, defined as one of: Bunted into Double Play, Fly into Double Play, Fouled into Double Play,
    Ground into Double Pla,y Line into Double Play, Popped into Double Play"""

    pitching_double_plays: OptionalNullable[float] = Field(default=UNSET, alias="PitchingDoublePlays")
    """Total double plays while pitching"""

    batting_order_confirmed: OptionalNullable[bool] = Field(default=UNSET, alias="BattingOrderConfirmed")
    """Whether the batting order is confirmed (true/false)"""

    isolated_power: OptionalNullable[float] = Field(default=UNSET, alias="IsolatedPower")
    """Total isolated power (ISO)"""

    fielding_independent_pitching: OptionalNullable[float] = Field(default=UNSET, alias="FieldingIndependentPitching")
    """Total fielding independent pitching (FIP)"""

    pitching_quality_starts: OptionalNullable[float] = Field(default=UNSET, alias="PitchingQualityStarts")
    """Total quality starts pitched"""

    pitching_inning_started: OptionalNullable[int] = Field(default=UNSET, alias="PitchingInningStarted")
    """The inning that the pitcher entered the game (if any)."""

    left_on_base: OptionalNullable[float] = Field(default=UNSET, alias="LeftOnBase")
    """Total left on base percentage"""

    pitching_holds: OptionalNullable[float] = Field(default=UNSET, alias="PitchingHolds")
    """Total holds pitched"""

    pitching_blown_saves: OptionalNullable[float] = Field(default=UNSET, alias="PitchingBlownSaves")
    """Total blown saves pitched"""

    substitute_batting_order: OptionalNullable[int] = Field(default=UNSET, alias="SubstituteBattingOrder")
    """The position in the batting order where this player was substituted into the game (does not include players in
    the starting lineup)"""

    substitute_batting_order_sequence: OptionalNullable[int] = Field(
        default=UNSET, alias="SubstituteBattingOrderSequence"
    )
    """The sequence in which this player was substituted into the game, within the particular batting order"""

    fantasy_points_fantasy_draft: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFantasyDraft")
    """Total FantasyDraft fantasy points"""

    fantasy_points_batting: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsBatting")
    """Total batting fantasy points"""

    fantasy_points_pitching: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsPitching")
    """Total pitching fantasy points"""


class PlayerSeasonProjection2Dict(TypedDict):
    stat_id: NotRequired[int]
    team_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
    position_category: NotRequired[str | None]
    started: NotRequired[int | None]
    batting_order: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    average_draft_position: NotRequired[float | None]
    auction_value: NotRequired[int | None]
    updated: NotRequired[str | None]
    games: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    at_bats: NotRequired[float | None]
    runs: NotRequired[float | None]
    hits: NotRequired[float | None]
    singles: NotRequired[float | None]
    doubles: NotRequired[float | None]
    triples: NotRequired[float | None]
    home_runs: NotRequired[float | None]
    runs_batted_in: NotRequired[float | None]
    batting_average: NotRequired[float | None]
    outs: NotRequired[float | None]
    strikeouts: NotRequired[float | None]
    walks: NotRequired[float | None]
    hit_by_pitch: NotRequired[float | None]
    sacrifices: NotRequired[float | None]
    sacrifice_flies: NotRequired[float | None]
    ground_into_double_play: NotRequired[float | None]
    stolen_bases: NotRequired[float | None]
    caught_stealing: NotRequired[float | None]
    pitches_seen: NotRequired[float | None]
    on_base_percentage: NotRequired[float | None]
    slugging_percentage: NotRequired[float | None]
    on_base_plus_slugging: NotRequired[float | None]
    errors: NotRequired[float | None]
    wins: NotRequired[float | None]
    losses: NotRequired[float | None]
    saves: NotRequired[float | None]
    innings_pitched_decimal: NotRequired[float | None]
    total_outs_pitched: NotRequired[float | None]
    innings_pitched_full: NotRequired[float | None]
    innings_pitched_outs: NotRequired[float | None]
    earned_run_average: NotRequired[float | None]
    pitching_hits: NotRequired[float | None]
    pitching_runs: NotRequired[float | None]
    pitching_earned_runs: NotRequired[float | None]
    pitching_walks: NotRequired[float | None]
    pitching_strikeouts: NotRequired[float | None]
    pitching_home_runs: NotRequired[float | None]
    pitches_thrown: NotRequired[float | None]
    pitches_thrown_strikes: NotRequired[float | None]
    walks_hits_per_innings_pitched: NotRequired[float | None]
    pitching_batting_average_against: NotRequired[float | None]
    grand_slams: NotRequired[float | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    plate_appearances: NotRequired[float | None]
    total_bases: NotRequired[float | None]
    fly_outs: NotRequired[float | None]
    ground_outs: NotRequired[float | None]
    line_outs: NotRequired[float | None]
    pop_outs: NotRequired[float | None]
    intentional_walks: NotRequired[float | None]
    reached_on_error: NotRequired[float | None]
    balls_in_play: NotRequired[float | None]
    batting_average_on_balls_in_play: NotRequired[float | None]
    weighted_on_base_percentage: NotRequired[float | None]
    pitching_singles: NotRequired[float | None]
    pitching_doubles: NotRequired[float | None]
    pitching_triples: NotRequired[float | None]
    pitching_grand_slams: NotRequired[float | None]
    pitching_hit_by_pitch: NotRequired[float | None]
    pitching_sacrifices: NotRequired[float | None]
    pitching_sacrifice_flies: NotRequired[float | None]
    pitching_ground_into_double_play: NotRequired[float | None]
    pitching_complete_games: NotRequired[float | None]
    pitching_shut_outs: NotRequired[float | None]
    pitching_no_hitters: NotRequired[float | None]
    pitching_perfect_games: NotRequired[float | None]
    pitching_plate_appearances: NotRequired[float | None]
    pitching_total_bases: NotRequired[float | None]
    pitching_fly_outs: NotRequired[float | None]
    pitching_ground_outs: NotRequired[float | None]
    pitching_line_outs: NotRequired[float | None]
    pitching_pop_outs: NotRequired[float | None]
    pitching_intentional_walks: NotRequired[float | None]
    pitching_reached_on_error: NotRequired[float | None]
    pitching_catchers_interference: NotRequired[float | None]
    pitching_balls_in_play: NotRequired[float | None]
    pitching_on_base_percentage: NotRequired[float | None]
    pitching_slugging_percentage: NotRequired[float | None]
    pitching_on_base_plus_slugging: NotRequired[float | None]
    pitching_strikeouts_per_nine_innings: NotRequired[float | None]
    pitching_walks_per_nine_innings: NotRequired[float | None]
    pitching_batting_average_on_balls_in_play: NotRequired[float | None]
    pitching_weighted_on_base_percentage: NotRequired[float | None]
    double_plays: NotRequired[float | None]
    pitching_double_plays: NotRequired[float | None]
    batting_order_confirmed: NotRequired[bool | None]
    isolated_power: NotRequired[float | None]
    fielding_independent_pitching: NotRequired[float | None]
    pitching_quality_starts: NotRequired[float | None]
    pitching_inning_started: NotRequired[int | None]
    left_on_base: NotRequired[float | None]
    pitching_holds: NotRequired[float | None]
    pitching_blown_saves: NotRequired[float | None]
    substitute_batting_order: NotRequired[int | None]
    substitute_batting_order_sequence: NotRequired[int | None]
    fantasy_points_fantasy_draft: NotRequired[float | None]
    fantasy_points_batting: NotRequired[float | None]
    fantasy_points_pitching: NotRequired[float | None]
