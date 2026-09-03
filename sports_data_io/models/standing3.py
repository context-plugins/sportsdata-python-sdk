from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Standing3(SdkBaseModel):
    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NHL regular season for which these totals apply"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 5=AllStar;
    6=Exhibition)."""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """The abbreviation [Key] of the team associated with this market (Ex. BOS, EDM, LAK)"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city/location of the team (e.g. Los Angeles; Philadelphia; Boston; Chicago; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The team's full name (ex. Minnesota Wild; New York Islanders)"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The conference of the team (possible values: Eastern; Western)"""

    division: OptionalNullable[str] = Field(default=UNSET, alias="Division")
    """The division of the team (e.g. Atlantic; Metropolitan; Central; or Pacific)"""

    wins: OptionalNullable[int] = Field(default=UNSET, alias="Wins")
    """Total number of wins by the team in the season"""

    losses: OptionalNullable[int] = Field(default=UNSET, alias="Losses")
    """Total losses for a team in the regular season"""

    overtime_losses: OptionalNullable[int] = Field(default=UNSET, alias="OvertimeLosses")
    """Total overtime losses by the team in the season"""

    percentage: OptionalNullable[float] = Field(default=UNSET, alias="Percentage")
    """The team's winning percentage"""

    conference_wins: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceWins")
    """Total number of conference wins for a team"""

    conference_losses: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceLosses")
    """Total number of conference losses for a team"""

    division_wins: OptionalNullable[int] = Field(default=UNSET, alias="DivisionWins")
    """Total number of division wins by the team"""

    division_losses: OptionalNullable[int] = Field(default=UNSET, alias="DivisionLosses")
    """Total number of division losses by the team"""

    shutout_wins: OptionalNullable[int] = Field(default=UNSET, alias="ShutoutWins")
    """Total regular season shutout wins by the team"""

    conference_rank: OptionalNullable[int] = Field(default=UNSET, alias="ConferenceRank")
    """Team rank at the conference level"""

    division_rank: OptionalNullable[int] = Field(default=UNSET, alias="DivisionRank")
    """Team rank at the division level"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    clinched_division: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedDivision")
    """Returns TRUE if team has clinched their division; FALSE if not"""

    clinched_playoff_berth: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedPlayoffBerth")
    """Returns TRUE if team has clinched a playoff spot; FALSE if not"""

    clinched_best_record_in_conference: OptionalNullable[bool] = Field(
        default=UNSET, alias="ClinchedBestRecordInConference"
    )
    """Returns TRUE if team has clinched the best record in their respective conference; FALSE if not"""

    clinched_presidents_trophy: OptionalNullable[bool] = Field(default=UNSET, alias="ClinchedPresidentsTrophy")
    """Returns TRUE if team has clinched best record in NHL (President's Trophy); FALSE if not"""

    eliminated_from_playoff_contention: OptionalNullable[bool] = Field(
        default=UNSET, alias="EliminatedFromPlayoffContention"
    )
    """Returns TRUE if team has been eliminated from playoff contention; FALSE if not"""


class Standing3Dict(TypedDict):
    season: NotRequired[int]
    season_type: NotRequired[int]
    team_id: NotRequired[int]
    key: NotRequired[str | None]
    city: NotRequired[str | None]
    name: NotRequired[str | None]
    conference: NotRequired[str | None]
    division: NotRequired[str | None]
    wins: NotRequired[int | None]
    losses: NotRequired[int | None]
    overtime_losses: NotRequired[int | None]
    percentage: NotRequired[float | None]
    conference_wins: NotRequired[int | None]
    conference_losses: NotRequired[int | None]
    division_wins: NotRequired[int | None]
    division_losses: NotRequired[int | None]
    shutout_wins: NotRequired[int | None]
    conference_rank: NotRequired[int | None]
    division_rank: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    clinched_division: NotRequired[bool | None]
    clinched_playoff_berth: NotRequired[bool | None]
    clinched_best_record_in_conference: NotRequired[bool | None]
    clinched_presidents_trophy: NotRequired[bool | None]
    eliminated_from_playoff_contention: NotRequired[bool | None]
