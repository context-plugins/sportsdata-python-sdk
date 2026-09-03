from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .stadium2 import Stadium2, Stadium2Dict


class Schedule(SdkBaseModel):
    game_key: OptionalNullable[str] = Field(default=UNSET, alias="GameKey")
    """A 9 digit unique code identifying the game that this record corresponds to. The GameID is composed of Season;
    SeasonType; Week and HomeTeam. Note: This value will be NULL for bye weeks"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this game corresponds to (1=Regular Season; 2=Preseason; 3=Postseason; 4=Offseason;
    5=All-Star)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the game"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    date: OptionalNullable[str] = Field(default=UNSET, alias="Date")
    """The date and time of the game (in US Eastern Time)"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    channel: OptionalNullable[str] = Field(default=UNSET, alias="Channel")
    """The television station broadcasting the game"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """The oddsmaker point spread at game start from the perspective of the team (negative numbers indicate the HomeTeam
    is favored; positive numbers indicate the AwayTeam is favored)"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The total points line (over/under) at game start"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the team's current home stadium"""

    canceled: OptionalNullable[bool] = Field(default=UNSET, alias="Canceled")
    """Indicates whether the game was canceled"""

    geo_lat: OptionalNullable[float] = Field(default=UNSET, alias="GeoLat")
    """The geographic latitude coordinate of the venue where the game is taking place"""

    geo_long: OptionalNullable[float] = Field(default=UNSET, alias="GeoLong")
    """The geographic longitude coordinate of the venue where the game is taking place"""

    forecast_temp_low: OptionalNullable[int] = Field(default=UNSET, alias="ForecastTempLow")
    """The forecasted low temperature on game day at this venue (Fahrenheit)."""

    forecast_temp_high: OptionalNullable[int] = Field(default=UNSET, alias="ForecastTempHigh")
    """The forecasted high temperature on game day at this venue (Fahrenheit)."""

    forecast_description: OptionalNullable[str] = Field(default=UNSET, alias="ForecastDescription")
    """The forecast description on game day at this venue."""

    forecast_wind_chill: OptionalNullable[int] = Field(default=UNSET, alias="ForecastWindChill")
    """The forecasted wind chill on game day at this venue."""

    forecast_wind_speed: OptionalNullable[int] = Field(default=UNSET, alias="ForecastWindSpeed")
    """The forecasted wind speed on game day at this venue."""

    away_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamMoneyLine")
    """The sportsbook's moneyline for the away team"""

    home_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamMoneyLine")
    """The sportsbook's moneyline for the home team"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game (in US Eastern Time)"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues"""

    score_id: Optional[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the score/game"""

    stadium_details: Optional[Stadium2] = Field(default=UNSET, alias="StadiumDetails")
    """The details of the stadium where this game is played"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The status of the game. For a description of possible values, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/14287629964567-Process-Guide-Game-Status"
    target="_blank">here.</a> For how suspended and postponed games are handled specifically, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/4404845580567-Postponed-and-Rescheduled-Games"
    target="_blank">here</a>."""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out."""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game (in UTC)"""


class ScheduleDict(TypedDict):
    game_key: NotRequired[str | None]
    season_type: NotRequired[int]
    season: NotRequired[int]
    week: NotRequired[int]
    date: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    channel: NotRequired[str | None]
    point_spread: NotRequired[float | None]
    over_under: NotRequired[float | None]
    stadium_id: NotRequired[int | None]
    canceled: NotRequired[bool | None]
    geo_lat: NotRequired[float | None]
    geo_long: NotRequired[float | None]
    forecast_temp_low: NotRequired[int | None]
    forecast_temp_high: NotRequired[int | None]
    forecast_description: NotRequired[str | None]
    forecast_wind_chill: NotRequired[int | None]
    forecast_wind_speed: NotRequired[int | None]
    away_team_money_line: NotRequired[int | None]
    home_team_money_line: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    global_game_id: NotRequired[int | None]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    score_id: NotRequired[int]
    stadium_details: NotRequired[Stadium2 | Stadium2Dict]
    status: NotRequired[str | None]
    is_closed: NotRequired[bool | None]
    date_time_utc: NotRequired[str | None]
