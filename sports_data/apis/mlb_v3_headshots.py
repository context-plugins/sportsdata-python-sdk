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
from ..errors.mlb_v3_headshots_headshots_error import (
    MlbV3HeadshotsHeadshotsErrorBody,
    mlb_v3_headshots_headshots_error_mapper,
)
from ..models.enums.format import FormatOrStr
from ..models.headshot1 import Headshot1
from ..server.server import Server


class MlbV3Headshots:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MlbV3HeadshotsWithRawResponse(client, server, auth)

    def mlb_v3_headshots_headshots(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Headshot1]:
        """USA Today/IMAGN cropped action headshots for all active NFL players, delivered shortly after the season
        starts.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mlb_v3_headshots_headshots(format, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MlbV3HeadshotsWithRawResponse:
        return self._with_raw_response


class AsyncMlbV3Headshots:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMlbV3HeadshotsWithRawResponse(client, server, auth)

    async def mlb_v3_headshots_headshots(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Headshot1]:
        """USA Today/IMAGN cropped action headshots for all active NFL players, delivered shortly after the season
        starts.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mlb_v3_headshots_headshots(format, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMlbV3HeadshotsWithRawResponse:
        return self._with_raw_response


class MlbV3HeadshotsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mlb_v3_headshots_headshots(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Headshot1], MlbV3HeadshotsHeadshotsErrorBody]:
        """USA Today/IMAGN cropped action headshots for all active NFL players, delivered shortly after the season
        starts.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/headshots/{format}/Headshots"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Headshot1]],
            error_mapper=mlb_v3_headshots_headshots_error_mapper,
            request_options=request_options,
        )


class AsyncMlbV3HeadshotsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mlb_v3_headshots_headshots(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Headshot1], MlbV3HeadshotsHeadshotsErrorBody]:
        """USA Today/IMAGN cropped action headshots for all active NFL players, delivered shortly after the season
        starts.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/headshots/{format}/Headshots"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Headshot1]],
            error_mapper=mlb_v3_headshots_headshots_error_mapper,
            request_options=request_options,
        )
