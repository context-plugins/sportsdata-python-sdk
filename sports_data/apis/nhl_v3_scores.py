from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.nhl_v3_scores_are_games_in_progress_error import (
    NhlV3ScoresAreGamesInProgressErrorBody,
    nhl_v3_scores_are_games_in_progress_error_mapper,
)
from ..errors.nhl_v3_scores_depth_charts_goalies_error import (
    NhlV3ScoresDepthChartsGoaliesErrorBody,
    nhl_v3_scores_depth_charts_goalies_error_mapper,
)
from ..errors.nhl_v3_scores_games_basic_by_date_final_error import (
    NhlV3ScoresGamesBasicByDateFinalErrorBody,
    nhl_v3_scores_games_basic_by_date_final_error_mapper,
)
from ..errors.nhl_v3_scores_games_basic_by_date_live_final_error import (
    NhlV3ScoresGamesBasicByDateLiveFinalErrorBody,
    nhl_v3_scores_games_basic_by_date_live_final_error_mapper,
)
from ..errors.nhl_v3_scores_games_by_date_final_error import (
    NhlV3ScoresGamesByDateFinalErrorBody,
    nhl_v3_scores_games_by_date_final_error_mapper,
)
from ..errors.nhl_v3_scores_games_by_date_live_final_error import (
    NhlV3ScoresGamesByDateLiveFinalErrorBody,
    nhl_v3_scores_games_by_date_live_final_error_mapper,
)
from ..errors.nhl_v3_scores_news_by_date_error import (
    NhlV3ScoresNewsByDateErrorBody,
    nhl_v3_scores_news_by_date_error_mapper,
)
from ..errors.nhl_v3_scores_news_error import NhlV3ScoresNewsErrorBody, nhl_v3_scores_news_error_mapper
from ..errors.nhl_v3_scores_player_details_by_active2_error import (
    NhlV3ScoresPlayerDetailsByActive2ErrorBody,
    nhl_v3_scores_player_details_by_active2_error_mapper,
)
from ..errors.nhl_v3_scores_player_details_by_active_error import (
    NhlV3ScoresPlayerDetailsByActiveErrorBody,
    nhl_v3_scores_player_details_by_active_error_mapper,
)
from ..errors.nhl_v3_scores_player_details_by_free_agents2_error import (
    NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody,
    nhl_v3_scores_player_details_by_free_agents2_error_mapper,
)
from ..errors.nhl_v3_scores_player_details_by_free_agents_error import (
    NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody,
    nhl_v3_scores_player_details_by_free_agents_error_mapper,
)
from ..errors.nhl_v3_scores_players_details_by_team_error import (
    NhlV3ScoresPlayersDetailsByTeamErrorBody,
    nhl_v3_scores_players_details_by_team_error_mapper,
)
from ..errors.nhl_v3_scores_players_profiles_by_team_error import (
    NhlV3ScoresPlayersProfilesByTeamErrorBody,
    nhl_v3_scores_players_profiles_by_team_error_mapper,
)
from ..errors.nhl_v3_scores_referees_error import NhlV3ScoresRefereesErrorBody, nhl_v3_scores_referees_error_mapper
from ..errors.nhl_v3_scores_schedules_basic_error import (
    NhlV3ScoresSchedulesBasicErrorBody,
    nhl_v3_scores_schedules_basic_error_mapper,
)
from ..errors.nhl_v3_scores_schedules_error import NhlV3ScoresSchedulesErrorBody, nhl_v3_scores_schedules_error_mapper
from ..errors.nhl_v3_scores_season_current_error import (
    NhlV3ScoresSeasonCurrentErrorBody,
    nhl_v3_scores_season_current_error_mapper,
)
from ..errors.nhl_v3_scores_stadiums_error import NhlV3ScoresStadiumsErrorBody, nhl_v3_scores_stadiums_error_mapper
from ..errors.nhl_v3_scores_standings_error import NhlV3ScoresStandingsErrorBody, nhl_v3_scores_standings_error_mapper
from ..errors.nhl_v3_scores_team_game_logs_by_season_error import (
    NhlV3ScoresTeamGameLogsBySeasonErrorBody,
    nhl_v3_scores_team_game_logs_by_season_error_mapper,
)
from ..errors.nhl_v3_scores_team_game_stats_by_date_live_final_error import (
    NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody,
    nhl_v3_scores_team_game_stats_by_date_live_final_error_mapper,
)
from ..errors.nhl_v3_scores_team_profiles_all_error import (
    NhlV3ScoresTeamProfilesAllErrorBody,
    nhl_v3_scores_team_profiles_all_error_mapper,
)
from ..errors.nhl_v3_scores_team_profiles_by_active_error import (
    NhlV3ScoresTeamProfilesByActiveErrorBody,
    nhl_v3_scores_team_profiles_by_active_error_mapper,
)
from ..errors.nhl_v3_scores_team_profiles_by_season_error import (
    NhlV3ScoresTeamProfilesBySeasonErrorBody,
    nhl_v3_scores_team_profiles_by_season_error_mapper,
)
from ..errors.nhl_v3_scores_team_season_stats_error import (
    NhlV3ScoresTeamSeasonStatsErrorBody,
    nhl_v3_scores_team_season_stats_error_mapper,
)
from ..errors.nhl_v3_scores_transactions_error import (
    NhlV3ScoresTransactionsErrorBody,
    nhl_v3_scores_transactions_error_mapper,
)
from ..models.enums.format import FormatOrStr
from ..models.game8 import Game8
from ..models.news2 import News2
from ..models.player6 import Player6
from ..models.player_basic5 import PlayerBasic5
from ..models.referee import Referee
from ..models.schedule_basic6 import ScheduleBasic6
from ..models.score_basic5 import ScoreBasic5
from ..models.season5 import Season5
from ..models.stadium import Stadium
from ..models.standing3 import Standing3
from ..models.team6 import Team6
from ..models.team_game5 import TeamGame5
from ..models.team_goalie_depth_chart import TeamGoalieDepthChart
from ..models.team_season5 import TeamSeason5
from ..models.transaction import Transaction
from ..server.server import Server


class NhlV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NhlV3ScoresWithRawResponse(client, server, auth)

    def nhl_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_are_games_in_progress(
            format, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_depth_charts_goalies(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGoalieDepthChart]:
        """Returns the full list of NHL Goalies by Team organized into Depth Charts.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_depth_charts_goalies(
            format, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game8]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the period
        scores and full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_games_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game8]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_games_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic5]:
        """A slimmed-down score endpoint, giving just the period scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_games_basic_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic5]:
        """This endpoint simply delivers period, clock, period score and total score live; no gameday info is included.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_games_basic_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
        """Basic RotoBaller news feed, with limited stories available.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_news(format, request_options=request_options).unwrap()

    def nhl_v3_scores_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
        """Basic RotoBaller news feed, with limited stories available, called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_news_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_player_details_by_active(
            format, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_player_details_by_active2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic5]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_player_details_by_active2(
            format, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_player_details_by_free_agents(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_player_details_by_free_agents(
            format, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_player_details_by_free_agents2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic5]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_player_details_by_free_agents2(
            format, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_players_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all players on a given team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_players_details_by_team(
            format, team, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_players_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic5]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_players_profiles_by_team(
            format, team, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_referees(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Referee]:
        """Returns the full list of NHL Referees.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_referees(format, request_options=request_options).unwrap()

    def nhl_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game8]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_schedules(format, season, request_options=request_options).unwrap()

    def nhl_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic6]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_schedules_basic(
            format, season, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Season5:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_season_current(format, request_options=request_options).unwrap()

    def nhl_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_stadiums(format, request_options=request_options).unwrap()

    def nhl_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing3]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_standings(format, season, request_options=request_options).unwrap()

    def nhl_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame5]:
        """Game-by-game log of total team statistics for a given season, split up by game (not aggregated into season
        totals.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 8 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_team_game_logs_by_season(
            format, season, teamid, numberofgames, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame5]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_team_game_stats_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team6]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_team_profiles_all(format, request_options=request_options).unwrap()

    def nhl_v3_scores_team_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team6]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_team_profiles_by_active(
            format, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_team_profiles_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team6]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the active teams for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_team_profiles_by_season(
            format, season, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason5]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_team_season_stats(
            format, season, request_options=request_options
        ).unwrap()

    def nhl_v3_scores_transactions(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """Transactions, such as injuries and assignments and trades, are organized here by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_scores_transactions(
            format, date, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NhlV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncNhlV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNhlV3ScoresWithRawResponse(client, server, auth)

    async def nhl_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_are_games_in_progress(format, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_depth_charts_goalies(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGoalieDepthChart]:
        """Returns the full list of NHL Goalies by Team organized into Depth Charts.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_depth_charts_goalies(format, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game8]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the period
        scores and full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_games_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game8]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_games_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic5]:
        """A slimmed-down score endpoint, giving just the period scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_games_basic_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic5]:
        """This endpoint simply delivers period, clock, period score and total score live; no gameday info is included.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_games_basic_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
        """Basic RotoBaller news feed, with limited stories available.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.nhl_v3_scores_news(format, request_options=request_options)).unwrap()

    async def nhl_v3_scores_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
        """Basic RotoBaller news feed, with limited stories available, called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_news_by_date(format, date, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_player_details_by_active(
                format, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_player_details_by_active2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic5]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_player_details_by_active2(
                format, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_player_details_by_free_agents(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_player_details_by_free_agents(
                format, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_player_details_by_free_agents2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic5]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_player_details_by_free_agents2(
                format, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_players_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all players on a given team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_players_details_by_team(
                format, team, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_players_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic5]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_players_profiles_by_team(
                format, team, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_referees(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Referee]:
        """Returns the full list of NHL Referees.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.nhl_v3_scores_referees(format, request_options=request_options)).unwrap()

    async def nhl_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game8]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_schedules(format, season, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic6]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_schedules_basic(format, season, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Season5:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_season_current(format, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.nhl_v3_scores_stadiums(format, request_options=request_options)).unwrap()

    async def nhl_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing3]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_standings(format, season, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame5]:
        """Game-by-game log of total team statistics for a given season, split up by game (not aggregated into season
        totals.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 8 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_team_game_logs_by_season(
                format, season, teamid, numberofgames, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame5]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_team_game_stats_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team6]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_team_profiles_all(format, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_team_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team6]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_team_profiles_by_active(format, request_options=request_options)
        ).unwrap()

    async def nhl_v3_scores_team_profiles_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team6]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the active teams for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_team_profiles_by_season(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason5]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_team_season_stats(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_scores_transactions(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """Transactions, such as injuries and assignments and trades, are organized here by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_scores_transactions(format, date, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNhlV3ScoresWithRawResponse:
        return self._with_raw_response


class NhlV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nhl_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, NhlV3ScoresAreGamesInProgressErrorBody]:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=nhl_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_depth_charts_goalies(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGoalieDepthChart], NhlV3ScoresDepthChartsGoaliesErrorBody]:
        """Returns the full list of NHL Goalies by Team organized into Depth Charts.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/GoalieDepthCharts"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGoalieDepthChart]],
            error_mapper=nhl_v3_scores_depth_charts_goalies_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game8], NhlV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the period
        scores and full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game8]],
            error_mapper=nhl_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game8], NhlV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game8]],
            error_mapper=nhl_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic5], NhlV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the period scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic5]],
            error_mapper=nhl_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic5], NhlV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers period, clock, period score and total score live; no gameday info is included.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic5]],
            error_mapper=nhl_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], NhlV3ScoresNewsErrorBody]:
        """Basic RotoBaller news feed, with limited stories available.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=nhl_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], NhlV3ScoresNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available, called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=nhl_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], NhlV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=nhl_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_player_details_by_active2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic5], NhlV3ScoresPlayerDetailsByActive2ErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/PlayersByActive"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic5]],
            error_mapper=nhl_v3_scores_player_details_by_active2_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_player_details_by_free_agents(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=nhl_v3_scores_player_details_by_free_agents_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_player_details_by_free_agents2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic5], NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic5]],
            error_mapper=nhl_v3_scores_player_details_by_free_agents2_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_players_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], NhlV3ScoresPlayersDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all players on a given team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=nhl_v3_scores_players_details_by_team_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_players_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic5], NhlV3ScoresPlayersProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic5]],
            error_mapper=nhl_v3_scores_players_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_referees(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Referee], NhlV3ScoresRefereesErrorBody]:
        """Returns the full list of NHL Referees.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Referees"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Referee]],
            error_mapper=nhl_v3_scores_referees_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game8], NhlV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game8]],
            error_mapper=nhl_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic6], NhlV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic6]],
            error_mapper=nhl_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season5, NhlV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season5],
            error_mapper=nhl_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium], NhlV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium]],
            error_mapper=nhl_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing3], NhlV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Standing3]],
            error_mapper=nhl_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame5], NhlV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game-by-game log of total team statistics for a given season, split up by game (not aggregated into season
        totals.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 8 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nhl/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame5]],
            error_mapper=nhl_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame5], NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame5]],
            error_mapper=nhl_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team6], NhlV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team6]],
            error_mapper=nhl_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_team_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team6], NhlV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/teams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team6]],
            error_mapper=nhl_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_team_profiles_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team6], NhlV3ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the active teams for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/teams/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team6]],
            error_mapper=nhl_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason5], NhlV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason5]],
            error_mapper=nhl_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_scores_transactions(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], NhlV3ScoresTransactionsErrorBody]:
        """Transactions, such as injuries and assignments and trades, are organized here by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Transaction]],
            error_mapper=nhl_v3_scores_transactions_error_mapper,
            request_options=request_options,
        )


