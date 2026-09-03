from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Courses(SdkBaseModel):
    tournament_id: Optional[int] = Field(default=UNSET, alias="TournamentID")
    """The unique ID of the tournament"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the tournament that is being played at this course"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date of this tournament"""

    end_date: OptionalNullable[str] = Field(default=UNSET, alias="EndDate")
    """The end date of this tournament"""

    venue: OptionalNullable[str] = Field(default=UNSET, alias="Venue")
    """The name of the venue where this tournament takes place"""

    location: OptionalNullable[str] = Field(default=UNSET, alias="Location")
    """The location of this course"""

    par: OptionalNullable[int] = Field(default=UNSET, alias="Par")
    """The 18-hole par of this course"""

    yards: OptionalNullable[int] = Field(default=UNSET, alias="Yards")
    """The total course yardage"""

    purse: OptionalNullable[float] = Field(default=UNSET, alias="Purse")
    """The total prize money of this tournament"""

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


class CoursesDict(TypedDict):
    tournament_id: NotRequired[int]
    name: NotRequired[str | None]
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
    venue: NotRequired[str | None]
    location: NotRequired[str | None]
    par: NotRequired[int | None]
    yards: NotRequired[int | None]
    purse: NotRequired[float | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    zip_code: NotRequired[str | None]
    country: NotRequired[str | None]
    time_zone: NotRequired[str | None]
    format: NotRequired[str | None]
