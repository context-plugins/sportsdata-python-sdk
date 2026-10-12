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
from ..errors.nascar_v2_driver_driver_profiles_by_driver_error import (
    NascarV2DriverDriverProfilesByDriverErrorBody,
    nascar_v2_driver_driver_profiles_by_driver_error_mapper,
)
from ..errors.nascar_v2_driverraceprojections_projected_player_race_stats_by_race_error import (
    NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody,
    nascar_v2_driverraceprojections_projected_player_race_stats_by_race_error_mapper,
)
from ..errors.nascar_v2_drivers_driver_profiles_all_error import (
    NascarV2DriversDriverProfilesAllErrorBody,
    nascar_v2_drivers_driver_profiles_all_error_mapper,
)
from ..errors.nascar_v2_driversbyactive_drivers_by_active_error import (
    NascarV2DriversbyactiveDriversByActiveErrorBody,
    nascar_v2_driversbyactive_drivers_by_active_error_mapper,
)
from ..errors.nascar_v2_entrylistbyrace_entry_list_by_race_error import (
    NascarV2EntrylistbyraceEntryListByRaceErrorBody,
    nascar_v2_entrylistbyrace_entry_list_by_race_error_mapper,
)
from ..errors.nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race_error import (
    NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody,
    nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race_error_mapper,
)
from ..errors.nascar_v2_leaderboardbasic_leaderboard_basic_error import (
    NascarV2LeaderboardbasicLeaderboardBasicErrorBody,
    nascar_v2_leaderboardbasic_leaderboard_basic_error_mapper,
)
from ..errors.nascar_v2_leaderboardbasicfinal_leaderboard_basic_final_error import (
    NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody,
    nascar_v2_leaderboardbasicfinal_leaderboard_basic_final_error_mapper,
)
from ..errors.nascar_v2_raceresult_leaderboard_live_final_error import (
    NascarV2RaceresultLeaderboardLiveFinalErrorBody,
    nascar_v2_raceresult_leaderboard_live_final_error_mapper,
)
from ..errors.nascar_v2_raceresultfinal_leaderboard_final_error import (
    NascarV2RaceresultfinalLeaderboardFinalErrorBody,
    nascar_v2_raceresultfinal_leaderboard_final_error_mapper,
)
from ..errors.nascar_v2_races_schedules_error import (
    NascarV2RacesSchedulesErrorBody,
    nascar_v2_races_schedules_error_mapper,
)
from ..errors.nascar_v2_series_series_error import NascarV2SeriesSeriesErrorBody, nascar_v2_series_series_error_mapper
from ..errors.nascar_v2_tracks_tracks_error import NascarV2TracksTracksErrorBody, nascar_v2_tracks_tracks_error_mapper
from ..models.driver import Driver
from ..models.driver_basic import DriverBasic
from ..models.driver_race_basic import DriverRaceBasic
from ..models.driver_race_projection import DriverRaceProjection
from ..models.enums.format import Format, FormatOrStr
from ..models.fantasy_race import FantasyRace
from ..models.race import Race
from ..models.race_result import RaceResult
from ..models.race_result_basic import RaceResultBasic
from ..models.series1 import Series1
from ..models.tracks import Tracks
from ..server.server import Server


