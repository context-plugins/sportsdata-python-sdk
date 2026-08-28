from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .player_hole import PlayerHole, PlayerHoleDict


class PlayerRound(SdkBaseModel):
    player_round_id: Optional[int] = Field(default=UNSET, alias="PlayerRoundID")
    """The unique ID of this golfer/round combination"""

    player_tournament_id: Optional[int] = Field(default=UNSET, alias="PlayerTournamentID")
    """The unique ID of this player/tournament combination"""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """The number of the round associated with these stats"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date that this round is being played on"""

    par: OptionalNullable[int] = Field(default=UNSET, alias="Par")
    """The par of the course this round is played on"""

    score: OptionalNullable[int] = Field(default=UNSET, alias="Score")
    """The total strokes this golfer has for this round in the tournament"""

    bogey_free: Optional[bool] = Field(default=UNSET, alias="BogeyFree")
    """Indicates whether the player shot bogey-free during this round"""

    includes_streak_of_three_birdies_or_better: Optional[bool] = Field(
        default=UNSET, alias="IncludesStreakOfThreeBirdiesOrBetter"
    )
    """Indicates whether the player got a streak of three birdies (or better) on this round"""

    double_eagles: OptionalNullable[int] = Field(default=UNSET, alias="DoubleEagles")
    """Total number of double eagles shot by this player on this round"""

    eagles: OptionalNullable[int] = Field(default=UNSET, alias="Eagles")
    """Total eagles scored by the golfer in this round"""

    birdies: OptionalNullable[int] = Field(default=UNSET, alias="Birdies")
    """Total birdies scored by the golfer for this round"""

    pars: OptionalNullable[int] = Field(default=UNSET, alias="Pars")
    """Total pars scored by the player in this round of the tournament"""

    bogeys: OptionalNullable[int] = Field(default=UNSET, alias="Bogeys")
    """Total bogeys scored by the golfer for this round"""

    double_bogeys: OptionalNullable[int] = Field(default=UNSET, alias="DoubleBogeys")
    """Total double bogeys scored by the golfer in this round"""

    worse_than_double_bogey: OptionalNullable[int] = Field(default=UNSET, alias="WorseThanDoubleBogey")
    """Total holes the golfer scored worse than a double bogey for the round"""

    hole_in_ones: OptionalNullable[int] = Field(default=UNSET, alias="HoleInOnes")
    """Total holes-in-one scored by the golfer in this round"""

    triple_bogeys: OptionalNullable[int] = Field(default=UNSET, alias="TripleBogeys")
    """Total triple bogeys this golfer scored for the round"""

    worse_than_triple_bogey: OptionalNullable[int] = Field(default=UNSET, alias="WorseThanTripleBogey")
    """Total holes the golfer scored worse than a triple bogey for the round"""

    holes: Optional[list[PlayerHole]] = Field(default=UNSET, alias="Holes")
    """The hole-by-hole results for this player in this round"""

    longest_birdie_or_better_streak: OptionalNullable[float] = Field(default=UNSET, alias="LongestBirdieOrBetterStreak")
    """The longest streak of birdies (or better) by the golfer"""

    consecutive_birdie_or_better_count: OptionalNullable[float] = Field(
        default=UNSET, alias="ConsecutiveBirdieOrBetterCount"
    )
    """The sum of all back to back birdies (or better) by the golfer in this round"""

    bounce_back_count: OptionalNullable[float] = Field(default=UNSET, alias="BounceBackCount")
    """Total bounce back holes by the golfer for this round"""

    includes_streak_of_four_birdies_or_better: Optional[bool] = Field(
        default=UNSET, alias="IncludesStreakOfFourBirdiesOrBetter"
    )
    """Indicates whether the player shot a streak of four birdies or better on this round"""

    includes_streak_of_five_birdies_or_better: Optional[bool] = Field(
        default=UNSET, alias="IncludesStreakOfFiveBirdiesOrBetter"
    )
    """Indicates whether the player shot a streak of five birdies or better on this round"""

    includes_five_or_more_birdies_or_better: Optional[bool] = Field(
        default=UNSET, alias="IncludesFiveOrMoreBirdiesOrBetter"
    )
    """Indicates whether the player shot a streak of five (or more) birdies or better on this round"""

    includes_streak_of_six_birdies_or_better: Optional[bool] = Field(
        default=UNSET, alias="IncludesStreakOfSixBirdiesOrBetter"
    )
    """Indicates whether the player shot a six of five birdies or better on this round"""

    tee_time: OptionalNullable[str] = Field(default=UNSET, alias="TeeTime")
    """The time that this golfer tees off for the upcoming round (in US Eastern Time)"""

    back_nine_start: OptionalNullable[bool] = Field(default=UNSET, alias="BackNineStart")
    """Indicates whether the player started with the back nine holes"""


class PlayerRoundDict(TypedDict):
    player_round_id: NotRequired[int]
    player_tournament_id: NotRequired[int]
    number: NotRequired[int | None]
    day: NotRequired[str | None]
    par: NotRequired[int | None]
    score: NotRequired[int | None]
    bogey_free: NotRequired[bool]
    includes_streak_of_three_birdies_or_better: NotRequired[bool]
    double_eagles: NotRequired[int | None]
    eagles: NotRequired[int | None]
    birdies: NotRequired[int | None]
    pars: NotRequired[int | None]
    bogeys: NotRequired[int | None]
    double_bogeys: NotRequired[int | None]
    worse_than_double_bogey: NotRequired[int | None]
    hole_in_ones: NotRequired[int | None]
    triple_bogeys: NotRequired[int | None]
    worse_than_triple_bogey: NotRequired[int | None]
    holes: NotRequired[list[PlayerHole | PlayerHoleDict]]
    longest_birdie_or_better_streak: NotRequired[float | None]
    consecutive_birdie_or_better_count: NotRequired[float | None]
    bounce_back_count: NotRequired[float | None]
    includes_streak_of_four_birdies_or_better: NotRequired[bool]
    includes_streak_of_five_birdies_or_better: NotRequired[bool]
    includes_five_or_more_birdies_or_better: NotRequired[bool]
    includes_streak_of_six_birdies_or_better: NotRequired[bool]
    tee_time: NotRequired[str | None]
    back_nine_start: NotRequired[bool | None]
