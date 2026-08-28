from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .opponent_season21 import OpponentSeason21, OpponentSeason21Dict


class TeamSeason5(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of the stat"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 5=AllStar;
    6=Exhibition)"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The NHL regular season for which these totals apply"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The team's full name (ex. Minnesota Wild; New York Islanders)"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """Total number of wins by the team in the season"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """Total losses for the team in the season"""

    overtime_losses: OptionalNullable[int] = Field(default=UNSET, alias="OvertimeLosses")
    """Total overtime losses by the team in the season"""

    opponent_position: OptionalNullable[str] = Field(default=UNSET, alias="OpponentPosition")
    """Indicates which position is included in opponent stats that are aggregated together"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    opponent_stat: Optional[OpponentSeason21] = Field(default=UNSET, alias="OpponentStat")
    """The aggregated season stats for this team's opponents"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)."""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The number of games played."""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Total FanDuel daily fantasy points scored"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total DraftKings daily fantasy points scored"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total Yahoo daily fantasy points scored"""

    minutes: OptionalNullable[int] = Field(default=UNSET, alias="Minutes")
    """Total number of minutes played"""

    seconds: OptionalNullable[int] = Field(default=UNSET, alias="Seconds")
    """Total number of seconds played"""

    goals: OptionalNullable[float] = Field(default=UNSET, alias="Goals")
    """Total number of goals scored"""

    assists: OptionalNullable[float] = Field(default=UNSET, alias="Assists")
    """Total number of assists"""

    shots_on_goal: OptionalNullable[float] = Field(default=UNSET, alias="ShotsOnGoal")
    """Total number of shots on goal"""

    power_play_goals: OptionalNullable[float] = Field(default=UNSET, alias="PowerPlayGoals")
    """Total number of power play goals"""

    short_handed_goals: OptionalNullable[float] = Field(default=UNSET, alias="ShortHandedGoals")
    """Total number of short handed goals"""

    empty_net_goals: OptionalNullable[float] = Field(default=UNSET, alias="EmptyNetGoals")
    """Total number of empty net goals"""

    power_play_assists: OptionalNullable[float] = Field(default=UNSET, alias="PowerPlayAssists")
    """Total number of power play assists"""

    short_handed_assists: OptionalNullable[float] = Field(default=UNSET, alias="ShortHandedAssists")
    """Total number of short handed assists"""

    hat_tricks: OptionalNullable[float] = Field(default=UNSET, alias="HatTricks")
    """Total number of hat tricks"""

    shootout_goals: OptionalNullable[float] = Field(default=UNSET, alias="ShootoutGoals")
    """Total number of shootout goals"""

    plus_minus: OptionalNullable[float] = Field(default=UNSET, alias="PlusMinus")
    """Total plus minus"""

    penalty_minutes: OptionalNullable[float] = Field(default=UNSET, alias="PenaltyMinutes")
    """Total pentalty minutes"""

    blocks: OptionalNullable[float] = Field(default=UNSET, alias="Blocks")
    """Total blocked shots"""

    hits: OptionalNullable[float] = Field(default=UNSET, alias="Hits")
    """Total hits"""

    takeaways: OptionalNullable[float] = Field(default=UNSET, alias="Takeaways")
    """Total takeaways"""

    giveaways: OptionalNullable[float] = Field(default=UNSET, alias="Giveaways")
    """Total giveaways"""

    faceoffs_won: OptionalNullable[float] = Field(default=UNSET, alias="FaceoffsWon")
    """Total faceoffs won"""

    faceoffs_lost: OptionalNullable[float] = Field(default=UNSET, alias="FaceoffsLost")
    """Total faceoffs lost"""

    shifts: OptionalNullable[float] = Field(default=UNSET, alias="Shifts")
    """Total shifts"""

    goaltending_minutes: OptionalNullable[int] = Field(default=UNSET, alias="GoaltendingMinutes")
    """Total goaltending minutes"""

    goaltending_seconds: OptionalNullable[int] = Field(default=UNSET, alias="GoaltendingSeconds")
    """Total goaltending seconds"""

    goaltending_shots_against: OptionalNullable[float] = Field(default=UNSET, alias="GoaltendingShotsAgainst")
    """Total goaltending shots against"""

    goaltending_goals_against: OptionalNullable[float] = Field(default=UNSET, alias="GoaltendingGoalsAgainst")
    """Total goaltending goals against"""

    goaltending_saves: OptionalNullable[float] = Field(default=UNSET, alias="GoaltendingSaves")
    """Total goaltending saves"""

    goaltending_wins: OptionalNullable[float] = Field(default=UNSET, alias="GoaltendingWins")
    """Total goaltending wins"""

    goaltending_losses: OptionalNullable[float] = Field(default=UNSET, alias="GoaltendingLosses")
    """Total goaltendings losses"""

    goaltending_shutouts: OptionalNullable[float] = Field(default=UNSET, alias="GoaltendingShutouts")
    """Total goaltendings shutouts"""

    started: OptionalNullable[int] = Field(default=UNSET, alias="Started")
    """Total games started"""

    bench_penalty_minutes: OptionalNullable[float] = Field(default=UNSET, alias="BenchPenaltyMinutes")
    """Total bench pentalty minutes"""

    goaltending_overtime_losses: OptionalNullable[float] = Field(default=UNSET, alias="GoaltendingOvertimeLosses")
    """Total goaltending overtime losses"""

    fantasy_points_fantasy_draft: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFantasyDraft")
    """Total FantasyDraft daily fantasy points scored"""


class TeamSeason5Dict(TypedDict):
    stat_id: NotRequired[int]
    team_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    overtime_losses: NotRequired[int | None]
    opponent_position: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    opponent_stat: NotRequired[OpponentSeason21 | OpponentSeason21Dict]
    updated: NotRequired[str | None]
    games: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    minutes: NotRequired[int | None]
    seconds: NotRequired[int | None]
    goals: NotRequired[float | None]
    assists: NotRequired[float | None]
    shots_on_goal: NotRequired[float | None]
    power_play_goals: NotRequired[float | None]
    short_handed_goals: NotRequired[float | None]
    empty_net_goals: NotRequired[float | None]
    power_play_assists: NotRequired[float | None]
    short_handed_assists: NotRequired[float | None]
    hat_tricks: NotRequired[float | None]
    shootout_goals: NotRequired[float | None]
    plus_minus: NotRequired[float | None]
    penalty_minutes: NotRequired[float | None]
    blocks: NotRequired[float | None]
    hits: NotRequired[float | None]
    takeaways: NotRequired[float | None]
    giveaways: NotRequired[float | None]
    faceoffs_won: NotRequired[float | None]
    faceoffs_lost: NotRequired[float | None]
    shifts: NotRequired[float | None]
    goaltending_minutes: NotRequired[int | None]
    goaltending_seconds: NotRequired[int | None]
    goaltending_shots_against: NotRequired[float | None]
    goaltending_goals_against: NotRequired[float | None]
    goaltending_saves: NotRequired[float | None]
    goaltending_wins: NotRequired[float | None]
    goaltending_losses: NotRequired[float | None]
    goaltending_shutouts: NotRequired[float | None]
    started: NotRequired[int | None]
    bench_penalty_minutes: NotRequired[float | None]
    goaltending_overtime_losses: NotRequired[float | None]
    fantasy_points_fantasy_draft: NotRequired[float | None]
