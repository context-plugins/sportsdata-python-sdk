from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Team6(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """A unique abbreviation of the team (e.g. LA; PHX; NY; etc.). Note: Due to being selected for uniqueness; these are
    not always matching broadcaster abbreviations. For that use case; use ShortDisplayName."""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this team is active. Note: Active = True & Inactive = False"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city in which the team is located in (e.g. Los Angeles, Phoenix, New York, etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The mascot of the team (e.g. Sparks, Suns, Dream, etc.)"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The conference of a given team (possible values: Eastern; Western)"""

    wikipedia_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaLogoUrl")
    """The link to the team's logo hosted on Wikipedia. (This is not licensed for public or commercial use)"""

    global_team_id: Optional[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for the team. This value is guaranteed to be unique across all sports/leagues."""


class Team6Dict(TypedDict):
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    active: NotRequired[bool]
    city: NotRequired[str | None]
    name: NotRequired[str | None]
    conference: NotRequired[str | None]
    wikipedia_logo_url: NotRequired[str | None]
    global_team_id: NotRequired[int]
