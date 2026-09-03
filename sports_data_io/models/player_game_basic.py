from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerGameBasic(SdkBaseModel):
    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (in US Eastern Time)"""

    updated_utc: OptionalNullable[str] = Field(default=UNSET, alias="UpdatedUtc")
    """The timestamp of when the record was last updated (in UTC Time)"""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """Total number of games played by the player in the game"""

    minutes: OptionalNullable[float] = Field(default=UNSET, alias="Minutes")
    """Total regular time minutes played by the player in the game. Note: this excludes stoppage time minutes"""

    goals: OptionalNullable[float] = Field(default=UNSET, alias="Goals")
    """Total goals scored by the player in the game"""

    assists: OptionalNullable[float] = Field(default=UNSET, alias="Assists")
    """Total assists scored by the player in the game"""

    shots: OptionalNullable[float] = Field(default=UNSET, alias="Shots")
    """Total shots attempted by the player in the game"""

    shots_on_goal: OptionalNullable[float] = Field(default=UNSET, alias="ShotsOnGoal")
    """Total shots on goal attempted by the player in the game"""

    yellow_cards: OptionalNullable[float] = Field(default=UNSET, alias="YellowCards")
    """Total yellow cards against the player in the game"""

    red_cards: OptionalNullable[float] = Field(default=UNSET, alias="RedCards")
    """Total red cards against by the player in the game"""

    yellow_red_cards: OptionalNullable[float] = Field(default=UNSET, alias="YellowRedCards")
    """Total double yellow cards against the player in the game. Note: A double yellow card results in a red card"""

    crosses: OptionalNullable[float] = Field(default=UNSET, alias="Crosses")
    """Total crosses by the player in the game. Note: a cross means a pass from a wide area of the field towards the
    center of the field near the opponent's goal."""

    tackles_won: OptionalNullable[float] = Field(default=UNSET, alias="TacklesWon")
    """Total tackles won by the player in the game"""

    interceptions: OptionalNullable[float] = Field(default=UNSET, alias="Interceptions")
    """Total interceptions made by the player in the game"""

    own_goals: OptionalNullable[float] = Field(default=UNSET, alias="OwnGoals")
    """Total goals scored against own team (accidentally)"""

    fouls: OptionalNullable[float] = Field(default=UNSET, alias="Fouls")
    """Total fouls made by the player in the game"""

    fouled: OptionalNullable[float] = Field(default=UNSET, alias="Fouled")
    """Total times the player was fouled in the game"""

    offsides: OptionalNullable[float] = Field(default=UNSET, alias="Offsides")
    """Total offsides against by the player in the game"""

    passes: OptionalNullable[float] = Field(default=UNSET, alias="Passes")
    """Total passes attempted by the player in the game"""

    passes_completed: OptionalNullable[float] = Field(default=UNSET, alias="PassesCompleted")
    """Total passes completed by the player in the game"""

    last_man_tackle: OptionalNullable[float] = Field(default=UNSET, alias="LastManTackle")
    """Total tackles made by the player when there is no one else available to stop the opponent from scoring in the
    game"""

    corners_won: OptionalNullable[float] = Field(default=UNSET, alias="CornersWon")
    """Total corner kicks awarded to the player in the game"""

    blocked_shots: OptionalNullable[float] = Field(default=UNSET, alias="BlockedShots")
    """Total shots blocked by the player in the game"""

    touches: OptionalNullable[float] = Field(default=UNSET, alias="Touches")
    """Total times the player touched the ball in the game"""

    defender_clean_sheets: OptionalNullable[float] = Field(default=UNSET, alias="DefenderCleanSheets")
    """Total defender clean sheets by the player in the game. Note: clean sheets are awarded when zero goals were
    allowed to the opponent and the player played at least 60 minutes)."""

    goalkeeper_saves: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperSaves")
    """Total saves made by goalkeeper in the game"""

    goalkeeper_goals_against: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperGoalsAgainst")
    """Total goals allowed by goalkeeper in the game"""

    goalkeeper_single_goal_against: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperSingleGoalAgainst")
    """Total games where the goalkeeper allowed exactly one goal in the game"""

    goalkeeper_clean_sheets: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperCleanSheets")
    """Total number of clean sheets by the goalkeeper in the game. Note: Awarded when zero goals were allowed to the
    opponent and the player played at least 60 minutes"""

    goalkeeper_wins: OptionalNullable[float] = Field(default=UNSET, alias="GoalkeeperWins")
    """Total wins by the goalkeeper in the game"""

    penalty_kick_goals: OptionalNullable[float] = Field(default=UNSET, alias="PenaltyKickGoals")
    """Total penalty kick goals scored by the player in the game"""

    penalty_kick_misses: OptionalNullable[float] = Field(default=UNSET, alias="PenaltyKickMisses")
    """Total penalty kicks missed by the player in the game"""

    penalty_kick_saves: OptionalNullable[float] = Field(default=UNSET, alias="PenaltyKickSaves")
    """Total penalty kicks saved by the player in the game"""

    penalties_won: OptionalNullable[float] = Field(default=UNSET, alias="PenaltiesWon")
    """Total penalties won by the player in the game"""

    penalties_conceded: OptionalNullable[float] = Field(default=UNSET, alias="PenaltiesConceded")
    """Total penalties conceded by the player in the game"""

    score: OptionalNullable[float] = Field(default=UNSET, alias="Score")
    """Total goals scored by the player's team in the game"""

    opponent_score: OptionalNullable[float] = Field(default=UNSET, alias="OpponentScore")
    """Total goals scored against own team by the player in the game"""

    tackles: OptionalNullable[float] = Field(default=UNSET, alias="Tackles")
    """Total tackles by the player in the game"""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of the game"""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentId")
    """The unique ID of the team's opponent"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The name of the opponent team"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in UTC)"""

    home_or_away: OptionalNullable[str] = Field(default=UNSET, alias="HomeOrAway")
    """Whether the team is the home team or away team"""

    is_game_over: Optional[bool] = Field(default=UNSET, alias="IsGameOver")
    """Whether the game is over (true) or not (false)"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameId")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalOpponentId")
    """A globally unique ID for this opponent. This value is guaranteed to be unique across all sports/leagues."""

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
    career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The short name of the player"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the player's team"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The position of the player. Possible values include: A (Attacker); M (Midfielder); D (Defender); GK
    (Goalkeeper)"""

    jersey: Optional[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number"""

    started: OptionalNullable[int] = Field(default=UNSET, alias="Started")
    """The total number of games the player started"""

    captain: OptionalNullable[bool] = Field(default=UNSET, alias="Captain")
    """Whether the player is a captain (true/false)"""

    suspension: OptionalNullable[bool] = Field(default=UNSET, alias="Suspension")
    """Whether the player is suspended or not (true/false)"""

    suspension_reason: OptionalNullable[str] = Field(default=UNSET, alias="SuspensionReason")
    """The reason given for the player's suspension"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamId")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""


class PlayerGameBasicDict(TypedDict):
    updated: NotRequired[str | None]
    updated_utc: NotRequired[str | None]
    games: NotRequired[int | None]
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
    game_id: NotRequired[int | None]
    opponent_id: NotRequired[int | None]
    opponent: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    home_or_away: NotRequired[str | None]
    is_game_over: NotRequired[bool]
    global_game_id: NotRequired[int | None]
    global_opponent_id: NotRequired[int | None]
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
    jersey: NotRequired[int]
    started: NotRequired[int | None]
    captain: NotRequired[bool | None]
    suspension: NotRequired[bool | None]
    suspension_reason: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
