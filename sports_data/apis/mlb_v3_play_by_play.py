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
from ..errors.mlb_v3_pbp_play_by_play_delta_error import (
    MlbV3PbpPlayByPlayDeltaErrorBody,
    mlb_v3_pbp_play_by_play_delta_error_mapper,
)
from ..errors.mlb_v3_pbp_play_by_play_final_error import (
    MlbV3PbpPlayByPlayFinalErrorBody,
    mlb_v3_pbp_play_by_play_final_error_mapper,
)
from ..errors.mlb_v3_pbp_play_by_play_live_final_error import (
    MlbV3PbpPlayByPlayLiveFinalErrorBody,
    mlb_v3_pbp_play_by_play_live_final_error_mapper,
)
from ..models.enums.format import FormatOrStr
from ..models.play_by_play import PlayByPlay
from ..server.server import Server


class MlbV3PlayByPlay:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MlbV3PlayByPlayWithRawResponse(client, server, auth)

    def mlb_v3_pbp_play_by_play_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mlb_v3_pbp_play_by_play_final(
            format, gameid, request_options=request_options
        ).unwrap()

    def mlb_v3_pbp_play_by_play_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mlb_v3_pbp_play_by_play_live_final(
            format, gameid, request_options=request_options
        ).unwrap()

    def mlb_v3_pbp_play_by_play_delta(
        self, format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayByPlay]:
        """This method returns all play-by-plays for a given season and week, but only returns plays that have changed
        in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            minutes: Only returns plays that have changed in the last X minutes. You specify how many minutes in time to
                go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mlb_v3_pbp_play_by_play_delta(
            format, date, minutes, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MlbV3PlayByPlayWithRawResponse:
        return self._with_raw_response


class AsyncMlbV3PlayByPlay:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMlbV3PlayByPlayWithRawResponse(client, server, auth)

    async def mlb_v3_pbp_play_by_play_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mlb_v3_pbp_play_by_play_final(format, gameid, request_options=request_options)
        ).unwrap()

    async def mlb_v3_pbp_play_by_play_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mlb_v3_pbp_play_by_play_live_final(
                format, gameid, request_options=request_options
            )
        ).unwrap()

    async def mlb_v3_pbp_play_by_play_delta(
        self, format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayByPlay]:
        """This method returns all play-by-plays for a given season and week, but only returns plays that have changed
        in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            minutes: Only returns plays that have changed in the last X minutes. You specify how many minutes in time to
                go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mlb_v3_pbp_play_by_play_delta(
                format, date, minutes, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMlbV3PlayByPlayWithRawResponse:
        return self._with_raw_response


class MlbV3PlayByPlayWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mlb_v3_pbp_play_by_play_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay, MlbV3PbpPlayByPlayFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/pbp/{format}/PlayByPlayFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay],
            error_mapper=mlb_v3_pbp_play_by_play_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_pbp_play_by_play_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay, MlbV3PbpPlayByPlayLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/pbp/{format}/PlayByPlay/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay],
            error_mapper=mlb_v3_pbp_play_by_play_live_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_pbp_play_by_play_delta(
        self, format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayByPlay], MlbV3PbpPlayByPlayDeltaErrorBody]:
        """This method returns all play-by-plays for a given season and week, but only returns plays that have changed
        in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            minutes: Only returns plays that have changed in the last X minutes. You specify how many minutes in time to
                go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/pbp/{format}/PlayByPlayDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay]],
            error_mapper=mlb_v3_pbp_play_by_play_delta_error_mapper,
            request_options=request_options,
        )


class AsyncMlbV3PlayByPlayWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mlb_v3_pbp_play_by_play_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay, MlbV3PbpPlayByPlayFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/pbp/{format}/PlayByPlayFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay],
            error_mapper=mlb_v3_pbp_play_by_play_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_pbp_play_by_play_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay, MlbV3PbpPlayByPlayLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/pbp/{format}/PlayByPlay/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay],
            error_mapper=mlb_v3_pbp_play_by_play_live_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_pbp_play_by_play_delta(
        self, format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayByPlay], MlbV3PbpPlayByPlayDeltaErrorBody]:
        """This method returns all play-by-plays for a given season and week, but only returns plays that have changed
        in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            minutes: Only returns plays that have changed in the last X minutes. You specify how many minutes in time to
                go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/pbp/{format}/PlayByPlayDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay]],
            error_mapper=mlb_v3_pbp_play_by_play_delta_error_mapper,
            request_options=request_options,
        )
