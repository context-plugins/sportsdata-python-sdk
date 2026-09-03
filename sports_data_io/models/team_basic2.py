from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .stadium1 import Stadium1, Stadium1Dict


class TeamBasic2(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """A unique abbreviation of the team (e.g. OKL; TXTECH; USC; UK; etc.). Note: Due to being selected for uniqueness;
    these are not always a match with broadcaster abbreviations. For that use case; use ShortDisplayName."""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this team is active. Note: Active = True & Inactive = False"""

    school: OptionalNullable[str] = Field(default=UNSET, alias="School")
    """The name of the school as used in college sports (e.g. SMU; South Florida; Stony Brook; UCLA; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The mascot of the team (e.g. Sooners, Red Raiders, Trojans, Wildcats, etc.)"""

    global_team_id: Optional[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    conference_id: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceID")
    """The ID of the team's conference"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The name of the team's conference (e.g. American Athletic, Big Ten, Conference USA)"""

    team_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="TeamLogoUrl")
    """The URL of the team logo image (png format)"""

    short_display_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortDisplayName")
    """A abbreviation of the team as seen on most broadcasts. Note: This field could have the same name for multiple
    teams. If a completely unique name is need use [Key]"""

    stadium: Optional[Stadium1] = Field(default=UNSET, alias="Stadium")
    """The active home stadium of the team"""

    primary_color: OptionalNullable[str] = Field(default=UNSET, alias="PrimaryColor")
    """The team's primary color. (This is not licensed for public or commercial use)"""

    secondary_color: OptionalNullable[str] = Field(default=UNSET, alias="SecondaryColor")
    """The team's secondary color. (This is not licensed for public or commercial use)"""

    tertiary_color: OptionalNullable[str] = Field(default=UNSET, alias="TertiaryColor")
    """The team's tertiary color. (This is not licensed for public or commercial use)"""

    quaternary_color: OptionalNullable[str] = Field(default=UNSET, alias="QuaternaryColor")
    """The team's quaternary color. (This is not licensed for public or commercial use)"""


class TeamBasic2Dict(TypedDict):
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    active: NotRequired[bool]
    school: NotRequired[str | None]
    name: NotRequired[str | None]
    global_team_id: NotRequired[int]
    conference_id: NotRequired[int | None]
    conference: NotRequired[str | None]
    team_logo_url: NotRequired[str | None]
    short_display_name: NotRequired[str | None]
    stadium: NotRequired[Stadium1 | Stadium1Dict]
    primary_color: NotRequired[str | None]
    secondary_color: NotRequired[str | None]
    tertiary_color: NotRequired[str | None]
    quaternary_color: NotRequired[str | None]
