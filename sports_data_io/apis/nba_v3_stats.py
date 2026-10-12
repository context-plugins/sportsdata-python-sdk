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
from ..errors.nba_v3_stats_all_stars_error import NbaV3StatsAllStarsErrorBody, nba_v3_stats_all_stars_error_mapper
from ..errors.nba_v3_stats_box_score_final_error import (
    NbaV3StatsBoxScoreFinalErrorBody,
    nba_v3_stats_box_score_final_error_mapper,
)
from ..errors.nba_v3_stats_box_score_live_final_error import (
    NbaV3StatsBoxScoreLiveFinalErrorBody,
    nba_v3_stats_box_score_live_final_error_mapper,
)
from ..errors.nba_v3_stats_box_scores_by_date_final_error import (
    NbaV3StatsBoxScoresByDateFinalErrorBody,
    nba_v3_stats_box_scores_by_date_final_error_mapper,
)
from ..errors.nba_v3_stats_box_scores_by_date_live_final_error import (
    NbaV3StatsBoxScoresByDateLiveFinalErrorBody,
    nba_v3_stats_box_scores_by_date_live_final_error_mapper,
)
from ..errors.nba_v3_stats_box_scores_delta_by_date_error import (
    NbaV3StatsBoxScoresDeltaByDateErrorBody,
    nba_v3_stats_box_scores_delta_by_date_error_mapper,
)
from ..errors.nba_v3_stats_fantasy_points_by_date_error import (
    NbaV3StatsFantasyPointsByDateErrorBody,
    nba_v3_stats_fantasy_points_by_date_error_mapper,
)
from ..errors.nba_v3_stats_player_game_logs_by_season_error import (
    NbaV3StatsPlayerGameLogsBySeasonErrorBody,
    nba_v3_stats_player_game_logs_by_season_error_mapper,
)
from ..errors.nba_v3_stats_player_game_stats_by_date_final_error import (
    NbaV3StatsPlayerGameStatsByDateFinalErrorBody,
    nba_v3_stats_player_game_stats_by_date_final_error_mapper,
)
from ..errors.nba_v3_stats_player_game_stats_by_date_live_final_error import (
    NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody,
    nba_v3_stats_player_game_stats_by_date_live_final_error_mapper,
)
from ..errors.nba_v3_stats_player_season_stats_by_team_error import (
    NbaV3StatsPlayerSeasonStatsByTeamErrorBody,
    nba_v3_stats_player_season_stats_by_team_error_mapper,
)
from ..errors.nba_v3_stats_player_season_stats_error import (
    NbaV3StatsPlayerSeasonStatsErrorBody,
    nba_v3_stats_player_season_stats_error_mapper,
)
from ..errors.nba_v3_stats_team_game_stats_by_date_final_error import (
    NbaV3StatsTeamGameStatsByDateFinalErrorBody,
    nba_v3_stats_team_game_stats_by_date_final_error_mapper,
)
from ..errors.nba_v3_stats_team_stats_allowed_by_position_error import (
    NbaV3StatsTeamStatsAllowedByPositionErrorBody,
    nba_v3_stats_team_stats_allowed_by_position_error_mapper,
)
from ..models.box_score import BoxScore
from ..models.enums.format import Format, FormatOrStr
from ..models.fantasy_game1 import FantasyGame1
from ..models.player_game1 import PlayerGame1
from ..models.player_info import PlayerInfo
from ..models.player_season1 import PlayerSeason1
from ..models.team_game1 import TeamGame1
from ..models.team_season1 import TeamSeason1
from ..server.server import Server


class NbaV3Stats:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NbaV3StatsWithRawResponse(client, server, auth)

    def nba_v3_stats_all_stars(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerInfo]:
        """A list of players selected for the All-Star Game for a given season.

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
            self._with_raw_response.nba_v3_stats_all_stars(season, format_=format_, request_options=request_options)
        )

    def nba_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an NBA game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code>, <code>16905</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_box_score_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an NBA game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code>, <code>16905</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_box_score_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_box_scores_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_box_scores_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_box_scores_delta_by_date(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyGame1]:
        """A simple list of fantasy points scored for all players who took part in games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_fantasy_points_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame1]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>20000571</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame1]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_player_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame1]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_player_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

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
            self._with_raw_response.nba_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame1]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games on a given date,
        delivered as each game concludes.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nba_v3_stats_team_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nba_v3_stats_team_stats_allowed_by_position(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason1]:
        """For each team, deliveres a season total of statistical records for their opponents' positions (e.g. all field
        goals made against this team by Centers.)

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
            self._with_raw_response.nba_v3_stats_team_stats_allowed_by_position(
                season, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NbaV3StatsWithRawResponse:
        return self._with_raw_response


class AsyncNbaV3Stats:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNbaV3StatsWithRawResponse(client, server, auth)

    async def nba_v3_stats_all_stars(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerInfo]:
        """A list of players selected for the All-Star Game for a given season.

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
            await self._with_raw_response.nba_v3_stats_all_stars(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an NBA game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code>, <code>16905</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_box_score_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an NBA game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code>, <code>16905</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_box_score_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_box_scores_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_box_scores_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_box_scores_delta_by_date(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyGame1]:
        """A simple list of fantasy points scored for all players who took part in games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_fantasy_points_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame1]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>20000571</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame1]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_player_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame1]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_player_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

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
            await self._with_raw_response.nba_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame1]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games on a given date,
        delivered as each game concludes.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nba_v3_stats_team_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nba_v3_stats_team_stats_allowed_by_position(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason1]:
        """For each team, deliveres a season total of statistical records for their opponents' positions (e.g. all field
        goals made against this team by Centers.)

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
            await self._with_raw_response.nba_v3_stats_team_stats_allowed_by_position(
                season, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNbaV3StatsWithRawResponse:
        return self._with_raw_response


class NbaV3StatsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nba_v3_stats_all_stars(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerInfo], NbaV3StatsAllStarsErrorBody]:
        """A list of players selected for the All-Star Game for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/AllStars/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerInfo]],
            error_mapper=nba_v3_stats_all_stars_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore, NbaV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an NBA game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code>, <code>16905</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore],
            error_mapper=nba_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore, NbaV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an NBA game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code>, <code>16905</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore],
            error_mapper=nba_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore], NbaV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore]],
            error_mapper=nba_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore], NbaV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore]],
            error_mapper=nba_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore], NbaV3StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScoresDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore]],
            error_mapper=nba_v3_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FantasyGame1], NbaV3StatsFantasyPointsByDateErrorBody]:
        """A simple list of fantasy points scored for all players who took part in games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/FantasyGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyGame1]],
            error_mapper=nba_v3_stats_fantasy_points_by_date_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>20000571</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nba/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=nba_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/PlayerGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=nba_v3_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/PlayerGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame1]],
            error_mapper=nba_v3_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason1], NbaV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason1]],
            error_mapper=nba_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason1], NbaV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason1]],
            error_mapper=nba_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame1], NbaV3StatsTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games on a given date,
        delivered as each game concludes.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=nba_v3_stats_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nba_v3_stats_team_stats_allowed_by_position(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason1], NbaV3StatsTeamStatsAllowedByPositionErrorBody]:
        """For each team, deliveres a season total of statistical records for their opponents' positions (e.g. all field
        goals made against this team by Centers.)

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/TeamStatsAllowedByPosition/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason1]],
            error_mapper=nba_v3_stats_team_stats_allowed_by_position_error_mapper,
            request_options=request_options,
        )


class AsyncNbaV3StatsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nba_v3_stats_all_stars(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerInfo], NbaV3StatsAllStarsErrorBody]:
        """A list of players selected for the All-Star Game for a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/AllStars/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerInfo]],
            error_mapper=nba_v3_stats_all_stars_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore, NbaV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an NBA game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code>, <code>16905</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScore],
            error_mapper=nba_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore, NbaV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an NBA game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code>, <code>16905</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScore],
            error_mapper=nba_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore], NbaV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore]],
            error_mapper=nba_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore], NbaV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore]],
            error_mapper=nba_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore], NbaV3StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/BoxScoresDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore]],
            error_mapper=nba_v3_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FantasyGame1], NbaV3StatsFantasyPointsByDateErrorBody]:
        """A simple list of fantasy points scored for all players who took part in games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/FantasyGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyGame1]],
            error_mapper=nba_v3_stats_fantasy_points_by_date_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>20000571</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nba/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame1]],
            error_mapper=nba_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/PlayerGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame1]],
            error_mapper=nba_v3_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/PlayerGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame1]],
            error_mapper=nba_v3_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason1], NbaV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason1]],
            error_mapper=nba_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason1], NbaV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>MIA</code>, <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason1]],
            error_mapper=nba_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame1], NbaV3StatsTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games on a given date,
        delivered as each game concludes.

        Args:
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame1]],
            error_mapper=nba_v3_stats_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nba_v3_stats_team_stats_allowed_by_position(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason1], NbaV3StatsTeamStatsAllowedByPositionErrorBody]:
        """For each team, deliveres a season total of statistical records for their opponents' positions (e.g. all field
        goals made against this team by Centers.)

        Args:
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nba/stats/{format}/TeamStatsAllowedByPosition/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamSeason1]],
            error_mapper=nba_v3_stats_team_stats_allowed_by_position_error_mapper,
            request_options=request_options,
        )
