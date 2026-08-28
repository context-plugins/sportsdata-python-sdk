from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerSeason(SdkBaseModel):
    stat_id: Optional[int] = Field(default=UNSET, alias="StatID")
    """The unique ID of the stat"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the player's team"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their collegiate career"""

    season_type: OptionalNullable[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=AllStar)"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The season that the game the player is playing in occurs. Note: season is a single year that the majority of the
    season occurs in"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the player's team"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's eligible position(s). Possible values: C; F; F-C; G; G-F, PG, SG, SF, PF"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the record was last updated (US Eastern Time)."""

    games: OptionalNullable[int] = Field(default=UNSET, alias="Games")
    """The number of games played."""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """Total fantasy points"""

    minutes: OptionalNullable[int] = Field(default=UNSET, alias="Minutes")
    """Total number of minutes played"""

    field_goals_made: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalsMade")
    """Total number of field goals made"""

    field_goals_attempted: OptionalNullable[int] = Field(default=UNSET, alias="FieldGoalsAttempted")
    """Total number of field goals attempted"""

    field_goals_percentage: OptionalNullable[float] = Field(default=UNSET, alias="FieldGoalsPercentage")
    """Total field goal percentage"""

    effective_field_goals_percentage: OptionalNullable[float] = Field(
        default=UNSET, alias="EffectiveFieldGoalsPercentage"
    )
    """Total effective field goals percentage"""

    two_pointers_made: OptionalNullable[int] = Field(default=UNSET, alias="TwoPointersMade")
    """Total two pointers made"""

    two_pointers_attempted: OptionalNullable[int] = Field(default=UNSET, alias="TwoPointersAttempted")
    """Total two pointers attempted"""

    two_pointers_percentage: OptionalNullable[float] = Field(default=UNSET, alias="TwoPointersPercentage")
    """Total two pointers percentage"""

    three_pointers_made: OptionalNullable[int] = Field(default=UNSET, alias="ThreePointersMade")
    """Total three pointers made"""

    three_pointers_attempted: OptionalNullable[int] = Field(default=UNSET, alias="ThreePointersAttempted")
    """Total three pointers attempted"""

    three_pointers_percentage: OptionalNullable[float] = Field(default=UNSET, alias="ThreePointersPercentage")
    """Total three pointers percentage"""

    free_throws_made: OptionalNullable[int] = Field(default=UNSET, alias="FreeThrowsMade")
    """Total free throws made"""

    free_throws_attempted: OptionalNullable[int] = Field(default=UNSET, alias="FreeThrowsAttempted")
    """Total free throws attempted"""

    free_throws_percentage: OptionalNullable[float] = Field(default=UNSET, alias="FreeThrowsPercentage")
    """Total free throws percentage"""

    offensive_rebounds: OptionalNullable[int] = Field(default=UNSET, alias="OffensiveRebounds")
    """Total offensive rebounds"""

    defensive_rebounds: OptionalNullable[int] = Field(default=UNSET, alias="DefensiveRebounds")
    """Total defensive rebounds"""

    rebounds: OptionalNullable[int] = Field(default=UNSET, alias="Rebounds")
    """Total rebounds"""

    offensive_rebounds_percentage: OptionalNullable[float] = Field(default=UNSET, alias="OffensiveReboundsPercentage")
    """Total offensive rebounds percentage"""

    defensive_rebounds_percentage: OptionalNullable[float] = Field(default=UNSET, alias="DefensiveReboundsPercentage")
    """Total defensive rebounds percentage"""

    total_rebounds_percentage: OptionalNullable[float] = Field(default=UNSET, alias="TotalReboundsPercentage")
    """The player/team total rebounds percentage"""

    assists: OptionalNullable[int] = Field(default=UNSET, alias="Assists")
    """Total assists"""

    steals: OptionalNullable[int] = Field(default=UNSET, alias="Steals")
    """Total steals"""

    blocked_shots: OptionalNullable[int] = Field(default=UNSET, alias="BlockedShots")
    """Total blocked shots"""

    turnovers: OptionalNullable[int] = Field(default=UNSET, alias="Turnovers")
    """Total turnovers"""

    personal_fouls: OptionalNullable[int] = Field(default=UNSET, alias="PersonalFouls")
    """Total personal fouls"""

    points: OptionalNullable[int] = Field(default=UNSET, alias="Points")
    """Total points"""

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
    """Total Fan Duel daily fantasy points scored"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """Total Draft Kings daily fantasy points scored"""

    fantasy_points_yahoo: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsYahoo")
    """Total Yahoo daily fantasy points scored"""


class PlayerSeasonDict(TypedDict):
    stat_id: NotRequired[int]
    team_id: NotRequired[int | None]
    player_id: NotRequired[int | None]
    season_type: NotRequired[int | None]
    season: NotRequired[int | None]
    name: NotRequired[str | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    updated: NotRequired[str | None]
    games: NotRequired[int | None]
    fantasy_points: NotRequired[float | None]
    minutes: NotRequired[int | None]
    field_goals_made: NotRequired[int | None]
    field_goals_attempted: NotRequired[int | None]
    field_goals_percentage: NotRequired[float | None]
    effective_field_goals_percentage: NotRequired[float | None]
    two_pointers_made: NotRequired[int | None]
    two_pointers_attempted: NotRequired[int | None]
    two_pointers_percentage: NotRequired[float | None]
    three_pointers_made: NotRequired[int | None]
    three_pointers_attempted: NotRequired[int | None]
    three_pointers_percentage: NotRequired[float | None]
    free_throws_made: NotRequired[int | None]
    free_throws_attempted: NotRequired[int | None]
    free_throws_percentage: NotRequired[float | None]
    offensive_rebounds: NotRequired[int | None]
    defensive_rebounds: NotRequired[int | None]
    rebounds: NotRequired[int | None]
    offensive_rebounds_percentage: NotRequired[float | None]
    defensive_rebounds_percentage: NotRequired[float | None]
    total_rebounds_percentage: NotRequired[float | None]
    assists: NotRequired[int | None]
    steals: NotRequired[int | None]
    blocked_shots: NotRequired[int | None]
    turnovers: NotRequired[int | None]
    personal_fouls: NotRequired[int | None]
    points: NotRequired[int | None]
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
