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
from ..errors.nfl_v3_pbp_play_by_play_by_team_final_error import (
    NflV3PbpPlayByPlayByTeamFinalErrorBody,
    nfl_v3_pbp_play_by_play_by_team_final_error_mapper,
)
from ..errors.nfl_v3_pbp_play_by_play_by_team_live_final_error import (
    NflV3PbpPlayByPlayByTeamLiveFinalErrorBody,
    nfl_v3_pbp_play_by_play_by_team_live_final_error_mapper,
)
from ..errors.nfl_v3_pbp_play_by_play_delta_error import (
    NflV3PbpPlayByPlayDeltaErrorBody,
    nfl_v3_pbp_play_by_play_delta_error_mapper,
)
from ..errors.nfl_v3_pbp_play_by_play_final_error import (
    NflV3PbpPlayByPlayFinalErrorBody,
    nfl_v3_pbp_play_by_play_final_error_mapper,
)
from ..errors.nfl_v3_pbp_play_by_play_live_final_error import (
    NflV3PbpPlayByPlayLiveFinalErrorBody,
    nfl_v3_pbp_play_by_play_live_final_error_mapper,
)
from ..errors.nfl_v3_pbp_play_by_play_simulation_error import (
    NflV3PbpPlayByPlaySimulationErrorBody,
    nfl_v3_pbp_play_by_play_simulation_error_mapper,
)
from ..models.enums.format import FormatOrStr
from ..models.play_by_play2 import PlayByPlay2
from ..server.server import Server


class NflV3PlayByPlay:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NflV3PlayByPlayWithRawResponse(client, server, auth)

    def nfl_v3_pbp_play_by_play_by_team_final(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        hometeam: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlayByPlay2:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_pbp_play_by_play_by_team_final(
            format, season, week, hometeam, request_options=request_options
        ).unwrap()

    def nfl_v3_pbp_play_by_play_by_team_live_final(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        hometeam: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlayByPlay2:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_pbp_play_by_play_by_team_live_final(
            format, season, week, hometeam, request_options=request_options
        ).unwrap()

    def nfl_v3_pbp_play_by_play_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay2:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_pbp_play_by_play_final(
            format, gameid, request_options=request_options
        ).unwrap()

    def nfl_v3_pbp_play_by_play_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay2:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_pbp_play_by_play_live_final(
            format, gameid, request_options=request_options
        ).unwrap()

    def nfl_v3_pbp_play_by_play_delta(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayByPlay2]:
        """This method returns all play-by-plays for a given season and week, but only returnsplays that have changed in
        the last X minutes as specified in your API call. by definition this is a live endpoint, not final.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br> <code>1</code> or <code>2</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_pbp_play_by_play_delta(
            format, season, week, minutes, request_options=request_options
        ).unwrap()

    def nfl_v3_pbp_play_by_play_simulation(
        self, format: FormatOrStr, numberofplays: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayByPlay2]:
        """Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21,
        2018.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.nfl_v3_pbp_play_by_play_simulation(
            format, numberofplays, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> NflV3PlayByPlayWithRawResponse:
        return self._with_raw_response


class AsyncNflV3PlayByPlay:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNflV3PlayByPlayWithRawResponse(client, server, auth)

    async def nfl_v3_pbp_play_by_play_by_team_final(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        hometeam: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlayByPlay2:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_pbp_play_by_play_by_team_final(
                format, season, week, hometeam, request_options=request_options
            )
        ).unwrap()

    async def nfl_v3_pbp_play_by_play_by_team_live_final(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        hometeam: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlayByPlay2:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_pbp_play_by_play_by_team_live_final(
                format, season, week, hometeam, request_options=request_options
            )
        ).unwrap()

    async def nfl_v3_pbp_play_by_play_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay2:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_pbp_play_by_play_final(format, gameid, request_options=request_options)
        ).unwrap()

    async def nfl_v3_pbp_play_by_play_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay2:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_pbp_play_by_play_live_final(
                format, gameid, request_options=request_options
            )
        ).unwrap()

    async def nfl_v3_pbp_play_by_play_delta(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayByPlay2]:
        """This method returns all play-by-plays for a given season and week, but only returnsplays that have changed in
        the last X minutes as specified in your API call. by definition this is a live endpoint, not final.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br> <code>1</code> or <code>2</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_pbp_play_by_play_delta(
                format, season, week, minutes, request_options=request_options
            )
        ).unwrap()

    async def nfl_v3_pbp_play_by_play_simulation(
        self, format: FormatOrStr, numberofplays: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayByPlay2]:
        """Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21,
        2018.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.nfl_v3_pbp_play_by_play_simulation(
                format, numberofplays, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNflV3PlayByPlayWithRawResponse:
        return self._with_raw_response


class NflV3PlayByPlayWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfl_v3_pbp_play_by_play_by_team_final(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        hometeam: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlayByPlay2, NflV3PbpPlayByPlayByTeamFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayFinal/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay2],
            error_mapper=nfl_v3_pbp_play_by_play_by_team_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_by_team_live_final(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        hometeam: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlayByPlay2, NflV3PbpPlayByPlayByTeamLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlay/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay2],
            error_mapper=nfl_v3_pbp_play_by_play_by_team_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay2, NflV3PbpPlayByPlayFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay2],
            error_mapper=nfl_v3_pbp_play_by_play_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay2, NflV3PbpPlayByPlayLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlay/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay2],
            error_mapper=nfl_v3_pbp_play_by_play_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_delta(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayByPlay2], NflV3PbpPlayByPlayDeltaErrorBody]:
        """This method returns all play-by-plays for a given season and week, but only returnsplays that have changed in
        the last X minutes as specified in your API call. by definition this is a live endpoint, not final.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br> <code>1</code> or <code>2</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayDelta/{season}/{week}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay2]],
            error_mapper=nfl_v3_pbp_play_by_play_delta_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_simulation(
        self, format: FormatOrStr, numberofplays: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayByPlay2], NflV3PbpPlayByPlaySimulationErrorBody]:
        """Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21,
        2018.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/SimulatedPlayByPlay/{numberofplays}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("numberofplays", numberofplays)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay2]],
            error_mapper=nfl_v3_pbp_play_by_play_simulation_error_mapper,
            request_options=request_options,
        )


