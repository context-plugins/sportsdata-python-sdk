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
from ..errors.cfb_v3_stats_box_score_final_error import (
    CfbV3StatsBoxScoreFinalErrorBody,
    cfb_v3_stats_box_score_final_error_mapper,
)
from ..errors.cfb_v3_stats_box_score_live_final_error import (
    CfbV3StatsBoxScoreLiveFinalErrorBody,
    cfb_v3_stats_box_score_live_final_error_mapper,
)
from ..errors.cfb_v3_stats_box_scores_by_date_final_error import (
    CfbV3StatsBoxScoresByDateFinalErrorBody,
    cfb_v3_stats_box_scores_by_date_final_error_mapper,
)
from ..errors.cfb_v3_stats_box_scores_by_date_live_final_error import (
    CfbV3StatsBoxScoresByDateLiveFinalErrorBody,
    cfb_v3_stats_box_scores_by_date_live_final_error_mapper,
)
from ..errors.cfb_v3_stats_box_scores_by_week_final_error import (
    CfbV3StatsBoxScoresByWeekFinalErrorBody,
    cfb_v3_stats_box_scores_by_week_final_error_mapper,
)
from ..errors.cfb_v3_stats_box_scores_by_week_live_final_error import (
    CfbV3StatsBoxScoresByWeekLiveFinalErrorBody,
    cfb_v3_stats_box_scores_by_week_live_final_error_mapper,
)
from ..errors.cfb_v3_stats_box_scores_delta_by_week_error import (
    CfbV3StatsBoxScoresDeltaByWeekErrorBody,
    cfb_v3_stats_box_scores_delta_by_week_error_mapper,
)
from ..errors.cfb_v3_stats_player_game_logs_by_season_error import (
    CfbV3StatsPlayerGameLogsBySeasonErrorBody,
    cfb_v3_stats_player_game_logs_by_season_error_mapper,
)
from ..errors.cfb_v3_stats_player_game_stats_by_week_final_error import (
    CfbV3StatsPlayerGameStatsByWeekFinalErrorBody,
    cfb_v3_stats_player_game_stats_by_week_final_error_mapper,
)
from ..errors.cfb_v3_stats_player_game_stats_by_week_live_final_error import (
    CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody,
    cfb_v3_stats_player_game_stats_by_week_live_final_error_mapper,
)
from ..errors.cfb_v3_stats_player_season_stats_by_team_error import (
    CfbV3StatsPlayerSeasonStatsByTeamErrorBody,
    cfb_v3_stats_player_season_stats_by_team_error_mapper,
)
from ..errors.cfb_v3_stats_player_season_stats_error import (
    CfbV3StatsPlayerSeasonStatsErrorBody,
    cfb_v3_stats_player_season_stats_error_mapper,
)
from ..errors.cfb_v3_stats_team_game_stats_by_week_final_error import (
    CfbV3StatsTeamGameStatsByWeekFinalErrorBody,
    cfb_v3_stats_team_game_stats_by_week_final_error_mapper,
)
from ..models.box_score1 import BoxScore1
from ..models.enums.format import FormatOrStr
from ..models.player_game1 import PlayerGame1
from ..models.player_season1 import PlayerSeason1
from ..models.team_game1 import TeamGame1
from ..server.server import Server


class CfbV3Stats:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CfbV3StatsWithRawResponse(client, server, auth)

    def cfb_v3_stats_box_score_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>1148</code> or <code>1149</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_box_score_final(
            format, gameid, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_box_score_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game. Note that defensive player stats update 1-2 hours after the game
        has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>1148</code> or <code>1149</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_box_score_live_final(
            format, gameid, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_box_scores_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified date, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-JAN-01</code>, <code>2017-JAN-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_box_scores_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_box_scores_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date. Note that defensive player stats update 1-2 hours after
        the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-JAN-01</code>, <code>2017-JAN-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_box_scores_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_box_scores_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game week for each game that took place, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season.<br> Examples: <code>2017</code>, <code>2018</code>, etc.
            week: The week of the game(s).<br> Examples: <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_box_scores_by_week_final(
            format, season, week, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_box_scores_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information, down to the team and player stat level, delivered live during the games, called
        for all games on a given week of a given season. Note that defensive player stats update 1-2 hours after the
        game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season.<br> Examples: <code>2017</code>, <code>2018</code>, etc.
            week: The week of the game(s).<br> Examples: <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_box_scores_by_week_live_final(
            format, season, week, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_box_scores_delta_by_week(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore1]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.
        Note that defensive player stats update 1-2 hours after the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_box_scores_delta_by_week(
            format, season, week, minutes, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_player_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame1]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>50036283</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_player_game_logs_by_season(
            format, season, playerid, numberofgames, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_player_game_stats_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame1]:
        """Returns the box score statistical record for all involved players across all teams' games on a given week
        after each game has concluded.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_player_game_stats_by_week_final(
            format, season, week, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_player_game_stats_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame1]:
        """Returns the box score statistical record for all involved players across a given week, updated live as the
        games take place. Note that defensive player stats update 1-2 hours after the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_player_game_stats_by_week_live_final(
            format, season, week, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_player_season_stats(
            format, season, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_player_season_stats_by_team(
        self, format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_player_season_stats_by_team(
            format, season, team, request_options=request_options
        ).unwrap()

    def cfb_v3_stats_team_game_stats_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame1]:
        """Returns the box score statistical record team-wide (aggregated from all players) for games in a given week
        after the game has concluded.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_stats_team_game_stats_by_week_final(
            format, season, week, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CfbV3StatsWithRawResponse:
        return self._with_raw_response


class AsyncCfbV3Stats:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCfbV3StatsWithRawResponse(client, server, auth)

    async def cfb_v3_stats_box_score_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>1148</code> or <code>1149</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_box_score_final(format, gameid, request_options=request_options)
        ).unwrap()

    async def cfb_v3_stats_box_score_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game. Note that defensive player stats update 1-2 hours after the game
        has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>1148</code> or <code>1149</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_box_score_live_final(
                format, gameid, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_box_scores_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified date, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-JAN-01</code>, <code>2017-JAN-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_box_scores_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_box_scores_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date. Note that defensive player stats update 1-2 hours after
        the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-JAN-01</code>, <code>2017-JAN-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_box_scores_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_box_scores_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game week for each game that took place, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season.<br> Examples: <code>2017</code>, <code>2018</code>, etc.
            week: The week of the game(s).<br> Examples: <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_box_scores_by_week_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_box_scores_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information, down to the team and player stat level, delivered live during the games, called
        for all games on a given week of a given season. Note that defensive player stats update 1-2 hours after the
        game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season.<br> Examples: <code>2017</code>, <code>2018</code>, etc.
            week: The week of the game(s).<br> Examples: <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_box_scores_by_week_live_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_box_scores_delta_by_week(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore1]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.
        Note that defensive player stats update 1-2 hours after the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_box_scores_delta_by_week(
                format, season, week, minutes, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_player_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame1]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>50036283</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_player_game_logs_by_season(
                format, season, playerid, numberofgames, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_player_game_stats_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame1]:
        """Returns the box score statistical record for all involved players across all teams' games on a given week
        after each game has concluded.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_player_game_stats_by_week_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_player_game_stats_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame1]:
        """Returns the box score statistical record for all involved players across a given week, updated live as the
        games take place. Note that defensive player stats update 1-2 hours after the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_player_game_stats_by_week_live_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_player_season_stats(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_player_season_stats_by_team(
        self, format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_player_season_stats_by_team(
                format, season, team, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_stats_team_game_stats_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame1]:
        """Returns the box score statistical record team-wide (aggregated from all players) for games in a given week
        after the game has concluded.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_stats_team_game_stats_by_week_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCfbV3StatsWithRawResponse:
        return self._with_raw_response


class CfbV3StatsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cfb_v3_stats_box_score_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>1148</code> or <code>1149</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_box_score_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game. Note that defensive player stats update 1-2 hours after the game
        has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>1148</code> or <code>1149</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_box_scores_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-JAN-01</code>, <code>2017-JAN-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_box_scores_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date. Note that defensive player stats update 1-2 hours after
        the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-JAN-01</code>, <code>2017-JAN-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_box_scores_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByWeekFinalErrorBody]:
        """Full statistical information for a specified game week for each game that took place, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season.<br> Examples: <code>2017</code>, <code>2018</code>, etc.
            week: The week of the game(s).<br> Examples: <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_by_week_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_box_scores_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByWeekLiveFinalErrorBody]:
        """Full statistical information, down to the team and player stat level, delivered live during the games, called
        for all games on a given week of a given season. Note that defensive player stats update 1-2 hours after the
        game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season.<br> Examples: <code>2017</code>, <code>2018</code>, etc.
            week: The week of the game(s).<br> Examples: <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_box_scores_delta_by_week(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresDeltaByWeekErrorBody]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.
        Note that defensive player stats update 1-2 hours after the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresByWeekDelta/{season}/{week}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_delta_by_week_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_player_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>50036283</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=cfb_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_player_game_stats_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameStatsByWeekFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given week
        after each game has concluded.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/PlayerGameStatsByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=cfb_v3_stats_player_game_stats_by_week_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_player_game_stats_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given week, updated live as the
        games take place. Note that defensive player stats update 1-2 hours after the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/PlayerGameStatsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=cfb_v3_stats_player_game_stats_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason1], CfbV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason1]],
            error_mapper=cfb_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_player_season_stats_by_team(
        self, format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason1], CfbV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason1]],
            error_mapper=cfb_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_stats_team_game_stats_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame1], CfbV3StatsTeamGameStatsByWeekFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for games in a given week
        after the game has concluded.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/TeamGameStatsByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=cfb_v3_stats_team_game_stats_by_week_final_error_mapper,
            request_options=request_options,
        )


