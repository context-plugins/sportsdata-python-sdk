from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Injury(SdkBaseModel):
    injury_id: Optional[int] = Field(default=UNSET, alias="InjuryID")
    """The unique ID of the injury record for the player"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this player corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season of the game that this injury leads up to"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game that this injury leads up to (regular season: 1 to 18; preseason: 0 to 4; postseason: 1
    to 4). Note: seasons prior to 2021 will have 3 preseason weeks."""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The primary position of the player. Possible Values: C; CB; DB; DE; DL; DT; FB; FS; G; ILB; K; KR; LB; LS; NT;
    OL; OLB; OT; P; QB; RB; S; SS; T; TE; WR."""

    number: Optional[int] = Field(default=UNSET, alias="Number")
    """Player's jersey number"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on. Note: If this player is a free agent; this field is
    NULL."""

    opponent: OptionalNullable[str] = Field(default=UNSET, alias="Opponent")
    """The abbreviation [Key] of the opponent team of the injured player"""

    body_part: OptionalNullable[str] = Field(default=UNSET, alias="BodyPart")
    """The body part that is injured (Knee; Groin; Calf; Hamstring; etc.)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The injury designation assigned to the player (Probable; Questionable; Doubtful; Out)"""

    practice: OptionalNullable[str] = Field(default=UNSET, alias="Practice")
    """This field is deprecated"""

    practice_description: OptionalNullable[str] = Field(default=UNSET, alias="PracticeDescription")
    """This field is deprecated"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date/time the injury status was updated (in US Eastern time)"""

    declared_inactive: OptionalNullable[bool] = Field(default=UNSET, alias="DeclaredInactive")
    """Whether the player has been declared inactive. This value is updated in the hours leading up to game start time;
    as teams announce their inactive players. Note: This is only updated for offensive skill position players (QB; RB;
    WR; TE)."""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that the player is on. Note: If the player is a free agent; this field is NULL."""

    opponent_id: OptionalNullable[int] = Field(default=UNSET, alias="OpponentID")
    """The unique ID of the opponent this player played on during this game"""


class InjuryDict(TypedDict):
    injury_id: NotRequired[int]
    season_type: NotRequired[int]
    season: NotRequired[int]
    week: NotRequired[int]
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    position: NotRequired[str | None]
    number: NotRequired[int]
    team: NotRequired[str | None]
    opponent: NotRequired[str | None]
    body_part: NotRequired[str | None]
    status: NotRequired[str | None]
    practice: NotRequired[str | None]
    practice_description: NotRequired[str | None]
    updated: NotRequired[str | None]
    declared_inactive: NotRequired[bool | None]
    team_id: NotRequired[int | None]
    opponent_id: NotRequired[int | None]