class NascarV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NascarV2WithRawResponse(client, server, auth)

    def nascar_v2_driver_driver_profiles_by_driver(
        self, driverid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Driver:
        """Driver Profiles - by Driver

        Args:
            driverid: Unique FantasyData Driver ID. Example:<code>80000268</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_driver_driver_profiles_by_driver(
                driverid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_driverraceprojections_projected_player_race_stats_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DriverRaceProjection]:
        """Projected Player Race Stats - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_driverraceprojections_projected_player_race_stats_by_race(
                raceid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_drivers_driver_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Driver]:
        """Driver Profiles - All

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_drivers_driver_profiles_all(
                format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_driversbyactive_drivers_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DriverBasic]:
        """Drivers - by Active

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_driversbyactive_drivers_by_active(
                format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_entrylistbyrace_entry_list_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DriverRaceBasic]:
        """Entry List - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_entrylistbyrace_entry_list_by_race(
                raceid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FantasyRace:
        """Fantasy Points - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race(
                raceid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_leaderboardbasic_leaderboard_basic(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceResultBasic:
        """Leaderboard (Basic)

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_leaderboardbasic_leaderboard_basic(
                raceid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_leaderboardbasicfinal_leaderboard_basic_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceResultBasic:
        """Leaderboard (Basic) [Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_leaderboardbasicfinal_leaderboard_basic_final(
                raceid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_raceresult_leaderboard_live_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceResult:
        """Leaderboard [Live & Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_raceresult_leaderboard_live_final(
                raceid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_raceresultfinal_leaderboard_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceResult:
        """Leaderboard [Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_raceresultfinal_leaderboard_final(
                raceid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v2_races_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Race]:
        """Schedules

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_races_schedules(season, format_=format_, request_options=request_options)
        )

    def nascar_v2_series_series(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Series1]:
        """Lists the different Series - the type of races administered by NASCAR - currently active.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(self._with_raw_response.nascar_v2_series_series(format_=format_, request_options=request_options))

    def nascar_v2_tracks_tracks(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Tracks]:
        """Tracks

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v2_tracks_tracks(season, format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> NascarV2WithRawResponse:
        return self._with_raw_response


class AsyncNascarV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNascarV2WithRawResponse(client, server, auth)

    async def nascar_v2_driver_driver_profiles_by_driver(
        self, driverid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> Driver:
        """Driver Profiles - by Driver

        Args:
            driverid: Unique FantasyData Driver ID. Example:<code>80000268</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_driver_driver_profiles_by_driver(
                driverid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_driverraceprojections_projected_player_race_stats_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DriverRaceProjection]:
        """Projected Player Race Stats - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_driverraceprojections_projected_player_race_stats_by_race(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_drivers_driver_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Driver]:
        """Driver Profiles - All

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_drivers_driver_profiles_all(
                format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_driversbyactive_drivers_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DriverBasic]:
        """Drivers - by Active

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_driversbyactive_drivers_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_entrylistbyrace_entry_list_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DriverRaceBasic]:
        """Entry List - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_entrylistbyrace_entry_list_by_race(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> FantasyRace:
        """Fantasy Points - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_leaderboardbasic_leaderboard_basic(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceResultBasic:
        """Leaderboard (Basic)

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_leaderboardbasic_leaderboard_basic(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_leaderboardbasicfinal_leaderboard_basic_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceResultBasic:
        """Leaderboard (Basic) [Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_leaderboardbasicfinal_leaderboard_basic_final(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_raceresult_leaderboard_live_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceResult:
        """Leaderboard [Live & Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_raceresult_leaderboard_live_final(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_raceresultfinal_leaderboard_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceResult:
        """Leaderboard [Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_raceresultfinal_leaderboard_final(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_races_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Race]:
        """Schedules

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_races_schedules(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v2_series_series(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Series1]:
        """Lists the different Series - the type of races administered by NASCAR - currently active.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_series_series(format_=format_, request_options=request_options)
        )

    async def nascar_v2_tracks_tracks(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Tracks]:
        """Tracks

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v2_tracks_tracks(
                season, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNascarV2WithRawResponse:
        return self._with_raw_response


class NascarV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nascar_v2_driver_driver_profiles_by_driver(
        self, driverid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Driver, NascarV2DriverDriverProfilesByDriverErrorBody]:
        """Driver Profiles - by Driver

        Args:
            driverid: Unique FantasyData Driver ID. Example:<code>80000268</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/driver/{driverid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("driverid", driverid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Driver],
            error_mapper=nascar_v2_driver_driver_profiles_by_driver_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_driverraceprojections_projected_player_race_stats_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DriverRaceProjection], NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody]:
        """Projected Player Race Stats - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/DriverRaceProjections/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DriverRaceProjection]],
            error_mapper=nascar_v2_driverraceprojections_projected_player_race_stats_by_race_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_drivers_driver_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Driver], NascarV2DriversDriverProfilesAllErrorBody]:
        """Driver Profiles - All

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/drivers"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Driver]],
            error_mapper=nascar_v2_drivers_driver_profiles_all_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_driversbyactive_drivers_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DriverBasic], NascarV2DriversbyactiveDriversByActiveErrorBody]:
        """Drivers - by Active

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/driversbyactive"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DriverBasic]],
            error_mapper=nascar_v2_driversbyactive_drivers_by_active_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_entrylistbyrace_entry_list_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DriverRaceBasic], NascarV2EntrylistbyraceEntryListByRaceErrorBody]:
        """Entry List - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/EntryListbyRace/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DriverRaceBasic]],
            error_mapper=nascar_v2_entrylistbyrace_entry_list_by_race_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FantasyRace, NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody]:
        """Fantasy Points - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/FantasyGameStatsByRace/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FantasyRace],
            error_mapper=nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_leaderboardbasic_leaderboard_basic(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceResultBasic, NascarV2LeaderboardbasicLeaderboardBasicErrorBody]:
        """Leaderboard (Basic)

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/LeaderboardBasic/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[RaceResultBasic],
            error_mapper=nascar_v2_leaderboardbasic_leaderboard_basic_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_leaderboardbasicfinal_leaderboard_basic_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceResultBasic, NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody]:
        """Leaderboard (Basic) [Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/LeaderboardBasicFinal/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[RaceResultBasic],
            error_mapper=nascar_v2_leaderboardbasicfinal_leaderboard_basic_final_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_raceresult_leaderboard_live_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceResult, NascarV2RaceresultLeaderboardLiveFinalErrorBody]:
        """Leaderboard [Live & Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/raceresult/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[RaceResult],
            error_mapper=nascar_v2_raceresult_leaderboard_live_final_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_raceresultfinal_leaderboard_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceResult, NascarV2RaceresultfinalLeaderboardFinalErrorBody]:
        """Leaderboard [Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/raceresultfinal/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[RaceResult],
            error_mapper=nascar_v2_raceresultfinal_leaderboard_final_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_races_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Race], NascarV2RacesSchedulesErrorBody]:
        """Schedules

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/races/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Race]],
            error_mapper=nascar_v2_races_schedules_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_series_series(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Series1], NascarV2SeriesSeriesErrorBody]:
        """Lists the different Series - the type of races administered by NASCAR - currently active.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/series"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Series1]],
            error_mapper=nascar_v2_series_series_error_mapper,
            request_options=request_options,
        )

    def nascar_v2_tracks_tracks(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Tracks], NascarV2TracksTracksErrorBody]:
        """Tracks

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/tracks/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Tracks]],
            error_mapper=nascar_v2_tracks_tracks_error_mapper,
            request_options=request_options,
        )


class AsyncNascarV2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nascar_v2_driver_driver_profiles_by_driver(
        self, driverid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Driver, NascarV2DriverDriverProfilesByDriverErrorBody]:
        """Driver Profiles - by Driver

        Args:
            driverid: Unique FantasyData Driver ID. Example:<code>80000268</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/driver/{driverid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("driverid", driverid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[Driver],
            error_mapper=nascar_v2_driver_driver_profiles_by_driver_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_driverraceprojections_projected_player_race_stats_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DriverRaceProjection], NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody]:
        """Projected Player Race Stats - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/DriverRaceProjections/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DriverRaceProjection]],
            error_mapper=nascar_v2_driverraceprojections_projected_player_race_stats_by_race_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_drivers_driver_profiles_all(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Driver], NascarV2DriversDriverProfilesAllErrorBody]:
        """Driver Profiles - All

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/drivers"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Driver]],
            error_mapper=nascar_v2_drivers_driver_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_driversbyactive_drivers_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DriverBasic], NascarV2DriversbyactiveDriversByActiveErrorBody]:
        """Drivers - by Active

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/driversbyactive"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DriverBasic]],
            error_mapper=nascar_v2_driversbyactive_drivers_by_active_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_entrylistbyrace_entry_list_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DriverRaceBasic], NascarV2EntrylistbyraceEntryListByRaceErrorBody]:
        """Entry List - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/EntryListbyRace/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DriverRaceBasic]],
            error_mapper=nascar_v2_entrylistbyrace_entry_list_by_race_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FantasyRace, NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody]:
        """Fantasy Points - by Race

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/FantasyGameStatsByRace/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[FantasyRace],
            error_mapper=nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_leaderboardbasic_leaderboard_basic(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceResultBasic, NascarV2LeaderboardbasicLeaderboardBasicErrorBody]:
        """Leaderboard (Basic)

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/LeaderboardBasic/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[RaceResultBasic],
            error_mapper=nascar_v2_leaderboardbasic_leaderboard_basic_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_leaderboardbasicfinal_leaderboard_basic_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceResultBasic, NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody]:
        """Leaderboard (Basic) [Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/LeaderboardBasicFinal/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[RaceResultBasic],
            error_mapper=nascar_v2_leaderboardbasicfinal_leaderboard_basic_final_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_raceresult_leaderboard_live_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceResult, NascarV2RaceresultLeaderboardLiveFinalErrorBody]:
        """Leaderboard [Live & Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/raceresult/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[RaceResult],
            error_mapper=nascar_v2_raceresult_leaderboard_live_final_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_raceresultfinal_leaderboard_final(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceResult, NascarV2RaceresultfinalLeaderboardFinalErrorBody]:
        """Leaderboard [Final]

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/raceresultfinal/{raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[RaceResult],
            error_mapper=nascar_v2_raceresultfinal_leaderboard_final_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_races_schedules(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Race], NascarV2RacesSchedulesErrorBody]:
        """Schedules

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/races/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Race]],
            error_mapper=nascar_v2_races_schedules_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_series_series(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Series1], NascarV2SeriesSeriesErrorBody]:
        """Lists the different Series - the type of races administered by NASCAR - currently active.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/series"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Series1]],
            error_mapper=nascar_v2_series_series_error_mapper,
            request_options=request_options,
        )

    async def nascar_v2_tracks_tracks(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Tracks], NascarV2TracksTracksErrorBody]:
        """Tracks

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/nascar/v2/{format}/tracks/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Tracks]],
            error_mapper=nascar_v2_tracks_tracks_error_mapper,
            request_options=request_options,
        )
