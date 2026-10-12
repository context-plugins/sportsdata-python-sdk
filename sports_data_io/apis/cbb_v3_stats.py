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
from ..errors.cbb_v3_stats_box_score_final_error import (
    CbbV3StatsBoxScoreFinalErrorBody,
    cbb_v3_stats_box_score_final_error_mapper,
)
from ..errors.cbb_v3_stats_box_score_live_final_error import (
    CbbV3StatsBoxScoreLiveFinalErrorBody,
    cbb_v3_stats_box_score_live_final_error_mapper,
)
from ..errors.cbb_v3_stats_box_scores_by_date_final_error import (
    CbbV3StatsBoxScoresByDateFinalErrorBody,
    cbb_v3_stats_box_scores_by_date_final_error_mapper,
)
from ..errors.cbb_v3_stats_box_scores_by_date_live_final_error import (
    CbbV3StatsBoxScoresByDateLiveFinalErrorBody,
    cbb_v3_stats_box_scores_by_date_live_final_error_mapper,
)
from ..errors.cbb_v3_stats_box_scores_delta_by_date_error import (
    CbbV3StatsBoxScoresDeltaByDateErrorBody,
    cbb_v3_stats_box_scores_delta_by_date_error_mapper,
)
from ..errors.cbb_v3_stats_player_game_logs_by_season_error import (
    CbbV3StatsPlayerGameLogsBySeasonErrorBody,
    cbb_v3_stats_player_game_logs_by_season_error_mapper,
)
from ..errors.cbb_v3_stats_player_game_stats_by_date_final_error import (
    CbbV3StatsPlayerGameStatsByDateFinalErrorBody,
    cbb_v3_stats_player_game_stats_by_date_final_error_mapper,
)
from ..errors.cbb_v3_stats_player_game_stats_by_date_live_final_error import (
    CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody,
    cbb_v3_stats_player_game_stats_by_date_live_final_error_mapper,
)
from ..errors.cbb_v3_stats_player_season_stats_by_team_error import (
    CbbV3StatsPlayerSeasonStatsByTeamErrorBody,
    cbb_v3_stats_player_season_stats_by_team_error_mapper,
)
from ..errors.cbb_v3_stats_player_season_stats_error import (
    CbbV3StatsPlayerSeasonStatsErrorBody,
    cbb_v3_stats_player_season_stats_error_mapper,
)
from ..errors.cbb_v3_stats_team_game_stats_by_date_final_error import (
    CbbV3StatsTeamGameStatsByDateFinalErrorBody,
    cbb_v3_stats_team_game_stats_by_date_final_error_mapper,
)
from ..models.box_score4 import BoxScore4
from ..models.enums.format import Format, FormatOrStr
from ..models.player_game5 import PlayerGame5
from ..models.player_season6 import PlayerSeason6
from ..models.team_game5 import TeamGame5
from ..server.server import Server


class CbbV3Stats:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CbbV3StatsWithRawResponse(client, server, auth)

    def cbb_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore4:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an CBB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_box_score_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore4:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an CBB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_box_score_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore4]:
        """Full statistical information for all games on a given date, down to the team and player stat level, delivered
        after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_box_scores_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore4]:
        """Full statistical information for games, down to the team and player stat level, delivered live during the
        game, called for a given date (returns all games on that date.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_box_scores_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore4]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_box_scores_delta_by_date(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame5]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID.Example:<code>60008094</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame5]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date.
        After each game has concluded its players' records are added.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_player_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame5]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_player_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason6]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018POST</code>, <code>2019</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason6]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018POST</code>, <code>2019</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    def cbb_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame5]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, updated as each game concludes.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cbb_v3_stats_team_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> CbbV3StatsWithRawResponse:
        return self._with_raw_response


class AsyncCbbV3Stats:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCbbV3StatsWithRawResponse(client, server, auth)

    async def cbb_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore4:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an CBB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_box_score_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore4:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an CBB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_box_score_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore4]:
        """Full statistical information for all games on a given date, down to the team and player stat level, delivered
        after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_box_scores_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore4]:
        """Full statistical information for games, down to the team and player stat level, delivered live during the
        game, called for a given date (returns all games on that date.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_box_scores_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore4]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_box_scores_delta_by_date(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame5]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID.Example:<code>60008094</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame5]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date.
        After each game has concluded its players' records are added.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_player_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame5]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_player_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason6]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018POST</code>, <code>2019</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason6]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018POST</code>, <code>2019</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    async def cbb_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame5]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, updated as each game concludes.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cbb_v3_stats_team_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCbbV3StatsWithRawResponse:
        return self._with_raw_response


class CbbV3StatsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cbb_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore4, CbbV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an CBB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore4],
            error_mapper=cbb_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore4, CbbV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an CBB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore4],
            error_mapper=cbb_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore4], CbbV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for all games on a given date, down to the team and player stat level, delivered
        after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore4]],
            error_mapper=cbb_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore4], CbbV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for games, down to the team and player stat level, delivered live during the
        game, called for a given date (returns all games on that date.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore4]],
            error_mapper=cbb_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore4], CbbV3StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScoresDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore4]],
            error_mapper=cbb_v3_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID.Example:<code>60008094</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cbb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame5]],
            error_mapper=cbb_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date.
        After each game has concluded its players' records are added.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/PlayerGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame5]],
            error_mapper=cbb_v3_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/PlayerGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame5]],
            error_mapper=cbb_v3_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason6], CbbV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018POST</code>, <code>2019</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason6]],
            error_mapper=cbb_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason6], CbbV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018POST</code>, <code>2019</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason6]],
            error_mapper=cbb_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def cbb_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame5], CbbV3StatsTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, updated as each game concludes.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame5]],
            error_mapper=cbb_v3_stats_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )


class AsyncCbbV3StatsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cbb_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore4, CbbV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an CBB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScore4],
            error_mapper=cbb_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore4, CbbV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an CBB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScore4],
            error_mapper=cbb_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore4], CbbV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for all games on a given date, down to the team and player stat level, delivered
        after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore4]],
            error_mapper=cbb_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore4], CbbV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for games, down to the team and player stat level, delivered live during the
        game, called for a given date (returns all games on that date.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore4]],
            error_mapper=cbb_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore4], CbbV3StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/BoxScoresDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore4]],
            error_mapper=cbb_v3_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID.Example:<code>60008094</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cbb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame5]],
            error_mapper=cbb_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date.
        After each game has concluded its players' records are added.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/PlayerGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame5]],
            error_mapper=cbb_v3_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/PlayerGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame5]],
            error_mapper=cbb_v3_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason6], CbbV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018POST</code>, <code>2019</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason6]],
            error_mapper=cbb_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason6], CbbV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018POST</code>, <code>2019</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason6]],
            error_mapper=cbb_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def cbb_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame5], CbbV3StatsTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, updated as each game concludes.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cbb/stats/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame5]],
            error_mapper=cbb_v3_stats_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )
