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
from ..errors.nfl_v3_stats_box_score_by_team_final_error import (
    NflV3StatsBoxScoreByTeamFinalErrorBody,
    nfl_v3_stats_box_score_by_team_final_error_mapper,
)
from ..errors.nfl_v3_stats_box_score_by_team_live_final_error import (
    NflV3StatsBoxScoreByTeamLiveFinalErrorBody,
    nfl_v3_stats_box_score_by_team_live_final_error_mapper,
)
from ..errors.nfl_v3_stats_box_score_final_error import (
    NflV3StatsBoxScoreFinalErrorBody,
    nfl_v3_stats_box_score_final_error_mapper,
)
from ..errors.nfl_v3_stats_box_score_live_final_error import (
    NflV3StatsBoxScoreLiveFinalErrorBody,
    nfl_v3_stats_box_score_live_final_error_mapper,
)
from ..errors.nfl_v3_stats_box_scores_by_week_final_error import (
    NflV3StatsBoxScoresByWeekFinalErrorBody,
    nfl_v3_stats_box_scores_by_week_final_error_mapper,
)
from ..errors.nfl_v3_stats_box_scores_delta_by_week_error import (
    NflV3StatsBoxScoresDeltaByWeekErrorBody,
    nfl_v3_stats_box_scores_delta_by_week_error_mapper,
)
from ..errors.nfl_v3_stats_box_scores_simulation_error import (
    NflV3StatsBoxScoresSimulationErrorBody,
    nfl_v3_stats_box_scores_simulation_error_mapper,
)
from ..errors.nfl_v3_stats_fantasy_defense_game_stats_all_error import (
    NflV3StatsFantasyDefenseGameStatsAllErrorBody,
    nfl_v3_stats_fantasy_defense_game_stats_all_error_mapper,
)
from ..errors.nfl_v3_stats_fantasy_defense_game_stats_by_team_error import (
    NflV3StatsFantasyDefenseGameStatsByTeamErrorBody,
    nfl_v3_stats_fantasy_defense_game_stats_by_team_error_mapper,
)
from ..errors.nfl_v3_stats_fantasy_defense_season_stats_all_error import (
    NflV3StatsFantasyDefenseSeasonStatsAllErrorBody,
    nfl_v3_stats_fantasy_defense_season_stats_all_error_mapper,
)
from ..errors.nfl_v3_stats_fantasy_defense_season_stats_by_team_error import (
    NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody,
    nfl_v3_stats_fantasy_defense_season_stats_by_team_error_mapper,
)
from ..errors.nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week_error import (
    NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody,
    nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week_error_mapper,
)
from ..errors.nfl_v3_stats_fantasy_points_by_week_error import (
    NflV3StatsFantasyPointsByWeekErrorBody,
    nfl_v3_stats_fantasy_points_by_week_error_mapper,
)
from ..errors.nfl_v3_stats_games_by_season_final_error import (
    NflV3StatsGamesBySeasonFinalErrorBody,
    nfl_v3_stats_games_by_season_final_error_mapper,
)
from ..errors.nfl_v3_stats_injuries_all_error import (
    NflV3StatsInjuriesAllErrorBody,
    nfl_v3_stats_injuries_all_error_mapper,
)
from ..errors.nfl_v3_stats_injuries_by_team_error import (
    NflV3StatsInjuriesByTeamErrorBody,
    nfl_v3_stats_injuries_by_team_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_logs_by_season_error import (
    NflV3StatsPlayerGameLogsBySeasonErrorBody,
    nfl_v3_stats_player_game_logs_by_season_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_red_zone_stats_error import (
    NflV3StatsPlayerGameRedZoneStatsErrorBody,
    nfl_v3_stats_player_game_red_zone_stats_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_red_zone_stats_inside_five_error import (
    NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody,
    nfl_v3_stats_player_game_red_zone_stats_inside_five_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_red_zone_stats_inside_ten_error import (
    NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody,
    nfl_v3_stats_player_game_red_zone_stats_inside_ten_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_stats_by_team_final_error import (
    NflV3StatsPlayerGameStatsByTeamFinalErrorBody,
    nfl_v3_stats_player_game_stats_by_team_final_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_stats_by_team_live_final_error import (
    NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody,
    nfl_v3_stats_player_game_stats_by_team_live_final_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_stats_by_week_final_error import (
    NflV3StatsPlayerGameStatsByWeekFinalErrorBody,
    nfl_v3_stats_player_game_stats_by_week_final_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_stats_by_week_live_final_error import (
    NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody,
    nfl_v3_stats_player_game_stats_by_week_live_final_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_stats_delta_by_week_error import (
    NflV3StatsPlayerGameStatsDeltaByWeekErrorBody,
    nfl_v3_stats_player_game_stats_delta_by_week_error_mapper,
)
from ..errors.nfl_v3_stats_player_game_stats_delta_error import (
    NflV3StatsPlayerGameStatsDeltaErrorBody,
    nfl_v3_stats_player_game_stats_delta_error_mapper,
)
from ..errors.nfl_v3_stats_player_season_red_zone_stats_error import (
    NflV3StatsPlayerSeasonRedZoneStatsErrorBody,
    nfl_v3_stats_player_season_red_zone_stats_error_mapper,
)
from ..errors.nfl_v3_stats_player_season_red_zone_stats_inside_five_error import (
    NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody,
    nfl_v3_stats_player_season_red_zone_stats_inside_five_error_mapper,
)
from ..errors.nfl_v3_stats_player_season_red_zone_stats_inside_ten_error import (
    NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody,
    nfl_v3_stats_player_season_red_zone_stats_inside_ten_error_mapper,
)
from ..errors.nfl_v3_stats_player_season_stats_by_team_error import (
    NflV3StatsPlayerSeasonStatsByTeamErrorBody,
    nfl_v3_stats_player_season_stats_by_team_error_mapper,
)
from ..errors.nfl_v3_stats_player_season_stats_error import (
    NflV3StatsPlayerSeasonStatsErrorBody,
    nfl_v3_stats_player_season_stats_error_mapper,
)
from ..errors.nfl_v3_stats_player_season_third_down_stats_error import (
    NflV3StatsPlayerSeasonThirdDownStatsErrorBody,
    nfl_v3_stats_player_season_third_down_stats_error_mapper,
)
from ..errors.nfl_v3_stats_pro_bowlers_error import NflV3StatsProBowlersErrorBody, nfl_v3_stats_pro_bowlers_error_mapper
from ..errors.nfl_v3_stats_team_game_stats_by_game_final_error import (
    NflV3StatsTeamGameStatsByGameFinalErrorBody,
    nfl_v3_stats_team_game_stats_by_game_final_error_mapper,
)
from ..models.box_score_v3 import BoxScoreV3
from ..models.enums.format import Format, FormatOrStr
from ..models.enums.playerstoinclude import Playerstoinclude, PlayerstoincludeOrStr
from ..models.fantasy_defense_game import FantasyDefenseGame
from ..models.fantasy_defense_season import FantasyDefenseSeason
from ..models.fantasy_game import FantasyGame
from ..models.injury import Injury
from ..models.player_game import PlayerGame
from ..models.player_game_red_zone import PlayerGameRedZone
from ..models.player_info import PlayerInfo
from ..models.player_ownership import PlayerOwnership
from ..models.player_season import PlayerSeason
from ..models.player_season_red_zone import PlayerSeasonRedZone
from ..models.player_season_third_down import PlayerSeasonThirdDown
from ..models.score import Score
from ..models.team_game import TeamGame
from ..server.server import Server


class NflV3Stats:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NflV3StatsWithRawResponse(client, server, auth)

    def nfl_v3_stats_box_score_by_team_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BoxScoreV3:
        """Full statistical information for a given team's game in a specified season and week, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of a team playing in this game. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_box_score_by_team_final(
                season, week, hometeam, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_box_score_by_team_live_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BoxScoreV3:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called for a given team's game in a given week and season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of a team playing in this game. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_box_score_by_team_live_final(
                season, week, hometeam, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_box_score_final(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScoreV3:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            scoreid: The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_box_score_final(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_box_score_live_final(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScoreV3:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            scoreid: The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_box_score_live_final(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_box_scores_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScoreV3]:
        """Full statistical information for a specified game week for each game that took place, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_box_scores_by_week_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_box_scores_delta_by_week(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        playerstoinclude: PlayerstoincludeOrStr = Playerstoinclude.ALL,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScoreV3]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. You can also filter by type of player stats to
        include, such as traditional fantasy players, IDP players or all players. by definition this is a live endpoint,
        not final.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br><code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            playerstoinclude: The subcategory of players to include in the returned PlayerGame records. Possible values
                include:<br><br> <code>all</code> Returns all players<br> <code>fantasy</code> Returns traditional
                fantasy players (QB, RB, WR, TE, K, DST)<br> <code>idp</code> Returns traditional fantasy players and
                IDP players.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_box_scores_delta_by_week(
                season,
                week,
                minutes,
                format_=format_,
                playerstoinclude=playerstoinclude,
                request_options=request_options,
            ),
        )

    def nfl_v3_stats_box_scores_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScoreV3]:
        """Gets simulated live box scores of NFL games, covering the Conference Championship games on January 21, 2018.

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
            self._with_raw_response.nfl_v3_stats_box_scores_simulation(
                numberofplays, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_fantasy_defense_game_stats_all(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FantasyDefenseGame]:
        """Returns stats and fantasy points for a given game for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_fantasy_defense_game_stats_all(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_fantasy_defense_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FantasyDefenseGame:
        """Returns stats and fantasy points for a given team's game for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_fantasy_defense_game_stats_by_team(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_fantasy_defense_season_stats_all(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyDefenseSeason]:
        """Returns stats and fantasy points for a given season for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_fantasy_defense_season_stats_all(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_fantasy_defense_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FantasyDefenseSeason:
        """Returns stats and fantasy points for a given team and season for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_fantasy_defense_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerOwnership]:
        """Projected fantasy ownership of all players for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_fantasy_points_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FantasyGame]:
        """Returns a simple list of fantasy points and stats for each player for a given week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_fantasy_points_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_games_by_season_final(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Score]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_games_by_season_final(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_injuries_all(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Injury]:
        """A list of all injured players and a description of their injuries.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_injuries_all(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_injuries_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Injury]:
        """A list of all injured players on a specified team and a description of their injuries.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_injuries_by_team(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>17920</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_red_zone_stats(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameRedZone]:
        """Delivers all offensive stats within the red zone (within the 20-yard line of the defensive team) for all
        players in a given season or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_game_red_zone_stats(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_red_zone_stats_inside_five(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameRedZone]:
        """Delivers all offensive stats within the 5-yard line of the defensive team for all players in a given season
        or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_game_red_zone_stats_inside_five(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_red_zone_stats_inside_ten(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameRedZone]:
        """Delivers all offensive stats within the 10-yard line of the defensive team for all players in a given season
        or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_game_red_zone_stats_inside_ten(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_stats_by_team_final(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Returns the box score statistical record for all involved players in a given team's game in a given week
        after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_game_stats_by_team_final(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_stats_by_team_live_final(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Returns the box score statistical record for all involved players across a given team's game in a given week,
        updated live as the game takes place.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_game_stats_by_team_live_final(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_stats_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Returns the box score statistical record for all involved players across all teams' games in a given week
        after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_game_stats_by_week_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_stats_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Returns the box score statistical record for all involved players across a given week, updated live as the
        game takes place.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_game_stats_by_week_live_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_stats_delta(
        self, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame]:
        """This method returns all player game stats, but only returns player stats that have changed in the last X
        minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
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
            self._with_raw_response.nfl_v3_stats_player_game_stats_delta(
                minutes, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_game_stats_delta_by_week(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """This method returns all player scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. Ideal for live applications.

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
            self._with_raw_response.nfl_v3_stats_player_game_stats_delta_by_week(
                season, week, minutes, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_season_red_zone_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonRedZone]:
        """Delivers all offensive stats within the red zone (within the 20-yard line of the defensive team) for all
        players in a given season (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_season_red_zone_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_season_red_zone_stats_inside_five(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonRedZone]:
        """Delivers all offensive stats within the 5-yard line of the defensive team for all players in a given season
        (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_season_red_zone_stats_inside_five(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_season_red_zone_stats_inside_ten(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonRedZone]:
        """Delivers all offensive stats within the 10-yard line of the defensive team for all players in a given season
        (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_season_red_zone_stats_inside_ten(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_player_season_third_down_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonThirdDown]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players on the
        third down for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_player_season_third_down_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_stats_pro_bowlers(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerInfo]:
        """A list of players involved in the Pro Bowl, by season.

        Args:
            season: Year of the season <br>Examples: <code>2016</code>, <code>2017</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_pro_bowlers(season, format_=format_, request_options=request_options)
        )

    def nfl_v3_stats_team_game_stats_by_game_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_stats_team_game_stats_by_game_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NflV3StatsWithRawResponse:
        return self._with_raw_response


class AsyncNflV3Stats:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNflV3StatsWithRawResponse(client, server, auth)

    async def nfl_v3_stats_box_score_by_team_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BoxScoreV3:
        """Full statistical information for a given team's game in a specified season and week, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of a team playing in this game. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_box_score_by_team_final(
                season, week, hometeam, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_box_score_by_team_live_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BoxScoreV3:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called for a given team's game in a given week and season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of a team playing in this game. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_box_score_by_team_live_final(
                season, week, hometeam, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_box_score_final(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScoreV3:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            scoreid: The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_box_score_final(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_box_score_live_final(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScoreV3:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            scoreid: The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_box_score_live_final(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_box_scores_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScoreV3]:
        """Full statistical information for a specified game week for each game that took place, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_box_scores_by_week_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_box_scores_delta_by_week(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        playerstoinclude: PlayerstoincludeOrStr = Playerstoinclude.ALL,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScoreV3]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. You can also filter by type of player stats to
        include, such as traditional fantasy players, IDP players or all players. by definition this is a live endpoint,
        not final.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br><code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            playerstoinclude: The subcategory of players to include in the returned PlayerGame records. Possible values
                include:<br><br> <code>all</code> Returns all players<br> <code>fantasy</code> Returns traditional
                fantasy players (QB, RB, WR, TE, K, DST)<br> <code>idp</code> Returns traditional fantasy players and
                IDP players.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_box_scores_delta_by_week(
                season,
                week,
                minutes,
                format_=format_,
                playerstoinclude=playerstoinclude,
                request_options=request_options,
            ),
        )

    async def nfl_v3_stats_box_scores_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BoxScoreV3]:
        """Gets simulated live box scores of NFL games, covering the Conference Championship games on January 21, 2018.

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
            await self._with_raw_response.nfl_v3_stats_box_scores_simulation(
                numberofplays, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_fantasy_defense_game_stats_all(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FantasyDefenseGame]:
        """Returns stats and fantasy points for a given game for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_fantasy_defense_game_stats_all(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_fantasy_defense_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FantasyDefenseGame:
        """Returns stats and fantasy points for a given team's game for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_fantasy_defense_game_stats_by_team(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_fantasy_defense_season_stats_all(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyDefenseSeason]:
        """Returns stats and fantasy points for a given season for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_fantasy_defense_season_stats_all(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_fantasy_defense_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FantasyDefenseSeason:
        """Returns stats and fantasy points for a given team and season for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_fantasy_defense_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerOwnership]:
        """Projected fantasy ownership of all players for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_fantasy_points_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FantasyGame]:
        """Returns a simple list of fantasy points and stats for each player for a given week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_fantasy_points_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_games_by_season_final(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Score]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_games_by_season_final(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_injuries_all(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Injury]:
        """A list of all injured players and a description of their injuries.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_injuries_all(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_injuries_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Injury]:
        """A list of all injured players on a specified team and a description of their injuries.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_injuries_by_team(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>17920</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_game_logs_by_season(
                season, playerid, numberofgames, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_red_zone_stats(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameRedZone]:
        """Delivers all offensive stats within the red zone (within the 20-yard line of the defensive team) for all
        players in a given season or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_game_red_zone_stats(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_red_zone_stats_inside_five(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameRedZone]:
        """Delivers all offensive stats within the 5-yard line of the defensive team for all players in a given season
        or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_game_red_zone_stats_inside_five(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_red_zone_stats_inside_ten(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameRedZone]:
        """Delivers all offensive stats within the 10-yard line of the defensive team for all players in a given season
        or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_game_red_zone_stats_inside_ten(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_stats_by_team_final(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Returns the box score statistical record for all involved players in a given team's game in a given week
        after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_game_stats_by_team_final(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_stats_by_team_live_final(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Returns the box score statistical record for all involved players across a given team's game in a given week,
        updated live as the game takes place.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_game_stats_by_team_live_final(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_stats_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Returns the box score statistical record for all involved players across all teams' games in a given week
        after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_game_stats_by_week_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_stats_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """Returns the box score statistical record for all involved players across a given week, updated live as the
        game takes place.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_game_stats_by_week_live_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_stats_delta(
        self, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerGame]:
        """This method returns all player game stats, but only returns player stats that have changed in the last X
        minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
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
            await self._with_raw_response.nfl_v3_stats_player_game_stats_delta(
                minutes, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_game_stats_delta_by_week(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGame]:
        """This method returns all player scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. Ideal for live applications.

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
            await self._with_raw_response.nfl_v3_stats_player_game_stats_delta_by_week(
                season, week, minutes, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_season_red_zone_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonRedZone]:
        """Delivers all offensive stats within the red zone (within the 20-yard line of the defensive team) for all
        players in a given season (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_season_red_zone_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_season_red_zone_stats_inside_five(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonRedZone]:
        """Delivers all offensive stats within the 5-yard line of the defensive team for all players in a given season
        (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_season_red_zone_stats_inside_five(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_season_red_zone_stats_inside_ten(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonRedZone]:
        """Delivers all offensive stats within the 10-yard line of the defensive team for all players in a given season
        (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_season_red_zone_stats_inside_ten(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_season_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeason]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_season_stats_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_player_season_third_down_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonThirdDown]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players on the
        third down for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_player_season_third_down_stats(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_pro_bowlers(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerInfo]:
        """A list of players involved in the Pro Bowl, by season.

        Args:
            season: Year of the season <br>Examples: <code>2016</code>, <code>2017</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_pro_bowlers(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_stats_team_game_stats_by_game_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_stats_team_game_stats_by_game_final(
                season, week, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNflV3StatsWithRawResponse:
        return self._with_raw_response


class NflV3StatsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfl_v3_stats_box_score_by_team_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BoxScoreV3, NflV3StatsBoxScoreByTeamFinalErrorBody]:
        """Full statistical information for a given team's game in a specified season and week, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of a team playing in this game. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoreByTeamFinal/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScoreV3],
            error_mapper=nfl_v3_stats_box_score_by_team_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_box_score_by_team_live_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BoxScoreV3, NflV3StatsBoxScoreByTeamLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called for a given team's game in a given week and season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of a team playing in this game. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoreV3/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScoreV3],
            error_mapper=nfl_v3_stats_box_score_by_team_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_box_score_final(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScoreV3, NflV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            scoreid: The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoreFinal/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScoreV3],
            error_mapper=nfl_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_box_score_live_final(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScoreV3, NflV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            scoreid: The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoreByScoreIDV3/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScoreV3],
            error_mapper=nfl_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_box_scores_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresByWeekFinalErrorBody]:
        """Full statistical information for a specified game week for each game that took place, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoresFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScoreV3]],
            error_mapper=nfl_v3_stats_box_scores_by_week_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_box_scores_delta_by_week(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        playerstoinclude: PlayerstoincludeOrStr = Playerstoinclude.ALL,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresDeltaByWeekErrorBody]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. You can also filter by type of player stats to
        include, such as traditional fantasy players, IDP players or all players. by definition this is a live endpoint,
        not final.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br><code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            playerstoinclude: The subcategory of players to include in the returned PlayerGame records. Possible values
                include:<br><br> <code>all</code> Returns all players<br> <code>fantasy</code> Returns traditional
                fantasy players (QB, RB, WR, TE, K, DST)<br> <code>idp</code> Returns traditional fantasy players and
                IDP players.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/BoxScoresDeltaV3/{season}/{week}/{playerstoinclude}/{minutes}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[PlayerstoincludeOrStr]("playerstoinclude", playerstoinclude),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScoreV3]],
            error_mapper=nfl_v3_stats_box_scores_delta_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_box_scores_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresSimulationErrorBody]:
        """Gets simulated live box scores of NFL games, covering the Conference Championship games on January 21, 2018.

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
            url_template=self._server.default("/v3/nfl/stats/{format}/SimulatedBoxScoresV3/{numberofplays}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("numberofplays", numberofplays)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScoreV3]],
            error_mapper=nfl_v3_stats_box_scores_simulation_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_fantasy_defense_game_stats_all(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[FantasyDefenseGame], NflV3StatsFantasyDefenseGameStatsAllErrorBody]:
        """Returns stats and fantasy points for a given game for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/FantasyDefenseByGame/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyDefenseGame]],
            error_mapper=nfl_v3_stats_fantasy_defense_game_stats_all_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_fantasy_defense_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FantasyDefenseGame, NflV3StatsFantasyDefenseGameStatsByTeamErrorBody]:
        """Returns stats and fantasy points for a given team's game for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/FantasyDefenseByGameByTeam/{season}/{week}/{team}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FantasyDefenseGame],
            error_mapper=nfl_v3_stats_fantasy_defense_game_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_fantasy_defense_season_stats_all(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FantasyDefenseSeason], NflV3StatsFantasyDefenseSeasonStatsAllErrorBody]:
        """Returns stats and fantasy points for a given season for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/FantasyDefenseBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyDefenseSeason]],
            error_mapper=nfl_v3_stats_fantasy_defense_season_stats_all_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_fantasy_defense_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FantasyDefenseSeason, NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody]:
        """Returns stats and fantasy points for a given team and season for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/FantasyDefenseBySeasonByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FantasyDefenseSeason],
            error_mapper=nfl_v3_stats_fantasy_defense_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerOwnership], NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody]:
        """Projected fantasy ownership of all players for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerOwnership/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerOwnership]],
            error_mapper=nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_fantasy_points_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[FantasyGame], NflV3StatsFantasyPointsByWeekErrorBody]:
        """Returns a simple list of fantasy points and stats for each player for a given week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/FantasyGameStatsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyGame]],
            error_mapper=nfl_v3_stats_fantasy_points_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_games_by_season_final(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Score], NflV3StatsGamesBySeasonFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/ScoresFinal/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Score]],
            error_mapper=nfl_v3_stats_games_by_season_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_injuries_all(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Injury], NflV3StatsInjuriesAllErrorBody]:
        """A list of all injured players and a description of their injuries.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/Injuries/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Injury]],
            error_mapper=nfl_v3_stats_injuries_all_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_injuries_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Injury], NflV3StatsInjuriesByTeamErrorBody]:
        """A list of all injured players on a specified team and a description of their injuries.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/Injuries/{season}/{week}/{team}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Injury]],
            error_mapper=nfl_v3_stats_injuries_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>17920</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_red_zone_stats(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsErrorBody]:
        """Delivers all offensive stats within the red zone (within the 20-yard line of the defensive team) for all
        players in a given season or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameRedZoneStats/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameRedZone]],
            error_mapper=nfl_v3_stats_player_game_red_zone_stats_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_red_zone_stats_inside_five(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody]:
        """Delivers all offensive stats within the 5-yard line of the defensive team for all players in a given season
        or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/PlayerGameRedZoneInsideFiveStats/{season}/{week}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameRedZone]],
            error_mapper=nfl_v3_stats_player_game_red_zone_stats_inside_five_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_red_zone_stats_inside_ten(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody]:
        """Delivers all offensive stats within the 10-yard line of the defensive team for all players in a given season
        or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameRedZoneInsideTenStats/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameRedZone]],
            error_mapper=nfl_v3_stats_player_game_red_zone_stats_inside_ten_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_stats_by_team_final(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByTeamFinalErrorBody]:
        """Returns the box score statistical record for all involved players in a given team's game in a given week
        after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/PlayerGameStatsByTeamFinal/{season}/{week}/{team}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_by_team_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_stats_by_team_live_final(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given team's game in a given week,
        updated live as the game takes place.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameStatsByTeam/{season}/{week}/{team}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_by_team_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_stats_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByWeekFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games in a given week
        after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameStatsByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_by_week_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_stats_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given week, updated live as the
        game takes place.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameStatsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_stats_delta(
        self, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsDeltaErrorBody]:
        """This method returns all player game stats, but only returns player stats that have changed in the last X
        minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameStatsDelta/{minutes}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("minutes", minutes)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_delta_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_game_stats_delta_by_week(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsDeltaByWeekErrorBody]:
        """This method returns all player scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. Ideal for live applications.

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
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/PlayerGameStatsByWeekDelta/{season}/{week}/{minutes}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_delta_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_season_red_zone_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsErrorBody]:
        """Delivers all offensive stats within the red zone (within the 20-yard line of the defensive team) for all
        players in a given season (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonRedZoneStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonRedZone]],
            error_mapper=nfl_v3_stats_player_season_red_zone_stats_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_season_red_zone_stats_inside_five(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody]:
        """Delivers all offensive stats within the 5-yard line of the defensive team for all players in a given season
        (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonRedZoneInsideFiveStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonRedZone]],
            error_mapper=nfl_v3_stats_player_season_red_zone_stats_inside_five_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_season_red_zone_stats_inside_ten(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody]:
        """Delivers all offensive stats within the 10-yard line of the defensive team for all players in a given season
        (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonRedZoneInsideTenStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonRedZone]],
            error_mapper=nfl_v3_stats_player_season_red_zone_stats_inside_ten_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason], NflV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason]],
            error_mapper=nfl_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason], NflV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason]],
            error_mapper=nfl_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_player_season_third_down_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonThirdDown], NflV3StatsPlayerSeasonThirdDownStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players on the
        third down for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonThirdDownStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonThirdDown]],
            error_mapper=nfl_v3_stats_player_season_third_down_stats_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_pro_bowlers(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerInfo], NflV3StatsProBowlersErrorBody]:
        """A list of players involved in the Pro Bowl, by season.

        Args:
            season: Year of the season <br>Examples: <code>2016</code>, <code>2017</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/ProBowlers/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerInfo]],
            error_mapper=nfl_v3_stats_pro_bowlers_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_stats_team_game_stats_by_game_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame], NflV3StatsTeamGameStatsByGameFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/TeamGameStatsFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame]],
            error_mapper=nfl_v3_stats_team_game_stats_by_game_final_error_mapper,
            request_options=request_options,
        )


class AsyncNflV3StatsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfl_v3_stats_box_score_by_team_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BoxScoreV3, NflV3StatsBoxScoreByTeamFinalErrorBody]:
        """Full statistical information for a given team's game in a specified season and week, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of a team playing in this game. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoreByTeamFinal/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScoreV3],
            error_mapper=nfl_v3_stats_box_score_by_team_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_box_score_by_team_live_final(
        self,
        season: str,
        week: str,
        hometeam: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BoxScoreV3, NflV3StatsBoxScoreByTeamLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called for a given team's game in a given week and season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            hometeam: Abbreviation of a team playing in this game. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoreV3/{season}/{week}/{hometeam}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("hometeam", hometeam),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScoreV3],
            error_mapper=nfl_v3_stats_box_score_by_team_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_box_score_final(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScoreV3, NflV3StatsBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            scoreid: The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoreFinal/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScoreV3],
            error_mapper=nfl_v3_stats_box_score_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_box_score_live_final(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScoreV3, NflV3StatsBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            scoreid: The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoreByScoreIDV3/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BoxScoreV3],
            error_mapper=nfl_v3_stats_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_box_scores_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresByWeekFinalErrorBody]:
        """Full statistical information for a specified game week for each game that took place, down to the team and
        player stat level, delivered after the game is complete.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/BoxScoresFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScoreV3]],
            error_mapper=nfl_v3_stats_box_scores_by_week_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_box_scores_delta_by_week(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        playerstoinclude: PlayerstoincludeOrStr = Playerstoinclude.ALL,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresDeltaByWeekErrorBody]:
        """This method returns all box scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. You can also filter by type of player stats to
        include, such as traditional fantasy players, IDP players or all players. by definition this is a live endpoint,
        not final.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are:<br><code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            playerstoinclude: The subcategory of players to include in the returned PlayerGame records. Possible values
                include:<br><br> <code>all</code> Returns all players<br> <code>fantasy</code> Returns traditional
                fantasy players (QB, RB, WR, TE, K, DST)<br> <code>idp</code> Returns traditional fantasy players and
                IDP players.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/BoxScoresDeltaV3/{season}/{week}/{playerstoinclude}/{minutes}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[PlayerstoincludeOrStr]("playerstoinclude", playerstoinclude),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScoreV3]],
            error_mapper=nfl_v3_stats_box_scores_delta_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_box_scores_simulation(
        self,
        numberofplays: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresSimulationErrorBody]:
        """Gets simulated live box scores of NFL games, covering the Conference Championship games on January 21, 2018.

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
            url_template=self._server.default("/v3/nfl/stats/{format}/SimulatedBoxScoresV3/{numberofplays}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("numberofplays", numberofplays)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BoxScoreV3]],
            error_mapper=nfl_v3_stats_box_scores_simulation_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_fantasy_defense_game_stats_all(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[FantasyDefenseGame], NflV3StatsFantasyDefenseGameStatsAllErrorBody]:
        """Returns stats and fantasy points for a given game for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/FantasyDefenseByGame/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyDefenseGame]],
            error_mapper=nfl_v3_stats_fantasy_defense_game_stats_all_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_fantasy_defense_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FantasyDefenseGame, NflV3StatsFantasyDefenseGameStatsByTeamErrorBody]:
        """Returns stats and fantasy points for a given team's game for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/FantasyDefenseByGameByTeam/{season}/{week}/{team}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[FantasyDefenseGame],
            error_mapper=nfl_v3_stats_fantasy_defense_game_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_fantasy_defense_season_stats_all(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FantasyDefenseSeason], NflV3StatsFantasyDefenseSeasonStatsAllErrorBody]:
        """Returns stats and fantasy points for a given season for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/FantasyDefenseBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyDefenseSeason]],
            error_mapper=nfl_v3_stats_fantasy_defense_season_stats_all_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_fantasy_defense_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FantasyDefenseSeason, NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody]:
        """Returns stats and fantasy points for a given team and season for the fantasy defense team (not IDP.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/FantasyDefenseBySeasonByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[FantasyDefenseSeason],
            error_mapper=nfl_v3_stats_fantasy_defense_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerOwnership], NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody]:
        """Projected fantasy ownership of all players for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerOwnership/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerOwnership]],
            error_mapper=nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_fantasy_points_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[FantasyGame], NflV3StatsFantasyPointsByWeekErrorBody]:
        """Returns a simple list of fantasy points and stats for each player for a given week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/FantasyGameStatsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyGame]],
            error_mapper=nfl_v3_stats_fantasy_points_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_games_by_season_final(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Score], NflV3StatsGamesBySeasonFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/ScoresFinal/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Score]],
            error_mapper=nfl_v3_stats_games_by_season_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_injuries_all(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Injury], NflV3StatsInjuriesAllErrorBody]:
        """A list of all injured players and a description of their injuries.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/Injuries/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Injury]],
            error_mapper=nfl_v3_stats_injuries_all_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_injuries_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Injury], NflV3StatsInjuriesByTeamErrorBody]:
        """A list of all injured players on a specified team and a description of their injuries.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/Injuries/{season}/{week}/{team}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Injury]],
            error_mapper=nfl_v3_stats_injuries_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_logs_by_season(
        self,
        season: str,
        playerid: str,
        numberofgames: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameLogsBySeasonErrorBody]:
        """Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their
        box score logs. Refreshed after their most recent game is complete.

        Args:
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            playerid: Unique SportsDataIO Player ID. Example:<code>17920</code>.
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("playerid", playerid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_red_zone_stats(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsErrorBody]:
        """Delivers all offensive stats within the red zone (within the 20-yard line of the defensive team) for all
        players in a given season or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameRedZoneStats/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameRedZone]],
            error_mapper=nfl_v3_stats_player_game_red_zone_stats_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_red_zone_stats_inside_five(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody]:
        """Delivers all offensive stats within the 5-yard line of the defensive team for all players in a given season
        or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/PlayerGameRedZoneInsideFiveStats/{season}/{week}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameRedZone]],
            error_mapper=nfl_v3_stats_player_game_red_zone_stats_inside_five_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_red_zone_stats_inside_ten(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody]:
        """Delivers all offensive stats within the 10-yard line of the defensive team for all players in a given season
        or week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameRedZoneInsideTenStats/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameRedZone]],
            error_mapper=nfl_v3_stats_player_game_red_zone_stats_inside_ten_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_stats_by_team_final(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByTeamFinalErrorBody]:
        """Returns the box score statistical record for all involved players in a given team's game in a given week
        after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/PlayerGameStatsByTeamFinal/{season}/{week}/{team}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_by_team_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_stats_by_team_live_final(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given team's game in a given week,
        updated live as the game takes place.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameStatsByTeam/{season}/{week}/{team}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_by_team_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_stats_by_week_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByWeekFinalErrorBody]:
        """Returns the box score statistical record for all involved players across all teams' games in a given week
        after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameStatsByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_by_week_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_stats_by_week_live_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody]:
        """Returns the box score statistical record for all involved players across a given week, updated live as the
        game takes place.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameStatsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_stats_delta(
        self, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsDeltaErrorBody]:
        """This method returns all player game stats, but only returns player stats that have changed in the last X
        minutes as specified in your API call. By definition this is a live endpoint, not final.

        Args:
            minutes: Only returns player statistics that have changed in the last X minutes. You specify how many
                minutes in time to go back. Valid entries are: <code>1</code> or <code>2</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerGameStatsDelta/{minutes}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("minutes", minutes)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_delta_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_game_stats_delta_by_week(
        self,
        season: str,
        week: str,
        minutes: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsDeltaByWeekErrorBody]:
        """This method returns all player scores for a given season and week, but only returns player stats that have
        changed in the last X minutes as specified in your API call. Ideal for live applications.

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
            url_template=self._server.default(
                "/v3/nfl/stats/{format}/PlayerGameStatsByWeekDelta/{season}/{week}/{minutes}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("minutes", minutes),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGame]],
            error_mapper=nfl_v3_stats_player_game_stats_delta_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_season_red_zone_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsErrorBody]:
        """Delivers all offensive stats within the red zone (within the 20-yard line of the defensive team) for all
        players in a given season (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonRedZoneStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonRedZone]],
            error_mapper=nfl_v3_stats_player_season_red_zone_stats_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_season_red_zone_stats_inside_five(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody]:
        """Delivers all offensive stats within the 5-yard line of the defensive team for all players in a given season
        (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonRedZoneInsideFiveStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonRedZone]],
            error_mapper=nfl_v3_stats_player_season_red_zone_stats_inside_five_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_season_red_zone_stats_inside_ten(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody]:
        """Delivers all offensive stats within the 10-yard line of the defensive team for all players in a given season
        (i.e. the season total, not each individual game record.)

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonRedZoneInsideTenStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonRedZone]],
            error_mapper=nfl_v3_stats_player_season_red_zone_stats_inside_ten_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_season_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason], NflV3StatsPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason]],
            error_mapper=nfl_v3_stats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_season_stats_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeason], NflV3StatsPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's
        players in a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            team: Abbreviation of the team. Example: <code>WAS</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeason]],
            error_mapper=nfl_v3_stats_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_player_season_third_down_stats(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonThirdDown], NflV3StatsPlayerSeasonThirdDownStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players on the
        third down for a given season.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/PlayerSeasonThirdDownStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonThirdDown]],
            error_mapper=nfl_v3_stats_player_season_third_down_stats_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_pro_bowlers(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerInfo], NflV3StatsProBowlersErrorBody]:
        """A list of players involved in the Pro Bowl, by season.

        Args:
            season: Year of the season <br>Examples: <code>2016</code>, <code>2017</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/ProBowlers/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerInfo]],
            error_mapper=nfl_v3_stats_pro_bowlers_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_stats_team_game_stats_by_game_final(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame], NflV3StatsTeamGameStatsByGameFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a given team's game in a
        given week after the game has concluded.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/stats/{format}/TeamGameStatsFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame]],
            error_mapper=nfl_v3_stats_team_game_stats_by_game_final_error_mapper,
            request_options=request_options,
        )
