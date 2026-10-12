from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .inning import Inning, InningDict
from .series import Series, SeriesDict


class Game21(SdkBaseModel):
    """Next scheduled game for the team"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameID")
    """The unique ID of this game"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The MLB season of the game"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season stage the game belongs to, e.g. Regular season, Post-season. For a description of possible
    values and how they work, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/15196612633623-Process-Guide-Season-Types-and-Parameters"
    target="_blank">here."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The status of the game. For a description of possible values, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/14287629964567-Process-Guide-Game-Status"
    target="_blank">here.</a> For how suspended and postponed games are handled specifically, see <a
    href="https://support.sportsdata.io/hc/en-us/articles/4404845580567-Postponed-and-Rescheduled-Games"
    target="_blank">here</a>."""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in US Eastern Time)"""

    away_team: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeam")
    """The abbreviation [Key] of the away team"""

    home_team: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeam")
    """The abbreviation [Key] of the home team"""

    away_team_id: Optional[int] = Field(default=UNSET, alias="AwayTeamID")
    """The unique TeamID of the away team"""

    home_team_id: Optional[int] = Field(default=UNSET, alias="HomeTeamID")
    """The unique ID of the home team"""

    rescheduled_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledGameID")
    """The GameID of the game that was rescheduled from this game. This only pertains to postponed games that require
    rescheduling."""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the stadium"""

    channel: OptionalNullable[str] = Field(default=UNSET, alias="Channel")
    """The television station broadcasting the game"""

    inning: OptionalNullable[int] = Field(default=UNSET, alias="Inning")
    """The inning that the game is currently in, or the inning in which the game ended. Possible values include: NULL,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, etc)"""

    inning_half: OptionalNullable[str] = Field(default=UNSET, alias="InningHalf")
    """The inning half that the game is currently in; or the inning half in which the game ended (possible values: T; B;
    E: M: NULL)"""

    away_team_runs: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamRuns")
    """Number of runs scored by the away team in the game"""

    home_team_runs: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamRuns")
    """Number of runs scored by the home team in the game"""

    away_team_hits: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamHits")
    """Total hits by the away team in the game"""

    home_team_hits: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamHits")
    """Total hits by the home team in the game"""

    away_team_errors: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamErrors")
    """Total errors committed by the away team in the game"""

    home_team_errors: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamErrors")
    """Total errors committed by the home team in the game"""

    winning_pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="WinningPitcherID")
    """The PlayerID of the pitcher who recorded the win in the game"""

    losing_pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="LosingPitcherID")
    """The PlayerID of the losing pitcher in the game"""

    saving_pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="SavingPitcherID")
    """The PlayerID of the pitcher who recorded the save in the game"""

    attendance: OptionalNullable[int] = Field(default=UNSET, alias="Attendance")
    """Total number of people who attended the game"""

    away_team_probable_pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamProbablePitcherID")
    """The PlayerID of the away team's probable pitcher"""

    home_team_probable_pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamProbablePitcherID")
    """The PlayerID of the home team's probable pitcher"""

    outs: OptionalNullable[int] = Field(default=UNSET, alias="Outs")
    """The number of outs recorded in the current inning of the game"""

    balls: OptionalNullable[int] = Field(default=UNSET, alias="Balls")
    """The number of balls thrown for the current at bat"""

    strikes: OptionalNullable[int] = Field(default=UNSET, alias="Strikes")
    """The number of strikes thrown for the current at bat"""

    current_pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="CurrentPitcherID")
    """The PlayerID of the current pitcher"""

    current_hitter_id: OptionalNullable[int] = Field(default=UNSET, alias="CurrentHitterID")
    """The PlayerID of the current hitter"""

    away_team_starting_pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamStartingPitcherID")
    """The PlayerID of the away team's starting pitcher"""

    home_team_starting_pitcher_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamStartingPitcherID")
    """The PlayerID of the home team starting pitcher in the game"""

    current_pitching_team_id: OptionalNullable[int] = Field(default=UNSET, alias="CurrentPitchingTeamID")
    """The TeamID of the current pitcher's team"""

    current_hitting_team_id: OptionalNullable[int] = Field(default=UNSET, alias="CurrentHittingTeamID")
    """The TeamID of the current hitter's team"""

    point_spread: OptionalNullable[float] = Field(default=UNSET, alias="PointSpread")
    """The consensus Run Line at game start from the perspective of the HomeTeam (in the Game table, the PointSpread
    field's negative numbers indicate the HomeTeam is favored; positive numbers indicate the AwayTeam is favored. Note
    that this rule does not hold in betting-related tables, where the run line is contingent on the bet line). Note: In
    MLB, Point Spread may also be referred to as Run Line"""

    over_under: OptionalNullable[float] = Field(default=UNSET, alias="OverUnder")
    """The oddsmaker total points line at game start"""

    away_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamMoneyLine")
    """Moneyline from the perspective of the away team"""

    home_team_money_line: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamMoneyLine")
    """Moneyline from the perspective of the home team"""

    forecast_temp_low: OptionalNullable[int] = Field(default=UNSET, alias="ForecastTempLow")
    """The forecasted low temperature on game day at this venue (in Fahrenheit)"""

    forecast_temp_high: OptionalNullable[int] = Field(default=UNSET, alias="ForecastTempHigh")
    """The forecasted high temperature on game day at this venue (in Fahrenheit)"""

    forecast_description: OptionalNullable[str] = Field(default=UNSET, alias="ForecastDescription")
    """The description of the weather forecast. Posible values include: Broken Clouds, Clear Sky, Few Clouds, Heavy
    Intensity Rain, Light Rain, Moderate Rain, Mostly Cloudy, Mostly Sunny, Overcast Clouds, Partly Cloudy, Scattered
    Clouds, Showers, Thunderstorms"""

    forecast_wind_chill: OptionalNullable[int] = Field(default=UNSET, alias="ForecastWindChill")
    """The forecasted wind chill on game day at this venue."""

    forecast_wind_speed: OptionalNullable[int] = Field(default=UNSET, alias="ForecastWindSpeed")
    """The forecasted wind speed on game day at this venue."""

    forecast_wind_direction: OptionalNullable[int] = Field(default=UNSET, alias="ForecastWindDirection")
    """The wind direction isn't baseball specific. It refers to the direction that the wind is coming from. 90 would be
    wind coming from the east. 180 is wind from the south. 270 is a wind from the west ... and so on."""

    rescheduled_from_game_id: OptionalNullable[int] = Field(default=UNSET, alias="RescheduledFromGameID")
    """The GameID of the originally scheduled, postponed game, that this game was rescheduled from. This only pertains
    to games that are scheduled as "make up" games."""

    runner_on_first: OptionalNullable[bool] = Field(default=UNSET, alias="RunnerOnFirst")
    """Indicates if there is a runner on first base"""

    runner_on_second: OptionalNullable[bool] = Field(default=UNSET, alias="RunnerOnSecond")
    """Indicates if there is a runner on second base"""

    runner_on_third: OptionalNullable[bool] = Field(default=UNSET, alias="RunnerOnThird")
    """Indicates if there is a runner on third base"""

    away_team_starting_pitcher: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamStartingPitcher")
    """The first and last name of the away team's starting pitcher for the game"""

    home_team_starting_pitcher: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamStartingPitcher")
    """The first and last name of the home team starting pitcher for the game"""

    current_pitcher: OptionalNullable[str] = Field(default=UNSET, alias="CurrentPitcher")
    """Indicates the current pitcher's name"""

    current_hitter: OptionalNullable[str] = Field(default=UNSET, alias="CurrentHitter")
    """Indicates the current hitter's name"""

    winning_pitcher: OptionalNullable[str] = Field(default=UNSET, alias="WinningPitcher")
    """The name of the pitcher who recorded the win in the game"""

    losing_pitcher: OptionalNullable[str] = Field(default=UNSET, alias="LosingPitcher")
    """The first and last name of the losing pitcher in the game"""

    saving_pitcher: OptionalNullable[str] = Field(default=UNSET, alias="SavingPitcher")
    """The name of the pitcher who recorded the save in the game"""

    due_up_hitter_id1: OptionalNullable[int] = Field(default=UNSET, alias="DueUpHitterID1")
    """The PlayerID of the hitter due up first from the current hitter"""

    due_up_hitter_id2: OptionalNullable[int] = Field(default=UNSET, alias="DueUpHitterID2")
    """The PlayerID of the hitter due up second from the current hitter"""

    due_up_hitter_id3: OptionalNullable[int] = Field(default=UNSET, alias="DueUpHitterID3")
    """The PlayerID of the hitter due up third from the current hitter"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameID")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues"""

    global_away_team_id: Optional[int] = Field(default=UNSET, alias="GlobalAwayTeamID")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues"""

    global_home_team_id: Optional[int] = Field(default=UNSET, alias="GlobalHomeTeamID")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    point_spread_away_team_money_line: OptionalNullable[int] = Field(
        default=UNSET, alias="PointSpreadAwayTeamMoneyLine"
    )
    """The moneyline payout odds when betting on the away team with the run line"""

    point_spread_home_team_money_line: OptionalNullable[int] = Field(
        default=UNSET, alias="PointSpreadHomeTeamMoneyLine"
    )
    """The moneyline payout odds when betting on the home team with the run line"""

    last_play: OptionalNullable[str] = Field(default=UNSET, alias="LastPlay")
    """The description of the most recent play/event of the game. This is for display purposes and does not include
    corresponding data points."""

    is_closed: Optional[bool] = Field(default=UNSET, alias="IsClosed")
    """Indicates whether the game is over and the final score has been verified and closed out. Note: it is recommend
    for bet resulting to use IsClosed = True rather than simply Final game status"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date and time of the late update made to this record (in US Eastern Time)"""

    innings: Optional[list[Inning]] = Field(default=UNSET, alias="Innings")
    """The inning details associated with the game"""

    game_end_date_time: OptionalNullable[str] = Field(default=UNSET, alias="GameEndDateTime")
    """The date and time that the game ended in US Eastern Time"""

    home_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="HomeRotationNumber")
    """Rotation number of home team for this game"""

    away_rotation_number: OptionalNullable[int] = Field(default=UNSET, alias="AwayRotationNumber")
    """Rotation number of away team for this game"""

    neutral_venue: OptionalNullable[bool] = Field(default=UNSET, alias="NeutralVenue")
    """Indicates whether this game is played in a neutral venue. Note: Neutral = True, not neutral = False"""

    inning_description: OptionalNullable[str] = Field(default=UNSET, alias="InningDescription")
    """The current status of the inning for display purposes (possible values: Top 2, Mid 2, Bot 2, End 2, etc)"""

    over_payout: OptionalNullable[int] = Field(default=UNSET, alias="OverPayout")
    """The sportsbook's payout for the over"""

    under_payout: OptionalNullable[int] = Field(default=UNSET, alias="UnderPayout")
    """The sportsbook's payout for the under"""

    series_info: Optional[Series] = Field(default=UNSET, alias="SeriesInfo")
    """Contains relevant series data for postseason series only - HomeTeamWins; AwayTeamWins; GameNumber; and
    MaxLength"""

    date_time_utc: OptionalNullable[str] = Field(default=UNSET, alias="DateTimeUTC")
    """The date and time of the game in UTC"""

    home_team_opener: OptionalNullable[bool] = Field(default=UNSET, alias="HomeTeamOpener")
    """Indicates whether the home team will use an opener as the starting pitcher. NOTE: An opener is a pitcher
    (typically a relief pitcher) that is only scheduled to pitch the first 1-3 innings of the game"""

    away_team_opener: OptionalNullable[bool] = Field(default=UNSET, alias="AwayTeamOpener")
    """Indicates whether the away team will use an opener as the starting pitcher.. NOTE: An opener is a pitcher
    (typically a relief pitcher) that is only scheduled to pitch the first 1-3 innings of the game"""

    suspension_resume_day: OptionalNullable[str] = Field(default=UNSET, alias="SuspensionResumeDay")
    """The date a game that was suspended in play will be resumed for play. Useful for tracking when a Suspended game
    will return to an InProgress status."""

    suspension_resume_date_time: OptionalNullable[str] = Field(default=UNSET, alias="SuspensionResumeDateTime")
    """The date and start-time that the suspended in play game will be resumed for play. Useful for tracking when a
    Suspended game will return to an InProgress status."""


