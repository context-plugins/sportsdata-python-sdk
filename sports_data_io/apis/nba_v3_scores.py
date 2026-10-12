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
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
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
from ..models.enums.format import Format, FormatOrStr
from ..models.game import Game
from ..models.news import News
from ..models.player1 import Player1
from ..models.player_basic1 import PlayerBasic1
from ..models.referee1 import Referee1
from ..models.schedule_basic1 import ScheduleBasic1
from ..models.score_basic1 import ScoreBasic1
from ..models.season import Season
from ..models.stadium1 import Stadium1
from ..models.standing1 import Standing1
from ..models.team1 import Team1
from ..models.team_depth_chart1 import TeamDepthChart1
from ..models.team_game1 import TeamGame1
from ..models.team_season1 import TeamSeason1
from ..models.transaction import Transaction
from ..server.server import Server


class NbaV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NbaV3ScoresWithRawResponse(client, server, auth)

    def nba_v3_scores_are_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_are_games_in_progress(
                format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_depth_charts(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart1]:
        """Returns the full list of NBA Depth Charts as of the time of the call.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_depth_charts(format_=format_, request_options=request_options)
        )

    def nba_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game]:
        """Full scores and gameday info, including referee, infotainment odds, as well as all of the quarter scores and
        full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_games_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_games_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_games_basic_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_games_basic_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_games_basic_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """This endpoint simply delivers the quarter, time, quarter scores, and total score live; no gameday info is
        provided.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_games_basic_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(self._with_raw_response.nba_v3_scores_news(format_=format_, request_options=request_options))

    def nba_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_news_by_date(date, format_=format_, request_options=request_options)
        )

    def nba_v3_scores_player_details_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_player_details_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_player_details_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_player_details_by_free_agent(
                format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_player_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_player_details_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_player_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players currently active.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_player_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_player_profiles_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all free agents not currently attached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_player_profiles_by_free_agent(
                format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_players_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_players_profiles_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_referees(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Referee1]:
        """Returns the full list of NBA Referees.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(self._with_raw_response.nba_v3_scores_referees(format_=format_, request_options=request_options))

    def nba_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_schedules(season, format_=format_, request_options=request_options)
        )

    def nba_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic1]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_schedules_basic(
                season, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Season:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_season_current(format_=format_, request_options=request_options)
        )

    def nba_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium1]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(self._with_raw_response.nba_v3_scores_stadiums(format_=format_, request_options=request_options))

    def nba_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing1]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_standings(season, format_=format_, request_options=request_options)
        )

    def nba_v3_scores_team_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame1]:
        """Game by game log of total team statistics.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 8 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_team_game_logs_by_season(
                season, teamid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_team_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame1]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_team_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team1]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_team_profiles_all(format_=format_, request_options=request_options)
        )

    def nba_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team1]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_team_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team1]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the active teams for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_team_profiles_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_team_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_scores_transactions(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """A list of transactions, such as player trades, injuries, assignments etc., delivered by date.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_scores_transactions(date, format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> NbaV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncNbaV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNbaV3ScoresWithRawResponse(client, server, auth)

    async def nba_v3_scores_are_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_are_games_in_progress(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_depth_charts(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart1]:
        """Returns the full list of NBA Depth Charts as of the time of the call.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_depth_charts(format_=format_, request_options=request_options)
        )

    async def nba_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game]:
        """Full scores and gameday info, including referee, infotainment odds, as well as all of the quarter scores and
        full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_games_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_games_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_games_basic_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_games_basic_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_games_basic_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """This endpoint simply delivers the quarter, time, quarter scores, and total score live; no gameday info is
        provided.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_games_basic_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_news(format_=format_, request_options=request_options)
        )

    async def nba_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_player_details_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_player_details_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_player_details_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_player_details_by_free_agent(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_player_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_player_details_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_player_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players currently active.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_player_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_player_profiles_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all free agents not currently attached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_player_profiles_by_free_agent(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_players_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_players_profiles_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_referees(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Referee1]:
        """Returns the full list of NBA Referees.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_referees(format_=format_, request_options=request_options)
        )

    async def nba_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_schedules(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic1]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_schedules_basic(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Season:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_season_current(format_=format_, request_options=request_options)
        )

    async def nba_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium1]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_stadiums(format_=format_, request_options=request_options)
        )

    async def nba_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing1]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_standings(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_team_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame1]:
        """Game by game log of total team statistics.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 8 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_team_game_logs_by_season(
                season, teamid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_team_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame1]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_team_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team1]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_team_profiles_all(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team1]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_team_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team1]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the active teams for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_team_profiles_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_team_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_scores_transactions(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """A list of transactions, such as player trades, injuries, assignments etc., delivered by date.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_scores_transactions(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNbaV3ScoresWithRawResponse:
        return self._with_raw_response


class NbaV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nba_v3_scores_are_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, NbaV3ScoresAreGamesInProgressErrorBody]:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=nba_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_depth_charts(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart1], NbaV3ScoresDepthChartsErrorBody]:
        """Returns the full list of NBA Depth Charts as of the time of the call.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/DepthCharts"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamDepthChart1]],
            error_mapper=nba_v3_scores_depth_charts_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game], NbaV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including referee, infotainment odds, as well as all of the quarter scores and
        full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game]],
            error_mapper=nba_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game], NbaV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game]],
            error_mapper=nba_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_games_basic_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], NbaV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic1]],
            error_mapper=nba_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_games_basic_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], NbaV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers the quarter, time, quarter scores, and total score live; no gameday info is
        provided.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic1]],
            error_mapper=nba_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NbaV3ScoresNewsErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nba_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NbaV3ScoresNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nba_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_details_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], NbaV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=nba_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_details_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], NbaV3ScoresPlayerDetailsByFreeAgentErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=nba_v3_scores_player_details_by_free_agent_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], NbaV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=nba_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], NbaV3ScoresPlayerProfilesByActiveErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players currently active.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersActiveBasic"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic1]],
            error_mapper=nba_v3_scores_player_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_player_profiles_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], NbaV3ScoresPlayerProfilesByFreeAgentErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all free agents not currently attached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic1]],
            error_mapper=nba_v3_scores_player_profiles_by_free_agent_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_players_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], NbaV3ScoresPlayersProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic1]],
            error_mapper=nba_v3_scores_players_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_referees(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Referee1], NbaV3ScoresRefereesErrorBody]:
        """Returns the full list of NBA Referees.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Referees"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Referee1]],
            error_mapper=nba_v3_scores_referees_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game], NbaV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game]],
            error_mapper=nba_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic1], NbaV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic1]],
            error_mapper=nba_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season, NbaV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season],
            error_mapper=nba_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium1], NbaV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium1]],
            error_mapper=nba_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing1], NbaV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Standing1]],
            error_mapper=nba_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame1], NbaV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game by game log of total team statistics.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 8 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nba/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=nba_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame1], NbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=nba_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team1], NbaV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team1]],
            error_mapper=nba_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team1], NbaV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/teams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team1]],
            error_mapper=nba_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team1], NbaV3ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the active teams for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/teams/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team1]],
            error_mapper=nba_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason1], NbaV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason1]],
            error_mapper=nba_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    def nba_v3_scores_transactions(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], NbaV3ScoresTransactionsErrorBody]:
        """A list of transactions, such as player trades, injuries, assignments etc., delivered by date.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Transaction]],
            error_mapper=nba_v3_scores_transactions_error_mapper,
            request_options=request_options,
        )


class AsyncNbaV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nba_v3_scores_are_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, NbaV3ScoresAreGamesInProgressErrorBody]:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[bool],
            error_mapper=nba_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_depth_charts(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart1], NbaV3ScoresDepthChartsErrorBody]:
        """Returns the full list of NBA Depth Charts as of the time of the call.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/DepthCharts"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamDepthChart1]],
            error_mapper=nba_v3_scores_depth_charts_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game], NbaV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including referee, infotainment odds, as well as all of the quarter scores and
        full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game]],
            error_mapper=nba_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game], NbaV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game]],
            error_mapper=nba_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_games_basic_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], NbaV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScoreBasic1]],
            error_mapper=nba_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_games_basic_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], NbaV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers the quarter, time, quarter scores, and total score live; no gameday info is
        provided.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScoreBasic1]],
            error_mapper=nba_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NbaV3ScoresNewsErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nba_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NbaV3ScoresNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nba_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_details_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], NbaV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player1]],
            error_mapper=nba_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_details_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], NbaV3ScoresPlayerDetailsByFreeAgentErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player1]],
            error_mapper=nba_v3_scores_player_details_by_free_agent_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], NbaV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player1]],
            error_mapper=nba_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], NbaV3ScoresPlayerProfilesByActiveErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players currently active.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersActiveBasic"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic1]],
            error_mapper=nba_v3_scores_player_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_player_profiles_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], NbaV3ScoresPlayerProfilesByFreeAgentErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all free agents not currently attached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic1]],
            error_mapper=nba_v3_scores_player_profiles_by_free_agent_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_players_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], NbaV3ScoresPlayersProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            team: The abbreviation of the requested team.<br>Examples: <code>PHI</code>, <code>BKN</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic1]],
            error_mapper=nba_v3_scores_players_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_referees(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Referee1], NbaV3ScoresRefereesErrorBody]:
        """Returns the full list of NBA Referees.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Referees"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Referee1]],
            error_mapper=nba_v3_scores_referees_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game], NbaV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game]],
            error_mapper=nba_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic1], NbaV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScheduleBasic1]],
            error_mapper=nba_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season, NbaV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[Season],
            error_mapper=nba_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium1], NbaV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Stadium1]],
            error_mapper=nba_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing1], NbaV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Standing1]],
            error_mapper=nba_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame1], NbaV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game by game log of total team statistics.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 8 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nba/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame1]],
            error_mapper=nba_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame1], NbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame1]],
            error_mapper=nba_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team1], NbaV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team1]],
            error_mapper=nba_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team1], NbaV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/teams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team1]],
            error_mapper=nba_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team1], NbaV3ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the active teams for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/teams/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team1]],
            error_mapper=nba_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason1], NbaV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamSeason1]],
            error_mapper=nba_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_scores_transactions(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], NbaV3ScoresTransactionsErrorBody]:
        """A list of transactions, such as player trades, injuries, assignments etc., delivered by date.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Transaction]],
            error_mapper=nba_v3_scores_transactions_error_mapper,
            request_options=request_options,
        )
