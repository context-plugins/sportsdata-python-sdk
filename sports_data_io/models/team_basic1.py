from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TeamBasic1(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """A unique abbreviation of the team (e.g. OAE; TAS; UAD; KAF; etc.) These are not recommended for front end use as
    they may not match common usage; see the ShortDisplayName instead."""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this team is active"""

    school: OptionalNullable[str] = Field(default=UNSET, alias="School")
    """The name of the school as used in college sports (e.g. SMU; South Florida; Stony Brook; UCLA; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the stadium"""

    stadium_id: Optional[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium that the team plays its home games at"""

    global_team_id: Optional[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for the team. Note: This value is guaranteed to be unique across all sports/leagues"""

    team_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="TeamLogoUrl")
    """The url of the team logo image"""

    conference_id: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceID")
    """The unique ID of the team's conference"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The name of the team's parent conference (e.g. SEC; Big Ten; etc)"""

    short_display_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortDisplayName")
    """The shortened name of the team - recommended for front end applications. May not be unique; if you need a 100%
    unique letter identifier see the Key field in this table."""

    primary_color: OptionalNullable[str] = Field(default=UNSET, alias="PrimaryColor")
    """The team's primary color. (This is not licensed for public or commercial use)"""

    secondary_color: OptionalNullable[str] = Field(default=UNSET, alias="SecondaryColor")
    """The team's secondary color. (This is not licensed for public or commercial use)"""

    tertiary_color: OptionalNullable[str] = Field(default=UNSET, alias="TertiaryColor")
    """The team's tertiary color. (This is not licensed for public or commercial use)"""

    quaternary_color: OptionalNullable[str] = Field(default=UNSET, alias="QuaternaryColor")
    """The team's quaternary color. (This is not licensed for public or commercial use)"""


class TeamBasic1Dict(TypedDict):
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    active: NotRequired[bool]
    school: NotRequired[str | None]
    name: NotRequired[str | None]
    stadium_id: NotRequired[int]
    global_team_id: NotRequired[int]
    team_logo_url: NotRequired[str | None]
    conference_id: NotRequired[int | None]
    conference: NotRequired[str | None]
    short_display_name: NotRequired[str | None]
    primary_color: NotRequired[str | None]
    secondary_color: NotRequired[str | None]
    tertiary_color: NotRequired[str | None]
    quaternary_color: NotRequired[str | None]
