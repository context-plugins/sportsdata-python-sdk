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
from ..errors.mma_v3_stats_fight_basic_final_error import (
    MmaV3StatsFightBasicFinalErrorBody,
    mma_v3_stats_fight_basic_final_error_mapper,
)
from ..errors.mma_v3_stats_fight_basic_live_final_error import (
    MmaV3StatsFightBasicLiveFinalErrorBody,
    mma_v3_stats_fight_basic_live_final_error_mapper,
)
from ..errors.mma_v3_stats_fight_final_error import MmaV3StatsFightFinalErrorBody, mma_v3_stats_fight_final_error_mapper
from ..errors.mma_v3_stats_fight_live_final_error import (
    MmaV3StatsFightLiveFinalErrorBody,
    mma_v3_stats_fight_live_final_error_mapper,
)
from ..models.enums.format import Format, FormatOrStr
from ..models.fight_basic import FightBasic
from ..models.fight_detail import FightDetail
from ..server.server import Server


class MmaV3Stats:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MmaV3StatsWithRawResponse(client, server, auth)

    def mma_v3_stats_fight_basic_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FightBasic:
        """Simple fight information, such as the number of rounds, the clock etc., delivered after the fight only.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_stats_fight_basic_final(
                fightid, format_=format_, request_options=request_options
            ),
        )

    def mma_v3_stats_fight_basic_live_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FightBasic:
        """Simple fight information, such as the number of rounds, the clock etc., delivered live and after the fight.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_stats_fight_basic_live_final(
                fightid, format_=format_, request_options=request_options
            ),
        )

    def mma_v3_stats_fight_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FightDetail:
        """Statistical, round-by-round data for a given FightId, delivered after the fight ends.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_stats_fight_final(fightid, format_=format_, request_options=request_options)
        )

    def mma_v3_stats_fight_live_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FightDetail:
        """Statistical, round-by-round data for a given FightId, delivered round-by-round and confirmed post-fight.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_stats_fight_live_final(
                fightid, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> MmaV3StatsWithRawResponse:
        return self._with_raw_response


class AsyncMmaV3Stats:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMmaV3StatsWithRawResponse(client, server, auth)

    async def mma_v3_stats_fight_basic_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FightBasic:
        """Simple fight information, such as the number of rounds, the clock etc., delivered after the fight only.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_stats_fight_basic_final(
                fightid, format_=format_, request_options=request_options
            ),
        )

    async def mma_v3_stats_fight_basic_live_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FightBasic:
        """Simple fight information, such as the number of rounds, the clock etc., delivered live and after the fight.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_stats_fight_basic_live_final(
                fightid, format_=format_, request_options=request_options
            ),
        )

    async def mma_v3_stats_fight_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FightDetail:
        """Statistical, round-by-round data for a given FightId, delivered after the fight ends.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_stats_fight_final(
                fightid, format_=format_, request_options=request_options
            ),
        )

    async def mma_v3_stats_fight_live_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FightDetail:
        """Statistical, round-by-round data for a given FightId, delivered round-by-round and confirmed post-fight.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_stats_fight_live_final(
                fightid, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncMmaV3StatsWithRawResponse:
        return self._with_raw_response


class MmaV3StatsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mma_v3_stats_fight_basic_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FightBasic, MmaV3StatsFightBasicFinalErrorBody]:
        """Simple fight information, such as the number of rounds, the clock etc., delivered after the fight only.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/stats/{format}/FightBasicFinal/{fightid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fightid", fightid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FightBasic],
            error_mapper=mma_v3_stats_fight_basic_final_error_mapper,
            request_options=request_options,
        )

    def mma_v3_stats_fight_basic_live_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FightBasic, MmaV3StatsFightBasicLiveFinalErrorBody]:
        """Simple fight information, such as the number of rounds, the clock etc., delivered live and after the fight.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/stats/{format}/FightBasic/{fightid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fightid", fightid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FightBasic],
            error_mapper=mma_v3_stats_fight_basic_live_final_error_mapper,
            request_options=request_options,
        )

    def mma_v3_stats_fight_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FightDetail, MmaV3StatsFightFinalErrorBody]:
        """Statistical, round-by-round data for a given FightId, delivered after the fight ends.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/stats/{format}/FightFinal/{fightid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fightid", fightid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FightDetail],
            error_mapper=mma_v3_stats_fight_final_error_mapper,
            request_options=request_options,
        )

    def mma_v3_stats_fight_live_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FightDetail, MmaV3StatsFightLiveFinalErrorBody]:
        """Statistical, round-by-round data for a given FightId, delivered round-by-round and confirmed post-fight.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/stats/{format}/Fight/{fightid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fightid", fightid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FightDetail],
            error_mapper=mma_v3_stats_fight_live_final_error_mapper,
            request_options=request_options,
        )


class AsyncMmaV3StatsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mma_v3_stats_fight_basic_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FightBasic, MmaV3StatsFightBasicFinalErrorBody]:
        """Simple fight information, such as the number of rounds, the clock etc., delivered after the fight only.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/stats/{format}/FightBasicFinal/{fightid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fightid", fightid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[FightBasic],
            error_mapper=mma_v3_stats_fight_basic_final_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_stats_fight_basic_live_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FightBasic, MmaV3StatsFightBasicLiveFinalErrorBody]:
        """Simple fight information, such as the number of rounds, the clock etc., delivered live and after the fight.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/stats/{format}/FightBasic/{fightid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fightid", fightid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[FightBasic],
            error_mapper=mma_v3_stats_fight_basic_live_final_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_stats_fight_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FightDetail, MmaV3StatsFightFinalErrorBody]:
        """Statistical, round-by-round data for a given FightId, delivered after the fight ends.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/stats/{format}/FightFinal/{fightid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fightid", fightid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[FightDetail],
            error_mapper=mma_v3_stats_fight_final_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_stats_fight_live_final(
        self, fightid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FightDetail, MmaV3StatsFightLiveFinalErrorBody]:
        """Statistical, round-by-round data for a given FightId, delivered round-by-round and confirmed post-fight.

        Args:
            fightid: The unique ID of this fight. <br> Examples: <code>1100</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/stats/{format}/Fight/{fightid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fightid", fightid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[FightDetail],
            error_mapper=mma_v3_stats_fight_live_final_error_mapper,
            request_options=request_options,
        )
