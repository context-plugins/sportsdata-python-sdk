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
from ..errors.nfl_v3_scores_are_games_in_progress_error import (
    NflV3ScoresAreGamesInProgressErrorBody,
    nfl_v3_scores_are_games_in_progress_error_mapper,
)
from ..errors.nfl_v3_scores_bye_weeks_error import NflV3ScoresByeWeeksErrorBody, nfl_v3_scores_bye_weeks_error_mapper
from ..errors.nfl_v3_scores_depth_charts_all_error import (
    NflV3ScoresDepthChartsAllErrorBody,
    nfl_v3_scores_depth_charts_all_error_mapper,
)
from ..errors.nfl_v3_scores_depth_charts_by_active_error import (
    NflV3ScoresDepthChartsByActiveErrorBody,
    nfl_v3_scores_depth_charts_by_active_error_mapper,
)
from ..errors.nfl_v3_scores_depth_charts_by_week_error import (
    NflV3ScoresDepthChartsByWeekErrorBody,
    nfl_v3_scores_depth_charts_by_week_error_mapper,
)
from ..errors.nfl_v3_scores_games_basic_by_week_final_error import (
    NflV3ScoresGamesBasicByWeekFinalErrorBody,
    nfl_v3_scores_games_basic_by_week_final_error_mapper,
)
from ..errors.nfl_v3_scores_games_basic_by_week_live_final_error import (
    NflV3ScoresGamesBasicByWeekLiveFinalErrorBody,
    nfl_v3_scores_games_basic_by_week_live_final_error_mapper,
)
from ..errors.nfl_v3_scores_games_by_date_final_error import (
    NflV3ScoresGamesByDateFinalErrorBody,
    nfl_v3_scores_games_by_date_final_error_mapper,
)
from ..errors.nfl_v3_scores_games_by_date_live_final_error import (
    NflV3ScoresGamesByDateLiveFinalErrorBody,
    nfl_v3_scores_games_by_date_live_final_error_mapper,
)
from ..errors.nfl_v3_scores_games_by_season_live_final_error import (
    NflV3ScoresGamesBySeasonLiveFinalErrorBody,
    nfl_v3_scores_games_by_season_live_final_error_mapper,
)
from ..errors.nfl_v3_scores_games_by_week_final_error import (
    NflV3ScoresGamesByWeekFinalErrorBody,
    nfl_v3_scores_games_by_week_final_error_mapper,
)
from ..errors.nfl_v3_scores_games_by_week_live_final_error import (
    NflV3ScoresGamesByWeekLiveFinalErrorBody,
    nfl_v3_scores_games_by_week_live_final_error_mapper,
)
from ..errors.nfl_v3_scores_news_by_date_error import (
    NflV3ScoresNewsByDateErrorBody,
    nfl_v3_scores_news_by_date_error_mapper,
)
from ..errors.nfl_v3_scores_news_by_team_error import (
    NflV3ScoresNewsByTeamErrorBody,
    nfl_v3_scores_news_by_team_error_mapper,
)
from ..errors.nfl_v3_scores_news_error import NflV3ScoresNewsErrorBody, nfl_v3_scores_news_error_mapper
from ..errors.nfl_v3_scores_player_details_all_error import (
    NflV3ScoresPlayerDetailsAllErrorBody,
    nfl_v3_scores_player_details_all_error_mapper,
)
from ..errors.nfl_v3_scores_player_details_by_free_agents_error import (
    NflV3ScoresPlayerDetailsByFreeAgentsErrorBody,
    nfl_v3_scores_player_details_by_free_agents_error_mapper,
)
from ..errors.nfl_v3_scores_player_details_by_rookie_draft_year_error import (
    NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody,
    nfl_v3_scores_player_details_by_rookie_draft_year_error_mapper,
)
from ..errors.nfl_v3_scores_player_details_by_team_error import (
    NflV3ScoresPlayerDetailsByTeamErrorBody,
    nfl_v3_scores_player_details_by_team_error_mapper,
)
from ..errors.nfl_v3_scores_player_game_logs_by_season_error import (
    NflV3ScoresPlayerGameLogsBySeasonErrorBody,
    nfl_v3_scores_player_game_logs_by_season_error_mapper,
)
from ..errors.nfl_v3_scores_player_profiles_all_error import (
    NflV3ScoresPlayerProfilesAllErrorBody,
    nfl_v3_scores_player_profiles_all_error_mapper,
)
from ..errors.nfl_v3_scores_player_profiles_by_free_agent_error import (
    NflV3ScoresPlayerProfilesByFreeAgentErrorBody,
    nfl_v3_scores_player_profiles_by_free_agent_error_mapper,
)
from ..errors.nfl_v3_scores_player_profiles_by_rookie_draft_year_error import (
    NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody,
    nfl_v3_scores_player_profiles_by_rookie_draft_year_error_mapper,
)
from ..errors.nfl_v3_scores_player_profiles_by_team_error import (
    NflV3ScoresPlayerProfilesByTeamErrorBody,
    nfl_v3_scores_player_profiles_by_team_error_mapper,
)
from ..errors.nfl_v3_scores_referees_error import NflV3ScoresRefereesErrorBody, nfl_v3_scores_referees_error_mapper
from ..errors.nfl_v3_scores_schedules_basic_error import (
    NflV3ScoresSchedulesBasicErrorBody,
    nfl_v3_scores_schedules_basic_error_mapper,
)
from ..errors.nfl_v3_scores_schedules_error import NflV3ScoresSchedulesErrorBody, nfl_v3_scores_schedules_error_mapper
from ..errors.nfl_v3_scores_scores_by_week_simulation_error import (
    NflV3ScoresScoresByWeekSimulationErrorBody,
    nfl_v3_scores_scores_by_week_simulation_error_mapper,
)
from ..errors.nfl_v3_scores_season_current_error import (
    NflV3ScoresSeasonCurrentErrorBody,
    nfl_v3_scores_season_current_error_mapper,
)
from ..errors.nfl_v3_scores_season_last_completed_error import (
    NflV3ScoresSeasonLastCompletedErrorBody,
    nfl_v3_scores_season_last_completed_error_mapper,
)
from ..errors.nfl_v3_scores_season_upcoming_error import (
    NflV3ScoresSeasonUpcomingErrorBody,
    nfl_v3_scores_season_upcoming_error_mapper,
)
from ..errors.nfl_v3_scores_stadiums_error import NflV3ScoresStadiumsErrorBody, nfl_v3_scores_stadiums_error_mapper
from ..errors.nfl_v3_scores_standings_error import NflV3ScoresStandingsErrorBody, nfl_v3_scores_standings_error_mapper
from ..errors.nfl_v3_scores_team_game_stats_live_final_error import (
    NflV3ScoresTeamGameStatsLiveFinalErrorBody,
    nfl_v3_scores_team_game_stats_live_final_error_mapper,
)
from ..errors.nfl_v3_scores_team_profiles_all_error import (
    NflV3ScoresTeamProfilesAllErrorBody,
    nfl_v3_scores_team_profiles_all_error_mapper,
)
from ..errors.nfl_v3_scores_team_profiles_basic_all_error import (
    NflV3ScoresTeamProfilesBasicAllErrorBody,
    nfl_v3_scores_team_profiles_basic_all_error_mapper,
)
from ..errors.nfl_v3_scores_team_profiles_by_active_error import (
    NflV3ScoresTeamProfilesByActiveErrorBody,
    nfl_v3_scores_team_profiles_by_active_error_mapper,
)
from ..errors.nfl_v3_scores_team_profiles_by_season_error import (
    NflV3ScoresTeamProfilesBySeasonErrorBody,
    nfl_v3_scores_team_profiles_by_season_error_mapper,
)
from ..errors.nfl_v3_scores_team_season_stats_error import (
    NflV3ScoresTeamSeasonStatsErrorBody,
    nfl_v3_scores_team_season_stats_error_mapper,
)
from ..errors.nfl_v3_scores_timeframes_error import (
    NflV3ScoresTimeframesErrorBody,
    nfl_v3_scores_timeframes_error_mapper,
)
from ..errors.nfl_v3_scores_transactions_by_date_error import (
    NflV3ScoresTransactionsByDateErrorBody,
    nfl_v3_scores_transactions_by_date_error_mapper,
)
from ..errors.nfl_v3_scores_week_current_error import (
    NflV3ScoresWeekCurrentErrorBody,
    nfl_v3_scores_week_current_error_mapper,
)
from ..errors.nfl_v3_scores_week_last_completed_error import (
    NflV3ScoresWeekLastCompletedErrorBody,
    nfl_v3_scores_week_last_completed_error_mapper,
)
from ..errors.nfl_v3_scores_week_upcoming_error import (
    NflV3ScoresWeekUpcomingErrorBody,
    nfl_v3_scores_week_upcoming_error_mapper,
)
from ..models.bye import Bye
from ..models.enums.format import Format, FormatOrStr
from ..models.enums.type import Type, TypeOrStr
from ..models.news import News
from ..models.player import Player
from ..models.player_basic import PlayerBasic
from ..models.player_detail import PlayerDetail
from ..models.referee import Referee
from ..models.schedule import Schedule
from ..models.schedule_basic import ScheduleBasic
from ..models.score import Score
from ..models.score_basic import ScoreBasic
from ..models.stadium import Stadium
from ..models.standing import Standing
from ..models.team import Team
from ..models.team_basic import TeamBasic
from ..models.team_depth_chart import TeamDepthChart
from ..models.team_depth_chart_weekly import TeamDepthChartWeekly
from ..models.team_game import TeamGame
from ..models.team_season import TeamSeason
from ..models.timeframe import Timeframe
from ..models.transaction import Transaction
from ..server.server import Server


