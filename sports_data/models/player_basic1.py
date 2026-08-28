from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerBasic1(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the player as assigned by SportsDataIO. Note: this ID remains with the player their entire
    collegiate career"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team associated with this player"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on Note: If this player is a free agent; this field is
    NULL"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: C; CB; DB; DE; DL; DT; FB; G; K; KR; LB; LS; NT; OL; OLB; OT; P;
    PR; QB; RB; S; SS; TE; WR"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The category (Offense, Defense or Special Teams) of the players position (OFF, DEF, ST)"""

    class_: OptionalNullable[str] = Field(default=UNSET, alias="Class")
    """The class of the player. Possible values: Freshman; Sophomore; Junior; Senior; Graduate Student; as well as
    Redshirt for all classes"""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The player's height in inches"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The player's weight in pounds (lbs)"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city in which the player was born"""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The state in which the player was born"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The timestamp of when this player was last updated (US Eastern Time)"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date and time the player was created (US Eastern Time)"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for the player's team. Note: This value is guaranteed to be unique across all
    sports/leagues"""


class PlayerBasic1Dict(TypedDict):
    player_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    jersey: NotRequired[int | None]
    position: NotRequired[str | None]
    position_category: NotRequired[str | None]
    class_: NotRequired[str | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
    birth_city: NotRequired[str | None]
    birth_state: NotRequired[str | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
