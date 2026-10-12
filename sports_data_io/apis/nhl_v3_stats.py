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
from ..errors.nhl_v3_stats_box_score_final_error import (
    NhlV3StatsBoxScoreFinalErrorBody,
    nhl_v3_stats_box_score_final_error_mapper,
)
from ..errors.nhl_v3_stats_box_score_live_final_error import (
    NhlV3StatsBoxScoreLiveFinalErrorBody,
    nhl_v3_stats_box_score_live_final_error_mapper,
)
from ..errors.nhl_v3_stats_box_scores_by_date_final_error import (
    NhlV3StatsBoxScoresByDateFinalErrorBody,
    nhl_v3_stats_box_scores_by_date_final_error_mapper,
)
from ..errors.nhl_v3_stats_box_scores_by_date_live_final_error import (
    NhlV3StatsBoxScoresByDateLiveFinalErrorBody,
    nhl_v3_stats_box_scores_by_date_live_final_error_mapper,
)
from ..errors.nhl_v3_stats_box_scores_delta_by_date_error import (
    NhlV3StatsBoxScoresDeltaByDateErrorBody,
    nhl_v3_stats_box_scores_delta_by_date_error_mapper,
)
from ..errors.nhl_v3_stats_fantasy_points_by_date_error import (
    NhlV3StatsFantasyPointsByDateErrorBody,
    nhl_v3_stats_fantasy_points_by_date_error_mapper,
)
from ..errors.nhl_v3_stats_line_combinations_by_season_error import (
    NhlV3StatsLineCombinationsBySeasonErrorBody,
    nhl_v3_stats_line_combinations_by_season_error_mapper,
)
from ..errors.nhl_v3_stats_player_game_logs_by_season_error import (
    NhlV3StatsPlayerGameLogsBySeasonErrorBody,
    nhl_v3_stats_player_game_logs_by_season_error_mapper,
)
from ..errors.nhl_v3_stats_player_game_stats_by_date_final_error import (
    NhlV3StatsPlayerGameStatsByDateFinalErrorBody,
    nhl_v3_stats_player_game_stats_by_date_final_error_mapper,
)
from ..errors.nhl_v3_stats_player_game_stats_by_date_live_final_error import (
    NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody,
    nhl_v3_stats_player_game_stats_by_date_live_final_error_mapper,
)
from ..errors.nhl_v3_stats_player_season_stats_by_team_error import (
    NhlV3StatsPlayerSeasonStatsByTeamErrorBody,
    nhl_v3_stats_player_season_stats_by_team_error_mapper,
)
from ..errors.nhl_v3_stats_player_season_stats_error import (
    NhlV3StatsPlayerSeasonStatsErrorBody,
    nhl_v3_stats_player_season_stats_error_mapper,
)
from ..errors.nhl_v3_stats_team_game_stats_by_date_final_error import (
    NhlV3StatsTeamGameStatsByDateFinalErrorBody,
    nhl_v3_stats_team_game_stats_by_date_final_error_mapper,
)
from ..errors.nhl_v3_stats_team_stats_allowed_by_position_error import (
    NhlV3StatsTeamStatsAllowedByPositionErrorBody,
    nhl_v3_stats_team_stats_allowed_by_position_error_mapper,
)
from ..models.box_score2 import BoxScore2
from ..models.enums.format import Format, FormatOrStr
from ..models.fantasy_game3 import FantasyGame3
from ..models.player_game3 import PlayerGame3
from ..models.player_season4 import PlayerSeason4
from ..models.team_game3 import TeamGame3
from ..models.team_line import TeamLine
from ..models.team_season3 import TeamSeason3
from ..server.server import Server


class NhlV3Stats:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NhlV3StatsWithRawResponse(client, server, auth)

    def nhl_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore2:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_box_score_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore2:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_box_score_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore2]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_box_scores_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore2]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_box_scores_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore2]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
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
            self._with_raw_response.nhl_v3_stats_box_scores_delta_by_date(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyGame3]:
        """Simple fantasy points awarded to each player who took part in a game on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_fantasy_points_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_line_combinations_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamLine]:
        """The line combinations - groups of skaters that play together - ordered and given by season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_line_combinations_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame3]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>30000651</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame3]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_player_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame3]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_player_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason4]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason4]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame3]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week after the game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_team_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def nhl_v3_stats_team_stats_allowed_by_position(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason3]:
        """Aggregated season stats allowed by each team against a given position (e.g. C, LW.)

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nhl_v3_stats_team_stats_allowed_by_position(
                season, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NhlV3StatsWithRawResponse:
        return self._with_raw_response


class AsyncNhlV3Stats:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNhlV3StatsWithRawResponse(client, server, auth)

    async def nhl_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore2:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_box_score_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore2:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_box_score_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore2]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_box_scores_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore2]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_box_scores_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore2]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
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
            await self._with_raw_response.nhl_v3_stats_box_scores_delta_by_date(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyGame3]:
        """Simple fantasy points awarded to each player who took part in a game on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_fantasy_points_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_line_combinations_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamLine]:
        """The line combinations - groups of skaters that play together - ordered and given by season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_line_combinations_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame3]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>30000651</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame3]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_player_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame3]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_player_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason4]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason4]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame3]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week after the game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_team_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nhl_v3_stats_team_stats_allowed_by_position(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason3]:
        """Aggregated season stats allowed by each team against a given position (e.g. C, LW.)

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nhl_v3_stats_team_stats_allowed_by_position(
                season, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNhlV3StatsWithRawResponse:
        return self._with_raw_response


class NhlV3StatsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nhl_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore2, NhlV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore2],
            error_mapper=nhl_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore2, NhlV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore2],
            error_mapper=nhl_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore2], NhlV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore2]],
            error_mapper=nhl_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore2], NhlV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore2]],
            error_mapper=nhl_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore2], NhlV3StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScoresDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore2]],
            error_mapper=nhl_v3_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FantasyGame3], NhlV3StatsFantasyPointsByDateErrorBody]:
        """Simple fantasy points awarded to each player who took part in a game on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/FantasyGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyGame3]],
            error_mapper=nhl_v3_stats_fantasy_points_by_date_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_line_combinations_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamLine], NhlV3StatsLineCombinationsBySeasonErrorBody]:
        """The line combinations - groups of skaters that play together - ordered and given by season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/LinesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamLine]],
            error_mapper=nhl_v3_stats_line_combinations_by_season_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>30000651</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nhl/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame3]],
            error_mapper=nhl_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/PlayerGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame3]],
            error_mapper=nhl_v3_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/PlayerGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame3]],
            error_mapper=nhl_v3_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason4], NhlV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason4]],
            error_mapper=nhl_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason4], NhlV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason4]],
            error_mapper=nhl_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame3], NhlV3StatsTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week after the game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame3]],
            error_mapper=nhl_v3_stats_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def nhl_v3_stats_team_stats_allowed_by_position(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason3], NhlV3StatsTeamStatsAllowedByPositionErrorBody]:
        """Aggregated season stats allowed by each team against a given position (e.g. C, LW.)

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/TeamStatsAllowedByPosition/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason3]],
            error_mapper=nhl_v3_stats_team_stats_allowed_by_position_error_mapper,
            request_options=request_options,
        )


class AsyncNhlV3StatsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nhl_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore2, NhlV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScore2],
            error_mapper=nhl_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore2, NhlV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an NHL game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScore2],
            error_mapper=nhl_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore2], NhlV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore2]],
            error_mapper=nhl_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore2], NhlV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore2]],
            error_mapper=nhl_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore2], NhlV3StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/BoxScoresDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore2]],
            error_mapper=nhl_v3_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FantasyGame3], NhlV3StatsFantasyPointsByDateErrorBody]:
        """Simple fantasy points awarded to each player who took part in a game on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/FantasyGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyGame3]],
            error_mapper=nhl_v3_stats_fantasy_points_by_date_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_line_combinations_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamLine], NhlV3StatsLineCombinationsBySeasonErrorBody]:
        """The line combinations - groups of skaters that play together - ordered and given by season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/LinesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamLine]],
            error_mapper=nhl_v3_stats_line_combinations_by_season_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>30000651</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nhl/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame3]],
            error_mapper=nhl_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/PlayerGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame3]],
            error_mapper=nhl_v3_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-OCT-31</code>, <code>2018-FEB-15</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/PlayerGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame3]],
            error_mapper=nhl_v3_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason4], NhlV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason4]],
            error_mapper=nhl_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason4], NhlV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason4]],
            error_mapper=nhl_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_team_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame3], NhlV3StatsTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week after the game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-JAN-31</code>, <code>2017-OCT-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame3]],
            error_mapper=nhl_v3_stats_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def nhl_v3_stats_team_stats_allowed_by_position(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason3], NhlV3StatsTeamStatsAllowedByPositionErrorBody]:
        """Aggregated season stats allowed by each team against a given position (e.g. C, LW.)

        Args:
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nhl/stats/{format}/TeamStatsAllowedByPosition/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamSeason3]],
            error_mapper=nhl_v3_stats_team_stats_allowed_by_position_error_mapper,
            request_options=request_options,
        )