class NflV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NflV3ScoresWithRawResponse(client, server, auth)

    def nfl_v3_scores_are_games_in_progress(
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
            self._with_raw_response.nfl_v3_scores_are_games_in_progress(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_bye_weeks(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Bye]:
        """Get bye weeks for the teams during a specified NFL season.

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
            self._with_raw_response.nfl_v3_scores_bye_weeks(season, format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_depth_charts_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart]:
        """Depth charts for all players in all NFL teams split by offensive, defensive, and special teams position
        groupings.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_depth_charts_all(format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_depth_charts_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart]:
        """Depth charts for all active players NFL teams split by offensive, defensive, and special teams position
        groupings.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_depth_charts_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_depth_charts_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamDepthChartWeekly]:
        """Depth charts for active players by week in all NFL teams split by offensive, defensive, and special teams
        position groupings.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_depth_charts_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Score]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_games_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Score]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_games_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_games_by_season_live_final(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Score]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

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
            self._with_raw_response.nfl_v3_scores_games_by_season_live_final(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_games_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Score]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_games_by_week_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_games_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Score]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_games_by_week_live_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_games_basic_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScoreBasic]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_games_basic_by_week_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_games_basic_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScoreBasic]:
        """This endpoint simply delivers the game clock and quarter and total scores live; no down and distance and no
        gameday info such as weather.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_games_basic_by_week_live_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_news(
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
        return unwrap(self._with_raw_response.nfl_v3_scores_news(format_=format_, request_options=request_options))

    def nfl_v3_scores_news_by_date(
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
            self._with_raw_response.nfl_v3_scores_news_by_date(date, format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_news_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_news_by_team(team, format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_player_details_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player]:
        """Full player bio and details, including injury notes, for all NFL players in our database.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_player_details_all(format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_player_details_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player]:
        """Full player bio and details, including injury notes, for all available NFL free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_player_details_by_free_agents(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_player_details_by_rookie_draft_year(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player]:
        """Full player bio and details, including injury notes, for all available NFL players by a specified draft year.

        Args:
            season: Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_player_details_by_rookie_draft_year(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_player_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerDetail]:
        """Full player bio and details, including injury notes, for all available NFL players by team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_player_details_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_player_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

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
            self._with_raw_response.nfl_v3_scores_player_game_logs_by_season(
                season, teamid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_player_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_player_profiles_all(format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_player_profiles_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic]:
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
            self._with_raw_response.nfl_v3_scores_player_profiles_by_free_agent(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_player_profiles_by_rookie_draft_year(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) Specify a year parameter to receive all player profiles from that rookie draft year.

        Args:
            season: Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_player_profiles_by_rookie_draft_year(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_player_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_player_profiles_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_referees(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Referee]:
        """Returns referees with name, numbers, position (e.g. FJ for Field Judge), college, and years of experience.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(self._with_raw_response.nfl_v3_scores_referees(format_=format_, request_options=request_options))

    def nfl_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Schedule]:
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
            self._with_raw_response.nfl_v3_scores_schedules(season, format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic]:
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
            self._with_raw_response.nfl_v3_scores_schedules_basic(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_scores_by_week_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Score]:
        """Gets simulated live scores of NFL games, covering the Conference Championship games on January 21, 2018.

        Args:
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_scores_by_week_simulation(
                numberofplays, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Year of the current NFL season. This value changes at the start of the new NFL league year. NFL seasons run
        across two calendar years; the league year is the one in which it starts, not ends (that is, a season starting
        in 2023 and ending in 2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_season_current(format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_season_last_completed(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Year of the most recently completed NFL season. This value changes immediately after the Super Bowl. NFL
        seasons run across two calendar years; the league year is the one in which it starts, not ends (that is, a
        season starting in 2023 and ending in 2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_season_last_completed(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_season_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Year of the current NFL season, if we are in the mid-season. If we are in the off-season, then year of the
        next upcoming season. This value changes immediately after the Super Bowl. NFL seasons run across two calendar
        years; the league year is the one in which it starts, not ends (that is, a season starting in 2023 and ending in
        2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_season_upcoming(format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium]:
        """Returns all stadiums in the NFL with capacity, surface, latitude/longitude, city and state (and, where
        applicable, country.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(self._with_raw_response.nfl_v3_scores_stadiums(format_=format_, request_options=request_options))

    def nfl_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

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
            self._with_raw_response.nfl_v3_scores_standings(season, format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_team_game_stats_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week, during the game and with final stats after it ends.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_team_game_stats_live_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns all teams regardless
        of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_team_profiles_all(format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns the teams currently
        active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_team_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns the active teams for
        a given season.

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
            self._with_raw_response.nfl_v3_scores_team_profiles_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_team_profiles_basic_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamBasic]:
        """The most basic top-line team information, such as team name and city, conference and division, stadium ID,
        coach info, and team colors. Returns all teams regardless of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_team_profiles_basic_all(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

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
            self._with_raw_response.nfl_v3_scores_team_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_timeframes(
        self,
        *,
        format_: FormatOrStr = Format.JSON,
        type_: TypeOrStr = Type.CURRENT,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Timeframe]:
        """Timeframes for the NFL refer to current weeks, season status etc.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            type_: The type of timeframes to return. Valid entries are <code>current</code> or <code>upcoming</code> or
                <code>completed</code> or <code>recent</code> or <code>all</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_timeframes(
                format_=format_, type_=type_, request_options=request_options
            ),
        )

    def nfl_v3_scores_transactions_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """Includes a list of transactions for a given date, with type (e.g. trade, injury listing, assignment) and a
        brief note.

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
            self._with_raw_response.nfl_v3_scores_transactions_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_scores_week_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday
        mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard gameday this
        could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_week_current(format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_week_last_completed(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Number of the last completed week of the NFL season. This value usually changes on Tuesday nights or
        Wednesday mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard
        gameday this could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_week_last_completed(format_=format_, request_options=request_options)
        )

    def nfl_v3_scores_week_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Number of the next upcoming week of the NFL season. This value usually changes on Tuesday nights or Wednesday
        mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard gameday this
        could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_scores_week_upcoming(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> NflV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncNflV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNflV3ScoresWithRawResponse(client, server, auth)

    async def nfl_v3_scores_are_games_in_progress(
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
            await self._with_raw_response.nfl_v3_scores_are_games_in_progress(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_bye_weeks(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Bye]:
        """Get bye weeks for the teams during a specified NFL season.

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
            await self._with_raw_response.nfl_v3_scores_bye_weeks(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_depth_charts_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart]:
        """Depth charts for all players in all NFL teams split by offensive, defensive, and special teams position
        groupings.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_depth_charts_all(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_depth_charts_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart]:
        """Depth charts for all active players NFL teams split by offensive, defensive, and special teams position
        groupings.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_depth_charts_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_depth_charts_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamDepthChartWeekly]:
        """Depth charts for active players by week in all NFL teams split by offensive, defensive, and special teams
        position groupings.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_depth_charts_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Score]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_games_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Score]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_games_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_games_by_season_live_final(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Score]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

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
            await self._with_raw_response.nfl_v3_scores_games_by_season_live_final(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_games_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Score]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_games_by_week_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_games_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Score]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_games_by_week_live_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_games_basic_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScoreBasic]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_games_basic_by_week_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_games_basic_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScoreBasic]:
        """This endpoint simply delivers the game clock and quarter and total scores live; no down and distance and no
        gameday info such as weather.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_games_basic_by_week_live_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_news(
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
            await self._with_raw_response.nfl_v3_scores_news(format_=format_, request_options=request_options)
        )

    async def nfl_v3_scores_news_by_date(
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
            await self._with_raw_response.nfl_v3_scores_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_news_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_news_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_details_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player]:
        """Full player bio and details, including injury notes, for all NFL players in our database.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_player_details_all(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_details_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player]:
        """Full player bio and details, including injury notes, for all available NFL free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_player_details_by_free_agents(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_details_by_rookie_draft_year(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player]:
        """Full player bio and details, including injury notes, for all available NFL players by a specified draft year.

        Args:
            season: Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_player_details_by_rookie_draft_year(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerDetail]:
        """Full player bio and details, including injury notes, for all available NFL players by team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_player_details_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

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
            await self._with_raw_response.nfl_v3_scores_player_game_logs_by_season(
                season, teamid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_player_profiles_all(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_profiles_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic]:
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
            await self._with_raw_response.nfl_v3_scores_player_profiles_by_free_agent(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_profiles_by_rookie_draft_year(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) Specify a year parameter to receive all player profiles from that rookie draft year.

        Args:
            season: Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_player_profiles_by_rookie_draft_year(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_player_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_player_profiles_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_referees(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Referee]:
        """Returns referees with name, numbers, position (e.g. FJ for Field Judge), college, and years of experience.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_referees(format_=format_, request_options=request_options)
        )

    async def nfl_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Schedule]:
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
            await self._with_raw_response.nfl_v3_scores_schedules(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic]:
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
            await self._with_raw_response.nfl_v3_scores_schedules_basic(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_scores_by_week_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Score]:
        """Gets simulated live scores of NFL games, covering the Conference Championship games on January 21, 2018.

        Args:
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_scores_by_week_simulation(
                numberofplays, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Year of the current NFL season. This value changes at the start of the new NFL league year. NFL seasons run
        across two calendar years; the league year is the one in which it starts, not ends (that is, a season starting
        in 2023 and ending in 2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_season_current(format_=format_, request_options=request_options)
        )

    async def nfl_v3_scores_season_last_completed(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Year of the most recently completed NFL season. This value changes immediately after the Super Bowl. NFL
        seasons run across two calendar years; the league year is the one in which it starts, not ends (that is, a
        season starting in 2023 and ending in 2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_season_last_completed(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_season_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Year of the current NFL season, if we are in the mid-season. If we are in the off-season, then year of the
        next upcoming season. This value changes immediately after the Super Bowl. NFL seasons run across two calendar
        years; the league year is the one in which it starts, not ends (that is, a season starting in 2023 and ending in
        2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_season_upcoming(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium]:
        """Returns all stadiums in the NFL with capacity, surface, latitude/longitude, city and state (and, where
        applicable, country.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_stadiums(format_=format_, request_options=request_options)
        )

    async def nfl_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Standing]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

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
            await self._with_raw_response.nfl_v3_scores_standings(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_team_game_stats_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week, during the game and with final stats after it ends.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_team_game_stats_live_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns all teams regardless
        of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_team_profiles_all(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns the teams currently
        active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_team_profiles_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns the active teams for
        a given season.

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
            await self._with_raw_response.nfl_v3_scores_team_profiles_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_team_profiles_basic_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamBasic]:
        """The most basic top-line team information, such as team name and city, conference and division, stadium ID,
        coach info, and team colors. Returns all teams regardless of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_team_profiles_basic_all(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

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
            await self._with_raw_response.nfl_v3_scores_team_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_timeframes(
        self,
        *,
        format_: FormatOrStr = Format.JSON,
        type_: TypeOrStr = Type.CURRENT,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Timeframe]:
        """Timeframes for the NFL refer to current weeks, season status etc.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            type_: The type of timeframes to return. Valid entries are <code>current</code> or <code>upcoming</code> or
                <code>completed</code> or <code>recent</code> or <code>all</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_timeframes(
                format_=format_, type_=type_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_transactions_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Transaction]:
        """Includes a list of transactions for a given date, with type (e.g. trade, injury listing, assignment) and a
        brief note.

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
            await self._with_raw_response.nfl_v3_scores_transactions_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_week_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday
        mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard gameday this
        could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_week_current(format_=format_, request_options=request_options)
        )

    async def nfl_v3_scores_week_last_completed(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Number of the last completed week of the NFL season. This value usually changes on Tuesday nights or
        Wednesday mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard
        gameday this could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_week_last_completed(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_scores_week_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Number of the next upcoming week of the NFL season. This value usually changes on Tuesday nights or Wednesday
        mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard gameday this
        could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_scores_week_upcoming(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncNflV3ScoresWithRawResponse:
        return self._with_raw_response


class NflV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfl_v3_scores_are_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, NflV3ScoresAreGamesInProgressErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=nfl_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_bye_weeks(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Bye], NflV3ScoresByeWeeksErrorBody]:
        """Get bye weeks for the teams during a specified NFL season.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/Byes/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Bye]],
            error_mapper=nfl_v3_scores_bye_weeks_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_depth_charts_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart], NflV3ScoresDepthChartsAllErrorBody]:
        """Depth charts for all players in all NFL teams split by offensive, defensive, and special teams position
        groupings.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/DepthChartsAll"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamDepthChart]],
            error_mapper=nfl_v3_scores_depth_charts_all_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_depth_charts_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart], NflV3ScoresDepthChartsByActiveErrorBody]:
        """Depth charts for all active players NFL teams split by offensive, defensive, and special teams position
        groupings.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/DepthCharts"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamDepthChart]],
            error_mapper=nfl_v3_scores_depth_charts_by_active_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_depth_charts_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamDepthChartWeekly], NflV3ScoresDepthChartsByWeekErrorBody]:
        """Depth charts for active players by week in all NFL teams split by offensive, defensive, and special teams
        position groupings.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/DepthChartsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamDepthChartWeekly]],
            error_mapper=nfl_v3_scores_depth_charts_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Score], NflV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Score], NflV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_games_by_season_live_final(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Score], NflV3ScoresGamesBySeasonLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/Scores/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_season_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_games_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Score], NflV3ScoresGamesByWeekFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_week_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_games_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Score], NflV3ScoresGamesByWeekLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_games_basic_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScoreBasic], NflV3ScoresGamesBasicByWeekFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresBasicFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic]],
            error_mapper=nfl_v3_scores_games_basic_by_week_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_games_basic_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScoreBasic], NflV3ScoresGamesBasicByWeekLiveFinalErrorBody]:
        """This endpoint simply delivers the game clock and quarter and total scores live; no down and distance and no
        gameday info such as weather.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresBasic/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic]],
            error_mapper=nfl_v3_scores_games_basic_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3ScoresNewsErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3ScoresNewsByDateErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_news_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3ScoresNewsByTeamErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/NewsByTeam/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_scores_news_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_details_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player], NflV3ScoresPlayerDetailsAllErrorBody]:
        """Full player bio and details, including injury notes, for all NFL players in our database.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player]],
            error_mapper=nfl_v3_scores_player_details_all_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_details_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player], NflV3ScoresPlayerDetailsByFreeAgentsErrorBody]:
        """Full player bio and details, including injury notes, for all available NFL free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player]],
            error_mapper=nfl_v3_scores_player_details_by_free_agents_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_details_by_rookie_draft_year(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player], NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody]:
        """Full player bio and details, including injury notes, for all available NFL players by a specified draft year.

        Args:
            season: Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Rookies/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player]],
            error_mapper=nfl_v3_scores_player_details_by_rookie_draft_year_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerDetail], NflV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available NFL players by team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerDetail]],
            error_mapper=nfl_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame], NflV3ScoresPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

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
                "/v3/nfl/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame]],
            error_mapper=nfl_v3_scores_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesAllErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/PlayersByAvailable"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic]],
            error_mapper=nfl_v3_scores_player_profiles_all_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_profiles_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByFreeAgentErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic]],
            error_mapper=nfl_v3_scores_player_profiles_by_free_agent_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_profiles_by_rookie_draft_year(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) Specify a year parameter to receive all player profiles from that rookie draft year.

        Args:
            season: Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/PlayersByRookieDraftYear/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic]],
            error_mapper=nfl_v3_scores_player_profiles_by_rookie_draft_year_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_player_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic]],
            error_mapper=nfl_v3_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_referees(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Referee], NflV3ScoresRefereesErrorBody]:
        """Returns referees with name, numbers, position (e.g. FJ for Field Judge), college, and years of experience.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Referees"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Referee]],
            error_mapper=nfl_v3_scores_referees_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Schedule], NflV3ScoresSchedulesErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/Schedules/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Schedule]],
            error_mapper=nfl_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic], NflV3ScoresSchedulesBasicErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic]],
            error_mapper=nfl_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_scores_by_week_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Score], NflV3ScoresScoresByWeekSimulationErrorBody]:
        """Gets simulated live scores of NFL games, covering the Conference Championship games on January 21, 2018.

        Args:
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/SimulatedScores/{numberofplays}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("numberofplays", numberofplays)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_scores_by_week_simulation_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresSeasonCurrentErrorBody]:
        """Year of the current NFL season. This value changes at the start of the new NFL league year. NFL seasons run
        across two calendar years; the league year is the one in which it starts, not ends (that is, a season starting
        in 2023 and ending in 2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int | None],
            error_mapper=nfl_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_season_last_completed(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresSeasonLastCompletedErrorBody]:
        """Year of the most recently completed NFL season. This value changes immediately after the Super Bowl. NFL
        seasons run across two calendar years; the league year is the one in which it starts, not ends (that is, a
        season starting in 2023 and ending in 2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/LastCompletedSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int | None],
            error_mapper=nfl_v3_scores_season_last_completed_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_season_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresSeasonUpcomingErrorBody]:
        """Year of the current NFL season, if we are in the mid-season. If we are in the off-season, then year of the
        next upcoming season. This value changes immediately after the Super Bowl. NFL seasons run across two calendar
        years; the league year is the one in which it starts, not ends (that is, a season starting in 2023 and ending in
        2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/UpcomingSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int | None],
            error_mapper=nfl_v3_scores_season_upcoming_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium], NflV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the NFL with capacity, surface, latitude/longitude, city and state (and, where
        applicable, country.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium]],
            error_mapper=nfl_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing], NflV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Standing]],
            error_mapper=nfl_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_team_game_stats_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame], NflV3ScoresTeamGameStatsLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week, during the game and with final stats after it ends.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/TeamGameStats/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame]],
            error_mapper=nfl_v3_scores_team_game_stats_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team], NflV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns all teams regardless
        of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team]],
            error_mapper=nfl_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team], NflV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns the teams currently
        active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Teams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team]],
            error_mapper=nfl_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team], NflV3ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns the active teams for
        a given season.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/Teams/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team]],
            error_mapper=nfl_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_team_profiles_basic_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamBasic], NflV3ScoresTeamProfilesBasicAllErrorBody]:
        """The most basic top-line team information, such as team name and city, conference and division, stadium ID,
        coach info, and team colors. Returns all teams regardless of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/TeamsBasic"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamBasic]],
            error_mapper=nfl_v3_scores_team_profiles_basic_all_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason], NflV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason]],
            error_mapper=nfl_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_timeframes(
        self,
        *,
        format_: FormatOrStr = Format.JSON,
        type_: TypeOrStr = Type.CURRENT,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Timeframe], NflV3ScoresTimeframesErrorBody]:
        """Timeframes for the NFL refer to current weeks, season status etc.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            type_: The type of timeframes to return. Valid entries are <code>current</code> or <code>upcoming</code> or
                <code>completed</code> or <code>recent</code> or <code>all</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Timeframes/{type}"),
            path_params=[param[FormatOrStr]("format", format_), param[TypeOrStr]("type", type_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Timeframe]],
            error_mapper=nfl_v3_scores_timeframes_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_transactions_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], NflV3ScoresTransactionsByDateErrorBody]:
        """Includes a list of transactions for a given date, with type (e.g. trade, injury listing, assignment) and a
        brief note.

        Args:
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Transaction]],
            error_mapper=nfl_v3_scores_transactions_by_date_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_week_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresWeekCurrentErrorBody]:
        """Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday
        mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard gameday this
        could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/CurrentWeek"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int | None],
            error_mapper=nfl_v3_scores_week_current_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_week_last_completed(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresWeekLastCompletedErrorBody]:
        """Number of the last completed week of the NFL season. This value usually changes on Tuesday nights or
        Wednesday mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard
        gameday this could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/LastCompletedWeek"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int | None],
            error_mapper=nfl_v3_scores_week_last_completed_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_scores_week_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresWeekUpcomingErrorBody]:
        """Number of the next upcoming week of the NFL season. This value usually changes on Tuesday nights or Wednesday
        mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard gameday this
        could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/UpcomingWeek"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int | None],
            error_mapper=nfl_v3_scores_week_upcoming_error_mapper,
            request_options=request_options,
        )


class AsyncNflV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfl_v3_scores_are_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, NflV3ScoresAreGamesInProgressErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[bool],
            error_mapper=nfl_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_bye_weeks(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Bye], NflV3ScoresByeWeeksErrorBody]:
        """Get bye weeks for the teams during a specified NFL season.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/Byes/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Bye]],
            error_mapper=nfl_v3_scores_bye_weeks_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_depth_charts_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart], NflV3ScoresDepthChartsAllErrorBody]:
        """Depth charts for all players in all NFL teams split by offensive, defensive, and special teams position
        groupings.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/DepthChartsAll"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamDepthChart]],
            error_mapper=nfl_v3_scores_depth_charts_all_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_depth_charts_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart], NflV3ScoresDepthChartsByActiveErrorBody]:
        """Depth charts for all active players NFL teams split by offensive, defensive, and special teams position
        groupings.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/DepthCharts"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamDepthChart]],
            error_mapper=nfl_v3_scores_depth_charts_by_active_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_depth_charts_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamDepthChartWeekly], NflV3ScoresDepthChartsByWeekErrorBody]:
        """Depth charts for active players by week in all NFL teams split by offensive, defensive, and special teams
        position groupings.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/DepthChartsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamDepthChartWeekly]],
            error_mapper=nfl_v3_scores_depth_charts_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Score], NflV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Score], NflV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_games_by_season_live_final(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Score], NflV3ScoresGamesBySeasonLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/Scores/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_season_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_games_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Score], NflV3ScoresGamesByWeekFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_week_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_games_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Score], NflV3ScoresGamesByWeekLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes down and distance, as well as
        game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_games_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_games_basic_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScoreBasic], NflV3ScoresGamesBasicByWeekFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresBasicFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScoreBasic]],
            error_mapper=nfl_v3_scores_games_basic_by_week_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_games_basic_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScoreBasic], NflV3ScoresGamesBasicByWeekLiveFinalErrorBody]:
        """This endpoint simply delivers the game clock and quarter and total scores live; no down and distance and no
        gameday info such as weather.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/ScoresBasic/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScoreBasic]],
            error_mapper=nfl_v3_scores_games_basic_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3ScoresNewsErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/News"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nfl_v3_scores_news_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3ScoresNewsByDateErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nfl_v3_scores_news_by_date_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_news_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3ScoresNewsByTeamErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/NewsByTeam/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nfl_v3_scores_news_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_details_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player], NflV3ScoresPlayerDetailsAllErrorBody]:
        """Full player bio and details, including injury notes, for all NFL players in our database.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player]],
            error_mapper=nfl_v3_scores_player_details_all_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_details_by_free_agents(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player], NflV3ScoresPlayerDetailsByFreeAgentsErrorBody]:
        """Full player bio and details, including injury notes, for all available NFL free agents unattached to a team.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/FreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player]],
            error_mapper=nfl_v3_scores_player_details_by_free_agents_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_details_by_rookie_draft_year(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player], NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody]:
        """Full player bio and details, including injury notes, for all available NFL players by a specified draft year.

        Args:
            season: Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Rookies/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player]],
            error_mapper=nfl_v3_scores_player_details_by_rookie_draft_year_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_details_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerDetail], NflV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available NFL players by team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerDetail]],
            error_mapper=nfl_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_game_logs_by_season(
        self,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame], NflV3ScoresPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

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
                "/v3/nfl/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame]],
            error_mapper=nfl_v3_scores_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesAllErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) This returns all players.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/PlayersByAvailable"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic]],
            error_mapper=nfl_v3_scores_player_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_profiles_by_free_agent(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByFreeAgentErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/PlayersByFreeAgents"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic]],
            error_mapper=nfl_v3_scores_player_profiles_by_free_agent_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_profiles_by_rookie_draft_year(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody]:
        """Player profiles include basic biographical information, position, college, and current team (if attached to a
        team.) Specify a year parameter to receive all player profiles from that rookie draft year.

        Args:
            season: Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/PlayersByRookieDraftYear/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic]],
            error_mapper=nfl_v3_scores_player_profiles_by_rookie_draft_year_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_player_profiles_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic]],
            error_mapper=nfl_v3_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_referees(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Referee], NflV3ScoresRefereesErrorBody]:
        """Returns referees with name, numbers, position (e.g. FJ for Field Judge), college, and years of experience.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Referees"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Referee]],
            error_mapper=nfl_v3_scores_referees_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Schedule], NflV3ScoresSchedulesErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/Schedules/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Schedule]],
            error_mapper=nfl_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic], NflV3ScoresSchedulesBasicErrorBody]:
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
            url_template=self._server.default("/v3/nfl/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScheduleBasic]],
            error_mapper=nfl_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_scores_by_week_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Score], NflV3ScoresScoresByWeekSimulationErrorBody]:
        """Gets simulated live scores of NFL games, covering the Conference Championship games on January 21, 2018.

        Args:
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/SimulatedScores/{numberofplays}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("numberofplays", numberofplays)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Score]],
            error_mapper=nfl_v3_scores_scores_by_week_simulation_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresSeasonCurrentErrorBody]:
        """Year of the current NFL season. This value changes at the start of the new NFL league year. NFL seasons run
        across two calendar years; the league year is the one in which it starts, not ends (that is, a season starting
        in 2023 and ending in 2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[int | None],
            error_mapper=nfl_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_season_last_completed(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresSeasonLastCompletedErrorBody]:
        """Year of the most recently completed NFL season. This value changes immediately after the Super Bowl. NFL
        seasons run across two calendar years; the league year is the one in which it starts, not ends (that is, a
        season starting in 2023 and ending in 2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/LastCompletedSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[int | None],
            error_mapper=nfl_v3_scores_season_last_completed_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_season_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresSeasonUpcomingErrorBody]:
        """Year of the current NFL season, if we are in the mid-season. If we are in the off-season, then year of the
        next upcoming season. This value changes immediately after the Super Bowl. NFL seasons run across two calendar
        years; the league year is the one in which it starts, not ends (that is, a season starting in 2023 and ending in
        2024 will have the league year of 2023.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/UpcomingSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[int | None],
            error_mapper=nfl_v3_scores_season_upcoming_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_stadiums(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium], NflV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the NFL with capacity, surface, latitude/longitude, city and state (and, where
        applicable, country.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Stadium]],
            error_mapper=nfl_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_standings(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Standing], NflV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Standing]],
            error_mapper=nfl_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_team_game_stats_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame], NflV3ScoresTeamGameStatsLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week, during the game and with final stats after it ends.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/TeamGameStats/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame]],
            error_mapper=nfl_v3_scores_team_game_stats_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team], NflV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns all teams regardless
        of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/AllTeams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team]],
            error_mapper=nfl_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_team_profiles_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team], NflV3ScoresTeamProfilesByActiveErrorBody]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns the teams currently
        active in the league.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Teams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team]],
            error_mapper=nfl_v3_scores_team_profiles_by_active_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_team_profiles_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team], NflV3ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, colors, coaching and scheme info. Also
        contains basic fantasy info such as IDs as well as full stadium data. This endpoint returns the active teams for
        a given season.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/Teams/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team]],
            error_mapper=nfl_v3_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_team_profiles_basic_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamBasic], NflV3ScoresTeamProfilesBasicAllErrorBody]:
        """The most basic top-line team information, such as team name and city, conference and division, stadium ID,
        coach info, and team colors. Returns all teams regardless of current active status.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/TeamsBasic"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamBasic]],
            error_mapper=nfl_v3_scores_team_profiles_basic_all_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_team_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason], NflV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

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
            url_template=self._server.default("/v3/nfl/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamSeason]],
            error_mapper=nfl_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_timeframes(
        self,
        *,
        format_: FormatOrStr = Format.JSON,
        type_: TypeOrStr = Type.CURRENT,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Timeframe], NflV3ScoresTimeframesErrorBody]:
        """Timeframes for the NFL refer to current weeks, season status etc.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            type_: The type of timeframes to return. Valid entries are <code>current</code> or <code>upcoming</code> or
                <code>completed</code> or <code>recent</code> or <code>all</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/Timeframes/{type}"),
            path_params=[param[FormatOrStr]("format", format_), param[TypeOrStr]("type", type_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Timeframe]],
            error_mapper=nfl_v3_scores_timeframes_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_transactions_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Transaction], NflV3ScoresTransactionsByDateErrorBody]:
        """Includes a list of transactions for a given date, with type (e.g. trade, injury listing, assignment) and a
        brief note.

        Args:
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/TransactionsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Transaction]],
            error_mapper=nfl_v3_scores_transactions_by_date_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_week_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresWeekCurrentErrorBody]:
        """Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday
        mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard gameday this
        could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/CurrentWeek"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[int | None],
            error_mapper=nfl_v3_scores_week_current_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_week_last_completed(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresWeekLastCompletedErrorBody]:
        """Number of the last completed week of the NFL season. This value usually changes on Tuesday nights or
        Wednesday mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard
        gameday this could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/LastCompletedWeek"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[int | None],
            error_mapper=nfl_v3_scores_week_last_completed_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_scores_week_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, NflV3ScoresWeekUpcomingErrorBody]:
        """Number of the next upcoming week of the NFL season. This value usually changes on Tuesday nights or Wednesday
        mornings at midnight ET but in the rare case of a rescheduled or overseas game with a non-standard gameday this
        could change.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/scores/{format}/UpcomingWeek"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[int | None],
            error_mapper=nfl_v3_scores_week_upcoming_error_mapper,
            request_options=request_options,
        )
