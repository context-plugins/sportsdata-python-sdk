from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TeamBasic2(SdkBaseModel):
    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """Abbreviation [Key] of the team (e.g. LAC; PHI; NE; IND; etc.)"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The auto-generated unique ID of the Team, that avoids collisions with PlayerIDs. This is useful when combining
    players and fantasy defenses to create fantasy teams."""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city/location of the team (e.g. Minnesota; Philadelphia; New England; Indianapolis; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The mascot of the team (e.g. Chargers, Eagles, Patriots, Colts, etc.)"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The conference of the team (e.g. AFC or NFC)"""

    division: OptionalNullable[str] = Field(default=UNSET, alias="Division")
    """The division of the team (e.g. East, North, South, West)"""

    full_name: OptionalNullable[str] = Field(default=UNSET, alias="FullName")
    """The full name of the team (e.g. New England Patriots)"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the team's current home stadium"""

    bye_week: OptionalNullable[int] = Field(default=UNSET, alias="ByeWeek")
    """The bye week of the team in the upcoming or current regular season"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    head_coach: OptionalNullable[str] = Field(default=UNSET, alias="HeadCoach")
    """The current head coach of the team"""

    primary_color: OptionalNullable[str] = Field(default=UNSET, alias="PrimaryColor")
    """The team's first color. (This is not licensed for public or commercial use)"""

    secondary_color: OptionalNullable[str] = Field(default=UNSET, alias="SecondaryColor")
    """The team's second color. (This is not licensed for public or commercial use)"""

    tertiary_color: OptionalNullable[str] = Field(default=UNSET, alias="TertiaryColor")
    """The team's third color. (This is not licensed for public or commercial use)"""

    quaternary_color: OptionalNullable[str] = Field(default=UNSET, alias="QuaternaryColor")
    """The team's fourth color. (This is not licensed for public or commercial use)"""

    wikipedia_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaLogoURL")
    """The link to the team's logo hosted on Wikipedia (This is not licensed for public or commercial use)"""

    wikipedia_word_mark_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaWordMarkURL")
    """The link to the team's wordmark logo hosted on Wikipedia (This is not licensed for public or commercial use)"""

    offensive_coordinator: OptionalNullable[str] = Field(default=UNSET, alias="OffensiveCoordinator")
    """The current offensive coordinator of the team. Note: field will be NULL if team doesn't have an OFF
    coordinator"""

    defensive_coordinator: OptionalNullable[str] = Field(default=UNSET, alias="DefensiveCoordinator")
    """The current defensive coordinator of the team. Note: field will be NULL if team doesn't have an DEFF
    coordinator"""

    special_teams_coach: OptionalNullable[str] = Field(default=UNSET, alias="SpecialTeamsCoach")
    """The current special teams coordinator of the team. Note: field will be NULL if team doesn't have an ST
    coordinator"""

    offensive_scheme: OptionalNullable[str] = Field(default=UNSET, alias="OffensiveScheme")
    """The offensive scheme this team runs (PRO, 2TE, 3WR). This is decided at our discretion."""

    defensive_scheme: OptionalNullable[str] = Field(default=UNSET, alias="DefensiveScheme")
    """The current defensive scheme this team runs (3-4, 4-3)"""


class TeamBasic2Dict(TypedDict):
    key: NotRequired[str | None]
    team_id: NotRequired[int]
    player_id: NotRequired[int]
    city: NotRequired[str | None]
    name: NotRequired[str | None]
    conference: NotRequired[str | None]
    division: NotRequired[str | None]
    full_name: NotRequired[str | None]
    stadium_id: NotRequired[int | None]
    bye_week: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    head_coach: NotRequired[str | None]
    primary_color: NotRequired[str | None]
    secondary_color: NotRequired[str | None]
    tertiary_color: NotRequired[str | None]
    quaternary_color: NotRequired[str | None]
    wikipedia_logo_url: NotRequired[str | None]
    wikipedia_word_mark_url: NotRequired[str | None]
    offensive_coordinator: NotRequired[str | None]
    defensive_coordinator: NotRequired[str | None]
    special_teams_coach: NotRequired[str | None]
    offensive_scheme: NotRequired[str | None]
    defensive_scheme: NotRequired[str | None]
