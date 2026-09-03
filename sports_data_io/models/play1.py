from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Play1(SdkBaseModel):
    play_id: Optional[int] = Field(default=UNSET, alias="PlayID")
    """The unique identifier of the play."""

    quarter_id: Optional[int] = Field(default=UNSET, alias="QuarterID")
    """The unique identifier of the Quarter that this play occurred in."""

    quarter_name: OptionalNullable[str] = Field(default=UNSET, alias="QuarterName")
    """The name of the quarter that this play occurred in"""

    sequence: Optional[int] = Field(default=UNSET, alias="Sequence")
    """The order in which this play happened over the course of the game."""

    time_remaining_minutes: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingMinutes")
    """The number of minutes remaining in the quarter when this play occurred"""

    time_remaining_seconds: OptionalNullable[int] = Field(default=UNSET, alias="TimeRemainingSeconds")
    """The number of seconds remaining in the quarter when the play occurred"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Total number of points the away team scored after this play completed"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Total points scored by the home team after the completion of this play"""

    potential_points: OptionalNullable[int] = Field(default=UNSET, alias="PotentialPoints")
    """The points that would have been potentially scored by the shot attempt (if any)."""

    points: OptionalNullable[int] = Field(default=UNSET, alias="Points")
    """The points scores by the shot attempt (if any)."""

    shot_made: OptionalNullable[bool] = Field(default=UNSET, alias="ShotMade")
    """Whether the shot was made (if any)."""

    category: OptionalNullable[str] = Field(default=UNSET, alias="Category")
    """The category the play. Possible values: Period, Timeout, JumpBall, Shot, Rebound, Foul, Substitution, Turnover,
    Challenge."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The type of the play. Possible values: None, Period, Timeout, JumpBall, FieldGoalMade, FieldGoalMissed,
    FreeThrowMade, FreeThrowMissed, Rebound, Steal, Turnover, Foul, PersonalFoul, ShootingFoul, OffensiveFoul,
    LooseBallFoul, TechnicalFoul, FlagrantFoul, Traveling, Palming, Goaltending, KickedBall, LaneViolation, DelayOfGame,
    Substitution, Ejection, and Challenge."""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team associated with this play"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team associated with this play"""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentID")
    """The unique ID of the opponent team associated with this play"""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """Abbreviation [Key] of the opponent team (e.g. LAL; PHI; BOS; CHI; etc.)"""

    receiving_team_id: OptionalNullable[int] = Field(default=UNSET, alias="ReceivingTeamID")
    """The TeamID of the team that won the jump ball."""

    receiving_team: OptionalNullable[str] = Field(default=UNSET, alias="ReceivingTeam")
    """The team abbreviation [Key] of the team that won the jump ball"""

    description: OptionalNullable[str] = Field(default=UNSET, alias="Description")
    """The description of the play."""

    player_id: OptionalNullable[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    assisted_by_player_id: OptionalNullable[int] = Field(default=UNSET, alias="AssistedByPlayerID")
    """The PlayerID of the player who recorded an assist on a made field goal by another player (if applicable)"""

    blocked_by_player_id: OptionalNullable[int] = Field(default=UNSET, alias="BlockedByPlayerID")
    """The PlayerID of the player who blocked the field goal attempt on this play (if any)."""

    fast_break: OptionalNullable[bool] = Field(default=UNSET, alias="FastBreak")
    """Indicates whether this play happened on a fast break."""

    side_of_basket: OptionalNullable[str] = Field(default=UNSET, alias="SideOfBasket")
    """The side of the basket that the field goal was attempted from (if any). Possible values: L, R"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when this play was last updated (in US Eastern Time)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The database generated timestamp of when this play was first created (in US Eastern Time)"""

    substitute_in_player_id: OptionalNullable[int] = Field(default=UNSET, alias="SubstituteInPlayerID")
    """The PlayerID of the player who substituted into the game."""

    substitute_out_player_id: OptionalNullable[int] = Field(default=UNSET, alias="SubstituteOutPlayerID")
    """The PlayerID of the player who substituted out of the game."""

    away_player_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayPlayerID")
    """The PlayerID of the player who is involved in the play from the away team (if applicable)"""

    home_player_id: OptionalNullable[int] = Field(default=UNSET, alias="HomePlayerID")
    """The PlayerID of the player who is involved in the play from the home team"""

    receiving_player_id: OptionalNullable[int] = Field(default=UNSET, alias="ReceivingPlayerID")
    """The PlayerID of the player who received the ball"""

    baseline_offset_percentage: OptionalNullable[float] = Field(default=UNSET, alias="BaselineOffsetPercentage")
    """The baseline offset percentage of where the ball was shot/passed"""

    sideline_offset_percentage: OptionalNullable[float] = Field(default=UNSET, alias="SidelineOffsetPercentage")
    """The sideline offset percentage of where the ball was shot/passed"""

    coordinates: OptionalNullable[str] = Field(default=UNSET, alias="Coordinates")
    """The x/y coordinates of where the ball was shot/passed"""

    stolen_by_player_id: OptionalNullable[int] = Field(default=UNSET, alias="StolenByPlayerID")
    """The PlayerID of the player who stole the ball (if applicable)"""


class Play1Dict(TypedDict):
    play_id: NotRequired[int]
    quarter_id: NotRequired[int]
    quarter_name: NotRequired[str | None]
    sequence: NotRequired[int]
    time_remaining_minutes: NotRequired[int | None]
    time_remaining_seconds: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    home_team_score: NotRequired[int | None]
    potential_points: NotRequired[int | None]
    points: NotRequired[int | None]
    shot_made: NotRequired[bool | None]
    category: NotRequired[str | None]
    type_: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    opponent_id: NotRequired[int | None]
    opponent: NotRequired[str | None]
    receiving_team_id: NotRequired[int | None]
    receiving_team: NotRequired[str | None]
    description: NotRequired[str | None]
    player_id: NotRequired[int | None]
    assisted_by_player_id: NotRequired[int | None]
    blocked_by_player_id: NotRequired[int | None]
    fast_break: NotRequired[bool | None]
    side_of_basket: NotRequired[str | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    substitute_in_player_id: NotRequired[int | None]
    substitute_out_player_id: NotRequired[int | None]
    away_player_id: NotRequired[int | None]
    home_player_id: NotRequired[int | None]
    receiving_player_id: NotRequired[int | None]
    baseline_offset_percentage: NotRequired[float | None]
    sideline_offset_percentage: NotRequired[float | None]
    coordinates: NotRequired[str | None]
    stolen_by_player_id: NotRequired[int | None]
