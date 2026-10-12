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
from ..errors.golf_v3_news_rotoballer_premium_news_by_date_error import (
    GolfV3NewsRotoballerPremiumNewsByDateErrorBody,
    golf_v3_news_rotoballer_premium_news_by_date_error_mapper,
)
from ..errors.golf_v3_news_rotoballer_premium_news_error import (
    GolfV3NewsRotoballerPremiumNewsErrorBody,
    golf_v3_news_rotoballer_premium_news_error_mapper,
)
from ..models.enums.format import Format, FormatOrStr
from ..models.news2 import News2
from ..server.server import Server


class GolfV3RotoBallerPremiumNews:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GolfV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    def golf_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
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
            self._with_raw_response.golf_v3_news_rotoballer_premium_news(
                format_=format_, request_options=request_options
            ),
        )

    def golf_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
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
            self._with_raw_response.golf_v3_news_rotoballer_premium_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> GolfV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class AsyncGolfV3RotoBallerPremiumNews:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGolfV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    async def golf_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
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
            await self._with_raw_response.golf_v3_news_rotoballer_premium_news(
                format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
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
            await self._with_raw_response.golf_v3_news_rotoballer_premium_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncGolfV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class GolfV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def golf_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], GolfV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=golf_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    def golf_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], GolfV3NewsRotoballerPremiumNewsByDateErrorBody]:
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
            url_template=self._server.default("/v3/golf/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=golf_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )


class AsyncGolfV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def golf_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], GolfV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News2]],
            error_mapper=golf_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], GolfV3NewsRotoballerPremiumNewsByDateErrorBody]:
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
            url_template=self._server.default("/v3/golf/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News2]],
            error_mapper=golf_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )
