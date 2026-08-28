from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .playoff_aggregate_score2 import PlayoffAggregateScore2, PlayoffAggregateScore2Dict


class Game15(SdkBaseModel):
    """The details of the Game that this SlateGame refers to"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of the game"""

    round_id: Optional[int] = Field(default=UNSET, alias="RoundId")
    """The unique ID of the round that this game is associated with."""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The soccer regular season for which these totals apply"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    group: OptionalNullable[str] = Field(default=UNSET, alias="Group")
    """The name of the group in which this game occurs. Note: This is used in tournaments & cups"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamId")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamId")
    """The unique ID of the home team"""

    venue_id: OptionalNullable[int] = Field(default=UNSET, alias="VenueId")
    """The unique ID of the venue"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in UTC)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Break, Final, Awarded, Postponed,
    Canceled, Suspended, Start Delay, Rain Delay, No Result, & NotNecessary. If a game is called off before it starts,
    the Status is set to Postponed, until a new date/time is scheduled, at which point, the DateTime is updated, and the
    Status is set back to Scheduled. If a game has already started, and temporarily interrupted, it's Status is set to
    Suspended, until it either resumes, or gets postponed and replayed at a later date. If the game is at halftime, then
    the Status will be Break. Awarded is used in cases where a game is decided on the so called "green table." That
    means that a game was decided by the Federation/League to one team for a reason. This can include situations like
    riots, where the opponent team gets 3:0 win awarded as punishment. Awarded is also used when a club withdraws during
    the season from the competition then all the remaining matches getting awarded 3:0."""

    week: OptionalNullable[int] = Field(default=UNSET, alias="Week")
    """The week during the season/round in which this game occurs"""

    period: OptionalNullable[str] = Field(default=UNSET, alias="Period")
    """The final period of the game. Possible values: Regular = Game ended in 90 minutes of regular time; ExtraTime =
    Game ended in extra time / overtime; PenaltyShootout = Game finished in penalty shootout time"""

    clock: OptionalNullable[int] = Field(default=UNSET, alias="Clock")
    """The clock for the game if it is in progress. Note: if the game hasn't started or the game is over; then this will
    be NULL"""

    winner: OptionalNullable[str] = Field(default=UNSET, alias="Winner")
    """The winner of the game. Possible values: AwayTeam; HomeTeam; Draw"""

    venue_type: OptionalNullable[str] = Field(default=UNSET, alias="VenueType")
    """Shows which team has home field advantage. Possible values: Home; Away; Neutral"""

    away_team_key: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamKey")
    """The abbreviation [Key] of the away team"""

    away_team_name: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamName")
    """The name of the away team"""

    away_team_country_code: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamCountryCode")
    """The country code of the away team."""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """The final score of the away team"""

    away_team_score_period1: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScorePeriod1")
    """The first period score of the away team."""

    away_team_score_period2: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScorePeriod2")
    """The second period score of the away team."""

    away_team_score_extra_time: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScoreExtraTime")
    """The extra time (overtime) score of the away team (if applicable)."""

    away_team_score_penalty: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScorePenalty")
    """The penalty shootout score of the away team (if applicable)."""

    home_team_key: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamKey")
    """The abbreviation [Key] of the home team"""

    home_team_name: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamName")
    """The name of the home team"""

    home_team_country_code: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamCountryCode")
    """The country code of the home team"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """The final score of the home team"""

    home_team_score_period1: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScorePeriod1")
    """The first period score of the home team"""

    home_team_score_period2: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScorePeriod2")
    """The second period score of the home team"""

    home_team_score_extra_time: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScoreExtraTime")
    """The extra time (overtime) score of the home team (if applicable)"""

    home_team_score_penalty: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScorePenalty")
    """The penalty shootout score of the home team (if applicable)"""

    home_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamMoneyLine")
    """Payout on a bet that the away home wins"""

    away_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamMoneyLine")
    """Payout on a bet that the away team wins."""

    draw_money_line: OptionalNullable[int] = Field(default=UNSET, alias="DrawMoneyLine")
    """The sportsbook's money line for a draw"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """Point spread for the home team"""

    home_team_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamPointSpreadPayout")
    """Payout if the home team covers the spread"""

    away_team_point_spread_payout: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamPointSpreadPayout")
    """Payout if the away team covers the spread"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The sportsbook's total goals line (over/under) for the game"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for the over bet on the total goals line"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under"""

    attendance: OptionalNullable[int] = Field(default=UNSET, alias="Attendance")
    """The attendance for the game."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)"""

    updated_utc: OptionalNullable[str] = Field(default=UNSET, alias="UpdatedUtc")
    """The timestamp of when this record was updated (in UTC)"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameId")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamId")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamId")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    clock_extra: OptionalNullable[int] = Field(default=UNSET, alias="ClockExtra")
    """The added stoppage time minute the game is currently in. Note: will be null when game is not in stoppage time"""

    clock_display: OptionalNullable[str] = Field(default=UNSET, alias="ClockDisplay")
    """A convenient string display of the current clock with format Clock+ClockExtra (example: 90+3)"""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score and stats have been verified and closed out"""

    home_team_formation: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamFormation")
    """The formation for the home team (4-4-2; 4-3-3; etc.)"""

    away_team_formation: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamFormation")
    """The formation for the away team (4-4-2, 4-3-3, etc.)"""

    playoff_aggregate_score: Optional[PlayoffAggregateScore2] = Field(default=UNSET, alias="PlayoffAggregateScore")
    """Aggregate scoring information for 2-leg/home-and-home games (i.e. Champions League Round of 16). Team A is
    determined by the first legs home team."""


class Game15Dict(TypedDict):
    game_id: NotRequired[int]
    round_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    group: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    venue_id: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    status: NotRequired[str | None]
    week: NotRequired[int | None]
    period: NotRequired[str | None]
    clock: NotRequired[int | None]
    winner: NotRequired[str | None]
    venue_type: NotRequired[str | None]
    away_team_key: NotRequired[str | None]
    away_team_name: NotRequired[str | None]
    away_team_country_code: NotRequired[str | None]
    away_team_score: NotRequired[int | None]
    away_team_score_period1: NotRequired[int | None]
    away_team_score_period2: NotRequired[int | None]
    away_team_score_extra_time: NotRequired[int | None]
    away_team_score_penalty: NotRequired[int | None]
    home_team_key: NotRequired[str | None]
    home_team_name: NotRequired[str | None]
    home_team_country_code: NotRequired[str | None]
    home_team_score: NotRequired[int | None]
    home_team_score_period1: NotRequired[int | None]
    home_team_score_period2: NotRequired[int | None]
    home_team_score_extra_time: NotRequired[int | None]
    home_team_score_penalty: NotRequired[int | None]
    home_team_money_line: NotRequired[int | None]
    away_team_money_line: NotRequired[int | None]
    draw_money_line: NotRequired[int | None]
    point_spread: NotRequired[float | None]
    home_team_point_spread_payout: NotRequired[int | None]
    away_team_point_spread_payout: NotRequired[int | None]
    over_under: NotRequired[float | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
    attendance: NotRequired[int | None]
    updated: NotRequired[str | None]
    updated_utc: NotRequired[str | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    clock_extra: NotRequired[int | None]
    clock_display: NotRequired[str | None]
    is_closed: NotRequired[bool | None]
    home_team_formation: NotRequired[str | None]
    away_team_formation: NotRequired[str | None]
    playoff_aggregate_score: NotRequired[PlayoffAggregateScore2 | PlayoffAggregateScore2Dict]
