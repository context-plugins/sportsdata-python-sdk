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
from ..errors.nhl_v3_projections_dfs_slates_by_date_error import (
    NhlV3ProjectionsDfsSlatesByDateErrorBody,
    nhl_v3_projections_dfs_slates_by_date_error_mapper,
)
from ..errors.nhl_v3_projections_player_details_by_injured_error import (
    NhlV3ProjectionsPlayerDetailsByInjuredErrorBody,
    nhl_v3_projections_player_details_by_injured_error_mapper,
)
from ..errors.nhl_v3_projections_projected_player_game_stats_by_date_error import (
    NhlV3ProjectionsProjectedPlayerGameStatsByDateErrorBody,
    nhl_v3_projections_projected_player_game_stats_by_date_error_mapper,
)
from ..errors.nhl_v3_projections_starting_goaltenders_by_date_error import (
    NhlV3ProjectionsStartingGoaltendersByDateErrorBody,
    nhl_v3_projections_starting_goaltenders_by_date_error_mapper,
)
from ..models.dfs_slate import DfsSlate
from ..models.enums.format import FormatOrStr
from ..models.player3 import Player3
from ..models.player_game_projection3 import PlayerGameProjection3
from ..models.starting_goaltenders import StartingGoaltenders
from ..server.server import Server


class NhlV3Projections:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NhlV3ProjectionsWithRawResponse(client, server, auth)

    def nhl_v3_projections_dfs_slates_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_projections_dfs_slates_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def nhl_v3_projections_player_details_by_injured(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player3]:
        """This endpoint provides all currently injured NHL players, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_projections_player_details_by_injured(
            format, request_options=request_options
        ).unwrap()

    def nhl_v3_projections_projected_player_game_stats_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGameProjection3]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_projections_projected_player_game_stats_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def nhl_v3_projections_starting_goaltenders_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[StartingGoaltenders]:
        """This endpoint provides the projected and confirmed starting goaltenders for NHL games on a given date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nhl_v3_projections_starting_goaltenders_by_date(
            format, date, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NhlV3ProjectionsWithRawResponse:
        return self._with_raw_response


class AsyncNhlV3Projections:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNhlV3ProjectionsWithRawResponse(client, server, auth)

    async def nhl_v3_projections_dfs_slates_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_projections_dfs_slates_by_date(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_projections_player_details_by_injured(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player3]:
        """This endpoint provides all currently injured NHL players, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_projections_player_details_by_injured(
                format, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_projections_projected_player_game_stats_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGameProjection3]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_projections_projected_player_game_stats_by_date(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nhl_v3_projections_starting_goaltenders_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[StartingGoaltenders]:
        """This endpoint provides the projected and confirmed starting goaltenders for NHL games on a given date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nhl_v3_projections_starting_goaltenders_by_date(
                format, date, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNhlV3ProjectionsWithRawResponse:
        return self._with_raw_response


class NhlV3ProjectionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nhl_v3_projections_dfs_slates_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate], NhlV3ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/projections/{format}/DfsSlatesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate]],
            error_mapper=nhl_v3_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_projections_player_details_by_injured(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player3], NhlV3ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured NHL players, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/projections/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player3]],
            error_mapper=nhl_v3_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_projections_projected_player_game_stats_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGameProjection3], NhlV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/projections/{format}/PlayerGameProjectionStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection3]],
            error_mapper=nhl_v3_projections_projected_player_game_stats_by_date_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_projections_starting_goaltenders_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[StartingGoaltenders], NhlV3ProjectionsStartingGoaltendersByDateErrorBody]:
        """This endpoint provides the projected and confirmed starting goaltenders for NHL games on a given date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/projections/{format}/StartingGoaltendersByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[StartingGoaltenders]],
            error_mapper=nhl_v3_projections_starting_goaltenders_by_date_error_mapper,
            request_options=request_options,
        )


class AsyncNhlV3ProjectionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nhl_v3_projections_dfs_slates_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate], NhlV3ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2017-DEC-01</code>, <code>2018-FEB-15</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/projections/{format}/DfsSlatesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate]],
            error_mapper=nhl_v3_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_projections_player_details_by_injured(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player3], NhlV3ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured NHL players, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/projections/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player3]],
            error_mapper=nhl_v3_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_projections_projected_player_game_stats_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGameProjection3], NhlV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/projections/{format}/PlayerGameProjectionStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection3]],
            error_mapper=nhl_v3_projections_projected_player_game_stats_by_date_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_projections_starting_goaltenders_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[StartingGoaltenders], NhlV3ProjectionsStartingGoaltendersByDateErrorBody]:
        """This endpoint provides the projected and confirmed starting goaltenders for NHL games on a given date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2021-OCT-12</code>, <code>2021-DEC-09</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/projections/{format}/StartingGoaltendersByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[StartingGoaltenders]],
            error_mapper=nhl_v3_projections_starting_goaltenders_by_date_error_mapper,
            request_options=request_options,
        )
