from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Team3(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """Abbreviation of the team (e.g. LAD, PHI, BOS, CHC, etc.)"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this team is active"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city/location of the team (e.g. Los Angeles, Philadelphia, Boston, Chicago, etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The mascot of the team (e.g. Dodgers, Phillies, Red Sox, Cubs, etc.)"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the team's current home stadium"""

    league: OptionalNullable[str] = Field(default=UNSET, alias="League")
    """The league of the team (possible values: AL, NL)"""

    division: OptionalNullable[str] = Field(default=UNSET, alias="Division")
    """The division of the team (e.g. East; Central; West)"""

    primary_color: OptionalNullable[str] = Field(default=UNSET, alias="PrimaryColor")
    """The team's primary color. (This is not licensed for public or commercial use)"""

    secondary_color: OptionalNullable[str] = Field(default=UNSET, alias="SecondaryColor")
    """The team's secondary color. (This is not licensed for public or commercial use)"""

    tertiary_color: OptionalNullable[str] = Field(default=UNSET, alias="TertiaryColor")
    """The team's tertiary color. (This is not licensed for public or commercial use)"""

    quaternary_color: OptionalNullable[str] = Field(default=UNSET, alias="QuaternaryColor")
    """The team's quaternary color. (This is not licensed for public or commercial use)"""

    wikipedia_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaLogoUrl")
    """The link to the team's logo hosted on Wikipedia. (This is not licensed for public or commercial use)"""

    wikipedia_word_mark_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaWordMarkUrl")
    """The link to the team's wordmark logo hosted on Wikipedia. (This is not licensed for public or commercial use)"""

    global_team_id: Optional[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    head_coach: OptionalNullable[str] = Field(default=UNSET, alias="HeadCoach")
    """The current head coach (manager) of the team"""

    hitting_coach: OptionalNullable[str] = Field(default=UNSET, alias="HittingCoach")
    """The current hitting coach of the team. Note: some teams may have multiple or no hitting coaches"""

    pitching_coach: OptionalNullable[str] = Field(default=UNSET, alias="PitchingCoach")
    """The current pitching coach of the team. Note: some teams may have multiple or no pitching coaches"""


class Team3Dict(TypedDict):
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    active: NotRequired[bool]
    city: NotRequired[str | None]
    name: NotRequired[str | None]
    stadium_id: NotRequired[int | None]
    league: NotRequired[str | None]
    division: NotRequired[str | None]
    primary_color: NotRequired[str | None]
    secondary_color: NotRequired[str | None]
    tertiary_color: NotRequired[str | None]
    quaternary_color: NotRequired[str | None]
    wikipedia_logo_url: NotRequired[str | None]
    wikipedia_word_mark_url: NotRequired[str | None]
    global_team_id: NotRequired[int]
    head_coach: NotRequired[str | None]
    hitting_coach: NotRequired[str | None]
    pitching_coach: NotRequired[str | None]