class AsyncNflV3PlayByPlayWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfl_v3_pbp_play_by_play_by_team_final(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        hometeam: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlayByPlay2, NflV3PbpPlayByPlayByTeamFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayFinal/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay2],
            error_mapper=nfl_v3_pbp_play_by_play_by_team_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_by_team_live_final(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        hometeam: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlayByPlay2, NflV3PbpPlayByPlayByTeamLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlay/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay2],
            error_mapper=nfl_v3_pbp_play_by_play_by_team_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay2, NflV3PbpPlayByPlayFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay2],
            error_mapper=nfl_v3_pbp_play_by_play_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay2, NflV3PbpPlayByPlayLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlay/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay2],
            error_mapper=nfl_v3_pbp_play_by_play_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_delta(
        self,
        format: FormatOrStr,
        season: str,
        week: str,
        minutes: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayByPlay2], NflV3PbpPlayByPlayDeltaErrorBody]:
        """This method returns all play-by-plays for a given season and week, but only returnsplays that have changed in
        the last X minutes as specified in your API call. by definition this is a live endpoint, not final.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br> <code>1</code> or <code>2</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayDelta/{season}/{week}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay2]],
            error_mapper=nfl_v3_pbp_play_by_play_delta_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_simulation(
        self, format: FormatOrStr, numberofplays: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayByPlay2], NflV3PbpPlayByPlaySimulationErrorBody]:
        """Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21,
        2018.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/SimulatedPlayByPlay/{numberofplays}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("numberofplays", numberofplays)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay2]],
            error_mapper=nfl_v3_pbp_play_by_play_simulation_error_mapper,
            request_options=request_options,
        )
