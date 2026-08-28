from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TeamGame3(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of the stat"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar; 6=Exhibition)"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The NBA season of the game"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Team's name"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """Total number of team wins"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """Total number of team losses"""

    possessions: OptionalNullable[float] = Field(default=UNSET, alias="Possessions")
    """Total number of estimated possessions by the team in the game"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

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
    """The timestamp of when the record was last updated (US Eastern Time)"""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The number of games played"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points"""

    minutes: OptionalNullable[int] = Field(default=UNSET, alias="Minutes")
    """Total number of minutes played"""

    seconds: OptionalNullable[int] = Field(default=UNSET, alias="Seconds")
    """Total number of seconds played"""

    field_goals_made: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsMade")
    """Total number of field goals made"""

    field_goals_attempted: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsAttempted")
    """Total number of field goals attempted"""

    field_goals_percentage: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsPercentage")
    """Total field goal percentage"""

    effective_field_goals_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="EffectiveFieldGoalsPercentage"
    )
    """Total effective field goals percentage"""

    two_pointers_made: OptionalNullable[float] = Field(default=UNSET, alias="TwoPointersMade")
    """Total two pointers made"""

    two_pointers_attempted: OptionalNullable[float] = Field(default=UNSET, alias="TwoPointersAttempted")
    """Total two pointers attempted"""

    two_pointers_percentage: OptionalNullable[float] = Field(default=UNSET, alias="TwoPointersPercentage")
    """Total two pointers percentage"""

    three_pointers_made: OptionalNullable[float] = Field(default=UNSET, alias="ThreePointersMade")
    """Total three pointers made"""

    three_pointers_attempted: OptionalNullable[float] = Field(default=UNSET, alias="ThreePointersAttempted")
    """Total three pointers attempted"""

    three_pointers_percentage: OptionalNullable[float] = Field(default=UNSET, alias="ThreePointersPercentage")
    """Total three pointers percentage"""

    free_throws_made: OptionalNullable[float] = Field(default=UNSET, alias="FreeThrowsMade")
    """Total free throws made"""

    free_throws_attempted: OptionalNullable[float] = Field(default=UNSET, alias="FreeThrowsAttempted")
    """Total free throws attempted"""

    free_throws_percentage: OptionalNullable[float] = Field(default=UNSET, alias="FreeThrowsPercentage")
    """Total free throws percentage"""

    offensive_rebounds: OptionalNullable[float] = Field(default=UNSET, alias="OffensiveRebounds")
    """Total offensive rebounds"""

    defensive_rebounds: OptionalNullable[float] = Field(default=UNSET, alias="DefensiveRebounds")
    """Total defensive rebounds"""

    rebounds: OptionalNullable[float] = Field(default=UNSET, alias="Rebounds")
    """Total rebounds"""

    offensive_rebounds_percentage: OptionalNullable[float] = Field(default=UNSET, alias="OffensiveReboundsPercentage")
    """Total offensive rebounds percentage"""

    defensive_rebounds_percentage: OptionalNullable[float] = Field(default=UNSET, alias="DefensiveReboundsPercentage")
    """Total defensive rebounds percentage"""

    total_rebounds_percentage: OptionalNullable[float] = Field(default=UNSET, alias="TotalReboundsPercentage")
    """The player/team total rebounds percentage"""

    assists: OptionalNullable[float] = Field(default=UNSET, alias="Assists")
    """Total assists"""

    steals: OptionalNullable[float] = Field(default=UNSET, alias="Steals")
    """Total steals"""

    blocked_shots: OptionalNullable[float] = Field(default=UNSET, alias="BlockedShots")
    """Total blocked shots"""

    turnovers: OptionalNullable[float] = Field(default=UNSET, alias="Turnovers")
    """Total turnovers"""

    personal_fouls: OptionalNullable[float] = Field(default=UNSET, alias="PersonalFouls")
    """Total personal fouls"""

    points: OptionalNullable[float] = Field(default=UNSET, alias="Points")
    """Total points scored"""

    true_shooting_attempts: OptionalNullable[float] = Field(default=UNSET, alias="TrueShootingAttempts")
    """The player's true shooting attempts as defined here: http://www.basketball-reference.com/about/glossary.html"""

    true_shooting_percentage: OptionalNullable[float] = Field(default=UNSET, alias="TrueShootingPercentage")
    """The player's true shooting percentage as defined here: http://www.basketball-reference.com/about/glossary.html"""

    player_efficiency_rating: OptionalNullable[float] = Field(default=UNSET, alias="PlayerEfficiencyRating")
    """The player's linear weight efficiency rating as defined here:
    http://bleacherreport.com/articles/113144-cracking-the-code-how-to-calculate-hollingers-per-without-all-the-mess"""

    assists_percentage: OptionalNullable[float] = Field(default=UNSET, alias="AssistsPercentage")
    """The player's assist percentage as defined here: http://www.basketball-reference.com/about/glossary.html"""

    steals_percentage: OptionalNullable[float] = Field(default=UNSET, alias="StealsPercentage")
    """The player's steal percentage as defined here: http://www.basketball-reference.com/about/glossary.html"""

    blocks_percentage: OptionalNullable[float] = Field(default=UNSET, alias="BlocksPercentage")
    """The player's block percentage as defined here: http://www.basketball-reference.com/about/glossary.html"""

    turn_overs_percentage: OptionalNullable[float] = Field(default=UNSET, alias="TurnOversPercentage")
    """The player's turnover percentage as defined here: http://www.basketball-reference.com/about/glossary.html"""

    usage_rate_percentage: OptionalNullable[float] = Field(default=UNSET, alias="UsageRatePercentage")
    """The player's usage rate percentage as defined here: http://www.basketball-reference.com/about/glossary.html"""

    fantasy_points_fan_duel: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFanDuel")
    """Total FanDuel daily fantasy points scored"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total DraftKings daily fantasy points scored"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total Yahoo daily fantasy points scored"""

    plus_minus: OptionalNullable[float] = Field(default=UNSET, alias="PlusMinus")
    """Total plus minus"""

    double_doubles: OptionalNullable[float] = Field(default=UNSET, alias="DoubleDoubles")
    """Total double-doubles scored"""

    triple_doubles: OptionalNullable[float] = Field(default=UNSET, alias="TripleDoubles")
    """Total triple-doubles scored"""

    fantasy_points_fantasy_draft: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsFantasyDraft")
    """Total FantasyDraft daily fantasy points scored"""

    is_closed: Optional[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the stats for this player have been verified and closed out."""

    lineup_confirmed: OptionalNullable[bool] = Field(default=UNSET, alias="LineupConfirmed")
    """Indicates whether starting lineup is confirmed"""

    lineup_status: OptionalNullable[str] = Field(default=UNSET, alias="LineupStatus")
    """Indicates whether player is starting, active, or inactive"""


class TeamGame3Dict(TypedDict):
    stat_id: NotRequired[int]
    team_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    possessions: NotRequired[float | None]
    global_team_id: NotRequired[int | None]
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
    minutes: NotRequired[int | None]
    seconds: NotRequired[int | None]
    field_goals_made: NotRequired[float | None]
    field_goals_attempted: NotRequired[float | None]
    field_goals_percentage: NotRequired[float | None]
    effective_field_goals_percentage: NotRequired[float | None]
    two_pointers_made: NotRequired[float | None]
    two_pointers_attempted: NotRequired[float | None]
    two_pointers_percentage: NotRequired[float | None]
    three_pointers_made: NotRequired[float | None]
    three_pointers_attempted: NotRequired[float | None]
    three_pointers_percentage: NotRequired[float | None]
    free_throws_made: NotRequired[float | None]
    free_throws_attempted: NotRequired[float | None]
    free_throws_percentage: NotRequired[float | None]
    offensive_rebounds: NotRequired[float | None]
    defensive_rebounds: NotRequired[float | None]
    rebounds: NotRequired[float | None]
    offensive_rebounds_percentage: NotRequired[float | None]
    defensive_rebounds_percentage: NotRequired[float | None]
    total_rebounds_percentage: NotRequired[float | None]
    assists: NotRequired[float | None]
    steals: NotRequired[float | None]
    blocked_shots: NotRequired[float | None]
    turnovers: NotRequired[float | None]
    personal_fouls: NotRequired[float | None]
    points: NotRequired[float | None]
    true_shooting_attempts: NotRequired[float | None]
    true_shooting_percentage: NotRequired[float | None]
    player_efficiency_rating: NotRequired[float | None]
    assists_percentage: NotRequired[float | None]
    steals_percentage: NotRequired[float | None]
    blocks_percentage: NotRequired[float | None]
    turn_overs_percentage: NotRequired[float | None]
    usage_rate_percentage: NotRequired[float | None]
    fantasy_points_fan_duel: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    fantasy_points_yahoo: NotRequired[float | None]
    plus_minus: NotRequired[float | None]
    double_doubles: NotRequired[float | None]
    triple_doubles: NotRequired[float | None]
    fantasy_points_fantasy_draft: NotRequired[float | None]
    is_closed: NotRequired[bool]
    lineup_confirmed: NotRequired[bool | None]
    lineup_status: NotRequired[str | None]
