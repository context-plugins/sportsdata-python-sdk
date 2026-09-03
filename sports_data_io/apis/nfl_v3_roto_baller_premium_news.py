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
from ..models.enums.format import FormatOrStr
from ..models.news import News
from ..server.server import Server


class NflV3RotoBallerPremiumNews:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NflV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    def nfl_v3_news_rotoballer_premium_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_news_rotoballer_premium_news(
            format, request_options=request_options
        ).unwrap()

    def nfl_v3_news_rotoballer_premium_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_news_rotoballer_premium_news_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def nfl_v3_news_rotoballer_premium_news_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_news_rotoballer_premium_news_by_team(
            format, team, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NflV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class AsyncNflV3RotoBallerPremiumNews:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNflV3RotoBallerPremiumNewsWithRawResponse(client, server, auth)

    async def nfl_v3_news_rotoballer_premium_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_news_rotoballer_premium_news(format, request_options=request_options)
        ).unwrap()

    async def nfl_v3_news_rotoballer_premium_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_news_rotoballer_premium_news_by_date(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def nfl_v3_news_rotoballer_premium_news_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_news_rotoballer_premium_news_by_team(
                format, team, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNflV3RotoBallerPremiumNewsWithRawResponse:
        return self._with_raw_response


class NflV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfl_v3_news_rotoballer_premium_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_news_rotoballer_premium_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByDateErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_news_rotoballer_premium_news_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByTeamErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByTeam/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_by_team_error_mapper,
            request_options=request_options,
        )


class AsyncNflV3RotoBallerPremiumNewsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfl_v3_news_rotoballer_premium_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNews"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_news_rotoballer_premium_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByDateErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_by_date_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_news_rotoballer_premium_news_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByTeamErrorBody]:
        """RotoBaller's Premium News feed, with the latest updated stories in greater detail called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByTeam/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News]],
            error_mapper=nfl_v3_news_rotoballer_premium_news_by_team_error_mapper,
            request_options=request_options,
        )
