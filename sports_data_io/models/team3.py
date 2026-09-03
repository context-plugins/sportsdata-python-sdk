from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Team3(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """Abbreviation of the team (e.g. LA, PHI, BOS, CHI, etc.)"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this team is active"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city/location of the team (e.g. Los Angeles, Philadelphia, Boston, Chicago, etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The mascot of the team (e.g. Kings, Flyers, Bruins, Blackhawks, etc.)"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the team's current home arena"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The conference of the team (possible values: Eastern, Western)"""

    division: OptionalNullable[str] = Field(default=UNSET, alias="Division")
    """The division of the team (e.g. Atlantic; Metropolitan; Central; or Pacific)"""

    primary_color: OptionalNullable[str] = Field(default=UNSET, alias="PrimaryColor")
    """The team's first color (This is not licensed for public or commercial use)"""

    secondary_color: OptionalNullable[str] = Field(default=UNSET, alias="SecondaryColor")
    """The team's second color (This is not licensed for public or commercial use)"""

    tertiary_color: OptionalNullable[str] = Field(default=UNSET, alias="TertiaryColor")
    """The team's third color (This is not licensed for public or commercial use)"""

    quaternary_color: OptionalNullable[str] = Field(default=UNSET, alias="QuaternaryColor")
    """The team's fourth color (This is not licensed for public or commercial use)"""

    wikipedia_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaLogoUrl")
    """The link to the team's logo hosted on Wikipedia. (This is not licensed for public or commercial use)"""

    wikipedia_word_mark_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaWordMarkUrl")
    """The link to the team's wordmark logo hosted on Wikipedia. (This is not licensed for public or commercial use)"""

    global_team_id: Optional[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    head_coach: OptionalNullable[str] = Field(default=UNSET, alias="HeadCoach")
    """The current head coach of the team"""


class Team3Dict(TypedDict):
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    active: NotRequired[bool]
    city: NotRequired[str | None]
    name: NotRequired[str | None]
    stadium_id: NotRequired[int | None]
    conference: NotRequired[str | None]
    division: NotRequired[str | None]
    primary_color: NotRequired[str | None]
    secondary_color: NotRequired[str | None]
    tertiary_color: NotRequired[str | None]
    quaternary_color: NotRequired[str | None]
    wikipedia_logo_url: NotRequired[str | None]
    wikipedia_word_mark_url: NotRequired[str | None]
    global_team_id: NotRequired[int]
    head_coach: NotRequired[str | None]
