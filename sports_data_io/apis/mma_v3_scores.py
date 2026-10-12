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
from ..errors.mma_v3_scores_event_error import MmaV3ScoresEventErrorBody, mma_v3_scores_event_error_mapper
from ..errors.mma_v3_scores_fighter_profile_by_fighter_error import (
    MmaV3ScoresFighterProfileByFighterErrorBody,
    mma_v3_scores_fighter_profile_by_fighter_error_mapper,
)
from ..errors.mma_v3_scores_fighter_profiles_all_error import (
    MmaV3ScoresFighterProfilesAllErrorBody,
    mma_v3_scores_fighter_profiles_all_error_mapper,
)
from ..errors.mma_v3_scores_fighter_profiles_basic_all_error import (
    MmaV3ScoresFighterProfilesBasicAllErrorBody,
    mma_v3_scores_fighter_profiles_basic_all_error_mapper,
)
from ..errors.mma_v3_scores_leagues_error import MmaV3ScoresLeaguesErrorBody, mma_v3_scores_leagues_error_mapper
from ..errors.mma_v3_scores_schedules_error import MmaV3ScoresSchedulesErrorBody, mma_v3_scores_schedules_error_mapper
from ..models.enums.format import Format, FormatOrStr
from ..models.event import Event
from ..models.event_detail import EventDetail
from ..models.fighter import Fighter
from ..models.fighter_basic import FighterBasic
from ..models.league import League
from ..server.server import Server


class MmaV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MmaV3ScoresWithRawResponse(client, server, auth)

    def mma_v3_scores_event(
        self, eventid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> EventDetail:
        """Returns all fights that will take place within a given EventId (fight card.)

        Args:
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_scores_event(eventid, format_=format_, request_options=request_options)
        )

    def mma_v3_scores_fighter_profile_by_fighter(
        self, fighterid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Fighter:
        """An individual fighter profile.

        Args:
            fighterid: Each fighter has a unique ID assigned by FantasyData. Fighter IDs can be determined by pulling
                player related data. Example: <code>140000098</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_scores_fighter_profile_by_fighter(
                fighterid, format_=format_, request_options=request_options
            ),
        )

    def mma_v3_scores_fighter_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Fighter]:
        """A list of all fighters with their basic biographical information and career records.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_scores_fighter_profiles_all(format_=format_, request_options=request_options)
        )

    def mma_v3_scores_fighter_profiles_basic_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FighterBasic]:
        """A stripped-down list of all fighters with basic profile information, ideal for simple applications.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_scores_fighter_profiles_basic_all(
                format_=format_, request_options=request_options
            ),
        )

    def mma_v3_scores_leagues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[League]:
        """A list of all leagues (currently this returns just UFC.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(self._with_raw_response.mma_v3_scores_leagues(format_=format_, request_options=request_options))

    def mma_v3_scores_schedules(
        self,
        league: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Event]:
        """A list of all upcoming Events, from which the Fights can be discovered.

        Args:
            league: The name of the league.<br>Examples: <code>UFC</code>, etc
            season: Year of the season.<br>Examples: <code>2019</code>, <code>2020</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mma_v3_scores_schedules(
                league, season, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> MmaV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncMmaV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMmaV3ScoresWithRawResponse(client, server, auth)

    async def mma_v3_scores_event(
        self, eventid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> EventDetail:
        """Returns all fights that will take place within a given EventId (fight card.)

        Args:
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_scores_event(eventid, format_=format_, request_options=request_options)
        )

    async def mma_v3_scores_fighter_profile_by_fighter(
        self, fighterid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Fighter:
        """An individual fighter profile.

        Args:
            fighterid: Each fighter has a unique ID assigned by FantasyData. Fighter IDs can be determined by pulling
                player related data. Example: <code>140000098</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_scores_fighter_profile_by_fighter(
                fighterid, format_=format_, request_options=request_options
            ),
        )

    async def mma_v3_scores_fighter_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Fighter]:
        """A list of all fighters with their basic biographical information and career records.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_scores_fighter_profiles_all(
                format_=format_, request_options=request_options
            ),
        )

    async def mma_v3_scores_fighter_profiles_basic_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FighterBasic]:
        """A stripped-down list of all fighters with basic profile information, ideal for simple applications.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_scores_fighter_profiles_basic_all(
                format_=format_, request_options=request_options
            ),
        )

    async def mma_v3_scores_leagues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[League]:
        """A list of all leagues (currently this returns just UFC.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_scores_leagues(format_=format_, request_options=request_options)
        )

    async def mma_v3_scores_schedules(
        self,
        league: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Event]:
        """A list of all upcoming Events, from which the Fights can be discovered.

        Args:
            league: The name of the league.<br>Examples: <code>UFC</code>, etc
            season: Year of the season.<br>Examples: <code>2019</code>, <code>2020</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mma_v3_scores_schedules(
                league, season, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncMmaV3ScoresWithRawResponse:
        return self._with_raw_response


class MmaV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mma_v3_scores_event(
        self, eventid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventDetail, MmaV3ScoresEventErrorBody]:
        """Returns all fights that will take place within a given EventId (fight card.)

        Args:
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Event/{eventid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventid", eventid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[EventDetail],
            error_mapper=mma_v3_scores_event_error_mapper,
            request_options=request_options,
        )

    def mma_v3_scores_fighter_profile_by_fighter(
        self, fighterid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Fighter, MmaV3ScoresFighterProfileByFighterErrorBody]:
        """An individual fighter profile.

        Args:
            fighterid: Each fighter has a unique ID assigned by FantasyData. Fighter IDs can be determined by pulling
                player related data. Example: <code>140000098</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Fighter/{fighterid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fighterid", fighterid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Fighter],
            error_mapper=mma_v3_scores_fighter_profile_by_fighter_error_mapper,
            request_options=request_options,
        )

    def mma_v3_scores_fighter_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Fighter], MmaV3ScoresFighterProfilesAllErrorBody]:
        """A list of all fighters with their basic biographical information and career records.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Fighters"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Fighter]],
            error_mapper=mma_v3_scores_fighter_profiles_all_error_mapper,
            request_options=request_options,
        )

    def mma_v3_scores_fighter_profiles_basic_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FighterBasic], MmaV3ScoresFighterProfilesBasicAllErrorBody]:
        """A stripped-down list of all fighters with basic profile information, ideal for simple applications.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/FightersBasic"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FighterBasic]],
            error_mapper=mma_v3_scores_fighter_profiles_basic_all_error_mapper,
            request_options=request_options,
        )

    def mma_v3_scores_leagues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[League], MmaV3ScoresLeaguesErrorBody]:
        """A list of all leagues (currently this returns just UFC.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Leagues"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[League]],
            error_mapper=mma_v3_scores_leagues_error_mapper,
            request_options=request_options,
        )

    def mma_v3_scores_schedules(
        self,
        league: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Event], MmaV3ScoresSchedulesErrorBody]:
        """A list of all upcoming Events, from which the Fights can be discovered.

        Args:
            league: The name of the league.<br>Examples: <code>UFC</code>, etc
            season: Year of the season.<br>Examples: <code>2019</code>, <code>2020</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Schedule/{league}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("league", league), param[str]("season", season)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Event]],
            error_mapper=mma_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )


class AsyncMmaV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mma_v3_scores_event(
        self, eventid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventDetail, MmaV3ScoresEventErrorBody]:
        """Returns all fights that will take place within a given EventId (fight card.)

        Args:
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Event/{eventid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventid", eventid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[EventDetail],
            error_mapper=mma_v3_scores_event_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_scores_fighter_profile_by_fighter(
        self, fighterid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Fighter, MmaV3ScoresFighterProfileByFighterErrorBody]:
        """An individual fighter profile.

        Args:
            fighterid: Each fighter has a unique ID assigned by FantasyData. Fighter IDs can be determined by pulling
                player related data. Example: <code>140000098</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Fighter/{fighterid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("fighterid", fighterid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[Fighter],
            error_mapper=mma_v3_scores_fighter_profile_by_fighter_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_scores_fighter_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Fighter], MmaV3ScoresFighterProfilesAllErrorBody]:
        """A list of all fighters with their basic biographical information and career records.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Fighters"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Fighter]],
            error_mapper=mma_v3_scores_fighter_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_scores_fighter_profiles_basic_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FighterBasic], MmaV3ScoresFighterProfilesBasicAllErrorBody]:
        """A stripped-down list of all fighters with basic profile information, ideal for simple applications.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/FightersBasic"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FighterBasic]],
            error_mapper=mma_v3_scores_fighter_profiles_basic_all_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_scores_leagues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[League], MmaV3ScoresLeaguesErrorBody]:
        """A list of all leagues (currently this returns just UFC.)

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Leagues"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[League]],
            error_mapper=mma_v3_scores_leagues_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_scores_schedules(
        self,
        league: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Event], MmaV3ScoresSchedulesErrorBody]:
        """A list of all upcoming Events, from which the Fights can be discovered.

        Args:
            league: The name of the league.<br>Examples: <code>UFC</code>, etc
            season: Year of the season.<br>Examples: <code>2019</code>, <code>2020</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/scores/{format}/Schedule/{league}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("league", league), param[str]("season", season)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Event]],
            error_mapper=mma_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )
