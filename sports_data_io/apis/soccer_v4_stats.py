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
from ..errors.soccer_v4_stats_box_score_final_error import (
    SoccerV4StatsBoxScoreFinalErrorBody,
    soccer_v4_stats_box_score_final_error_mapper,
)
from ..errors.soccer_v4_stats_box_score_live_final_error import (
    SoccerV4StatsBoxScoreLiveFinalErrorBody,
    soccer_v4_stats_box_score_live_final_error_mapper,
)
from ..errors.soccer_v4_stats_box_scores_by_date_final_error import (
    SoccerV4StatsBoxScoresByDateFinalErrorBody,
    soccer_v4_stats_box_scores_by_date_final_error_mapper,
)
from ..errors.soccer_v4_stats_box_scores_by_date_live_final_error import (
    SoccerV4StatsBoxScoresByDateLiveFinalErrorBody,
    soccer_v4_stats_box_scores_by_date_live_final_error_mapper,
)
from ..errors.soccer_v4_stats_box_scores_delta_by_date_error import (
    SoccerV4StatsBoxScoresDeltaByDateErrorBody,
    soccer_v4_stats_box_scores_delta_by_date_error_mapper,
)
from ..errors.soccer_v4_stats_fantasy_points_by_date_error import (
    SoccerV4StatsFantasyPointsByDateErrorBody,
    soccer_v4_stats_fantasy_points_by_date_error_mapper,
)
from ..errors.soccer_v4_stats_lineups_by_date_error import (
    SoccerV4StatsLineupsByDateErrorBody,
    soccer_v4_stats_lineups_by_date_error_mapper,
)
from ..errors.soccer_v4_stats_player_game_stats_by_date_final_error import (
    SoccerV4StatsPlayerGameStatsByDateFinalErrorBody,
    soccer_v4_stats_player_game_stats_by_date_final_error_mapper,
)
from ..errors.soccer_v4_stats_player_game_stats_by_date_live_final_error import (
    SoccerV4StatsPlayerGameStatsByDateLiveFinalErrorBody,
    soccer_v4_stats_player_game_stats_by_date_live_final_error_mapper,
)
from ..errors.soccer_v4_stats_player_season_stats_error import (
    SoccerV4StatsPlayerSeasonStatsErrorBody,
    soccer_v4_stats_player_season_stats_error_mapper,
)
from ..errors.soccer_v4_stats_team_game_stats_by_date_final_error import (
    SoccerV4StatsTeamGameStatsByDateFinalErrorBody,
    soccer_v4_stats_team_game_stats_by_date_final_error_mapper,
)
from ..models.box_score6 import BoxScore6
from ..models.enums.format import Format, FormatOrStr
from ..models.fantasy_game4 import FantasyGame4
from ..models.player_game7 import PlayerGame7
from ..models.player_game_basic import PlayerGameBasic
from ..models.round import Round
from ..models.team_game7 import TeamGame7
from ..server.server import Server


class SoccerV4Stats:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoccerV4StatsWithRawResponse(client, server, auth)

    def soccer_v4_stats_box_score_final(
        self,
        competition: str,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>702</code>, <code>1274</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_box_score_final(
                competition, gameid, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_box_score_live_final(
        self,
        competition: str,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>702</code>, <code>1274</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_box_score_live_final(
                competition, gameid, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_box_scores_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_box_scores_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_box_scores_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date within a competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_box_scores_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_box_scores_delta_by_date(
        self,
        competition: str,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """This method returns all box scores for a given date in a given competition, but only returns player stats
        that have changed in the last X minutes as specified in your API call. By definition this is a live endpoint,
        not final.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_box_scores_delta_by_date(
                competition, date, minutes, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_fantasy_points_by_date(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FantasyGame4]:
        """A simple list of fantasy points awarded to players who took part in a given competition's games on a given
        date.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_fantasy_points_by_date(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_lineups_by_date(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameBasic]:
        """Projected and confirmed starting XIs and substitute benches for a given competition on a given date.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_lineups_by_date(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_player_game_stats_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame7]:
        """Returns the box score statistical record for all involved players across all teams' games for a given
        competition on a given date after each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_player_game_stats_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_player_game_stats_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame7]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date in
        a given competition, both live and after each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_player_game_stats_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_player_season_stats(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Round]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_player_season_stats(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_stats_team_game_stats_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame7]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games in a given
        competition on a given date, updated as each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_stats_team_game_stats_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SoccerV4StatsWithRawResponse:
        return self._with_raw_response


class AsyncSoccerV4Stats:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoccerV4StatsWithRawResponse(client, server, auth)

    async def soccer_v4_stats_box_score_final(
        self,
        competition: str,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>702</code>, <code>1274</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_box_score_final(
                competition, gameid, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_box_score_live_final(
        self,
        competition: str,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>702</code>, <code>1274</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_box_score_live_final(
                competition, gameid, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_box_scores_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_box_scores_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_box_scores_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date within a competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_box_scores_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_box_scores_delta_by_date(
        self,
        competition: str,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore6]:
        """This method returns all box scores for a given date in a given competition, but only returns player stats
        that have changed in the last X minutes as specified in your API call. By definition this is a live endpoint,
        not final.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_box_scores_delta_by_date(
                competition, date, minutes, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_fantasy_points_by_date(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FantasyGame4]:
        """A simple list of fantasy points awarded to players who took part in a given competition's games on a given
        date.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_fantasy_points_by_date(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_lineups_by_date(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameBasic]:
        """Projected and confirmed starting XIs and substitute benches for a given competition on a given date.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_lineups_by_date(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_player_game_stats_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame7]:
        """Returns the box score statistical record for all involved players across all teams' games for a given
        competition on a given date after each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_player_game_stats_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_player_game_stats_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame7]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date in
        a given competition, both live and after each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_player_game_stats_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_player_season_stats(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Round]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_player_season_stats(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_stats_team_game_stats_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame7]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games in a given
        competition on a given date, updated as each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_stats_team_game_stats_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSoccerV4StatsWithRawResponse:
        return self._with_raw_response


class SoccerV4StatsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def soccer_v4_stats_box_score_final(
        self,
        competition: str,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>702</code>, <code>1274</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/BoxScoreFinal/{competition}/{gameid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_box_score_live_final(
        self,
        competition: str,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>702</code>, <code>1274</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/BoxScore/{competition}/{gameid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_box_scores_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/BoxScoresFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_box_scores_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date within a competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/BoxScoresByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_box_scores_delta_by_date(
        self,
        competition: str,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given date in a given competition, but only returns player stats
        that have changed in the last X minutes as specified in your API call. By definition this is a live endpoint,
        not final.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/stats/{format}/BoxScoresDeltaByDate/{competition}/{date}/{minutes}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("date", date),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_fantasy_points_by_date(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[FantasyGame4], SoccerV4StatsFantasyPointsByDateErrorBody]:
        """A simple list of fantasy points awarded to players who took part in a given competition's games on a given
        date.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/FantasyGameStatsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyGame4]],
            error_mapper=soccer_v4_stats_fantasy_points_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_lineups_by_date(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameBasic], SoccerV4StatsLineupsByDateErrorBody]:
        """Projected and confirmed starting XIs and substitute benches for a given competition on a given date.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/LineupsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameBasic]],
            error_mapper=soccer_v4_stats_lineups_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_player_game_stats_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame7], SoccerV4StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games for a given
        competition on a given date after each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/stats/{format}/PlayerGameStatsByDateFinal/{competition}/{date}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame7]],
            error_mapper=soccer_v4_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_player_game_stats_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame7], SoccerV4StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date in
        a given competition, both live and after each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/PlayerGameStatsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame7]],
            error_mapper=soccer_v4_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_player_season_stats(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Round], SoccerV4StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/PlayerSeasonStats/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round]],
            error_mapper=soccer_v4_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_stats_team_game_stats_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame7], SoccerV4StatsTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games in a given
        competition on a given date, updated as each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/stats/{format}/TeamGameStatsByDateFinal/{competition}/{date}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame7]],
            error_mapper=soccer_v4_stats_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )


class AsyncSoccerV4StatsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def soccer_v4_stats_box_score_final(
        self,
        competition: str,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>702</code>, <code>1274</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/BoxScoreFinal/{competition}/{gameid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_box_score_live_final(
        self,
        competition: str,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>702</code>, <code>1274</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/BoxScore/{competition}/{gameid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_box_scores_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/BoxScoresFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_box_scores_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date within a competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/BoxScoresByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_box_scores_delta_by_date(
        self,
        competition: str,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore6], SoccerV4StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given date in a given competition, but only returns player stats
        that have changed in the last X minutes as specified in your API call. By definition this is a live endpoint,
        not final.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/stats/{format}/BoxScoresDeltaByDate/{competition}/{date}/{minutes}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("date", date),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore6]],
            error_mapper=soccer_v4_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_fantasy_points_by_date(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[FantasyGame4], SoccerV4StatsFantasyPointsByDateErrorBody]:
        """A simple list of fantasy points awarded to players who took part in a given competition's games on a given
        date.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/FantasyGameStatsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyGame4]],
            error_mapper=soccer_v4_stats_fantasy_points_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_lineups_by_date(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameBasic], SoccerV4StatsLineupsByDateErrorBody]:
        """Projected and confirmed starting XIs and substitute benches for a given competition on a given date.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/LineupsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameBasic]],
            error_mapper=soccer_v4_stats_lineups_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_player_game_stats_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame7], SoccerV4StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games for a given
        competition on a given date after each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/stats/{format}/PlayerGameStatsByDateFinal/{competition}/{date}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame7]],
            error_mapper=soccer_v4_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_player_game_stats_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame7], SoccerV4StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date in
        a given competition, both live and after each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/PlayerGameStatsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame7]],
            error_mapper=soccer_v4_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_player_season_stats(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Round], SoccerV4StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/stats/{format}/PlayerSeasonStats/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Round]],
            error_mapper=soccer_v4_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_stats_team_game_stats_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame7], SoccerV4StatsTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games in a given
        competition on a given date, updated as each game has concluded.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/stats/{format}/TeamGameStatsByDateFinal/{competition}/{date}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame7]],
            error_mapper=soccer_v4_stats_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )
