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
from ..errors.nba_v3_scores_are_games_in_progress_error import (
    NbaV3ScoresAreGamesInProgressErrorBody,
    nba_v3_scores_are_games_in_progress_error_mapper,
)
from ..errors.nba_v3_scores_depth_charts_error import (
    NbaV3ScoresDepthChartsErrorBody,
    nba_v3_scores_depth_charts_error_mapper,
)
from ..errors.nba_v3_scores_games_basic_by_date_final_error import (
    NbaV3ScoresGamesBasicByDateFinalErrorBody,
    nba_v3_scores_games_basic_by_date_final_error_mapper,
)
from ..errors.nba_v3_scores_games_basic_by_date_live_final_error import (
    NbaV3ScoresGamesBasicByDateLiveFinalErrorBody,
    nba_v3_scores_games_basic_by_date_live_final_error_mapper,
)
from ..errors.nba_v3_scores_games_by_date_final_error import (
    NbaV3ScoresGamesByDateFinalErrorBody,
    nba_v3_scores_games_by_date_final_error_mapper,
)
from ..errors.nba_v3_scores_games_by_date_live_final_error import (
    NbaV3ScoresGamesByDateLiveFinalErrorBody,
    nba_v3_scores_games_by_date_live_final_error_mapper,
)
from ..errors.nba_v3_scores_news_by_date_error import (
    NbaV3ScoresNewsByDateErrorBody,
    nba_v3_scores_news_by_date_error_mapper,
)
from ..errors.nba_v3_scores_news_error import NbaV3ScoresNewsErrorBody, nba_v3_scores_news_error_mapper
from ..errors.nba_v3_scores_player_details_by_active_error import (
    NbaV3ScoresPlayerDetailsByActiveErrorBody,
    nba_v3_scores_player_details_by_active_error_mapper,
)
from ..errors.nba_v3_scores_player_details_by_free_agent_error import (
    NbaV3ScoresPlayerDetailsByFreeAgentErrorBody,
    nba_v3_scores_player_details_by_free_agent_error_mapper,
)
from ..errors.nba_v3_scores_player_details_by_team_error import (
    NbaV3ScoresPlayerDetailsByTeamErrorBody,
    nba_v3_scores_player_details_by_team_error_mapper,
)
from ..errors.nba_v3_scores_player_profiles_by_active_error import (
    NbaV3ScoresPlayerProfilesByActiveErrorBody,
    nba_v3_scores_player_profiles_by_active_error_mapper,
)
from ..errors.nba_v3_scores_player_profiles_by_free_agent_error import (
    NbaV3ScoresPlayerProfilesByFreeAgentErrorBody,
    nba_v3_scores_player_profiles_by_free_agent_error_mapper,
)
from ..errors.nba_v3_scores_players_profiles_by_team_error import (
    NbaV3ScoresPlayersProfilesByTeamErrorBody,
    nba_v3_scores_players_profiles_by_team_error_mapper,
)
from ..errors.nba_v3_scores_referees_error import NbaV3ScoresRefereesErrorBody, nba_v3_scores_referees_error_mapper
from ..errors.nba_v3_scores_schedules_basic_error import (
    NbaV3ScoresSchedulesBasicErrorBody,
    nba_v3_scores_schedules_basic_error_mapper,
)
from ..errors.nba_v3_scores_schedules_error import NbaV3ScoresSchedulesErrorBody, nba_v3_scores_schedules_error_mapper
from ..errors.nba_v3_scores_season_current_error import (
    NbaV3ScoresSeasonCurrentErrorBody,
    nba_v3_scores_season_current_error_mapper,
)
from ..errors.nba_v3_scores_stadiums_error import NbaV3ScoresStadiumsErrorBody, nba_v3_scores_stadiums_error_mapper
from ..errors.nba_v3_scores_standings_error import NbaV3ScoresStandingsErrorBody, nba_v3_scores_standings_error_mapper
from ..errors.nba_v3_scores_team_game_logs_by_season_error import (
    NbaV3ScoresTeamGameLogsBySeasonErrorBody,
    nba_v3_scores_team_game_logs_by_season_error_mapper,
)
from ..errors.nba_v3_scores_team_game_stats_by_date_live_final_error import (
    NbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody,
    nba_v3_scores_team_game_stats_by_date_live_final_error_mapper,
)
from ..errors.nba_v3_scores_team_profiles_all_error import (
    NbaV3ScoresTeamProfilesAllErrorBody,
    nba_v3_scores_team_profiles_all_error_mapper,
)
from ..errors.nba_v3_scores_team_profiles_by_active_error import (
    NbaV3ScoresTeamProfilesByActiveErrorBody,
    nba_v3_scores_team_profiles_by_active_error_mapper,
)
from ..errors.nba_v3_scores_team_profiles_by_season_error import (
    NbaV3ScoresTeamProfilesBySeasonErrorBody,
    nba_v3_scores_team_profiles_by_season_error_mapper,
)
from ..errors.nba_v3_scores_team_season_stats_error import (
    NbaV3ScoresTeamSeasonStatsErrorBody,
    nba_v3_scores_team_season_stats_error_mapper,
)
from ..errors.nba_v3_scores_transactions_error import (
    NbaV3ScoresTransactionsErrorBody,
    nba_v3_scores_transactions_error_mapper,
)
from ..models.enums.format import FormatOrStr
from ..models.game7 import Game7
from ..models.news1 import News1
from ..models.player4 import Player4
from ..models.player_basic3 import PlayerBasic3
from ..models.referee import Referee
from ..models.schedule_basic4 import ScheduleBasic4
from ..models.score_basic3 import ScoreBasic3
from ..models.season5 import Season5
from ..models.stadium import Stadium
from ..models.standing1 import Standing1
from ..models.team4 import Team4
from ..models.team_depth_chart import TeamDepthChart
from ..models.team_game3 import TeamGame3
from ..models.team_season3 import TeamSeason3
from ..models.transaction import Transaction
from ..server.server import Server


