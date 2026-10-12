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
from ..errors.mlb_v3_stats_batter_vs_pitcher_stats_error import (
    MlbV3StatsBatterVsPitcherStatsErrorBody,
    mlb_v3_stats_batter_vs_pitcher_stats_error_mapper,
)
from ..errors.mlb_v3_stats_box_score_final_error import (
    MlbV3StatsBoxScoreFinalErrorBody,
    mlb_v3_stats_box_score_final_error_mapper,
)
from ..errors.mlb_v3_stats_box_score_live_final_error import (
    MlbV3StatsBoxScoreLiveFinalErrorBody,
    mlb_v3_stats_box_score_live_final_error_mapper,
)
from ..errors.mlb_v3_stats_box_scores_by_date_final_error import (
    MlbV3StatsBoxScoresByDateFinalErrorBody,
    mlb_v3_stats_box_scores_by_date_final_error_mapper,
)
from ..errors.mlb_v3_stats_box_scores_by_date_live_final_error import (
    MlbV3StatsBoxScoresByDateLiveFinalErrorBody,
    mlb_v3_stats_box_scores_by_date_live_final_error_mapper,
)
from ..errors.mlb_v3_stats_box_scores_delta_by_date_error import (
    MlbV3StatsBoxScoresDeltaByDateErrorBody,
    mlb_v3_stats_box_scores_delta_by_date_error_mapper,
)
from ..errors.mlb_v3_stats_fantasy_points_by_date_error import (
    MlbV3StatsFantasyPointsByDateErrorBody,
    mlb_v3_stats_fantasy_points_by_date_error_mapper,
)
from ..errors.mlb_v3_stats_player_game_logs_by_season_error import (
    MlbV3StatsPlayerGameLogsBySeasonErrorBody,
    mlb_v3_stats_player_game_logs_by_season_error_mapper,
)
from ..errors.mlb_v3_stats_player_game_stats_by_date_final_error import (
    MlbV3StatsPlayerGameStatsByDateFinalErrorBody,
    mlb_v3_stats_player_game_stats_by_date_final_error_mapper,
)
from ..errors.mlb_v3_stats_player_game_stats_by_date_live_final_error import (
    MlbV3StatsPlayerGameStatsByDateLiveFinalErrorBody,
    mlb_v3_stats_player_game_stats_by_date_live_final_error_mapper,
)
from ..errors.mlb_v3_stats_player_season_split_stats_error import (
    MlbV3StatsPlayerSeasonSplitStatsErrorBody,
    mlb_v3_stats_player_season_split_stats_error_mapper,
)
from ..errors.mlb_v3_stats_player_season_stats_by_away_error import (
    MlbV3StatsPlayerSeasonStatsByAwayErrorBody,
    mlb_v3_stats_player_season_stats_by_away_error_mapper,
)
from ..errors.mlb_v3_stats_player_season_stats_by_home_error import (
    MlbV3StatsPlayerSeasonStatsByHomeErrorBody,
    mlb_v3_stats_player_season_stats_by_home_error_mapper,
)
from ..errors.mlb_v3_stats_player_season_stats_by_team_error import (
    MlbV3StatsPlayerSeasonStatsByTeamErrorBody,
    mlb_v3_stats_player_season_stats_by_team_error_mapper,
)
from ..errors.mlb_v3_stats_player_season_stats_error import (
    MlbV3StatsPlayerSeasonStatsErrorBody,
    mlb_v3_stats_player_season_stats_error_mapper,
)
from ..errors.mlb_v3_stats_player_season_stats_split_by_team_error import (
    MlbV3StatsPlayerSeasonStatsSplitByTeamErrorBody,
    mlb_v3_stats_player_season_stats_split_by_team_error_mapper,
)
from ..errors.mlb_v3_stats_team_hitting_vs_starting_pitcher_error import (
    MlbV3StatsTeamHittingVsStartingPitcherErrorBody,
    mlb_v3_stats_team_hitting_vs_starting_pitcher_error_mapper,
)
from ..models.box_score1 import BoxScore1
from ..models.enums.format import Format, FormatOrStr
from ..models.enums.split import Split, SplitOrStr
from ..models.fantasy_game2 import FantasyGame2
from ..models.player_game2 import PlayerGame2
from ..models.player_season3 import PlayerSeason3
from ..server.server import Server


class MlbV3Stats:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MlbV3StatsWithRawResponse(client, server, auth)

    def mlb_v3_stats_batter_vs_pitcher_stats(
        self,
        hitterid: str,
        pitcherid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason3]:
        """Stat records for a given hitter and a given pitcher, called by PlayerId in both cases.

        Args:
            hitterid: Unique FantasyData Player ID. Example:<code>10000031</code>.
            pitcherid: Unique FantasyData Player ID. Example:<code>10000618</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_batter_vs_pitcher_stats(
                hitterid, pitcherid, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore1:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_box_score_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore1:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_box_score_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_box_scores_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_box_scores_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore1]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
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
            self._with_raw_response.mlb_v3_stats_box_scores_delta_by_date(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyGame2]:
        """Returns a simple list of fantasy points and stats for each player for a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_fantasy_points_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame2]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>10001365</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame2]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame2]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_season_split_stats(
        self,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        split: SplitOrStr = Split.L,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason3]:
        """All players' split stats for the season. Split stats are available for left, right, and switch-handed
        pitchers and hitters.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            split: The desired split of stats. Currently, we support vs. Left/Right/Switch handed pitchers/hitters.
                Possible values are: <code>L</code>, <code>R</code> and <code>S</code>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_season_split_stats(
                season, format_=format_, split=split, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason3]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_season_stats_by_away(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason3]:
        """All players' stats for the season taken only from their road games.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_season_stats_by_away(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_season_stats_by_home(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason3]:
        """All players' stats for the season taken only from their home games.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_season_stats_by_home(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason3]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_player_season_stats_split_by_team(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason3]:
        """All a given team's players' split stats for the season. Split stats are available for left, right, and
        switch-handed pitchers and hitters.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_player_season_stats_split_by_team(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_stats_team_hitting_vs_starting_pitcher(
        self,
        gameid: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason3]:
        """For a given game, returns a team's hitting record versus the projected or confirmed starting pitcher for the
        game in question.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_stats_team_hitting_vs_starting_pitcher(
                gameid, team, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> MlbV3StatsWithRawResponse:
        return self._with_raw_response


class AsyncMlbV3Stats:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMlbV3StatsWithRawResponse(client, server, auth)

    async def mlb_v3_stats_batter_vs_pitcher_stats(
        self,
        hitterid: str,
        pitcherid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason3]:
        """Stat records for a given hitter and a given pitcher, called by PlayerId in both cases.

        Args:
            hitterid: Unique FantasyData Player ID. Example:<code>10000031</code>.
            pitcherid: Unique FantasyData Player ID. Example:<code>10000618</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_batter_vs_pitcher_stats(
                hitterid, pitcherid, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore1:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_box_score_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore1:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_box_score_live_final(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_box_scores_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore1]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_box_scores_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScore1]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
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
            await self._with_raw_response.mlb_v3_stats_box_scores_delta_by_date(
                date, minutes, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyGame2]:
        """Returns a simple list of fantasy points and stats for each player for a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_fantasy_points_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame2]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>10001365</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame2]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_game_stats_by_date_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame2]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_game_stats_by_date_live_final(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_season_split_stats(
        self,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        split: SplitOrStr = Split.L,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason3]:
        """All players' split stats for the season. Split stats are available for left, right, and switch-handed
        pitchers and hitters.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            split: The desired split of stats. Currently, we support vs. Left/Right/Switch handed pitchers/hitters.
                Possible values are: <code>L</code>, <code>R</code> and <code>S</code>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_season_split_stats(
                season, format_=format_, split=split, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason3]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_season_stats_by_away(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason3]:
        """All players' stats for the season taken only from their road games.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_season_stats_by_away(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_season_stats_by_home(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason3]:
        """All players' stats for the season taken only from their home games.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_season_stats_by_home(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason3]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_player_season_stats_split_by_team(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason3]:
        """All a given team's players' split stats for the season. Split stats are available for left, right, and
        switch-handed pitchers and hitters.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_player_season_stats_split_by_team(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_stats_team_hitting_vs_starting_pitcher(
        self,
        gameid: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason3]:
        """For a given game, returns a team's hitting record versus the projected or confirmed starting pitcher for the
        game in question.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_stats_team_hitting_vs_starting_pitcher(
                gameid, team, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncMlbV3StatsWithRawResponse:
        return self._with_raw_response


class MlbV3StatsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mlb_v3_stats_batter_vs_pitcher_stats(
        self,
        hitterid: str,
        pitcherid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsBatterVsPitcherStatsErrorBody]:
        """Stat records for a given hitter and a given pitcher, called by PlayerId in both cases.

        Args:
            hitterid: Unique FantasyData Player ID. Example:<code>10000031</code>.
            pitcherid: Unique FantasyData Player ID. Example:<code>10000618</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/HitterVsPitcher/{hitterid}/{pitcherid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("hitterid", hitterid),
                param[str]("pitcherid", pitcherid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_batter_vs_pitcher_stats_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore1, MlbV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore1],
            error_mapper=mlb_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore1, MlbV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore1],
            error_mapper=mlb_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], MlbV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=mlb_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], MlbV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=mlb_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore1], MlbV3StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScoresDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore1]],
            error_mapper=mlb_v3_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FantasyGame2], MlbV3StatsFantasyPointsByDateErrorBody]:
        """Returns a simple list of fantasy points and stats for each player for a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/FantasyGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyGame2]],
            error_mapper=mlb_v3_stats_fantasy_points_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>10001365</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame2]],
            error_mapper=mlb_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame2]],
            error_mapper=mlb_v3_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame2]],
            error_mapper=mlb_v3_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_season_split_stats(
        self,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        split: SplitOrStr = Split.L,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonSplitStatsErrorBody]:
        """All players' split stats for the season. Split stats are available for left, right, and switch-handed
        pitchers and hitters.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            split: The desired split of stats. Currently, we support vs. Left/Right/Switch handed pitchers/hitters.
                Possible values are: <code>L</code>, <code>R</code> and <code>S</code>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonSplitStats/{season}/{split}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("season", season), param[SplitOrStr]("split", split)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_split_stats_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_season_stats_by_away(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByAwayErrorBody]:
        """All players' stats for the season taken only from their road games.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonAwayStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_by_away_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_season_stats_by_home(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByHomeErrorBody]:
        """All players' stats for the season taken only from their home games.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonHomeStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_by_home_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_player_season_stats_split_by_team(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsSplitByTeamErrorBody]:
        """All a given team's players' split stats for the season. Split stats are available for left, right, and
        switch-handed pitchers and hitters.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonStatsSplitByTeam/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_split_by_team_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_stats_team_hitting_vs_starting_pitcher(
        self,
        gameid: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsTeamHittingVsStartingPitcherErrorBody]:
        """For a given game, returns a team's hitting record versus the projected or confirmed starting pitcher for the
        game in question.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/TeamHittersVsPitcher/{gameid}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_team_hitting_vs_starting_pitcher_error_mapper,
            request_options=request_options,
        )


class AsyncMlbV3StatsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mlb_v3_stats_batter_vs_pitcher_stats(
        self,
        hitterid: str,
        pitcherid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsBatterVsPitcherStatsErrorBody]:
        """Stat records for a given hitter and a given pitcher, called by PlayerId in both cases.

        Args:
            hitterid: Unique FantasyData Player ID. Example:<code>10000031</code>.
            pitcherid: Unique FantasyData Player ID. Example:<code>10000618</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/HitterVsPitcher/{hitterid}/{pitcherid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("hitterid", hitterid),
                param[str]("pitcherid", pitcherid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_batter_vs_pitcher_stats_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_box_score_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore1, MlbV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScore1],
            error_mapper=mlb_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_box_score_live_final(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore1, MlbV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScore1],
            error_mapper=mlb_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_box_scores_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], MlbV3StatsBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore1]],
            error_mapper=mlb_v3_stats_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_box_scores_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore1], MlbV3StatsBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called for all games on a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore1]],
            error_mapper=mlb_v3_stats_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_box_scores_delta_by_date(
        self,
        date: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScore1], MlbV3StatsBoxScoresDeltaByDateErrorBody]:
        """This method returns all box scores for a given date, but only returns player stats that have changed in the
        last X minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code>, <code>2</code> ... <code>all</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/BoxScoresDelta/{date}/{minutes}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("date", date), param[str]("minutes", minutes)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScore1]],
            error_mapper=mlb_v3_stats_box_scores_delta_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_fantasy_points_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FantasyGame2], MlbV3StatsFantasyPointsByDateErrorBody]:
        """Returns a simple list of fantasy points and stats for each player for a given date.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/FantasyGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyGame2]],
            error_mapper=mlb_v3_stats_fantasy_points_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>10001365</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame2]],
            error_mapper=mlb_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_game_stats_by_date_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games on a given date
        after each game has concluded.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame2]],
            error_mapper=mlb_v3_stats_player_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_game_stats_by_date_live_final(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given date, updated live as the
        game takes place.

        Args:
            date: The date of the game(s). <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame2]],
            error_mapper=mlb_v3_stats_player_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_season_split_stats(
        self,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        split: SplitOrStr = Split.L,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonSplitStatsErrorBody]:
        """All players' split stats for the season. Split stats are available for left, right, and switch-handed
        pitchers and hitters.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            split: The desired split of stats. Currently, we support vs. Left/Right/Switch handed pitchers/hitters.
                Possible values are: <code>L</code>, <code>R</code> and <code>S</code>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonSplitStats/{season}/{split}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("season", season), param[SplitOrStr]("split", split)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_split_stats_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_season_stats_by_away(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByAwayErrorBody]:
        """All players' stats for the season taken only from their road games.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonAwayStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_by_away_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_season_stats_by_home(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByHomeErrorBody]:
        """All players' stats for the season taken only from their home games.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonHomeStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_by_home_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_player_season_stats_split_by_team(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsSplitByTeamErrorBody]:
        """All a given team's players' split stats for the season. Split stats are available for left, right, and
        switch-handed pitchers and hitters.

        Args:
            season: Year of the season. <br>Examples: <code>2017</code>, <code>2018</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/PlayerSeasonStatsSplitByTeam/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_player_season_stats_split_by_team_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_stats_team_hitting_vs_starting_pitcher(
        self,
        gameid: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason3], MlbV3StatsTeamHittingVsStartingPitcherErrorBody]:
        """For a given game, returns a team's hitting record versus the projected or confirmed starting pitcher for the
        game in question.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>14620</code> or <code>16905</code>
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/stats/{format}/TeamHittersVsPitcher/{gameid}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason3]],
            error_mapper=mlb_v3_stats_team_hitting_vs_starting_pitcher_error_mapper,
            request_options=request_options,
        )
