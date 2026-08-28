from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerGameProjection3(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of the stat"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 5=AllStar;
    6=Exhibition)"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The NHL season of the game"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: C; RW; LW; D; or G"""

    fantasy_data_salary: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDataSalary")
    """The player's salary as calculated by SportsDataIO (formerly known as FantasyData). Based on the same salary cap
    as DraftKings contests ($50,000)"""

    fan_duel_salary: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelSalary")
    """The player's salary for FanDuel daily fantasy contests"""

    draft_kings_salary: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsSalary")
    """The player's salary for DraftKings daily fantasy contests"""

    yahoo_salary: OptionalNullable[int] = Field(default=UNSET, alias="YahooSalary")
    """The player's salary for Yahoo daily fantasy contests."""

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """The player's current injury status; in the form of likelihood that player plays. Possible values: Probable;
    Questionable; Doubtful; Out"""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """The body part that is injured for the player (Knee; Groin; Calf; Upper-body; etc.)"""

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The day that the injury started or was first discovered"""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """Brief description of the player's injury and expected availability"""

    fan_duel_position: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelPosition")
    """The player's eligible position in FanDuel's daily fantasy sports platform"""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The player's eligible position in DraftKings' daily fantasy sports platform"""

    yahoo_position: OptionalNullable[str] = Field(default=UNSET, alias="YahooPosition")
    """The player's eligible position in Yahoo's daily fantasy sports platform."""

    opponent_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentRank")
    """The ranking of the player's opponent with regards to fantasy points allowed"""

    opponent_position_rank: OptionalNullable[int] = Field(default=UNSET, alias="OpponentPositionRank")
    """The ranking of the player's opponent by position with regards to fantasy points allowed"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    fantasy_draft_salary: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftSalary")
    """The player's salary for FantasyDraft daily fantasy contests"""

    fantasy_draft_position: OptionalNullable[str] = Field(default=UNSET, alias="FantasyDraftPosition")
    """The player's eligible position in Fantasy Drafts daily fantasy sports platform."""

    even_strength_minutes: OptionalNullable[int] = Field(default=UNSET, alias="EvenStrengthMinutes")
    """The number of minutes played at even strength by the player in the game"""

    even_strength_seconds: OptionalNullable[int] = Field(default=UNSET, alias="EvenStrengthSeconds")
    """The number of seconds played at even strength by the player in the game"""

    power_play_minutes: OptionalNullable[int] = Field(default=UNSET, alias="PowerPlayMinutes")
    """Total minutes played by the player on the power play in the game"""

    power_play_seconds: OptionalNullable[int] = Field(default=UNSET, alias="PowerPlaySeconds")
    """The number of seconds (remainder after minutes) played on a Power Play"""

    short_handed_minutes: OptionalNullable[int] = Field(default=UNSET, alias="ShortHandedMinutes")
    """The number of minutes played short handed by the player in the game"""

    short_handed_seconds: OptionalNullable[int] = Field(default=UNSET, alias="ShortHandedSeconds")
    """The number of seconds (remainder after minutes) played short handed by the player in the game"""

    points: OptionalNullable[float] = Field(default=UNSET, alias="Points")
    """Total points for the player in the game. Note: points are calculated by adding up a player's goals and assists"""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentID")
    """The unique ID of the team's opponent"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The name of the opponent"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Whether the team is home or away"""

    is_game_over: Optional[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether the game is over (true/false)"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalOpponentID")
    """A globally unique ID for this opponent. This value is guaranteed to be unique across all sports/leagues."""

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


class PlayerGameProjection3Dict(TypedDict):
    stat_id: NotRequired[int]
    team_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
    fantasy_data_salary: NotRequired[int | None]
    fan_duel_salary: NotRequired[int | None]
    draft_kings_salary: NotRequired[int | None]
    yahoo_salary: NotRequired[int | None]
    injury_status: NotRequired[str | None]
    injury_body_part: NotRequired[str | None]
    injury_start_date: NotRequired[str | None]
    injury_notes: NotRequired[str | None]
    fan_duel_position: NotRequired[str | None]
    draft_kings_position: NotRequired[str | None]
    yahoo_position: NotRequired[str | None]
    opponent_rank: NotRequired[int | None]
    opponent_position_rank: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    fantasy_draft_salary: NotRequired[int | None]
    fantasy_draft_position: NotRequired[str | None]
    even_strength_minutes: NotRequired[int | None]
    even_strength_seconds: NotRequired[int | None]
    power_play_minutes: NotRequired[int | None]
    power_play_seconds: NotRequired[int | None]
    short_handed_minutes: NotRequired[int | None]
    short_handed_seconds: NotRequired[int | None]
    points: NotRequired[float | None]
    game_id: NotRequired[int | None]
    opponent_id: NotRequired[int | None]
    opponent: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    home_or_away: NotRequired[str | None]
    is_game_over: NotRequired[bool]
    global_game_id: NotRequired[int | None]
    global_opponent_id: NotRequired[int | None]
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
