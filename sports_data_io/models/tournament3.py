from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .round1 import Round1, Round1Dict


class Tournament3(SdkBaseModel):
    """The details of the tournament"""

    tournament_id: Optional[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the tournament"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date of this tournament"""

    end_date: OptionalNullable[str] = Field(default=UNSET, alias="EndDate")
    """The end date of this tournament"""

    is_over: Optional[bool] = Field(default=UNSET, alias="IsOver")
    """Indicates whether this tournament is over"""

    is_in_progress: Optional[bool] = Field(default=UNSET, alias="IsInProgress")
    """Indicates whether this tournament is in progress"""

    venue: OptionalNullable[str] = Field(default=UNSET, alias="Venue")
    """The name of the venue where this tournament takes place"""

    location: OptionalNullable[str] = Field(default=UNSET, alias="Location")
    """The location where this tournament is played"""

    par: OptionalNullable[int] = Field(default=UNSET, alias="Par")
    """The 18-hole par of this course"""

    yards: OptionalNullable[int] = Field(default=UNSET, alias="Yards")
    """The total course yardage"""

    purse: OptionalNullable[float] = Field(default=UNSET, alias="Purse")
    """The total prize money of this tournament"""

    start_date_time: OptionalNullable[str] = Field(default=UNSET, alias="StartDateTime")
    """The first tee time of the upcoming round of this tournament (in US Eastern Time)"""

    canceled: OptionalNullable[bool] = Field(default=UNSET, alias="Canceled")
    """Indicates whether this tournament is canceled or not"""

    covered: OptionalNullable[bool] = Field(default=UNSET, alias="Covered")
    """Indicates whether this tournament is covered. Note: only stroke format tournaments are covered"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city where this course is located"""

    state: OptionalNullable[str] = Field(default=UNSET, alias="State")
    """The state where this course is located"""

    zip_code: OptionalNullable[str] = Field(default=UNSET, alias="ZipCode")
    """The zip code where this course is located"""

    country: OptionalNullable[str] = Field(default=UNSET, alias="Country")
    """The country where this course is located"""

    time_zone: OptionalNullable[str] = Field(default=UNSET, alias="TimeZone")
    """The description of the time zone in which the course is located"""

    format: OptionalNullable[str] = Field(default=UNSET, alias="Format")
    """The format of the tournament (possible values: Stroke, Match, Team, Stableford)"""

    rounds: Optional[list[Round1]] = Field(default=UNSET, alias="Rounds")
    """The details of the rounds of this tournament"""

    sport_radar_tournament_id: OptionalNullable[str] = Field(default=UNSET, alias="SportRadarTournamentID")
    """The unique ID of this tournament in the SportRadar API"""

    odds_coverage: OptionalNullable[str] = Field(default=UNSET, alias="OddsCoverage")
    """Shows the type of odds coverage for the tournament, with possible values being 'None'; 'Limited'; or 'Full'"""


class Tournament3Dict(TypedDict):
    tournament_id: NotRequired[int]
    name: NotRequired[str | None]
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
    is_over: NotRequired[bool]
    is_in_progress: NotRequired[bool]
    venue: NotRequired[str | None]
    location: NotRequired[str | None]
    par: NotRequired[int | None]
    yards: NotRequired[int | None]
    purse: NotRequired[float | None]
    start_date_time: NotRequired[str | None]
    canceled: NotRequired[bool | None]
    covered: NotRequired[bool | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    zip_code: NotRequired[str | None]
    country: NotRequired[str | None]
    time_zone: NotRequired[str | None]
    format: NotRequired[str | None]
    rounds: NotRequired[list[Round1 | Round1Dict]]
    sport_radar_tournament_id: NotRequired[str | None]
    odds_coverage: NotRequired[str | None]
