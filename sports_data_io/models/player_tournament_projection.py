from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .player_round import PlayerRound, PlayerRoundDict


class PlayerTournamentProjection(SdkBaseModel):
    player_tournament_id: Optional[int] = Field(default=UNSET, alias="PlayerTournamentID")
    """The unique ID of this player/tournament combination"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the golfer"""

    tournament_id: Optional[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the golfer"""

    rank: OptionalNullable[int] = Field(default=UNSET, alias="Rank")
    """The rank of this golfer in the tournament"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The country where this golfer is from"""

    total_score: OptionalNullable[float] = Field(default=UNSET, alias="TotalScore")
    """The total score of the golfer for this tournament as compared to par"""

    total_strokes: OptionalNullable[float] = Field(default=UNSET, alias="TotalStrokes")
    """The total strokes this golfer has for this tournament"""

    total_through: OptionalNullable[int] = Field(default=UNSET, alias="TotalThrough")
    """The current hole of this golfer for the current round"""

    earnings: OptionalNullable[float] = Field(default=UNSET, alias="Earnings")
    """Total money earned by the golfer in this tournament"""

    fed_ex_points: OptionalNullable[int] = Field(default=UNSET, alias="FedExPoints")
    """Total FedEx points scored by the golfer in this tournament"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points scored by the golfer in the tournament using the default SportsDataIO scoring system"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total fantasy points scored by the golfer in the tournament using DraftKings' scoring system"""

    draft_kings_salary: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsSalary")
    """The golfer's salary for DraftKings daily fantasy contests"""

    double_eagles: OptionalNullable[float] = Field(default=UNSET, alias="DoubleEagles")
    """Total double eagles scored by the golfer in this tournament"""

    eagles: OptionalNullable[float] = Field(default=UNSET, alias="Eagles")
    """Total eagles scored by the golfer in this tournament"""

    birdies: OptionalNullable[float] = Field(default=UNSET, alias="Birdies")
    """Total birdies scored by the golfer for this tournament"""

    pars: OptionalNullable[float] = Field(default=UNSET, alias="Pars")
    """Total pars scored by the player in this tournament"""

    bogeys: OptionalNullable[float] = Field(default=UNSET, alias="Bogeys")
    """Total bogeys scored by the golfer in this tournament"""

    double_bogeys: OptionalNullable[float] = Field(default=UNSET, alias="DoubleBogeys")
    """Total double bogeys scored by the golfer in this tournament"""

    worse_than_double_bogey: OptionalNullable[float] = Field(default=UNSET, alias="WorseThanDoubleBogey")
    """Total holes the golfer scored worse than a double bogey for the tournament"""

    hole_in_ones: OptionalNullable[float] = Field(default=UNSET, alias="HoleInOnes")
    """Total holes-in-one scored by the golfer in this tournament"""

    streaks_of_three_birdies_or_better: OptionalNullable[float] = Field(
        default=UNSET, alias="StreaksOfThreeBirdiesOrBetter"
    )
    """Total streaks of three birdies (or better) this golfer scored"""

    bogey_free_rounds: OptionalNullable[float] = Field(default=UNSET, alias="BogeyFreeRounds")
    """Total bogey-free rounds by the golfer in this tournament"""

    rounds_under_seventy: OptionalNullable[float] = Field(default=UNSET, alias="RoundsUnderSeventy")
    """Total rounds this golfer finished scoring under 70 strokes"""

    triple_bogeys: OptionalNullable[float] = Field(default=UNSET, alias="TripleBogeys")
    """Total triple bogeys this golfer scored for the tournament"""

    worse_than_triple_bogey: OptionalNullable[float] = Field(default=UNSET, alias="WorseThanTripleBogey")
    """Total holes the golfer scored worse than a triple bogey for the tournament"""

    tee_time: OptionalNullable[str] = Field(default=UNSET, alias="TeeTime")
    """The time that this golfer tees off for the upcoming round (in US Eastern Time)"""

    made_cut: OptionalNullable[float] = Field(default=UNSET, alias="MadeCut")
    """Indicates whether this golfer made the cut. This field defaults to 1 at tournament start, then flips to 0 once a
    golfer has been cut"""

    win: OptionalNullable[float] = Field(default=UNSET, alias="Win")
    """Indicates whether this golfer won the tournament. Note: For tournament projections; this value will be a decimal
    between 0 and 1 of the likelihood that the golfer wins the tournament"""

    tournament_status: OptionalNullable[str] = Field(default=UNSET, alias="TournamentStatus")
    """Indicates whether a golfer is not playing in this tournament. Note: If golfer is not playing; this will be out"""

    is_alternate: OptionalNullable[bool] = Field(default=UNSET, alias="IsAlternate")
    """Indicates if a golfer is in the regular playing field or if they are an alternate for this tournament"""

    fan_duel_salary: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelSalary")
    """The golfer's salary for FanDuel daily fantasy contests"""

    fantasy_draft_salary: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftSalary")
    """The golfer's salary for FantasyDraft's daily fantasy contests"""

    made_cut_did_not_finish: OptionalNullable[bool] = Field(default=UNSET, alias="MadeCutDidNotFinish")
    """Indicates whether this golfer made the cut but did not finish the tournament"""

    rounds: Optional[list[PlayerRound]] = Field(default=UNSET, alias="Rounds")
    """The details of the rounds this golfer played"""

    odds_to_win: OptionalNullable[float] = Field(default=UNSET, alias="OddsToWin")
    """Odds to win the tournament displayed as a decimal (assumed over 1; ex. 9/2 = 4.5). This is the payout from the
    sports book for each dollar wagered"""

    odds_to_win_description: OptionalNullable[str] = Field(default=UNSET, alias="OddsToWinDescription")
    """Odds to win the tournament displayed as text (ex. 9/2). This is the payout from the sports book for each dollar
    wagered"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Total fantasy points scored by the golfer in the tournament using FanDuel's scoring system"""

    fantasy_points_fantasy_draft: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFantasyDraft")
    """Total fantasy points scored by the golfer in the tournament using FantasyDraft's scoring system"""

    streaks_of_four_birdies_or_better: OptionalNullable[float] = Field(
        default=UNSET, alias="StreaksOfFourBirdiesOrBetter"
    )
    """Total streaks of four birdies (or better) this golfer scored"""

    streaks_of_five_birdies_or_better: OptionalNullable[float] = Field(
        default=UNSET, alias="StreaksOfFiveBirdiesOrBetter"
    )
    """Total streaks of five birdies (or better) this golfer scored"""

    consecutive_birdie_or_better_count: OptionalNullable[float] = Field(
        default=UNSET, alias="ConsecutiveBirdieOrBetterCount"
    )
    """The sum of all back to back birdies (or better) by the golfer in this tournament"""

    bounce_back_count: OptionalNullable[float] = Field(default=UNSET, alias="BounceBackCount")
    """The total bounce back holes for the golfer across all rounds of the tournament. Note: a bounce back hole is an
    under par hole following an over par hole"""

    rounds_with_five_or_more_birdies_or_better: OptionalNullable[float] = Field(
        default=UNSET, alias="RoundsWithFiveOrMoreBirdiesOrBetter"
    )
    """Total rounds that the golfer scored five or more birdies or better"""

    is_withdrawn: Optional[bool] = Field(default=UNSET, alias="IsWithdrawn")
    """Indicates whether the player has withdrawn from the tournament"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total fantasy points scored by the golfer in the tournament using Yahoo's scoring system"""

    streaks_of_six_birdies_or_better: OptionalNullable[float] = Field(
        default=UNSET, alias="StreaksOfSixBirdiesOrBetter"
    )
    """Total streaks of six birdies (or better) this golfer scored"""


class PlayerTournamentProjectionDict(TypedDict):
    player_tournament_id: NotRequired[int]
    player_id: NotRequired[int]
    tournament_id: NotRequired[int]
    name: NotRequired[str | None]
    rank: NotRequired[int | None]
    country: NotRequired[str | None]
    total_score: NotRequired[float | None]
    total_strokes: NotRequired[float | None]
    total_through: NotRequired[int | None]
    earnings: NotRequired[float | None]
    fed_ex_points: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    draft_kings_salary: NotRequired[int | None]
    double_eagles: NotRequired[float | None]
    eagles: NotRequired[float | None]
    birdies: NotRequired[float | None]
    pars: NotRequired[float | None]
    bogeys: NotRequired[float | None]
    double_bogeys: NotRequired[float | None]
    worse_than_double_bogey: NotRequired[float | None]
    hole_in_ones: NotRequired[float | None]
    streaks_of_three_birdies_or_better: NotRequired[float | None]
    bogey_free_rounds: NotRequired[float | None]
    rounds_under_seventy: NotRequired[float | None]
    triple_bogeys: NotRequired[float | None]
    worse_than_triple_bogey: NotRequired[float | None]
    tee_time: NotRequired[str | None]
    made_cut: NotRequired[float | None]
    win: NotRequired[float | None]
    tournament_status: NotRequired[str | None]
    is_alternate: NotRequired[bool | None]
    fan_duel_salary: NotRequired[int | None]
    fantasy_draft_salary: NotRequired[int | None]
    made_cut_did_not_finish: NotRequired[bool | None]
    rounds: NotRequired[list[PlayerRound | PlayerRoundDict]]
    odds_to_win: NotRequired[float | None]
    odds_to_win_description: NotRequired[str | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_fantasy_draft: NotRequired[float | None]
    streaks_of_four_birdies_or_better: NotRequired[float | None]
    streaks_of_five_birdies_or_better: NotRequired[float | None]
    consecutive_birdie_or_better_count: NotRequired[float | None]
    bounce_back_count: NotRequired[float | None]
    rounds_with_five_or_more_birdies_or_better: NotRequired[float | None]
    is_withdrawn: NotRequired[bool]
    fantasy_points_yahoo: NotRequired[float | None]
    streaks_of_six_birdies_or_better: NotRequired[float | None]
