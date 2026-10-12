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
from ..errors.nba_v3_news_rotoballer_premium_news_by_date_error import (
    NbaV3NewsRotoballerPremiumNewsByDateErrorBody,
    nba_v3_news_rotoballer_premium_news_by_date_error_mapper,
)
from ..errors.nba_v3_news_rotoballer_premium_news_error import (
    NbaV3NewsRotoballerPremiumNewsErrorBody,
    nba_v3_news_rotoballer_premium_news_error_mapper,
)
from ..models.enums.format import Format, FormatOrStr
from ..models.news import News
from ..server.server import Server


class NbaV3RotoBallerPremiumNews:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NbaV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    def nba_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
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
            self._with_raw_response.nba_v3_news_rotoballer_premium_news(
                format_=format_, request_options=request_options
            ),
        )

    def nba_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

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
            self._with_raw_response.nba_v3_news_rotoballer_premium_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NbaV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class AsyncNbaV3RotoBallerPremiumNews:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNbaV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    async def nba_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
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
            await self._with_raw_response.nba_v3_news_rotoballer_premium_news(
                format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

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
            await self._with_raw_response.nba_v3_news_rotoballer_premium_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNbaV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class NbaV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nba_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NbaV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nba_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    def nba_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NbaV3NewsRotoballerPremiumNewsByDateErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nba_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )


class AsyncNbaV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nba_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NbaV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nba_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NbaV3NewsRotoballerPremiumNewsByDateErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nba_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )
