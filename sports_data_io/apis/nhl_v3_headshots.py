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
from ..errors.nhl_v3_headshots_headshots_error import (
    NhlV3HeadshotsHeadshotsErrorBody,
    nhl_v3_headshots_headshots_error_mapper,
)
from ..models.enums.format import Format, FormatOrStr
from ..models.headshot import Headshot
from ..server.server import Server


class NhlV3Headshots:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NhlV3HeadshotsWithRawResponse(client, server, auth)

    def nhl_v3_headshots_headshots(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Headshot]:
        """Headshots

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_headshots_headshots(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> NhlV3HeadshotsWithRawResponse:
        return self._with_raw_response


class AsyncNhlV3Headshots:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNhlV3HeadshotsWithRawResponse(client, server, auth)

    async def nhl_v3_headshots_headshots(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Headshot]:
        """Headshots

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_headshots_headshots(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncNhlV3HeadshotsWithRawResponse:
        return self._with_raw_response


class NhlV3HeadshotsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nhl_v3_headshots_headshots(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Headshot], NhlV3HeadshotsHeadshotsErrorBody]:
        """Headshots

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/headshots/{format}/Headshots"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Headshot]],
            error_mapper=nhl_v3_headshots_headshots_error_mapper,
            request_options=request_options,
        )


class AsyncNhlV3HeadshotsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nhl_v3_headshots_headshots(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Headshot], NhlV3HeadshotsHeadshotsErrorBody]:
        """Headshots

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/headshots/{format}/Headshots"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Headshot]],
            error_mapper=nhl_v3_headshots_headshots_error_mapper,
            request_options=request_options,
        )
