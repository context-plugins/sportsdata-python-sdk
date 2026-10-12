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
from ..errors.nba_v3_projections_dfs_slates_by_date_error import (
    NbaV3ProjectionsDfsSlatesByDateErrorBody,
    nba_v3_projections_dfs_slates_by_date_error_mapper,
)
from ..errors.nba_v3_projections_player_details_by_injured_error import (
    NbaV3ProjectionsPlayerDetailsByInjuredErrorBody,
    nba_v3_projections_player_details_by_injured_error_mapper,
)
from ..errors.nba_v3_projections_projected_player_game_stats_by_date_error import (
    NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody,
    nba_v3_projections_projected_player_game_stats_by_date_error_mapper,
)
from ..errors.nba_v3_projections_projected_player_season_stats_by_team_error import (
    NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody,
    nba_v3_projections_projected_player_season_stats_by_team_error_mapper,
)
from ..errors.nba_v3_projections_projected_player_season_stats_error import (
    NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody,
    nba_v3_projections_projected_player_season_stats_error_mapper,
)
from ..errors.nba_v3_projections_starting_lineups_by_date_error import (
    NbaV3ProjectionsStartingLineupsByDateErrorBody,
    nba_v3_projections_starting_lineups_by_date_error_mapper,
)
from ..models.dfs_slate import DfsSlate
from ..models.enums.format import Format, FormatOrStr
from ..models.player1 import Player1
from ..models.player_game_projection1 import PlayerGameProjection1
from ..models.player_season_projection1 import PlayerSeasonProjection1
from ..models.starting_lineups import StartingLineups
from ..server.server import Server


class NbaV3Projections:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NbaV3ProjectionsWithRawResponse(client, server, auth)

    def nba_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_projections_dfs_slates_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """This endpoint provides all currently injured NBA players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_projections_player_details_by_injured(
                format_=format_, request_options=request_options
            ),
        )

    def nba_v3_projections_projected_player_game_stats_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGameProjection1]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

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
            self._with_raw_response.nba_v3_projections_projected_player_game_stats_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_projections_projected_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonProjection1]:
        """SportsDataIO's proprietary projections for all active players for the season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>,
                etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_projections_projected_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_projections_projected_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeasonProjection1]:
        """SportsDataIO's proprietary projections for all active players for the season, called by team

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>,
                etc.
            team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_projections_projected_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_projections_starting_lineups_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[StartingLineups]:
        """This endpoint provides the projected & confirmed starting lineups for NBA games on a given date.

        Args:
            date: The date of the game(s). <br> Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_projections_starting_lineups_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NbaV3ProjectionsWithRawResponse:
        return self._with_raw_response


class AsyncNbaV3Projections:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNbaV3ProjectionsWithRawResponse(client, server, auth)

    async def nba_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_projections_dfs_slates_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """This endpoint provides all currently injured NBA players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_projections_player_details_by_injured(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_projections_projected_player_game_stats_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGameProjection1]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

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
            await self._with_raw_response.nba_v3_projections_projected_player_game_stats_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_projections_projected_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonProjection1]:
        """SportsDataIO's proprietary projections for all active players for the season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>,
                etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_projections_projected_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_projections_projected_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeasonProjection1]:
        """SportsDataIO's proprietary projections for all active players for the season, called by team

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>,
                etc.
            team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_projections_projected_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_projections_starting_lineups_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[StartingLineups]:
        """This endpoint provides the projected & confirmed starting lineups for NBA games on a given date.

        Args:
            date: The date of the game(s). <br> Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_projections_starting_lineups_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNbaV3ProjectionsWithRawResponse:
        return self._with_raw_response


class NbaV3ProjectionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nba_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate], NbaV3ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/DfsSlatesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate]],
            error_mapper=nba_v3_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    def nba_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], NbaV3ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured NBA players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=nba_v3_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    def nba_v3_projections_projected_player_game_stats_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGameProjection1], NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/PlayerGameProjectionStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection1]],
            error_mapper=nba_v3_projections_projected_player_game_stats_by_date_error_mapper,
            request_options=request_options,
        )

    def nba_v3_projections_projected_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonProjection1], NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody]:
        """SportsDataIO's proprietary projections for all active players for the season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>,
                etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/PlayerSeasonProjectionStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonProjection1]],
            error_mapper=nba_v3_projections_projected_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def nba_v3_projections_projected_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeasonProjection1], NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody]:
        """SportsDataIO's proprietary projections for all active players for the season, called by team

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>,
                etc.
            team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nba/projections/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonProjection1]],
            error_mapper=nba_v3_projections_projected_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def nba_v3_projections_starting_lineups_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[StartingLineups], NbaV3ProjectionsStartingLineupsByDateErrorBody]:
        """This endpoint provides the projected & confirmed starting lineups for NBA games on a given date.

        Args:
            date: The date of the game(s). <br> Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/StartingLineupsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[StartingLineups]],
            error_mapper=nba_v3_projections_starting_lineups_by_date_error_mapper,
            request_options=request_options,
        )


class AsyncNbaV3ProjectionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nba_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate], NbaV3ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/DfsSlatesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DfsSlate]],
            error_mapper=nba_v3_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], NbaV3ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured NBA players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player1]],
            error_mapper=nba_v3_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_projections_projected_player_game_stats_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGameProjection1], NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/PlayerGameProjectionStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameProjection1]],
            error_mapper=nba_v3_projections_projected_player_game_stats_by_date_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_projections_projected_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonProjection1], NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody]:
        """SportsDataIO's proprietary projections for all active players for the season.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>,
                etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/PlayerSeasonProjectionStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonProjection1]],
            error_mapper=nba_v3_projections_projected_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_projections_projected_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeasonProjection1], NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody]:
        """SportsDataIO's proprietary projections for all active players for the season, called by team

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2019</code>,
                etc.
            team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nba/projections/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonProjection1]],
            error_mapper=nba_v3_projections_projected_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_projections_starting_lineups_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[StartingLineups], NbaV3ProjectionsStartingLineupsByDateErrorBody]:
        """This endpoint provides the projected & confirmed starting lineups for NBA games on a given date.

        Args:
            date: The date of the game(s). <br> Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/projections/{format}/StartingLineupsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[StartingLineups]],
            error_mapper=nba_v3_projections_starting_lineups_by_date_error_mapper,
            request_options=request_options,
        )
