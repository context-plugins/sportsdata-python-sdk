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
from ..errors.cwbb_v3_scores_are_any_games_in_progress_error import (
    CwbbV3ScoresAreAnyGamesInProgressErrorBody,
    cwbb_v3_scores_are_any_games_in_progress_error_mapper,
)
from ..errors.cwbb_v3_scores_games_by_date_final_error import (
    CwbbV3ScoresGamesByDateFinalErrorBody,
    cwbb_v3_scores_games_by_date_final_error_mapper,
)
from ..errors.cwbb_v3_scores_games_by_date_live_final_error import (
    CwbbV3ScoresGamesByDateLiveFinalErrorBody,
    cwbb_v3_scores_games_by_date_live_final_error_mapper,
)
from ..errors.cwbb_v3_scores_league_hierarchy_error import (
    CwbbV3ScoresLeagueHierarchyErrorBody,
    cwbb_v3_scores_league_hierarchy_error_mapper,
)
from ..errors.cwbb_v3_scores_schedules_basic_error import (
    CwbbV3ScoresSchedulesBasicErrorBody,
    cwbb_v3_scores_schedules_basic_error_mapper,
)
from ..errors.cwbb_v3_scores_schedules_error import (
    CwbbV3ScoresSchedulesErrorBody,
    cwbb_v3_scores_schedules_error_mapper,
)
from ..errors.cwbb_v3_scores_season_current_error import (
    CwbbV3ScoresSeasonCurrentErrorBody,
    cwbb_v3_scores_season_current_error_mapper,
)
from ..errors.cwbb_v3_scores_team_profiles_all_error import (
    CwbbV3ScoresTeamProfilesAllErrorBody,
    cwbb_v3_scores_team_profiles_all_error_mapper,
)
from ..models.conference2 import Conference2
from ..models.enums.format import Format, FormatOrStr
from ..models.game16 import Game16
from ..models.schedule_basic6 import ScheduleBasic6
from ..models.season5 import Season5
from ..models.team7 import Team7
from ..server.server import Server


