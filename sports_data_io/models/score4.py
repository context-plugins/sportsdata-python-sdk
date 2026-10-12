from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .stadium2 import Stadium2, Stadium2Dict


class Score4(SdkBaseModel):
    """The score object and other game details of the given game"""

    game_key: OptionalNullable[str] = Field(default=UNSET, alias="GameKey")
    """A 9 digit unique code identifying the game that this record corresponds to. The GameID is composed of Season;
    SeasonType; Week and HomeTeam. Note: This value will be NULL for bye weeks"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this game corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=All-Star)."""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The NFL season of the game"""

    week: Optional[int] = Field(default=UNSET, alias="Week")
    """The NFL week of the game (regular season: 1 to 18; preseason: 0 to 4; postseason: 1 to 4). Note: seasons after
    2021 will have only 3 preseason weeks"""

    date: OptionalNullable[str] = Field(default=UNSET, alias="Date")
    """The date and time of the game (in US Eastern Time)"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key} of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    away_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayScore")
    """The final score of the Away Team"""

    home_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeScore")
    """The final score of the Home Team"""

    channel: OptionalNullable[str] = Field(default=UNSET, alias="Channel")
    """The television station broadcasting the game"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """The oddsmaker point spread at game start from the perspective of the team (negative numbers indicate the HomeTeam
    is favored; positive numbers indicate the AwayTeam is favored)"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The total points line (over/under) at game start"""

    quarter: OptionalNullable[str] = Field(default=UNSET, alias="Quarter")
    """The current quarter of the game (1, 2, 3, 4, HALF, OT, F, F/OT or NULL if game has not yet started)"""

    time_remaining: OptionalNullable[str] = Field(default=UNSET, alias="TimeRemaining")
    """The amount of time remaining in the current quarter (e.g. 11:23; 5:34; NULL if game is not in progress or at
    halftime)"""

    possession: OptionalNullable[str] = Field(default=UNSET, alias="Possession")
    """The team that currently has possession of the ball (Ex. PHI; NE; NULL if game is not in progress or at
    halftime)"""

    down: OptionalNullable[int] = Field(default=UNSET, alias="Down")
    """The current down in the game (1, 2, 3, 4 or NULL)"""

    distance: OptionalNullable[str] = Field(default=UNSET, alias="Distance")
    """The yards to go for a first down (this can be any positive number or "Goal")"""

    yard_line: OptionalNullable[int] = Field(default=UNSET, alias="YardLine")
    """the yard line of the ball's current position on the field as of the most recently completed play"""

    yard_line_territory: OptionalNullable[str] = Field(default=UNSET, alias="YardLineTerritory")
    """The team's side of the field that the ball is on when the play occurred"""

    red_zone: OptionalNullable[str] = Field(default=UNSET, alias="RedZone")
    """The team abbreviation [Key] that currently has the ball in the opponent's red zone (Ex: "SF"; "BAL" or NULL)"""

    away_score_quarter1: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreQuarter1")
    """Points scored by the away team in Quarter 1"""

    away_score_quarter2: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreQuarter2")
    """Points scored by the away team in Quarter 2"""

    away_score_quarter3: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreQuarter3")
    """Points scored by the away team in Quarter 3"""

    away_score_quarter4: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreQuarter4")
    """Points scored by the away team in Quarter 4"""

    away_score_overtime: OptionalNullable[int] = Field(default=UNSET, alias="AwayScoreOvertime")
    """Points scored by the away team in overtime"""

    home_score_quarter1: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreQuarter1")
    """Points scored by the home team in Quarter 1"""

    home_score_quarter2: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreQuarter2")
    """Points scored by the home team in Quarter 2"""

    home_score_quarter3: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreQuarter3")
    """Points scored by the home team in Quarter 3"""

    home_score_quarter4: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreQuarter4")
    """Points scored by the home team in Quarter 4"""

    home_score_overtime: OptionalNullable[int] = Field(default=UNSET, alias="HomeScoreOvertime")
    """Points scored by the home team in overtime"""

    has_started: Optional[bool] = Field(default=UNSET, alias="HasStarted")
    """Whether the game has started (true/false)"""

    is_in_progress: Optional[bool] = Field(default=UNSET, alias="IsInProgress")
    """Whether the game is currently in progress (true/false)"""

    is_over: Optional[bool] = Field(default=UNSET, alias="IsOver")
    """Whether the game is over (true/false)"""

    has1st_quarter_started: Optional[bool] = Field(default=UNSET, alias="Has1stQuarterStarted")
    """Whether the 1st quarter has started"""

    has2nd_quarter_started: Optional[bool] = Field(default=UNSET, alias="Has2ndQuarterStarted")
    """Whether the 2nd quarter has started"""

    has3rd_quarter_started: Optional[bool] = Field(default=UNSET, alias="Has3rdQuarterStarted")
    """Whether the 3rd quarter has started"""

    has4th_quarter_started: Optional[bool] = Field(default=UNSET, alias="Has4thQuarterStarted")
    """Whether the 4th quarter has started"""

    is_overtime: Optional[bool] = Field(default=UNSET, alias="IsOvertime")
    """Whether this game went into overtime"""

    down_and_distance: OptionalNullable[str] = Field(default=UNSET, alias="DownAndDistance")
    """The description of the down and distance for display purposes"""

    quarter_description: OptionalNullable[str] = Field(default=UNSET, alias="QuarterDescription")
    """Description of the current quarter for display purposes"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the team's current home stadium"""

    last_updated: OptionalNullable[str] = Field(default=UNSET, alias="LastUpdated")
    """The date and time that this game was last updated (in US Eastern Time)"""

    geo_lat: OptionalNullable[float] = Field(default=UNSET, alias="GeoLat")
    """The geographic latitude coordinate of the venue where the game is taking place"""

    geo_long: OptionalNullable[float] = Field(default=UNSET, alias="GeoLong")
    """The geographic longitude coordinate of the venue where the game is taking place"""

    forecast_temp_low: OptionalNullable[int] = Field(default=UNSET, alias="ForecastTempLow")
    """The forecasted low temperature on game day at this venue (Fahrenheit)"""

    forecast_temp_high: OptionalNullable[int] = Field(default=UNSET, alias="ForecastTempHigh")
    """The forecasted high temperature on game day at this venue (Fahrenheit)"""

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

    canceled: OptionalNullable[bool] = Field(default=UNSET, alias="Canceled")
    """Indicates whether the game was canceled"""

    closed: OptionalNullable[bool] = Field(default=UNSET, alias="Closed")
    """Indicates whether the game is over and the final score has been verified and closed out. Note: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status"""

    last_play: OptionalNullable[str] = Field(default=UNSET, alias="LastPlay")
    """The description of the most recent play/event of the game. Note: This is for display purposes and does not
    include corresponding data points"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game (in US Eastern Time)"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    global_game_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues"""

    point_spread_away_team_money_line: OptionalNullable[int] = Field(
        default=UNSET, alias="PointSpreadAwayTeamMoneyLine"
    )
    """The payout on the away team's spread"""

    point_spread_home_team_money_line: OptionalNullable[int] = Field(
        default=UNSET, alias="PointSpreadHomeTeamMoneyLine"
    )
    """The payout on the home team's spread"""

    score_id: Optional[int] = Field(default=UNSET, alias="ScoreID")
    """Unique ID of the Score/Game"""

    stadium_details: Optional[Stadium2] = Field(default=UNSET, alias="StadiumDetails")
    """The details of the stadium where this game is played"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The status of the game. For a description of possible values, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/14287629964567-Process-Guide-Game-Status"
    target="_blank">here.</a> For how suspended and postponed games are handled specifically, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/4404845580567-Postponed-and-Rescheduled-Games"
    target="_blank">here</a>."""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time of when the game officially ended. Note: This field is populated after the game and score are
    finalized"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """Rotation number of home team in this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """Rotation number of away team in this game"""

    neutral_venue: OptionalNullable[bool] = Field(default=UNSET, alias="NeutralVenue")
    """Indicates whether this game is played in a neutral venue"""

    referee_id: OptionalNullable[int] = Field(default=UNSET, alias="RefereeID")
    """The unique ID of the head referee"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for over the total points line"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under"""

    home_timeouts: OptionalNullable[int] = Field(default=UNSET, alias="HomeTimeouts")
    """The number of timeouts remaining for the Home Team"""

    away_timeouts: OptionalNullable[int] = Field(default=UNSET, alias="AwayTimeouts")
    """The number of timeouts remaining for the Away Team"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game (in UTC)"""

    attendance: Optional[int] = Field(default=UNSET, alias="Attendance")
    """The total attendance for the game"""

    is_closed: OptionalNullable[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out."""


class Score4Dict(TypedDict):
    game_key: NotRequired[str | None]
    season_type: NotRequired[int]
    season: NotRequired[int]
    week: NotRequired[int]
    date: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    away_score: NotRequired[int | None]
    home_score: NotRequired[int | None]
    channel: NotRequired[str | None]
    point_spread: NotRequired[float | None]
    over_under: NotRequired[float | None]
    quarter: NotRequired[str | None]
    time_remaining: NotRequired[str | None]
    possession: NotRequired[str | None]
    down: NotRequired[int | None]
    distance: NotRequired[str | None]
    yard_line: NotRequired[int | None]
    yard_line_territory: NotRequired[str | None]
    red_zone: NotRequired[str | None]
    away_score_quarter1: NotRequired[int | None]
    away_score_quarter2: NotRequired[int | None]
    away_score_quarter3: NotRequired[int | None]
    away_score_quarter4: NotRequired[int | None]
    away_score_overtime: NotRequired[int | None]
    home_score_quarter1: NotRequired[int | None]
    home_score_quarter2: NotRequired[int | None]
    home_score_quarter3: NotRequired[int | None]
    home_score_quarter4: NotRequired[int | None]
    home_score_overtime: NotRequired[int | None]
    has_started: NotRequired[bool]
    is_in_progress: NotRequired[bool]
    is_over: NotRequired[bool]
    has1st_quarter_started: NotRequired[bool]
    has2nd_quarter_started: NotRequired[bool]
    has3rd_quarter_started: NotRequired[bool]
    has4th_quarter_started: NotRequired[bool]
    is_overtime: NotRequired[bool]
    down_and_distance: NotRequired[str | None]
    quarter_description: NotRequired[str | None]
    stadium_id: NotRequired[int | None]
    last_updated: NotRequired[str | None]
    geo_lat: NotRequired[float | None]
    geo_long: NotRequired[float | None]
    forecast_temp_low: NotRequired[int | None]
    forecast_temp_high: NotRequired[int | None]
    forecast_description: NotRequired[str | None]
    forecast_wind_chill: NotRequired[int | None]
    forecast_wind_speed: NotRequired[int | None]
    away_team_money_line: NotRequired[int | None]
    home_team_money_line: NotRequired[int | None]
    canceled: NotRequired[bool | None]
    closed: NotRequired[bool | None]
    last_play: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    global_game_id: NotRequired[int | None]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    point_spread_away_team_money_line: NotRequired[int | None]
    point_spread_home_team_money_line: NotRequired[int | None]
    score_id: NotRequired[int]
    stadium_details: NotRequired[Stadium2Dict]
    status: NotRequired[str | None]
    game_end_date_time: NotRequired[str | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    neutral_venue: NotRequired[bool | None]
    referee_id: NotRequired[int | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
    home_timeouts: NotRequired[int | None]
    away_timeouts: NotRequired[int | None]
    date_time_utc: NotRequired[str | None]
    attendance: NotRequired[int]
    is_closed: NotRequired[bool | None]
