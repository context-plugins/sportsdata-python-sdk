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
from ..errors.nfl_v3_news_rotoballer_premium_news_by_date_error import (
    NflV3NewsRotoballerPremiumNewsByDateErrorBody,
    nfl_v3_news_rotoballer_premium_news_by_date_error_mapper,
)
from ..errors.nfl_v3_news_rotoballer_premium_news_by_team_error import (
    NflV3NewsRotoballerPremiumNewsByTeamErrorBody,
    nfl_v3_news_rotoballer_premium_news_by_team_error_mapper,
)
from ..errors.nfl_v3_news_rotoballer_premium_news_error import (
    NflV3NewsRotoballerPremiumNewsErrorBody,
    nfl_v3_news_rotoballer_premium_news_error_mapper,
)
from ..models.enums.format import Format, FormatOrStr
from ..models.news import News
from ..server.server import Server


class NflV3RotoBallerPremiumNews:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NflV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    def nfl_v3_news_rotoballer_premium_news(
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
            self._with_raw_response.nfl_v3_news_rotoballer_premium_news(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_news_rotoballer_premium_news_by_date(
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
            self._with_raw_response.nfl_v3_news_rotoballer_premium_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_news_rotoballer_premium_news_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_news_rotoballer_premium_news_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NflV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class AsyncNflV3RotoBallerPremiumNews:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNflV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    async def nfl_v3_news_rotoballer_premium_news(
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
            await self._with_raw_response.nfl_v3_news_rotoballer_premium_news(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_news_rotoballer_premium_news_by_date(
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
            await self._with_raw_response.nfl_v3_news_rotoballer_premium_news_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_news_rotoballer_premium_news_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_news_rotoballer_premium_news_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNflV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class NflV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfl_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByDateErrorBody]:
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
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_news_rotoballer_premium_news_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByTeamErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByTeam/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_by_team_error_mapper,
            request_options=request_options,
        )


class AsyncNflV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfl_v3_news_rotoballer_premium_news(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_news_rotoballer_premium_news_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByDateErrorBody]:
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
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_news_rotoballer_premium_news_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByTeamErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by team.

        Args:
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByTeam/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_by_team_error_mapper,
            request_options=request_options,
        )