class CwbbV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CwbbV3ScoresWithRawResponse(client, server, auth)

    def cwbb_v3_scores_are_any_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Are Any Games In Progress

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cwbb_v3_scores_are_any_games_in_progress(
                format_=format_, request_options=request_options
            ),
        )

    def cwbb_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game16]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s).<br>Examples: <code>2020-FEB-27</code>, <code>2019-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cwbb_v3_scores_games_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def cwbb_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game16]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

        Args:
            date: The date of the game(s).<br>Examples: <code>2020-FEB-27</code>, <code>2019-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cwbb_v3_scores_games_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def cwbb_v3_scores_league_hierarchy(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Conference2]:
        """The list of all conferences and their teams, with standings data.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cwbb_v3_scores_league_hierarchy(format_=format_, request_options=request_options)
        )

    def cwbb_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game16]:
        """Home and away teams, date and time, season type etc. are included. Also includes gameday information. This
        includes full stadium information, top-line betting information (spread, moneyline, total), weather conditions,
        and broadcast information.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cwbb_v3_scores_schedules(season, format_=format_, request_options=request_options)
        )

    def cwbb_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic6]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cwbb_v3_scores_schedules_basic(
                season, format_=format_, request_options=request_options
            ),
        )

    def cwbb_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Season5:
        """Season Current

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cwbb_v3_scores_season_current(format_=format_, request_options=request_options)
        )

    def cwbb_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team7]:
        """Full team information: school, team name and city, conference and division, and colors.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cwbb_v3_scores_team_profiles_all(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> CwbbV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncCwbbV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCwbbV3ScoresWithRawResponse(client, server, auth)

    async def cwbb_v3_scores_are_any_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Are Any Games In Progress

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cwbb_v3_scores_are_any_games_in_progress(
                format_=format_, request_options=request_options
            ),
        )

    async def cwbb_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game16]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s).<br>Examples: <code>2020-FEB-27</code>, <code>2019-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cwbb_v3_scores_games_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def cwbb_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game16]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

        Args:
            date: The date of the game(s).<br>Examples: <code>2020-FEB-27</code>, <code>2019-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cwbb_v3_scores_games_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def cwbb_v3_scores_league_hierarchy(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Conference2]:
        """The list of all conferences and their teams, with standings data.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cwbb_v3_scores_league_hierarchy(
                format_=format_, request_options=request_options
            ),
        )

    async def cwbb_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game16]:
        """Home and away teams, date and time, season type etc. are included. Also includes gameday information. This
        includes full stadium information, top-line betting information (spread, moneyline, total), weather conditions,
        and broadcast information.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cwbb_v3_scores_schedules(
                season, format_=format_, request_options=request_options
            ),
        )

    async def cwbb_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic6]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cwbb_v3_scores_schedules_basic(
                season, format_=format_, request_options=request_options
            ),
        )

    async def cwbb_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Season5:
        """Season Current

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cwbb_v3_scores_season_current(
                format_=format_, request_options=request_options
            ),
        )

    async def cwbb_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team7]:
        """Full team information: school, team name and city, conference and division, and colors.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cwbb_v3_scores_team_profiles_all(
                format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCwbbV3ScoresWithRawResponse:
        return self._with_raw_response


class CwbbV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cwbb_v3_scores_are_any_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, CwbbV3ScoresAreAnyGamesInProgressErrorBody]:
        """Are Any Games In Progress

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=cwbb_v3_scores_are_any_games_in_progress_error_mapper,
            request_options=request_options,
        )

    def cwbb_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game16], CwbbV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s).<br>Examples: <code>2020-FEB-27</code>, <code>2019-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game16]],
            error_mapper=cwbb_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def cwbb_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game16], CwbbV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

        Args:
            date: The date of the game(s).<br>Examples: <code>2020-FEB-27</code>, <code>2019-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game16]],
            error_mapper=cwbb_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def cwbb_v3_scores_league_hierarchy(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Conference2], CwbbV3ScoresLeagueHierarchyErrorBody]:
        """The list of all conferences and their teams, with standings data.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/LeagueHierarchy"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Conference2]],
            error_mapper=cwbb_v3_scores_league_hierarchy_error_mapper,
            request_options=request_options,
        )

    def cwbb_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game16], CwbbV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type etc. are included. Also includes gameday information. This
        includes full stadium information, top-line betting information (spread, moneyline, total), weather conditions,
        and broadcast information.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game16]],
            error_mapper=cwbb_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def cwbb_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic6], CwbbV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic6]],
            error_mapper=cwbb_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def cwbb_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season5, CwbbV3ScoresSeasonCurrentErrorBody]:
        """Season Current

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season5],
            error_mapper=cwbb_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    def cwbb_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team7], CwbbV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: school, team name and city, conference and division, and colors.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/Teams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team7]],
            error_mapper=cwbb_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )


class AsyncCwbbV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cwbb_v3_scores_are_any_games_in_progress(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, CwbbV3ScoresAreAnyGamesInProgressErrorBody]:
        """Are Any Games In Progress

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[bool],
            error_mapper=cwbb_v3_scores_are_any_games_in_progress_error_mapper,
            request_options=request_options,
        )

    async def cwbb_v3_scores_games_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game16], CwbbV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score, delivered as the game ends.

        Args:
            date: The date of the game(s).<br>Examples: <code>2020-FEB-27</code>, <code>2019-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game16]],
            error_mapper=cwbb_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def cwbb_v3_scores_games_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game16], CwbbV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

        Args:
            date: The date of the game(s).<br>Examples: <code>2020-FEB-27</code>, <code>2019-DEC-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game16]],
            error_mapper=cwbb_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def cwbb_v3_scores_league_hierarchy(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Conference2], CwbbV3ScoresLeagueHierarchyErrorBody]:
        """The list of all conferences and their teams, with standings data.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/LeagueHierarchy"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Conference2]],
            error_mapper=cwbb_v3_scores_league_hierarchy_error_mapper,
            request_options=request_options,
        )

    async def cwbb_v3_scores_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game16], CwbbV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type etc. are included. Also includes gameday information. This
        includes full stadium information, top-line betting information (spread, moneyline, total), weather conditions,
        and broadcast information.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game16]],
            error_mapper=cwbb_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def cwbb_v3_scores_schedules_basic(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic6], CwbbV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScheduleBasic6]],
            error_mapper=cwbb_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def cwbb_v3_scores_season_current(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season5, CwbbV3ScoresSeasonCurrentErrorBody]:
        """Season Current

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[Season5],
            error_mapper=cwbb_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    async def cwbb_v3_scores_team_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team7], CwbbV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: school, team name and city, conference and division, and colors.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cwbb/scores/{format}/Teams"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team7]],
            error_mapper=cwbb_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )
