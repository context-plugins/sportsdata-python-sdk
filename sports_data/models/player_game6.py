from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerGame6(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatId")
    """The unique ID of the stat associated with this player"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The soccer regular season for which these totals apply"""

    round_id: OptionalNullable[int] = Field(default=UNSET, alias="RoundId")
    """The unique ID of the round that this player is associated with"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerId")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The short name of the player"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The name of the team"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The position of the player. Possible values include: A (Attacker); M (Midfielder); D (Defender); GK
    (Goalkeeper)."""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number"""

    started: OptionalNullable[int] = Field(default=UNSET, alias="Started")
    """The total number of games the player started"""

    captain: OptionalNullable[bool] = Field(default=UNSET, alias="Captain")
    """Whether the player is a captain (true/false)"""

    suspension: OptionalNullable[bool] = Field(default=UNSET, alias="Suspension")
    """Whether the player is suspended or not (true/false)"""

    suspension_reason: OptionalNullable[str] = Field(default=UNSET, alias="SuspensionReason")
    """The reason given for the player's suspension"""

    fan_duel_salary: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelSalary")
    """The player's salary for FanDuel daily fantasy contests."""

    draft_kings_salary: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsSalary")
    """The player's salary for DraftKings daily fantasy contests."""

    yahoo_salary: OptionalNullable[int] = Field(default=UNSET, alias="YahooSalary")
    """The player's salary for Yahoo daily fantasy contests"""

    mondogoal_salary: OptionalNullable[int] = Field(default=UNSET, alias="MondogoalSalary")
    """The player's salary for Mondogoal's daily fantasy contests"""

    fan_duel_position: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelPosition")
    """The player's eligible position in FanDuel's daily fantasy sports platform."""

    draft_kings_position: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsPosition")
    """The player's eligible position in DraftKings' daily fantasy sports platform."""

    yahoo_position: OptionalNullable[str] = Field(default=UNSET, alias="YahooPosition")
    """The player's eligible position in Yahoo's daily fantasy sports platform"""

    mondogoal_position: OptionalNullable[str] = Field(default=UNSET, alias="MondogoalPosition")
    """The player's eligible position in Mondogoal's daily fantasy sports platform."""

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """Indicates the player's injury status. Possible values: Questionable; Out."""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """The body part of the player that is injured (Knee; Groin; Calf; Hamstring; etc.)"""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """Not yet supported; will be null"""

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The date that the injury started or was first discovered"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamId")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    corners: OptionalNullable[float] = Field(default=UNSET, alias="Corners")
    """Total number of corner kicks taken by the player in the game"""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of this game"""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentId")
    """The unique ID of the team's opponent"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The name of the opponent"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (UTC)"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Whether the team is home or away"""

    is_game_over: Optional[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether the game is over (true/false)"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameId")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalOpponentId")
    """A globally unique ID for this opponent. This value is guaranteed to be unique across all sports/leagues."""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)"""

    updated_utc: OptionalNullable[str] = Field(default=UNSET, alias="UpdatedUtc")
    """The timestamp of when the record was last updated (UTC Time)"""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The number of games played"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Total Fan Duel daily fantasy points scored"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total Draft Kings daily fantasy points scored"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total Yahoo daily fantasy points scored"""

    fantasy_points_mondogoal: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsMondogoal")
    """Total Mondogoal fantasy points scored"""

    minutes: OptionalNullable[float] = Field(default=UNSET, alias="Minutes")
    """Total minutes played"""

    goals: OptionalNullable[float] = Field(default=UNSET, alias="Goals")
    """Total goals scored"""

    assists: OptionalNullable[float] = Field(default=UNSET, alias="Assists")
    """Total assists scored"""

    shots: OptionalNullable[float] = Field(default=UNSET, alias="Shots")
    """Total shots attempted"""

    shots_on_goal: OptionalNullable[float] = Field(default=UNSET, alias="ShotsOnGoal")
    """Total shots on goal attempted"""

    yellow_cards: OptionalNullable[float] = Field(default=UNSET, alias="YellowCards")
    """Total yellow cards against"""

    red_cards: OptionalNullable[float] = Field(default=UNSET, alias="RedCards")
    """Total red cards against"""

    yellow_red_cards: OptionalNullable[float] = Field(default=UNSET, alias="YellowRedCards")
    """Total double yellow cards against (which result in a red card)"""

    crosses: OptionalNullable[float] = Field(default=UNSET, alias="Crosses")
    """Total passes from a wide area of the field towards the center of the field near the opponent's goal"""

    tackles_won: OptionalNullable[float] = Field(default=UNSET, alias="TacklesWon")
    """Total tackles won"""

    interceptions: OptionalNullable[float] = Field(default=UNSET, alias="Interceptions")
    """Total interceptions made"""

    own_goals: OptionalNullable[float] = Field(default=UNSET, alias="OwnGoals")
    """Total goals scored against own team (accidentally)"""

    fouls: OptionalNullable[float] = Field(default=UNSET, alias="Fouls")
    """Total fouls made"""

    fouled: OptionalNullable[float] = Field(default=UNSET, alias="Fouled")
    """Total times fouled"""

    offsides: OptionalNullable[float] = Field(default=UNSET, alias="Offsides")
    """Total offsides against"""

    passes: OptionalNullable[float] = Field(default=UNSET, alias="Passes")
    """Total passes attempted"""

    passes_completed: OptionalNullable[float] = Field(default=UNSET, alias="PassesCompleted")
    """Total passes completed successfully to teammate"""

    last_man_tackle: OptionalNullable[float] = Field(default=UNSET, alias="LastManTackle")
    """Total tackles made when there is no one else available to stop the opponent from scoring (this can be the
    goalkeeper)"""

    corners_won: OptionalNullable[float] = Field(default=UNSET, alias="CornersWon")
    """Total corner kicks awarded"""

    blocked_shots: OptionalNullable[float] = Field(default=UNSET, alias="BlockedShots")
    """Total shots blocked"""

    touches: OptionalNullable[float] = Field(default=UNSET, alias="Touches")
    """Total times this player touched the ball"""

    defender_clean_sheets: OptionalNullable[float] = Field(default=UNSET, alias="DefenderCleanSheets")
    """Total defender clean sheets (awarded when zero goals were allowed to the opponent and the player played at least
    60 minutes)"""

    goalkeeper_saves: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperSaves")
    """Total saves made by goalkeeper"""

    goalkeeper_goals_against: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperGoalsAgainst")
    """Total goals allowed by goalkeeper"""

    goalkeeper_single_goal_against: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperSingleGoalAgainst")
    """Total games where this goalkeeper allowed exactly one goal"""

    goalkeeper_clean_sheets: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperCleanSheets")
    """Total goalkeeper clean sheets (awarded when zero goals were allowed to the opponent and the player played at
    least 60 minutes)"""

    goalkeeper_wins: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperWins")
    """Total goalkeeper wins (awarded when zero goals were allowed to the opponent and the player played at least 45
    minutes)"""

    penalty_kick_goals: OptionalNullable[float] = Field(default=UNSET, alias="PenaltyKickGoals")
    """Total penalty kick goals"""

    penalty_kick_misses: OptionalNullable[float] = Field(default=UNSET, alias="PenaltyKickMisses")
    """Total penalty kick misses"""

    penalty_kick_saves: OptionalNullable[float] = Field(default=UNSET, alias="PenaltyKickSaves")
    """Total penalty kick saves"""

    penalties_won: OptionalNullable[float] = Field(default=UNSET, alias="PenaltiesWon")
    """Total penalties won"""

    penalties_conceded: OptionalNullable[float] = Field(default=UNSET, alias="PenaltiesConceded")
    """Total penalties conceded"""

    score: OptionalNullable[float] = Field(default=UNSET, alias="Score")
    """Goals scored by entire team"""

    opponent_score: OptionalNullable[float] = Field(default=UNSET, alias="OpponentScore")
    """Goals allowed to opponent"""

    tackles: OptionalNullable[float] = Field(default=UNSET, alias="Tackles")
    """Total Tackles"""


class PlayerGame6Dict(TypedDict):
    stat_id: NotRequired[int]
    season_type: NotRequired[int]
    season: NotRequired[int]
    round_id: NotRequired[int | None]
    team_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    name: NotRequired[str | None]
    short_name: NotRequired[str | None]
    team: NotRequired[str | None]
    position_category: NotRequired[str | None]
    position: NotRequired[str | None]
    jersey: NotRequired[int | None]
    started: NotRequired[int | None]
    captain: NotRequired[bool | None]
    suspension: NotRequired[bool | None]
    suspension_reason: NotRequired[str | None]
    fan_duel_salary: NotRequired[int | None]
    draft_kings_salary: NotRequired[int | None]
    yahoo_salary: NotRequired[int | None]
    mondogoal_salary: NotRequired[int | None]
    fan_duel_position: NotRequired[str | None]
    draft_kings_position: NotRequired[str | None]
    yahoo_position: NotRequired[str | None]
    mondogoal_position: NotRequired[str | None]
    injury_status: NotRequired[str | None]
    injury_body_part: NotRequired[str | None]
    injury_notes: NotRequired[str | None]
    injury_start_date: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    corners: NotRequired[float | None]
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
    updated_utc: NotRequired[str | None]
    games: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    fantasy_points_mondogoal: NotRequired[float | None]
    minutes: NotRequired[float | None]
    goals: NotRequired[float | None]
    assists: NotRequired[float | None]
    shots: NotRequired[float | None]
    shots_on_goal: NotRequired[float | None]
    yellow_cards: NotRequired[float | None]
    red_cards: NotRequired[float | None]
    yellow_red_cards: NotRequired[float | None]
    crosses: NotRequired[float | None]
    tackles_won: NotRequired[float | None]
    interceptions: NotRequired[float | None]
    own_goals: NotRequired[float | None]
    fouls: NotRequired[float | None]
    fouled: NotRequired[float | None]
    offsides: NotRequired[float | None]
    passes: NotRequired[float | None]
    passes_completed: NotRequired[float | None]
    last_man_tackle: NotRequired[float | None]
    corners_won: NotRequired[float | None]
    blocked_shots: NotRequired[float | None]
    touches: NotRequired[float | None]
    defender_clean_sheets: NotRequired[float | None]
    goalkeeper_saves: NotRequired[float | None]
    goalkeeper_goals_against: NotRequired[float | None]
    goalkeeper_single_goal_against: NotRequired[float | None]
    goalkeeper_clean_sheets: NotRequired[float | None]
    goalkeeper_wins: NotRequired[float | None]
    penalty_kick_goals: NotRequired[float | None]
    penalty_kick_misses: NotRequired[float | None]
    penalty_kick_saves: NotRequired[float | None]
    penalties_won: NotRequired[float | None]
    penalties_conceded: NotRequired[float | None]
    score: NotRequired[float | None]
    opponent_score: NotRequired[float | None]
    tackles: NotRequired[float | None]