class AsyncCfbV3StatsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cfb_v3_stats_box_score_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>1148</code> or <code>1149</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_box_score_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game. Note that defensive player stats update 1-2 hours after the game
        has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>1148</code> or <code>1149</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_box_scores_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-JAN-01</code>, <code>2017-JAN-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_box_scores_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date. Note that defensive player stats update 1-2 hours after
        the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-JAN-01</code>, <code>2017-JAN-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_box_scores_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByWeekFinalErrorBody]:
        """Full statistical information for a specified game week for each game that took place, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season.<br> Examples: <code>2017</code>, <code>2018</code>, etc.
            week: The week of the game(s).<br> Examples: <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_by_week_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_box_scores_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByWeekLiveFinalErrorBody]:
        """Full statistical information, down to the team and player stat level, delivered live during the games, called
        for all games on a given week of a given season. Note that defensive player stats update 1-2 hours after the
        game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season.<br> Examples: <code>2017</code>, <code>2018</code>, etc.
            week: The week of the game(s).<br> Examples: <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_box_scores_delta_by_week(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore1], CfbV3StatsBoxScoresDeltaByWeekErrorBody]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.
        Note that defensive player stats update 1-2 hours after the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/BoxScoresByWeekDelta/{season}/{week}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=cfb_v3_stats_box_scores_delta_by_week_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_player_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>50036283</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=cfb_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_player_game_stats_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameStatsByWeekFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given week
        after each game has concluded.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/PlayerGameStatsByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=cfb_v3_stats_player_game_stats_by_week_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_player_game_stats_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given week, updated live as the
        games take place. Note that defensive player stats update 1-2 hours after the game has ended.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/PlayerGameStatsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=cfb_v3_stats_player_game_stats_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason1], CfbV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason1]],
            error_mapper=cfb_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_player_season_stats_by_team(
        self, format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason1], CfbV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason1]],
            error_mapper=cfb_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_stats_team_game_stats_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame1], CfbV3StatsTeamGameStatsByWeekFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for games in a given week
        after the game has concluded.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/stats/{format}/TeamGameStatsByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=cfb_v3_stats_team_game_stats_by_week_final_error_mapper,
            request_options=request_options,
        )
