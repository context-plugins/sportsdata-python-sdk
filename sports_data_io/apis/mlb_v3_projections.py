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
from ..errors.mlb_v3_projections_depth_charts_error import (
    MlbV3ProjectionsDepthChartsErrorBody,
    mlb_v3_projections_depth_charts_error_mapper,
)
from ..errors.mlb_v3_projections_dfs_slate_ownership_projections_by_slate_error import (
    MlbV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody,
    mlb_v3_projections_dfs_slate_ownership_projections_by_slate_error_mapper,
)
from ..errors.mlb_v3_projections_dfs_slate_ownership_projections_upcoming_error import (
    MlbV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody,
    mlb_v3_projections_dfs_slate_ownership_projections_upcoming_error_mapper,
)
from ..errors.mlb_v3_projections_dfs_slates_by_date_error import (
    MlbV3ProjectionsDfsSlatesByDateErrorBody,
    mlb_v3_projections_dfs_slates_by_date_error_mapper,
)
from ..errors.mlb_v3_projections_player_details_by_injured_error import (
    MlbV3ProjectionsPlayerDetailsByInjuredErrorBody,
    mlb_v3_projections_player_details_by_injured_error_mapper,
)
from ..errors.mlb_v3_projections_projected_player_game_stats_by_date_error import (
    MlbV3ProjectionsProjectedPlayerGameStatsByDateErrorBody,
    mlb_v3_projections_projected_player_game_stats_by_date_error_mapper,
)
from ..errors.mlb_v3_projections_projected_player_season_stats_with_adp_error import (
    MlbV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody,
    mlb_v3_projections_projected_player_season_stats_with_adp_error_mapper,
)
from ..errors.mlb_v3_projections_starting_lineups_by_date_error import (
    MlbV3ProjectionsStartingLineupsByDateErrorBody,
    mlb_v3_projections_starting_lineups_by_date_error_mapper,
)
from ..models.dfs_slate import DfsSlate
from ..models.dfs_slate_with_ownership_projection import DfsSlateWithOwnershipProjection
from ..models.enums.format import Format, FormatOrStr
from ..models.player2 import Player2
from ..models.player_game_projection2 import PlayerGameProjection2
from ..models.player_season_projection2 import PlayerSeasonProjection2
from ..models.starting_lineups1 import StartingLineups1
from ..models.team_depth_chart1 import TeamDepthChart1
from ..server.server import Server


class MlbV3Projections:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MlbV3ProjectionsWithRawResponse(client, server, auth)

    def mlb_v3_projections_depth_charts(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart1]:
        """Returns Depth Charts for all active MLB teams.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_projections_depth_charts(format_=format_, request_options=request_options)
        )

    def mlb_v3_projections_dfs_slate_ownership_projections_by_slate(
        self, slate_id: int, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> DfsSlateWithOwnershipProjection:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_projections_dfs_slate_ownership_projections_by_slate(
                slate_id, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_projections_dfs_slate_ownership_projections_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlateWithOwnershipProjection]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_projections_dfs_slate_ownership_projections_upcoming(
                format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate]:
        """Returns DFS Slates which have not yet started for which we have DFS projections.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_projections_dfs_slates_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player2]:
        """This endpoint provides all currently injured MLB players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_projections_player_details_by_injured(
                format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_projections_projected_player_game_stats_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGameProjection2]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

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
            self._with_raw_response.mlb_v3_projections_projected_player_game_stats_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_projections_projected_player_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonProjection2]:
        """SportsDataIO's proprietary projections, including average draft position, for all active players for the
        season.

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
            self._with_raw_response.mlb_v3_projections_projected_player_season_stats_with_adp(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_projections_starting_lineups_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[StartingLineups1]:
        """Returns both projected and confirmed starting lineups for all games on a given date.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_projections_starting_lineups_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> MlbV3ProjectionsWithRawResponse:
        return self._with_raw_response


class AsyncMlbV3Projections:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMlbV3ProjectionsWithRawResponse(client, server, auth)

    async def mlb_v3_projections_depth_charts(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamDepthChart1]:
        """Returns Depth Charts for all active MLB teams.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_projections_depth_charts(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_projections_dfs_slate_ownership_projections_by_slate(
        self, slate_id: int, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> DfsSlateWithOwnershipProjection:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_projections_dfs_slate_ownership_projections_by_slate(
                slate_id, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_projections_dfs_slate_ownership_projections_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlateWithOwnershipProjection]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_projections_dfs_slate_ownership_projections_upcoming(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate]:
        """Returns DFS Slates which have not yet started for which we have DFS projections.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_projections_dfs_slates_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player2]:
        """This endpoint provides all currently injured MLB players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_projections_player_details_by_injured(
                format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_projections_projected_player_game_stats_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGameProjection2]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

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
            await self._with_raw_response.mlb_v3_projections_projected_player_game_stats_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_projections_projected_player_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonProjection2]:
        """SportsDataIO's proprietary projections, including average draft position, for all active players for the
        season.

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
            await self._with_raw_response.mlb_v3_projections_projected_player_season_stats_with_adp(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_projections_starting_lineups_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[StartingLineups1]:
        """Returns both projected and confirmed starting lineups for all games on a given date.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_projections_starting_lineups_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncMlbV3ProjectionsWithRawResponse:
        return self._with_raw_response


class MlbV3ProjectionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mlb_v3_projections_depth_charts(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart1], MlbV3ProjectionsDepthChartsErrorBody]:
        """Returns Depth Charts for all active MLB teams.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/DepthCharts"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamDepthChart1]],
            error_mapper=mlb_v3_projections_depth_charts_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_projections_dfs_slate_ownership_projections_by_slate(
        self, slate_id: int, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DfsSlateWithOwnershipProjection, MlbV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody]:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/projections/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[int]("slateId", slate_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[DfsSlateWithOwnershipProjection],
            error_mapper=mlb_v3_projections_dfs_slate_ownership_projections_by_slate_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_projections_dfs_slate_ownership_projections_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[DfsSlateWithOwnershipProjection], MlbV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody
    ]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/UpcomingDfsSlateOwnershipProjections"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlateWithOwnershipProjection]],
            error_mapper=mlb_v3_projections_dfs_slate_ownership_projections_upcoming_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate], MlbV3ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS Slates which have not yet started for which we have DFS projections.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/DfsSlatesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate]],
            error_mapper=mlb_v3_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player2], MlbV3ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured MLB players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player2]],
            error_mapper=mlb_v3_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_projections_projected_player_game_stats_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGameProjection2], MlbV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/PlayerGameProjectionStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection2]],
            error_mapper=mlb_v3_projections_projected_player_game_stats_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_projections_projected_player_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonProjection2], MlbV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody]:
        """SportsDataIO's proprietary projections, including average draft position, for all active players for the
        season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/PlayerSeasonProjectionStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonProjection2]],
            error_mapper=mlb_v3_projections_projected_player_season_stats_with_adp_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_projections_starting_lineups_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[StartingLineups1], MlbV3ProjectionsStartingLineupsByDateErrorBody]:
        """Returns both projected and confirmed starting lineups for all games on a given date.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/StartingLineupsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[StartingLineups1]],
            error_mapper=mlb_v3_projections_starting_lineups_by_date_error_mapper,
            request_options=request_options,
        )


class AsyncMlbV3ProjectionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mlb_v3_projections_depth_charts(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamDepthChart1], MlbV3ProjectionsDepthChartsErrorBody]:
        """Returns Depth Charts for all active MLB teams.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/DepthCharts"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamDepthChart1]],
            error_mapper=mlb_v3_projections_depth_charts_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_projections_dfs_slate_ownership_projections_by_slate(
        self, slate_id: int, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DfsSlateWithOwnershipProjection, MlbV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody]:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/projections/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[int]("slateId", slate_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[DfsSlateWithOwnershipProjection],
            error_mapper=mlb_v3_projections_dfs_slate_ownership_projections_by_slate_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_projections_dfs_slate_ownership_projections_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[DfsSlateWithOwnershipProjection], MlbV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody
    ]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/UpcomingDfsSlateOwnershipProjections"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DfsSlateWithOwnershipProjection]],
            error_mapper=mlb_v3_projections_dfs_slate_ownership_projections_upcoming_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate], MlbV3ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS Slates which have not yet started for which we have DFS projections.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/DfsSlatesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DfsSlate]],
            error_mapper=mlb_v3_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player2], MlbV3ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured MLB players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player2]],
            error_mapper=mlb_v3_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_projections_projected_player_game_stats_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGameProjection2], MlbV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/PlayerGameProjectionStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameProjection2]],
            error_mapper=mlb_v3_projections_projected_player_game_stats_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_projections_projected_player_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonProjection2], MlbV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody]:
        """SportsDataIO's proprietary projections, including average draft position, for all active players for the
        season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/PlayerSeasonProjectionStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonProjection2]],
            error_mapper=mlb_v3_projections_projected_player_season_stats_with_adp_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_projections_starting_lineups_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[StartingLineups1], MlbV3ProjectionsStartingLineupsByDateErrorBody]:
        """Returns both projected and confirmed starting lineups for all games on a given date.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/projections/{format}/StartingLineupsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[StartingLineups1]],
            error_mapper=mlb_v3_projections_starting_lineups_by_date_error_mapper,
            request_options=request_options,
        )
