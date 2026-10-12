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
from ..models.enums.format import Format, FormatOrStr
from ..models.play_by_play import PlayByPlay
from ..server.server import Server


class NflV3PlayByPlay:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NflV3PlayByPlayWithRawResponse(client, server, auth)

    def nfl_v3_pbp_play_by_play_by_team_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_pbp_play_by_play_by_team_final(
                season, week, hometeam, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_pbp_play_by_play_by_team_live_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by team.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_pbp_play_by_play_by_team_live_final(
                season, week, hometeam, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_pbp_play_by_play_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_pbp_play_by_play_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_pbp_play_by_play_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_pbp_play_by_play_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_pbp_play_by_play_delta(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayByPlay]:
        """This method returns all play-by-plays for a given season and week, but only returnsplays that have changed in
        the last X minutes as specified in your API call. by definition this is a live endpoint, not final.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br> <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_pbp_play_by_play_delta(
                season, week, minutes, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_pbp_play_by_play_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayByPlay]:
        """Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21,
        2018.

        Args:
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_pbp_play_by_play_simulation(
                numberofplays, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NflV3PlayByPlayWithRawResponse:
        return self._with_raw_response


class AsyncNflV3PlayByPlay:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNflV3PlayByPlayWithRawResponse(client, server, auth)

    async def nfl_v3_pbp_play_by_play_by_team_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_pbp_play_by_play_by_team_final(
                season, week, hometeam, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_pbp_play_by_play_by_team_live_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by team.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_pbp_play_by_play_by_team_live_final(
                season, week, hometeam, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_pbp_play_by_play_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_pbp_play_by_play_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_pbp_play_by_play_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> PlayByPlay:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_pbp_play_by_play_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_pbp_play_by_play_delta(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayByPlay]:
        """This method returns all play-by-plays for a given season and week, but only returnsplays that have changed in
        the last X minutes as specified in your API call. by definition this is a live endpoint, not final.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br> <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_pbp_play_by_play_delta(
                season, week, minutes, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_pbp_play_by_play_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayByPlay]:
        """Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21,
        2018.

        Args:
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_pbp_play_by_play_simulation(
                numberofplays, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNflV3PlayByPlayWithRawResponse:
        return self._with_raw_response


class NflV3PlayByPlayWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfl_v3_pbp_play_by_play_by_team_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlayByPlay, NflV3PbpPlayByPlayByTeamFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayFinal/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay],
            error_mapper=nfl_v3_pbp_play_by_play_by_team_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_by_team_live_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlayByPlay, NflV3PbpPlayByPlayByTeamLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by team.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlay/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay],
            error_mapper=nfl_v3_pbp_play_by_play_by_team_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay, NflV3PbpPlayByPlayFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay],
            error_mapper=nfl_v3_pbp_play_by_play_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay, NflV3PbpPlayByPlayLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlay/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[PlayByPlay],
            error_mapper=nfl_v3_pbp_play_by_play_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_delta(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayByPlay], NflV3PbpPlayByPlayDeltaErrorBody]:
        """This method returns all play-by-plays for a given season and week, but only returnsplays that have changed in
        the last X minutes as specified in your API call. by definition this is a live endpoint, not final.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br> <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayDelta/{season}/{week}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay]],
            error_mapper=nfl_v3_pbp_play_by_play_delta_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_pbp_play_by_play_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayByPlay], NflV3PbpPlayByPlaySimulationErrorBody]:
        """Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21,
        2018.

        Args:
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/SimulatedPlayByPlay/{numberofplays}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("numberofplays", numberofplays)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayByPlay]],
            error_mapper=nfl_v3_pbp_play_by_play_simulation_error_mapper,
            request_options=request_options,
        )


class AsyncNflV3PlayByPlayWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfl_v3_pbp_play_by_play_by_team_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlayByPlay, NflV3PbpPlayByPlayByTeamFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayFinal/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[PlayByPlay],
            error_mapper=nfl_v3_pbp_play_by_play_by_team_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_by_team_live_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlayByPlay, NflV3PbpPlayByPlayByTeamLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by team.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of the home team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlay/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[PlayByPlay],
            error_mapper=nfl_v3_pbp_play_by_play_by_team_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay, NflV3PbpPlayByPlayFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered final (after the game ends), called by team.

        Args:
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[PlayByPlay],
            error_mapper=nfl_v3_pbp_play_by_play_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PlayByPlay, NflV3PbpPlayByPlayLiveFinalErrorBody]:
        """Each invididual play, its type and outcome, complete with player and team stats down to the play level,
        delivered live in real-time, called by game.

        Args:
            gameid: The GameID of a NFL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlay/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[PlayByPlay],
            error_mapper=nfl_v3_pbp_play_by_play_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_delta(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayByPlay], NflV3PbpPlayByPlayDeltaErrorBody]:
        """This method returns all play-by-plays for a given season and week, but only returnsplays that have changed in
        the last X minutes as specified in your API call. by definition this is a live endpoint, not final.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br> <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/PlayByPlayDelta/{season}/{week}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayByPlay]],
            error_mapper=nfl_v3_pbp_play_by_play_delta_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_pbp_play_by_play_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayByPlay], NflV3PbpPlayByPlaySimulationErrorBody]:
        """Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21,
        2018.

        Args:
            numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are
                <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/pbp/{format}/SimulatedPlayByPlay/{numberofplays}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("numberofplays", numberofplays)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayByPlay]],
            error_mapper=nfl_v3_pbp_play_by_play_simulation_error_mapper,
            request_options=request_options,
        )
