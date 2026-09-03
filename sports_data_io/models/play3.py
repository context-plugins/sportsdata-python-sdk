from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Play3(SdkBaseModel):
    play_id: Optional[int] = Field(default=UNSET, alias="PlayID")
    """The unique ID of the play"""

    period_id: Optional[int] = Field(default=UNSET, alias="PeriodID")
    """The unique ID of the period during which this play occurred"""

    period_name: OptionalNullable[str] = Field(default=UNSET, alias="PeriodName")
    """The name of the period that this play occurred in"""

    sequence: Optional[int] = Field(default=UNSET, alias="Sequence")
    """The order in which this play happened over the course of the game"""

    clock_minutes: OptionalNullable[int] = Field(default=UNSET, alias="ClockMinutes")
    """The number of minutes passed in the period when this play completed"""

    clock_seconds: OptionalNullable[int] = Field(default=UNSET, alias="ClockSeconds")
    """The number of seconds passed in the period when this play completed"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """The score of the away team after the play ended"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """The score of the home team after the play ended"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team associated with this play"""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentID")
    """The unique ID of the team's opponent associated with this play"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team"""

    category: OptionalNullable[str] = Field(default=UNSET, alias="Category")
    """The category of the play. Possible values: Block; Faceoff; Goal; Hit; Penalty; Period; Shootout; Shot; Stoppage;
    Turnover"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of the play. Possible values: AwayTeamTimeout, Block, Boarding, Charging, CheckToTheHead, Clipping,
    ClosingHandOnThePuck, CrossChecking, DelayOfGame, Elbowing, Faceoff, Fighting, GameMisconduct, Giveaway, Goal,
    GoalieStopped, HandPass, HighSticking, HighStickOnPuck, Hit, Holding, HoldingTheStick, HomeTeamTimeout, Hooking,
    Icing, IllegalEquipment, Interference, Kneeing, MinorPenalty, Misconduct, NetOffPost, ObjectsOnIce, Offside, Period,
    PeriodEnd, PlayerEquipment, PlayerInjury, PowerPlayGoal, PuckFrozen, PuckInBench, PuckInCrowd, PuckInNetting,
    Referee, RinkRepair, Roughing, ShootoutGoal, ShootoutMiss, ShootoutSave, ShotMissed, ShotOnGoal, Slashing, Stoppage,
    Takeaway, TooManyMen, Tripping, TvTimeout, Unsportsmanlike, VideoReview"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of the play (example: Sidney Crosby won faceoff against Aaron Ekblad)"""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when the play was last updated (in US Eastern Time)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The database generated timestamp of when this play was first created; based on US Eatern Time (EST/EDT)"""

    first_assisted_by_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FirstAssistedByPlayerID")
    """The PlayerID of the player who got the first assist on this play (if applicable)"""

    second_assisted_by_player_id: OptionalNullable[int] = Field(default=UNSET, alias="SecondAssistedByPlayerID")
    """The PlayerID of the player who got the second assist on this play (if applicable)"""

    power_play_team_id: OptionalNullable[int] = Field(default=UNSET, alias="PowerPlayTeamID")
    """The unique TeamID of the team on the power play this play (if any)"""

    power_play_team: OptionalNullable[str] = Field(default=UNSET, alias="PowerPlayTeam")
    """The abbreviation [Key] of the team on the power play this play (if any)"""

    opposing_player_id: OptionalNullable[int] = Field(default=UNSET, alias="OpposingPlayerID")
    """The PlayerID of the player involved in the play on the opposing team"""


class Play3Dict(TypedDict):
    play_id: NotRequired[int]
    period_id: NotRequired[int]
    period_name: NotRequired[str | None]
    sequence: NotRequired[int]
    clock_minutes: NotRequired[int | None]
    clock_seconds: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    opponent_id: NotRequired[int | None]
    opponent: NotRequired[str | None]
    category: NotRequired[str | None]
    type_: NotRequired[str | None]
    description: NotRequired[str | None]
    player_id: NotRequired[int | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    first_assisted_by_player_id: NotRequired[int | None]
    second_assisted_by_player_id: NotRequired[int | None]
    power_play_team_id: NotRequired[int | None]
    power_play_team: NotRequired[str | None]
    opposing_player_id: NotRequired[int | None]