class NbaV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NbaV3ScoresWithRawResponse(client, server, auth)

    def nba_v3_scores_are_games_in_progress(
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
        return self._with_raw_response.nba_v3_scores_are_games_in_progress(
            format, request_options=request_options
        ).unwrap()

    def nba_v3_scores_depth_charts(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart]:
        """Returns the full list of NBA Depth Charts as of the time of the call.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_depth_charts(format, request_options=request_options).unwrap()

    def nba_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game7]:
        """Full scores and gameday info, including referee, infotainment odds, as well as all of the quarter scores and
        full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_games_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def nba_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game7]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_games_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def nba_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic3]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_games_basic_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def nba_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic3]:
        """This endpoint simply delivers the quarter, time, quarter scores, and total score live; no gameday info is
        provided.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_games_basic_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def nba_v3_scores_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News1]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_news(format, request_options=request_options).unwrap()

    def nba_v3_scores_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News1]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_news_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def nba_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player4]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_player_details_by_active(
            format, request_options=request_options
        ).unwrap()

    def nba_v3_scores_player_details_by_free_agent(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player4]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_player_details_by_free_agent(
            format, request_options=request_options
        ).unwrap()

    def nba_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player4]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_player_details_by_team(
            format, team, request_options=request_options
        ).unwrap()

    def nba_v3_scores_player_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic3]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players currently active.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_player_profiles_by_active(
            format, request_options=request_options
        ).unwrap()

    def nba_v3_scores_player_profiles_by_free_agent(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic3]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all free agents not currently attached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_player_profiles_by_free_agent(
            format, request_options=request_options
        ).unwrap()

    def nba_v3_scores_players_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic3]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_players_profiles_by_team(
            format, team, request_options=request_options
        ).unwrap()

    def nba_v3_scores_referees(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Referee]:
        """Returns the full list of NBA Referees.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_referees(format, request_options=request_options).unwrap()

    def nba_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game7]:
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
        return self._with_raw_response.nba_v3_scores_schedules(format, season, request_options=request_options).unwrap()

    def nba_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic4]:
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
        return self._with_raw_response.nba_v3_scores_schedules_basic(
            format, season, request_options=request_options
        ).unwrap()

    def nba_v3_scores_season_current(
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
        return self._with_raw_response.nba_v3_scores_season_current(format, request_options=request_options).unwrap()

    def nba_v3_scores_stadiums(
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
        return self._with_raw_response.nba_v3_scores_stadiums(format, request_options=request_options).unwrap()

    def nba_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing1]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_standings(format, season, request_options=request_options).unwrap()

    def nba_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame3]:
        """Game by game log of total team statistics.

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
        return self._with_raw_response.nba_v3_scores_team_game_logs_by_season(
            format, season, teamid, numberofgames, request_options=request_options
        ).unwrap()

    def nba_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame3]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_team_game_stats_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def nba_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team4]:
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
        return self._with_raw_response.nba_v3_scores_team_profiles_all(format, request_options=request_options).unwrap()

    def nba_v3_scores_team_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team4]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_team_profiles_by_active(
            format, request_options=request_options
        ).unwrap()

    def nba_v3_scores_team_profiles_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team4]:
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
        return self._with_raw_response.nba_v3_scores_team_profiles_by_season(
            format, season, request_options=request_options
        ).unwrap()

    def nba_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason3]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_team_season_stats(
            format, season, request_options=request_options
        ).unwrap()

    def nba_v3_scores_transactions(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """A list of transactions, such as player trades, injuries, assignments etc., delivered by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nba_v3_scores_transactions(
            format, date, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NbaV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncNbaV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNbaV3ScoresWithRawResponse(client, server, auth)

    async def nba_v3_scores_are_games_in_progress(
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
            await self._with_raw_response.nba_v3_scores_are_games_in_progress(format, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_depth_charts(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart]:
        """Returns the full list of NBA Depth Charts as of the time of the call.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_depth_charts(format, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game7]:
        """Full scores and gameday info, including referee, infotainment odds, as well as all of the quarter scores and
        full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_games_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game7]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_games_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic3]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_games_basic_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic3]:
        """This endpoint simply delivers the quarter, time, quarter scores, and total score live; no gameday info is
        provided.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_games_basic_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News1]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.nba_v3_scores_news(format, request_options=request_options)).unwrap()

    async def nba_v3_scores_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News1]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_news_by_date(format, date, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player4]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_player_details_by_active(
                format, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_player_details_by_free_agent(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player4]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_player_details_by_free_agent(
                format, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player4]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_player_details_by_team(
                format, team, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_player_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic3]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players currently active.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_player_profiles_by_active(
                format, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_player_profiles_by_free_agent(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic3]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all free agents not currently attached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_player_profiles_by_free_agent(
                format, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_players_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic3]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_players_profiles_by_team(
                format, team, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_referees(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Referee]:
        """Returns the full list of NBA Referees.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.nba_v3_scores_referees(format, request_options=request_options)).unwrap()

    async def nba_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game7]:
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
            await self._with_raw_response.nba_v3_scores_schedules(format, season, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic4]:
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
            await self._with_raw_response.nba_v3_scores_schedules_basic(format, season, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_season_current(
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
            await self._with_raw_response.nba_v3_scores_season_current(format, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_stadiums(
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
        return (await self._with_raw_response.nba_v3_scores_stadiums(format, request_options=request_options)).unwrap()

    async def nba_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing1]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_standings(format, season, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame3]:
        """Game by game log of total team statistics.

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
            await self._with_raw_response.nba_v3_scores_team_game_logs_by_season(
                format, season, teamid, numberofgames, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame3]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_team_game_stats_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team4]:
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
            await self._with_raw_response.nba_v3_scores_team_profiles_all(format, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_team_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team4]:
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
            await self._with_raw_response.nba_v3_scores_team_profiles_by_active(format, request_options=request_options)
        ).unwrap()

    async def nba_v3_scores_team_profiles_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team4]:
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
            await self._with_raw_response.nba_v3_scores_team_profiles_by_season(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason3]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_team_season_stats(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def nba_v3_scores_transactions(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """A list of transactions, such as player trades, injuries, assignments etc., delivered by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nba_v3_scores_transactions(format, date, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNbaV3ScoresWithRawResponse:
        return self._with_raw_response


class NbaV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nba_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, NbaV3ScoresAreGamesInProgressErrorBody]:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=nba_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_depth_charts(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart], NbaV3ScoresDepthChartsErrorBody]:
        """Returns the full list of NBA Depth Charts as of the time of the call.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/DepthCharts"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamDepthChart]],
            error_mapper=nba_v3_scores_depth_charts_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game7], NbaV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including referee, infotainment odds, as well as all of the quarter scores and
        full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game7]],
            error_mapper=nba_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game7], NbaV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game7]],
            error_mapper=nba_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic3], NbaV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic3]],
            error_mapper=nba_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic3], NbaV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers the quarter, time, quarter scores, and total score live; no gameday info is
        provided.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic3]],
            error_mapper=nba_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News1], NbaV3ScoresNewsErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News1]],
            error_mapper=nba_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News1], NbaV3ScoresNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News1]],
            error_mapper=nba_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player4]],
            error_mapper=nba_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_details_by_free_agent(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByFreeAgentErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player4]],
            error_mapper=nba_v3_scores_player_details_by_free_agent_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player4]],
            error_mapper=nba_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic3], NbaV3ScoresPlayerProfilesByActiveErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players currently active.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersActiveBasic"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic3]],
            error_mapper=nba_v3_scores_player_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_profiles_by_free_agent(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic3], NbaV3ScoresPlayerProfilesByFreeAgentErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all free agents not currently attached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic3]],
            error_mapper=nba_v3_scores_player_profiles_by_free_agent_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_players_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic3], NbaV3ScoresPlayersProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic3]],
            error_mapper=nba_v3_scores_players_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_referees(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Referee], NbaV3ScoresRefereesErrorBody]:
        """Returns the full list of NBA Referees.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Referees"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Referee]],
            error_mapper=nba_v3_scores_referees_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game7], NbaV3ScoresSchedulesErrorBody]:
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
            url_template=self._server.default("/v3/nba/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game7]],
            error_mapper=nba_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic4], NbaV3ScoresSchedulesBasicErrorBody]:
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
            url_template=self._server.default("/v3/nba/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic4]],
            error_mapper=nba_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season5, NbaV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season5],
            error_mapper=nba_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium], NbaV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium]],
            error_mapper=nba_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing1], NbaV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Standing1]],
            error_mapper=nba_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame3], NbaV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game by game log of total team statistics.

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
                "/v3/nba/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame3]],
            error_mapper=nba_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame3], NbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame3]],
            error_mapper=nba_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team4], NbaV3ScoresTeamProfilesAllErrorBody]:
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
            url_template=self._server.default("/v3/nba/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team4]],
            error_mapper=nba_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team4], NbaV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/teams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team4]],
            error_mapper=nba_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_profiles_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team4], NbaV3ScoresTeamProfilesBySeasonErrorBody]:
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
            url_template=self._server.default("/v3/nba/scores/{format}/teams/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team4]],
            error_mapper=nba_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason3], NbaV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason3]],
            error_mapper=nba_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_transactions(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], NbaV3ScoresTransactionsErrorBody]:
        """A list of transactions, such as player trades, injuries, assignments etc., delivered by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Transaction]],
            error_mapper=nba_v3_scores_transactions_error_mapper,
            request_options=request_options,
        )


class AsyncNbaV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nba_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, NbaV3ScoresAreGamesInProgressErrorBody]:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=nba_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_depth_charts(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart], NbaV3ScoresDepthChartsErrorBody]:
        """Returns the full list of NBA Depth Charts as of the time of the call.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/DepthCharts"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamDepthChart]],
            error_mapper=nba_v3_scores_depth_charts_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game7], NbaV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including referee, infotainment odds, as well as all of the quarter scores and
        full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game7]],
            error_mapper=nba_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game7], NbaV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game7]],
            error_mapper=nba_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic3], NbaV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic3]],
            error_mapper=nba_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic3], NbaV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers the quarter, time, quarter scores, and total score live; no gameday info is
        provided.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic3]],
            error_mapper=nba_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News1], NbaV3ScoresNewsErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News1]],
            error_mapper=nba_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News1], NbaV3ScoresNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News1]],
            error_mapper=nba_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player4]],
            error_mapper=nba_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_details_by_free_agent(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByFreeAgentErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player4]],
            error_mapper=nba_v3_scores_player_details_by_free_agent_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player4]],
            error_mapper=nba_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic3], NbaV3ScoresPlayerProfilesByActiveErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players currently active.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersActiveBasic"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic3]],
            error_mapper=nba_v3_scores_player_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_profiles_by_free_agent(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic3], NbaV3ScoresPlayerProfilesByFreeAgentErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all free agents not currently attached to a team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic3]],
            error_mapper=nba_v3_scores_player_profiles_by_free_agent_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_players_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic3], NbaV3ScoresPlayersProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic3]],
            error_mapper=nba_v3_scores_players_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_referees(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Referee], NbaV3ScoresRefereesErrorBody]:
        """Returns the full list of NBA Referees.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Referees"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Referee]],
            error_mapper=nba_v3_scores_referees_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game7], NbaV3ScoresSchedulesErrorBody]:
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
            url_template=self._server.default("/v3/nba/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game7]],
            error_mapper=nba_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic4], NbaV3ScoresSchedulesBasicErrorBody]:
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
            url_template=self._server.default("/v3/nba/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic4]],
            error_mapper=nba_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season5, NbaV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season5],
            error_mapper=nba_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium], NbaV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium]],
            error_mapper=nba_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing1], NbaV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Standing1]],
            error_mapper=nba_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame3], NbaV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game by game log of total team statistics.

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
                "/v3/nba/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame3]],
            error_mapper=nba_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame3], NbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame3]],
            error_mapper=nba_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team4], NbaV3ScoresTeamProfilesAllErrorBody]:
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
            url_template=self._server.default("/v3/nba/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team4]],
            error_mapper=nba_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_profiles_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team4], NbaV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/teams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team4]],
            error_mapper=nba_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_profiles_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team4], NbaV3ScoresTeamProfilesBySeasonErrorBody]:
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
            url_template=self._server.default("/v3/nba/scores/{format}/teams/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team4]],
            error_mapper=nba_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason3], NbaV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason3]],
            error_mapper=nba_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_transactions(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], NbaV3ScoresTransactionsErrorBody]:
        """A list of transactions, such as player trades, injuries, assignments etc., delivered by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Transaction]],
            error_mapper=nba_v3_scores_transactions_error_mapper,
            request_options=request_options,
        )
