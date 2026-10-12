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
from ..errors.mlb_v3_scores_are_games_in_progress_error import (
    MlbV3ScoresAreGamesInProgressErrorBody,
    mlb_v3_scores_are_games_in_progress_error_mapper,
)
from ..errors.mlb_v3_scores_games_basic_by_date_final_error import (
    MlbV3ScoresGamesBasicByDateFinalErrorBody,
    mlb_v3_scores_games_basic_by_date_final_error_mapper,
)
from ..errors.mlb_v3_scores_games_basic_by_date_live_final_error import (
    MlbV3ScoresGamesBasicByDateLiveFinalErrorBody,
    mlb_v3_scores_games_basic_by_date_live_final_error_mapper,
)
from ..errors.mlb_v3_scores_games_by_date_final_error import (
    MlbV3ScoresGamesByDateFinalErrorBody,
    mlb_v3_scores_games_by_date_final_error_mapper,
)
from ..errors.mlb_v3_scores_games_by_date_live_final_error import (
    MlbV3ScoresGamesByDateLiveFinalErrorBody,
    mlb_v3_scores_games_by_date_live_final_error_mapper,
)
from ..errors.mlb_v3_scores_news_by_date_error import (
    MlbV3ScoresNewsByDateErrorBody,
    mlb_v3_scores_news_by_date_error_mapper,
)
from ..errors.mlb_v3_scores_news_error import MlbV3ScoresNewsErrorBody, mlb_v3_scores_news_error_mapper
from ..errors.mlb_v3_scores_player_details_by_active_error import (
    MlbV3ScoresPlayerDetailsByActiveErrorBody,
    mlb_v3_scores_player_details_by_active_error_mapper,
)
from ..errors.mlb_v3_scores_player_details_by_free_agents_error import (
    MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody,
    mlb_v3_scores_player_details_by_free_agents_error_mapper,
)
from ..errors.mlb_v3_scores_player_profiles_by_active_error import (
    MlbV3ScoresPlayerProfilesByActiveErrorBody,
    mlb_v3_scores_player_profiles_by_active_error_mapper,
)
from ..errors.mlb_v3_scores_player_profiles_by_free_agents_error import (
    MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody,
    mlb_v3_scores_player_profiles_by_free_agents_error_mapper,
)
from ..errors.mlb_v3_scores_player_profiles_by_team_error import (
    MlbV3ScoresPlayerProfilesByTeamErrorBody,
    mlb_v3_scores_player_profiles_by_team_error_mapper,
)
from ..errors.mlb_v3_scores_players_details_by_team_error import (
    MlbV3ScoresPlayersDetailsByTeamErrorBody,
    mlb_v3_scores_players_details_by_team_error_mapper,
)
from ..errors.mlb_v3_scores_schedules_basic_error import (
    MlbV3ScoresSchedulesBasicErrorBody,
    mlb_v3_scores_schedules_basic_error_mapper,
)
from ..errors.mlb_v3_scores_schedules_error import MlbV3ScoresSchedulesErrorBody, mlb_v3_scores_schedules_error_mapper
from ..errors.mlb_v3_scores_season_current_error import (
    MlbV3ScoresSeasonCurrentErrorBody,
    mlb_v3_scores_season_current_error_mapper,
)
from ..errors.mlb_v3_scores_stadiums_error import MlbV3ScoresStadiumsErrorBody, mlb_v3_scores_stadiums_error_mapper
from ..errors.mlb_v3_scores_standings_error import MlbV3ScoresStandingsErrorBody, mlb_v3_scores_standings_error_mapper
from ..errors.mlb_v3_scores_team_game_logs_by_season_error import (
    MlbV3ScoresTeamGameLogsBySeasonErrorBody,
    mlb_v3_scores_team_game_logs_by_season_error_mapper,
)
from ..errors.mlb_v3_scores_team_game_stats_by_date_final_error import (
    MlbV3ScoresTeamGameStatsByDateFinalErrorBody,
    mlb_v3_scores_team_game_stats_by_date_final_error_mapper,
)
from ..errors.mlb_v3_scores_team_game_stats_by_date_live_final_error import (
    MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody,
    mlb_v3_scores_team_game_stats_by_date_live_final_error_mapper,
)
from ..errors.mlb_v3_scores_team_profiles_all_error import (
    MlbV3ScoresTeamProfilesAllErrorBody,
    mlb_v3_scores_team_profiles_all_error_mapper,
)
from ..errors.mlb_v3_scores_team_profiles_by_active_error import (
    MlbV3ScoresTeamProfilesByActiveErrorBody,
    mlb_v3_scores_team_profiles_by_active_error_mapper,
)
from ..errors.mlb_v3_scores_team_profiles_by_season_error import (
    MlbV3ScoresTeamProfilesBySeasonErrorBody,
    mlb_v3_scores_team_profiles_by_season_error_mapper,
)
from ..errors.mlb_v3_scores_team_season_stats_error import (
    MlbV3ScoresTeamSeasonStatsErrorBody,
    mlb_v3_scores_team_season_stats_error_mapper,
)
from ..errors.mlb_v3_scores_transactions_error import (
    MlbV3ScoresTransactionsErrorBody,
    mlb_v3_scores_transactions_error_mapper,
)
from ..models.enums.format import Format, FormatOrStr
from ..models.game6 import Game6
from ..models.news import News
from ..models.player2 import Player2
from ..models.player_basic2 import PlayerBasic2
from ..models.schedule_basic2 import ScheduleBasic2
from ..models.score_basic2 import ScoreBasic2
from ..models.season1 import Season1
from ..models.stadium3 import Stadium3
from ..models.standing2 import Standing2
from ..models.team2 import Team2
from ..models.team_game2 import TeamGame2
from ..models.team_season2 import TeamSeason2
from ..models.transaction import Transaction
from ..server.server import Server


