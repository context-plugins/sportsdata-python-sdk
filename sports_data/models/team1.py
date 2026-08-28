from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Team1(SdkBaseModel):
    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """A unique abbreviation of the team (e.g. OAE; TAS; UAD; KAF; etc.) Note: Due to being selected for uniqueness;
    these are not always a match with broadcaster abbreviations. For that use case; use ShortDisplayName"""

    active: Optional[bool] = Field(default=UNSET, alias="Active")
    """Whether or not this team is active"""

    school: OptionalNullable[str] = Field(default=UNSET, alias="School")
    """The name of the school as used in college sports (e.g. SMU, South Florida, Stony Brook, UCLA, etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The mascot of the team (e.g. Sooners, Red Raiders, Trojans, Wildcats, etc.)"""

    stadium_id: Optional[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium that the team plays its home games at"""

    ap_rank: OptionalNullable[int] = Field(default=UNSET, alias="ApRank")
    """The rank of the team assigned to them by the Associated Press (AP)"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """Total number of wins by the team"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """The total number of losses by the team in the current season"""

    conference_wins: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceWins")
    """The total number of conference wins by the team"""

    conference_losses: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceLosses")
    """The total number of conference losses by the team"""

    global_team_id: Optional[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for the team. Note: This value is guaranteed to be unique across all sports/leagues"""

    coaches_rank: OptionalNullable[int] = Field(default=UNSET, alias="CoachesRank")
    """The Coaches Rank of the team"""

    playoff_rank: OptionalNullable[int] = Field(default=UNSET, alias="PlayoffRank")
    """The CFP Rank of the team"""

    team_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="TeamLogoUrl")
    """The url of the team logo image"""

    conference_id: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceID")
    """The unique ID of the team's conference"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The name of the team's parent conference (e.g. SEC; Big Ten; etc)"""

    short_display_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortDisplayName")
    """The shortened name of the team"""

    rank_week: OptionalNullable[int] = Field(default=UNSET, alias="RankWeek")
    """The week that the AP Rank/CoachesRank was last updated"""

    rank_season: OptionalNullable[int] = Field(default=UNSET, alias="RankSeason")
    """The season that the AP Rank/CoachesRank was last updated"""

    rank_season_type: OptionalNullable[int] = Field(default=UNSET, alias="RankSeasonType")
    """The season type that the AP Rank/CoachesRank was last updated"""

    primary_color: OptionalNullable[str] = Field(default=UNSET, alias="PrimaryColor")
    """The team's primary color. (This is not licensed for public or commercial use)"""

    secondary_color: OptionalNullable[str] = Field(default=UNSET, alias="SecondaryColor")
    """The team's secondary color. (This is not licensed for public or commercial use)"""

    tertiary_color: OptionalNullable[str] = Field(default=UNSET, alias="TertiaryColor")
    """The team's tertiary color. (This is not licensed for public or commercial use)"""

    quaternary_color: OptionalNullable[str] = Field(default=UNSET, alias="QuaternaryColor")
    """The team's quaternary color. (This is not licensed for public or commercial use)"""


class Team1Dict(TypedDict):
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    active: NotRequired[bool]
    school: NotRequired[str | None]
    name: NotRequired[str | None]
    stadium_id: NotRequired[int]
    ap_rank: NotRequired[int | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    conference_wins: NotRequired[int | None]
    conference_losses: NotRequired[int | None]
    global_team_id: NotRequired[int]
    coaches_rank: NotRequired[int | None]
    playoff_rank: NotRequired[int | None]
    team_logo_url: NotRequired[str | None]
    conference_id: NotRequired[int | None]
    conference: NotRequired[str | None]
    short_display_name: NotRequired[str | None]
    rank_week: NotRequired[int | None]
    rank_season: NotRequired[int | None]
    rank_season_type: NotRequired[int | None]
    primary_color: NotRequired[str | None]
    secondary_color: NotRequired[str | None]
    tertiary_color: NotRequired[str | None]
    quaternary_color: NotRequired[str | None]