class Game21Dict(TypedDict):
    game_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    status: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    away_team: NotRequired[str | None]
    home_team: NotRequired[str | None]
    away_team_id: NotRequired[int]
    home_team_id: NotRequired[int]
    rescheduled_game_id: NotRequired[int | None]
    stadium_id: NotRequired[int | None]
    channel: NotRequired[str | None]
    inning: NotRequired[int | None]
    inning_half: NotRequired[str | None]
    away_team_runs: NotRequired[int | None]
    home_team_runs: NotRequired[int | None]
    away_team_hits: NotRequired[int | None]
    home_team_hits: NotRequired[int | None]
    away_team_errors: NotRequired[int | None]
    home_team_errors: NotRequired[int | None]
    winning_pitcher_id: NotRequired[int | None]
    losing_pitcher_id: NotRequired[int | None]
    saving_pitcher_id: NotRequired[int | None]
    attendance: NotRequired[int | None]
    away_team_probable_pitcher_id: NotRequired[int | None]
    home_team_probable_pitcher_id: NotRequired[int | None]
    outs: NotRequired[int | None]
    balls: NotRequired[int | None]
    strikes: NotRequired[int | None]
    current_pitcher_id: NotRequired[int | None]
    current_hitter_id: NotRequired[int | None]
    away_team_starting_pitcher_id: NotRequired[int | None]
    home_team_starting_pitcher_id: NotRequired[int | None]
    current_pitching_team_id: NotRequired[int | None]
    current_hitting_team_id: NotRequired[int | None]
    point_spread: NotRequired[float | None]
    over_under: NotRequired[float | None]
    away_team_money_line: NotRequired[int | None]
    home_team_money_line: NotRequired[int | None]
    forecast_temp_low: NotRequired[int | None]
    forecast_temp_high: NotRequired[int | None]
    forecast_description: NotRequired[str | None]
    forecast_wind_chill: NotRequired[int | None]
    forecast_wind_speed: NotRequired[int | None]
    forecast_wind_direction: NotRequired[int | None]
    rescheduled_from_game_id: NotRequired[int | None]
    runner_on_first: NotRequired[bool | None]
    runner_on_second: NotRequired[bool | None]
    runner_on_third: NotRequired[bool | None]
    away_team_starting_pitcher: NotRequired[str | None]
    home_team_starting_pitcher: NotRequired[str | None]
    current_pitcher: NotRequired[str | None]
    current_hitter: NotRequired[str | None]
    winning_pitcher: NotRequired[str | None]
    losing_pitcher: NotRequired[str | None]
    saving_pitcher: NotRequired[str | None]
    due_up_hitter_id1: NotRequired[int | None]
    due_up_hitter_id2: NotRequired[int | None]
    due_up_hitter_id3: NotRequired[int | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int]
    global_home_team_id: NotRequired[int]
    point_spread_away_team_money_line: NotRequired[int | None]
    point_spread_home_team_money_line: NotRequired[int | None]
    last_play: NotRequired[str | None]
    is_closed: NotRequired[bool]
    updated: NotRequired[str | None]
    innings: NotRequired[list[InningDict]]
    game_end_date_time: NotRequired[str | None]
    home_rotation_number: NotRequired[int | None]
    away_rotation_number: NotRequired[int | None]
    neutral_venue: NotRequired[bool | None]
    inning_description: NotRequired[str | None]
    over_payout: NotRequired[int | None]
    under_payout: NotRequired[int | None]
    series_info: NotRequired[SeriesDict]
    date_time_utc: NotRequired[str | None]
    home_team_opener: NotRequired[bool | None]
    away_team_opener: NotRequired[bool | None]
    suspension_resume_day: NotRequired[str | None]
    suspension_resume_date_time: NotRequired[str | None]