class MlbV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MlbV3ScoresWithRawResponse(client, server, auth)

    def mlb_v3_scores_are_games_in_progress(
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
            self._with_raw_response.mlb_v3_scores_are_games_in_progress(
                format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game6]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the innings
        scores and full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_games_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game6]:
        """Full scores and gameday info delivered live and post-game. Live data includes innings, scores, pitch count
        etc. Gameday info includes referee, weather, TV channel etc.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_games_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_games_basic_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic2]:
        """A slimmed-down score endpoint, giving just the innings scores and final score, for simple applications.
        Delivered after the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_games_basic_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_games_basic_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic2]:
        """This endpoint simply delivers the innings count and total score live; no down and distance and no gameday
        info such as weather.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_games_basic_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_news(
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
        return unwrap(self._with_raw_response.mlb_v3_scores_news(format_=format_, request_options=request_options))

    def mlb_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_news_by_date(date, format_=format_, request_options=request_options)
        )

    def mlb_v3_scores_player_details_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player2]:
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
            self._with_raw_response.mlb_v3_scores_player_details_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_player_details_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player2]:
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
            self._with_raw_response.mlb_v3_scores_player_details_by_free_agents(
                format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_player_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic2]:
        """A more stripped-down list of players on a given team, for simple applications, including all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_player_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_player_profiles_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic2]:
        """A more stripped-down list of players on a given team, for simple applications, sorted by free agents.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_player_profiles_by_free_agents(
                format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_player_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic2]:
        """A more stripped-down list of players on a given team, for simple applications.

        Args:
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_player_profiles_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_players_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player2]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_players_details_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game6]:
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
            self._with_raw_response.mlb_v3_scores_schedules(season, format_=format_, request_options=request_options)
        )

    def mlb_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic2]:
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
            self._with_raw_response.mlb_v3_scores_schedules_basic(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Season1:
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
            self._with_raw_response.mlb_v3_scores_season_current(format_=format_, request_options=request_options)
        )

    def mlb_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium3]:
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
        return unwrap(self._with_raw_response.mlb_v3_scores_stadiums(format_=format_, request_options=request_options))

    def mlb_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing2]:
        """Includes regular season standings in division and league, from which postseason seeding can be derived.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_standings(season, format_=format_, request_options=request_options)
        )

    def mlb_v3_scores_team_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame2]:
        """Game by game log of total team statistics.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 12 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_team_game_logs_by_season(
                season, teamid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame2]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date after the game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_team_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_team_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame2]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week, both live and post-game.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_team_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team2]:
        """Full team information: team name and city, league and division, and colors. Also contains basic fantasy info
        such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_team_profiles_all(format_=format_, request_options=request_options)
        )

    def mlb_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team2]:
        """Full team information: team name and city, league and division, and colors. Also contains basic fantasy info
        such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_team_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team2]:
        """List of teams playing in a specified season, with their profile info.

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
            self._with_raw_response.mlb_v3_scores_team_profiles_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason2]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_scores_team_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_scores_transactions(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """A list of transactions, such as assignments, placement on the injury list, player trades etc., delivered by
        date.

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
            self._with_raw_response.mlb_v3_scores_transactions(date, format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> MlbV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncMlbV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMlbV3ScoresWithRawResponse(client, server, auth)

    async def mlb_v3_scores_are_games_in_progress(
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
            await self._with_raw_response.mlb_v3_scores_are_games_in_progress(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game6]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the innings
        scores and full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_games_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game6]:
        """Full scores and gameday info delivered live and post-game. Live data includes innings, scores, pitch count
        etc. Gameday info includes referee, weather, TV channel etc.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_games_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_games_basic_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic2]:
        """A slimmed-down score endpoint, giving just the innings scores and final score, for simple applications.
        Delivered after the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_games_basic_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_games_basic_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic2]:
        """This endpoint simply delivers the innings count and total score live; no down and distance and no gameday
        info such as weather.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_games_basic_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_news(
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
            await self._with_raw_response.mlb_v3_scores_news(format_=format_, request_options=request_options)
        )

    async def mlb_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_player_details_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player2]:
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
            await self._with_raw_response.mlb_v3_scores_player_details_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_player_details_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player2]:
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
            await self._with_raw_response.mlb_v3_scores_player_details_by_free_agents(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_player_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic2]:
        """A more stripped-down list of players on a given team, for simple applications, including all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_player_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_player_profiles_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic2]:
        """A more stripped-down list of players on a given team, for simple applications, sorted by free agents.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_player_profiles_by_free_agents(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_player_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic2]:
        """A more stripped-down list of players on a given team, for simple applications.

        Args:
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_player_profiles_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_players_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player2]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_players_details_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game6]:
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
            await self._with_raw_response.mlb_v3_scores_schedules(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic2]:
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
            await self._with_raw_response.mlb_v3_scores_schedules_basic(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Season1:
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
            await self._with_raw_response.mlb_v3_scores_season_current(format_=format_, request_options=request_options)
        )

    async def mlb_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium3]:
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
            await self._with_raw_response.mlb_v3_scores_stadiums(format_=format_, request_options=request_options)
        )

    async def mlb_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing2]:
        """Includes regular season standings in division and league, from which postseason seeding can be derived.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_standings(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_team_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame2]:
        """Game by game log of total team statistics.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 12 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_team_game_logs_by_season(
                season, teamid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame2]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date after the game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_team_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_team_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame2]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week, both live and post-game.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_team_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team2]:
        """Full team information: team name and city, league and division, and colors. Also contains basic fantasy info
        such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_team_profiles_all(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team2]:
        """Full team information: team name and city, league and division, and colors. Also contains basic fantasy info
        such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_team_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team2]:
        """List of teams playing in a specified season, with their profile info.

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
            await self._with_raw_response.mlb_v3_scores_team_profiles_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason2]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_scores_team_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_scores_transactions(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """A list of transactions, such as assignments, placement on the injury list, player trades etc., delivered by
        date.

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
            await self._with_raw_response.mlb_v3_scores_transactions(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncMlbV3ScoresWithRawResponse:
        return self._with_raw_response


class MlbV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mlb_v3_scores_are_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, MlbV3ScoresAreGamesInProgressErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=mlb_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game6], MlbV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the innings
        scores and full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game6]],
            error_mapper=mlb_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game6], MlbV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes innings, scores, pitch count
        etc. Gameday info includes referee, weather, TV channel etc.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game6]],
            error_mapper=mlb_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_games_basic_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic2], MlbV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the innings scores and final score, for simple applications.
        Delivered after the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic2]],
            error_mapper=mlb_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_games_basic_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic2], MlbV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers the innings count and total score live; no down and distance and no gameday
        info such as weather.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic2]],
            error_mapper=mlb_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], MlbV3ScoresNewsErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=mlb_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], MlbV3ScoresNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=mlb_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_player_details_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player2], MlbV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player2]],
            error_mapper=mlb_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_player_details_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player2], MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player2]],
            error_mapper=mlb_v3_scores_player_details_by_free_agents_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_player_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByActiveErrorBody]:
        """A more stripped-down list of players on a given team, for simple applications, including all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/PlayersByActive"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic2]],
            error_mapper=mlb_v3_scores_player_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_player_profiles_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody]:
        """A more stripped-down list of players on a given team, for simple applications, sorted by free agents.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic2]],
            error_mapper=mlb_v3_scores_player_profiles_by_free_agents_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_player_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByTeamErrorBody]:
        """A more stripped-down list of players on a given team, for simple applications.

        Args:
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic2]],
            error_mapper=mlb_v3_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_players_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player2], MlbV3ScoresPlayersDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player2]],
            error_mapper=mlb_v3_scores_players_details_by_team_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game6], MlbV3ScoresSchedulesErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game6]],
            error_mapper=mlb_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic2], MlbV3ScoresSchedulesBasicErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic2]],
            error_mapper=mlb_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season1, MlbV3ScoresSeasonCurrentErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season1],
            error_mapper=mlb_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium3], MlbV3ScoresStadiumsErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium3]],
            error_mapper=mlb_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing2], MlbV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and league, from which postseason seeding can be derived.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Standing2]],
            error_mapper=mlb_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_team_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame2], MlbV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game by game log of total team statistics.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 12 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame2]],
            error_mapper=mlb_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame2], MlbV3ScoresTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date after the game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame2]],
            error_mapper=mlb_v3_scores_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_team_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame2], MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week, both live and post-game.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame2]],
            error_mapper=mlb_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team2], MlbV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, league and division, and colors. Also contains basic fantasy info
        such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team2]],
            error_mapper=mlb_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team2], MlbV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, league and division, and colors. Also contains basic fantasy info
        such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/teams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team2]],
            error_mapper=mlb_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team2], MlbV3ScoresTeamProfilesBySeasonErrorBody]:
        """List of teams playing in a specified season, with their profile info.

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
            url_template=self._server.default("/v3/mlb/scores/{format}/teams/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team2]],
            error_mapper=mlb_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason2], MlbV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason2]],
            error_mapper=mlb_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_scores_transactions(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], MlbV3ScoresTransactionsErrorBody]:
        """A list of transactions, such as assignments, placement on the injury list, player trades etc., delivered by
        date.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Transaction]],
            error_mapper=mlb_v3_scores_transactions_error_mapper,
            request_options=request_options,
        )


class AsyncMlbV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mlb_v3_scores_are_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, MlbV3ScoresAreGamesInProgressErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[bool],
            error_mapper=mlb_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game6], MlbV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the innings
        scores and full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game6]],
            error_mapper=mlb_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game6], MlbV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes innings, scores, pitch count
        etc. Gameday info includes referee, weather, TV channel etc.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game6]],
            error_mapper=mlb_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_games_basic_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic2], MlbV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the innings scores and final score, for simple applications.
        Delivered after the game ends.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScoreBasic2]],
            error_mapper=mlb_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_games_basic_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic2], MlbV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers the innings count and total score live; no down and distance and no gameday
        info such as weather.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScoreBasic2]],
            error_mapper=mlb_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], MlbV3ScoresNewsErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=mlb_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], MlbV3ScoresNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=mlb_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_player_details_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player2], MlbV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player2]],
            error_mapper=mlb_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_player_details_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player2], MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody]:
        """Full player bio and details, including injury notes, for all available free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player2]],
            error_mapper=mlb_v3_scores_player_details_by_free_agents_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_player_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByActiveErrorBody]:
        """A more stripped-down list of players on a given team, for simple applications, including all active players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/PlayersByActive"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic2]],
            error_mapper=mlb_v3_scores_player_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_player_profiles_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody]:
        """A more stripped-down list of players on a given team, for simple applications, sorted by free agents.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic2]],
            error_mapper=mlb_v3_scores_player_profiles_by_free_agents_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_player_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByTeamErrorBody]:
        """A more stripped-down list of players on a given team, for simple applications.

        Args:
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic2]],
            error_mapper=mlb_v3_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_players_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player2], MlbV3ScoresPlayersDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player2]],
            error_mapper=mlb_v3_scores_players_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game6], MlbV3ScoresSchedulesErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game6]],
            error_mapper=mlb_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic2], MlbV3ScoresSchedulesBasicErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScheduleBasic2]],
            error_mapper=mlb_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season1, MlbV3ScoresSeasonCurrentErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[Season1],
            error_mapper=mlb_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium3], MlbV3ScoresStadiumsErrorBody]:
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
            url_template=self._server.default("/v3/mlb/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Stadium3]],
            error_mapper=mlb_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing2], MlbV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and league, from which postseason seeding can be derived.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Standing2]],
            error_mapper=mlb_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_team_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame2], MlbV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game by game log of total team statistics.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 12 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame2]],
            error_mapper=mlb_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame2], MlbV3ScoresTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date after the game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame2]],
            error_mapper=mlb_v3_scores_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_team_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame2], MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week, both live and post-game.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame2]],
            error_mapper=mlb_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team2], MlbV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, league and division, and colors. Also contains basic fantasy info
        such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team2]],
            error_mapper=mlb_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team2], MlbV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, league and division, and colors. Also contains basic fantasy info
        such as IDs as well as full stadium data. This endpoint returns the teams currently active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/teams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team2]],
            error_mapper=mlb_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team2], MlbV3ScoresTeamProfilesBySeasonErrorBody]:
        """List of teams playing in a specified season, with their profile info.

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
            url_template=self._server.default("/v3/mlb/scores/{format}/teams/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team2]],
            error_mapper=mlb_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason2], MlbV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamSeason2]],
            error_mapper=mlb_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_scores_transactions(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], MlbV3ScoresTransactionsErrorBody]:
        """A list of transactions, such as assignments, placement on the injury list, player trades etc., delivered by
        date.

        Args:
            date: The date of the news. <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Transaction]],
            error_mapper=mlb_v3_scores_transactions_error_mapper,
            request_options=request_options,
        )
