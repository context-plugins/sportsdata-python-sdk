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
from ..errors.nhl_v3_news_rotoballer_premium_news_by_date_error import (
    NhlV3NewsRotoballerPremiumNewsByDateErrorBody,
    nhl_v3_news_rotoballer_premium_news_by_date_error_mapper,
)
from ..errors.nhl_v3_news_rotoballer_premium_news_error import (
    NhlV3NewsRotoballerPremiumNewsErrorBody,
    nhl_v3_news_rotoballer_premium_news_error_mapper,
)
from ..models.enums.format import Format, FormatOrStr
from ..models.news1 import News1
from ..server.server import Server


class NhlV3RotoBallerPremiumNews:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NhlV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    def nhl_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News1]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_news_rotoballer_premium_news(
                format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News1]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            date: The date of the news. <br>Examples: <code>2021-JAN-06</code>, <code>2021-JAN-31</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_news_rotoballer_premium_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NhlV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class AsyncNhlV3RotoBallerPremiumNews:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNhlV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    async def nhl_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News1]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_news_rotoballer_premium_news(
                format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News1]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            date: The date of the news. <br>Examples: <code>2021-JAN-06</code>, <code>2021-JAN-31</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_news_rotoballer_premium_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNhlV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class NhlV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nhl_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News1], NhlV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News1]],
            error_mapper=nhl_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News1], NhlV3NewsRotoballerPremiumNewsByDateErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            date: The date of the news. <br>Examples: <code>2021-JAN-06</code>, <code>2021-JAN-31</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News1]],
            error_mapper=nhl_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )


class AsyncNhlV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nhl_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News1], NhlV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News1]],
            error_mapper=nhl_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News1], NhlV3NewsRotoballerPremiumNewsByDateErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            date: The date of the news. <br>Examples: <code>2021-JAN-06</code>, <code>2021-JAN-31</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News1]],
            error_mapper=nhl_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )
