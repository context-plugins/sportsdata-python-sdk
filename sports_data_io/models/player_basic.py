from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PlayerBasic(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on. Note: If this player is a free agent; this field is
    NULL"""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """Player's jersey number"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """Player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """Player's last name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The primary position of the player. Possible Values: C; CB; DB; DE; DL; DT; FB; FS; G; ILB; K; KR; LB; LS; NT;
    OL; OLB; OT; P; QB; RB; S; SS; T; TE; WR"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The player's current status. Possible values include Active, Inactive, Injured Reserve, Physically Unable to
    Perform, Practice Squad, Suspended, Non Football Injury, Non-Football Illness, Commissioner Exempt List, Exempt/Left
    Team, Paternity, Bereavement, Reserve/COVID-19, and Voluntary Opt Out. Inactive indicates that this player is a free
    agent. Active indicates that this player is on his team's active roster."""

    height: OptionalNullable[str] = Field(default=UNSET, alias="Height")
    """Height in feet, inches"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """Weight in pounds"""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The player's date of birth"""

    college: OptionalNullable[str] = Field(default=UNSET, alias="College")
    """College team the player played for prior to turning professional"""

    experience: OptionalNullable[int] = Field(default=UNSET, alias="Experience")
    """Number of years experience. Note: This number is incremented every year; in the Spring; when we load the rookies
    following the NFL Draft. Rookies will have Experience = Zero; while second year players will have Experience = 2."""

    fantasy_position: OptionalNullable[str] = Field(default=UNSET, alias="FantasyPosition")
    """The player's fantasy football position. Possible values: QB; RB; WR; TE; DL; LB; DB; K; P; OL"""

    active: OptionalNullable[bool] = Field(default=UNSET, alias="Active")
    """Whether or not the player is on the active roster of the NFL team"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The category of the player's position (OFF; DEF; ST)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    age: OptionalNullable[int] = Field(default=UNSET, alias="Age")
    """The player's current age"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The first initial and last name of the player (J. Doe)"""

    height_feet: OptionalNullable[int] = Field(default=UNSET, alias="HeightFeet")
    """The feet component of a player's height (if player is 6'3", then this value would be 6)"""

    height_inches: OptionalNullable[int] = Field(default=UNSET, alias="HeightInches")
    """The inches component of a player's height (if player is 6'3", then this value would be 3)"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that the player is on. Note: If the player is a free agent; this field is NULL"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    usa_today_player_id: OptionalNullable[int] = Field(default=UNSET, alias="UsaTodayPlayerID")
    """The player's cross reference PlayerID to USA Today headshot data feeds."""

    usa_today_headshot_url: OptionalNullable[str] = Field(default=UNSET, alias="UsaTodayHeadshotUrl")
    """The player's headshot URL as provided by USA Today. License from USA Today is required."""

    usa_today_headshot_no_background_url: OptionalNullable[str] = Field(
        default=UNSET, alias="UsaTodayHeadshotNoBackgroundUrl"
    )
    """The player's transparent background headshot URL as provided by USA Today. License from USA Today is required."""

    usa_today_headshot_updated: OptionalNullable[str] = Field(default=UNSET, alias="UsaTodayHeadshotUpdated")
    """The last updated date of the player's headshot as provided by USA Today. License from USA Today is required."""

    usa_today_headshot_no_background_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="UsaTodayHeadshotNoBackgroundUpdated"
    )
    """The last updated date of the player's transparent background headshot as provided by USA Today. License from USA
    Today is required."""


class PlayerBasicDict(TypedDict):
    player_id: NotRequired[int]
    team: NotRequired[str | None]
    number: NotRequired[int | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    position: NotRequired[str | None]
    status: NotRequired[str | None]
    height: NotRequired[str | None]
    weight: NotRequired[int | None]
    birth_date: NotRequired[str | None]
    college: NotRequired[str | None]
    experience: NotRequired[int | None]
    fantasy_position: NotRequired[str | None]
    active: NotRequired[bool | None]
    position_category: NotRequired[str | None]
    name: NotRequired[str | None]
    age: NotRequired[int | None]
    short_name: NotRequired[str | None]
    height_feet: NotRequired[int | None]
    height_inches: NotRequired[int | None]
    team_id: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    usa_today_player_id: NotRequired[int | None]
    usa_today_headshot_url: NotRequired[str | None]
    usa_today_headshot_no_background_url: NotRequired[str | None]
    usa_today_headshot_updated: NotRequired[str | None]
    usa_today_headshot_no_background_updated: NotRequired[str | None]
