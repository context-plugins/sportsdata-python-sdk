from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerGame6(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of the stat"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the player's team"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar; 6=Exhibition)."""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The WNBA season of the game"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: PG; SG; SF; PF; C"""

    started: OptionalNullable[int] = Field(default=UNSET, alias="Started")
    """Whether the player started in the game"""

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """Injury status used to project availability. Statuses: Probable; Questionable; Doubtful; Out. If a player has a
    NULL injury status, they are healthy/available to play."""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """"The player's body part(s) that are injured (e.g. Knee; Groin; Calf; Hamstring; etc.) Note: if a player has
    multiple injured body parts they will appear as such - Hamstring/Ankle"
    """

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The date that the injury occurred, was first discovered, or was freshly updated"""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """Short description of injury involving injured body part(s), game status, player name, team name, and other extra
    news necessary. Notes are custom and can be unique."""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    game_id: OptionalNullable[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

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

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)"""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The number of games played"""

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

    plus_minus: OptionalNullable[float] = Field(default=UNSET, alias="PlusMinus")
    """Total plus minus"""

    double_doubles: OptionalNullable[float] = Field(default=UNSET, alias="DoubleDoubles")
    """Total double-doubles scored"""

    triple_doubles: OptionalNullable[float] = Field(default=UNSET, alias="TripleDoubles")
    """Total triple-doubles scored"""


class PlayerGame6Dict(TypedDict):
    stat_id: NotRequired[int]
    team_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
    started: NotRequired[int | None]
    injury_status: NotRequired[str | None]
    injury_body_part: NotRequired[str | None]
    injury_start_date: NotRequired[str | None]
    injury_notes: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    game_id: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    home_or_away: NotRequired[str | None]
    is_game_over: NotRequired[bool]
    global_game_id: NotRequired[int | None]
    updated: NotRequired[str | None]
    games: NotRequired[int | None]
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
    assists: NotRequired[float | None]
    steals: NotRequired[float | None]
    blocked_shots: NotRequired[float | None]
    turnovers: NotRequired[float | None]
    personal_fouls: NotRequired[float | None]
    points: NotRequired[float | None]
    true_shooting_attempts: NotRequired[float | None]
    true_shooting_percentage: NotRequired[float | None]
    plus_minus: NotRequired[float | None]
    double_doubles: NotRequired[float | None]
    triple_doubles: NotRequired[float | None]