class AsyncNhlV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nhl_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, NhlV3ScoresAreGamesInProgressErrorBody]:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=nhl_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_depth_charts_goalies(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGoalieDepthChart], NhlV3ScoresDepthChartsGoaliesErrorBody]:
        """Returns the full list of NHL Goalies by Team organized into Depth Charts.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/GoalieDepthCharts"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGoalieDepthChart]],
            error_mapper=nhl_v3_scores_depth_charts_goalies_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game8], NhlV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the period
        scores and full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game8]],
            error_mapper=nhl_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game8], NhlV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game8]],
            error_mapper=nhl_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic5], NhlV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the period scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic5]],
            error_mapper=nhl_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic5], NhlV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers period, clock, period score and total score live; no gameday info is included.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic5]],
            error_mapper=nhl_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], NhlV3ScoresNewsErrorBody]:
        """Basic RotoBaller news feed, with limited stories available.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=nhl_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], NhlV3ScoresNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available, called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=nhl_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], NhlV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=nhl_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_player_details_by_active2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic5], NhlV3ScoresPlayerDetailsByActive2ErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/PlayersByActive"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic5]],
            error_mapper=nhl_v3_scores_player_details_by_active2_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_player_details_by_free_agents(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=nhl_v3_scores_player_details_by_free_agents_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_player_details_by_free_agents2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic5], NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic5]],
            error_mapper=nhl_v3_scores_player_details_by_free_agents2_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_players_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], NhlV3ScoresPlayersDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all players on a given team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=nhl_v3_scores_players_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_players_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic5], NhlV3ScoresPlayersProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic5]],
            error_mapper=nhl_v3_scores_players_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_referees(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Referee], NhlV3ScoresRefereesErrorBody]:
        """Returns the full list of NHL Referees.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Referees"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Referee]],
            error_mapper=nhl_v3_scores_referees_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game8], NhlV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game8]],
            error_mapper=nhl_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic6], NhlV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic6]],
            error_mapper=nhl_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season5, NhlV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season5],
            error_mapper=nhl_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium], NhlV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium]],
            error_mapper=nhl_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing3], NhlV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Standing3]],
            error_mapper=nhl_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame5], NhlV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game-by-game log of total team statistics for a given season, split up by game (not aggregated into season
        totals.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 8 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nhl/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame5]],
            error_mapper=nhl_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame5], NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame5]],
            error_mapper=nhl_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team6], NhlV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team6]],
            error_mapper=nhl_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_team_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team6], NhlV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/teams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team6]],
            error_mapper=nhl_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_team_profiles_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team6], NhlV3ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the active teams for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/teams/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team6]],
            error_mapper=nhl_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason5], NhlV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason5]],
            error_mapper=nhl_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_scores_transactions(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], NhlV3ScoresTransactionsErrorBody]:
        """Transactions, such as injuries and assignments and trades, are organized here by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Transaction]],
            error_mapper=nhl_v3_scores_transactions_error_mapper,
            request_options=request_options,
        )
