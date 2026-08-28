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
from ..errors.soccer_v4_projections_dfs_slates_by_date_error import (
    SoccerV4ProjectionsDfsSlatesByDateErrorBody,
    soccer_v4_projections_dfs_slates_by_date_error_mapper,
)
from ..errors.soccer_v4_projections_player_details_by_injured_error import (
    SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody,
    soccer_v4_projections_player_details_by_injured_error_mapper,
)
from ..errors.soccer_v4_projections_projected_player_game_stats_by_date_error import (
    SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody,
    soccer_v4_projections_projected_player_game_stats_by_date_error_mapper,
)
from ..errors.soccer_v4_projections_upcoming_dfs_slates_by_competition_error import (
    SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody,
    soccer_v4_projections_upcoming_dfs_slates_by_competition_error_mapper,
)
from ..models.dfs_slate5 import DfsSlate5
from ..models.enums.format import FormatOrStr
from ..models.player7 import Player7
from ..models.player_game_projection4 import PlayerGameProjection4
from ..server.server import Server


class SoccerV4Projections:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoccerV4ProjectionsWithRawResponse(client, server, auth)

    def soccer_v4_projections_dfs_slates_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate5]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2020-02-18</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_projections_dfs_slates_by_date(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_projections_player_details_by_injured(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player7]:
        """This endpoint provides all currently injured soccer players by competition, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_projections_player_details_by_injured(
            format, competition, request_options=request_options
        ).unwrap()

    def soccer_v4_projections_projected_player_game_stats_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGameProjection4]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_projections_projected_player_game_stats_by_date(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_projections_upcoming_dfs_slates_by_competition(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate5]:
        """Returns upcoming DFS Slates which have not yet started, with their player and salary information, by
        competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_projections_upcoming_dfs_slates_by_competition(
            format, competition, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoccerV4ProjectionsWithRawResponse:
        return self._with_raw_response


class AsyncSoccerV4Projections:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoccerV4ProjectionsWithRawResponse(client, server, auth)

    async def soccer_v4_projections_dfs_slates_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate5]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2020-02-18</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_projections_dfs_slates_by_date(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_projections_player_details_by_injured(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player7]:
        """This endpoint provides all currently injured soccer players by competition, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_projections_player_details_by_injured(
                format, competition, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_projections_projected_player_game_stats_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGameProjection4]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_projections_projected_player_game_stats_by_date(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_projections_upcoming_dfs_slates_by_competition(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate5]:
        """Returns upcoming DFS Slates which have not yet started, with their player and salary information, by
        competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_projections_upcoming_dfs_slates_by_competition(
                format, competition, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoccerV4ProjectionsWithRawResponse:
        return self._with_raw_response


class SoccerV4ProjectionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def soccer_v4_projections_dfs_slates_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate5], SoccerV4ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2020-02-18</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/projections/{format}/DfsSlatesByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate5]],
            error_mapper=soccer_v4_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_projections_player_details_by_injured(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player7], SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured soccer players by competition, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/projections/{format}/InjuredPlayers/{competition}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player7]],
            error_mapper=soccer_v4_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_projections_projected_player_game_stats_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGameProjection4], SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/projections/{format}/PlayerGameProjectionStatsByDate/{competition}/{date}"
            ),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection4]],
            error_mapper=soccer_v4_projections_projected_player_game_stats_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_projections_upcoming_dfs_slates_by_competition(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate5], SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody]:
        """Returns upcoming DFS Slates which have not yet started, with their player and salary information, by
        competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/projections/{format}/UpcomingDfsSlatesByCompetition/{competition}"
            ),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate5]],
            error_mapper=soccer_v4_projections_upcoming_dfs_slates_by_competition_error_mapper,
            request_options=request_options,
        )


class AsyncSoccerV4ProjectionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def soccer_v4_projections_dfs_slates_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate5], SoccerV4ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS Slates which have not yet started, with their player and salary information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2020-02-18</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/projections/{format}/DfsSlatesByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate5]],
            error_mapper=soccer_v4_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_projections_player_details_by_injured(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player7], SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured soccer players by competition, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/projections/{format}/InjuredPlayers/{competition}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player7]],
            error_mapper=soccer_v4_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_projections_projected_player_game_stats_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGameProjection4], SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/projections/{format}/PlayerGameProjectionStatsByDate/{competition}/{date}"
            ),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection4]],
            error_mapper=soccer_v4_projections_projected_player_game_stats_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_projections_upcoming_dfs_slates_by_competition(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate5], SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody]:
        """Returns upcoming DFS Slates which have not yet started, with their player and salary information, by
        competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/projections/{format}/UpcomingDfsSlatesByCompetition/{competition}"
            ),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate5]],
            error_mapper=soccer_v4_projections_upcoming_dfs_slates_by_competition_error_mapper,
            request_options=request_options,
        )
