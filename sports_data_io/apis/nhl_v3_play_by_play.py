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
from ..errors.nhl_v3_pbp_play_by_play_delta_error import (
    NhlV3PbpPlayByPlayDeltaErrorBody,
    nhl_v3_pbp_play_by_play_delta_error_mapper,
)
from ..errors.nhl_v3_pbp_play_by_play_final_error import (
    NhlV3PbpPlayByPlayFinalErrorBody,
    nhl_v3_pbp_play_by_play_final_error_mapper,
)
from ..errors.nhl_v3_pbp_play_by_play_live_final_error import (
    NhlV3PbpPlayByPlayLiveFinalErrorBody,
    nhl_v3_pbp_play_by_play_live_final_error_mapper,
)
from ..models.enums.format import Format, FormatOrStr
from ..models.play_by_play3 import PlayByPlay3
from ..server.server import Server


class NhlV3PlayByPlay:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NhlV3PlayByPlayWithRawResponse(client, server, auth)

    def nhl_v3_pbp_play_by_play_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay3:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_pbp_play_by_play_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_pbp_play_by_play_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay3:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_pbp_play_by_play_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_pbp_play_by_play_delta(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayByPlay3]:
        """This method returns all play-by-plays for a given season and week, but only returns plays that have changed
        in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            minutes: Only returns plays that have changed in the last X minutes. You specify how many minutes in time to
                go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_pbp_play_by_play_delta(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NhlV3PlayByPlayWithRawResponse:
        return self._with_raw_response


class AsyncNhlV3PlayByPlay:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNhlV3PlayByPlayWithRawResponse(client, server, auth)

    async def nhl_v3_pbp_play_by_play_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay3:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_pbp_play_by_play_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_pbp_play_by_play_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay3:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_pbp_play_by_play_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_pbp_play_by_play_delta(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayByPlay3]:
        """This method returns all play-by-plays for a given season and week, but only returns plays that have changed
        in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            minutes: Only returns plays that have changed in the last X minutes. You specify how many minutes in time to
                go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_pbp_play_by_play_delta(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNhlV3PlayByPlayWithRawResponse:
        return self._with_raw_response


class NhlV3PlayByPlayWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nhl_v3_pbp_play_by_play_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay3, NhlV3PbpPlayByPlayFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/pbp/{format}/PlayByPlayFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay3],
            error_mapper=nhl_v3_pbp_play_by_play_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_pbp_play_by_play_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay3, NhlV3PbpPlayByPlayLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/pbp/{format}/PlayByPlay/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay3],
            error_mapper=nhl_v3_pbp_play_by_play_live_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_pbp_play_by_play_delta(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayByPlay3], NhlV3PbpPlayByPlayDeltaErrorBody]:
        """This method returns all play-by-plays for a given season and week, but only returns plays that have changed
        in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            minutes: Only returns plays that have changed in the last X minutes. You specify how many minutes in time to
                go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/pbp/{format}/PlayByPlayDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay3]],
            error_mapper=nhl_v3_pbp_play_by_play_delta_error_mapper,
            request_options=request_options,
        )


class AsyncNhlV3PlayByPlayWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nhl_v3_pbp_play_by_play_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay3, NhlV3PbpPlayByPlayFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/pbp/{format}/PlayByPlayFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[PlayByPlay3],
            error_mapper=nhl_v3_pbp_play_by_play_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_pbp_play_by_play_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay3, NhlV3PbpPlayByPlayLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/pbp/{format}/PlayByPlay/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[PlayByPlay3],
            error_mapper=nhl_v3_pbp_play_by_play_live_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_pbp_play_by_play_delta(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayByPlay3], NhlV3PbpPlayByPlayDeltaErrorBody]:
        """This method returns all play-by-plays for a given season and week, but only returns plays that have changed
        in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            minutes: Only returns plays that have changed in the last X minutes. You specify how many minutes in time to
                go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/pbp/{format}/PlayByPlayDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayByPlay3]],
            error_mapper=nhl_v3_pbp_play_by_play_delta_error_mapper,
            request_options=request_options,
        )
