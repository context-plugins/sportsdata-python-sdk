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
from ..errors.cfb_v3_scores_are_games_in_progress_error import (
    CfbV3ScoresAreGamesInProgressErrorBody,
    cfb_v3_scores_are_games_in_progress_error_mapper,
)
from ..errors.cfb_v3_scores_conference_hierarchy_error import (
    CfbV3ScoresConferenceHierarchyErrorBody,
    cfb_v3_scores_conference_hierarchy_error_mapper,
)
from ..errors.cfb_v3_scores_games_basic_by_date_final_error import (
    CfbV3ScoresGamesBasicByDateFinalErrorBody,
    cfb_v3_scores_games_basic_by_date_final_error_mapper,
)
from ..errors.cfb_v3_scores_games_basic_by_date_live_final_error import (
    CfbV3ScoresGamesBasicByDateLiveFinalErrorBody,
    cfb_v3_scores_games_basic_by_date_live_final_error_mapper,
)
from ..errors.cfb_v3_scores_games_basic_by_week_final_error import (
    CfbV3ScoresGamesBasicByWeekFinalErrorBody,
    cfb_v3_scores_games_basic_by_week_final_error_mapper,
)
from ..errors.cfb_v3_scores_games_by_date_final_error import (
    CfbV3ScoresGamesByDateFinalErrorBody,
    cfb_v3_scores_games_by_date_final_error_mapper,
)
from ..errors.cfb_v3_scores_games_by_date_live_final_error import (
    CfbV3ScoresGamesByDateLiveFinalErrorBody,
    cfb_v3_scores_games_by_date_live_final_error_mapper,
)
from ..errors.cfb_v3_scores_games_by_week_final_error import (
    CfbV3ScoresGamesByWeekFinalErrorBody,
    cfb_v3_scores_games_by_week_final_error_mapper,
)
from ..errors.cfb_v3_scores_games_by_week_live_final_error import (
    CfbV3ScoresGamesByWeekLiveFinalErrorBody,
    cfb_v3_scores_games_by_week_live_final_error_mapper,
)
from ..errors.cfb_v3_scores_player_details_by_active2_error import (
    CfbV3ScoresPlayerDetailsByActive2ErrorBody,
    cfb_v3_scores_player_details_by_active2_error_mapper,
)
from ..errors.cfb_v3_scores_player_details_by_active_error import (
    CfbV3ScoresPlayerDetailsByActiveErrorBody,
    cfb_v3_scores_player_details_by_active_error_mapper,
)
from ..errors.cfb_v3_scores_player_details_by_injured_error import (
    CfbV3ScoresPlayerDetailsByInjuredErrorBody,
    cfb_v3_scores_player_details_by_injured_error_mapper,
)
from ..errors.cfb_v3_scores_player_details_by_team_error import (
    CfbV3ScoresPlayerDetailsByTeamErrorBody,
    cfb_v3_scores_player_details_by_team_error_mapper,
)
from ..errors.cfb_v3_scores_player_profiles_by_team_error import (
    CfbV3ScoresPlayerProfilesByTeamErrorBody,
    cfb_v3_scores_player_profiles_by_team_error_mapper,
)
from ..errors.cfb_v3_scores_schedules_basic_error import (
    CfbV3ScoresSchedulesBasicErrorBody,
    cfb_v3_scores_schedules_basic_error_mapper,
)
from ..errors.cfb_v3_scores_schedules_error import CfbV3ScoresSchedulesErrorBody, cfb_v3_scores_schedules_error_mapper
from ..errors.cfb_v3_scores_season_current_details_error import (
    CfbV3ScoresSeasonCurrentDetailsErrorBody,
    cfb_v3_scores_season_current_details_error_mapper,
)
from ..errors.cfb_v3_scores_season_current_error import (
    CfbV3ScoresSeasonCurrentErrorBody,
    cfb_v3_scores_season_current_error_mapper,
)
from ..errors.cfb_v3_scores_season_type_current_error import (
    CfbV3ScoresSeasonTypeCurrentErrorBody,
    cfb_v3_scores_season_type_current_error_mapper,
)
from ..errors.cfb_v3_scores_stadiums_error import CfbV3ScoresStadiumsErrorBody, cfb_v3_scores_stadiums_error_mapper
from ..errors.cfb_v3_scores_team_game_logs_by_season_error import (
    CfbV3ScoresTeamGameLogsBySeasonErrorBody,
    cfb_v3_scores_team_game_logs_by_season_error_mapper,
)
from ..errors.cfb_v3_scores_team_game_stats_by_week_live_final_error import (
    CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody,
    cfb_v3_scores_team_game_stats_by_week_live_final_error_mapper,
)
from ..errors.cfb_v3_scores_team_profiles_all_error import (
    CfbV3ScoresTeamProfilesAllErrorBody,
    cfb_v3_scores_team_profiles_all_error_mapper,
)
from ..errors.cfb_v3_scores_team_season_stats_standings_error import (
    CfbV3ScoresTeamSeasonStatsStandingsErrorBody,
    cfb_v3_scores_team_season_stats_standings_error_mapper,
)
from ..errors.cfb_v3_scores_teams_basic_all_error import (
    CfbV3ScoresTeamsBasicAllErrorBody,
    cfb_v3_scores_teams_basic_all_error_mapper,
)
from ..errors.cfb_v3_scores_week_current_error import (
    CfbV3ScoresWeekCurrentErrorBody,
    cfb_v3_scores_week_current_error_mapper,
)
from ..models.conference1 import Conference1
from ..models.enums.format import FormatOrStr
from ..models.game4 import Game4
from ..models.player1 import Player1
from ..models.player_basic1 import PlayerBasic1
from ..models.schedule_basic1 import ScheduleBasic1
from ..models.score_basic1 import ScoreBasic1
from ..models.season1 import Season1
from ..models.stadium1 import Stadium1
from ..models.team1 import Team1
from ..models.team_basic1 import TeamBasic1
from ..models.team_game1 import TeamGame1
from ..models.team_season1 import TeamSeason1
from ..server.server import Server


class CfbV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CfbV3ScoresWithRawResponse(client, server, auth)

    def cfb_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_are_games_in_progress(
            format, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_conference_hierarchy(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Conference1]:
        """A list of all conferences and their associated teams. Standings can be found here for each conference.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_conference_hierarchy(
            format, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Full scores and gameday info delivered live and post-game for a given date. Live data includes down and
        distance, as well as game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_games_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_games_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_games_by_week_final(
            format, season, week, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_games_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Full scores and gameday info delivered live and post-game for a given gameweek. Live data includes down and
        distance, as well as game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_games_by_week_live_final(
            format, season, week, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """This endpoint simply delivers quarter, clock, and total score live; no down and distance and no gameday info
        such as weather.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_games_basic_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_games_basic_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications,
        delivered as the game ends, called by week.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_games_basic_by_week_final(
            format, season, week, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications,
        delivered as the game ends, called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_games_basic_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_games_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_player_details_by_active(
            format, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_player_details_by_active2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_player_details_by_active2(
            format, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_player_details_by_injured(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """This endpoint provides all currently injured college football players, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_player_details_by_injured(
            format, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_player_details_by_team(
            format, team, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_player_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_player_profiles_by_team(
            format, team, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_schedules(format, season, request_options=request_options).unwrap()

    def cfb_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic1]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_schedules_basic(
            format, season, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> int:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_season_current(format, request_options=request_options).unwrap()

    def cfb_v3_scores_season_current_details(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Season1:
        """The current season year, its start and end years, season type, week etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_season_current_details(
            format, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_season_type_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> str | None:
        """The current type of season (e.g. REG, POST for regular or playoff.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_season_type_current(
            format, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium1]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_stadiums(format, request_options=request_options).unwrap()

    def cfb_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame1]:
        """Game by game log of total team statistics.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 1 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_team_game_logs_by_season(
            format, season, teamid, numberofgames, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_team_game_stats_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame1]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a all teams' games in a
        given week, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_team_game_stats_by_week_live_final(
            format, season, week, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team1]:
        """Full team information: team name, school and city, conference and division, and colors. Also contains basic
        fantasy info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current
        active status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_team_profiles_all(format, request_options=request_options).unwrap()

    def cfb_v3_scores_team_season_stats_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season. Also includes their standing information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_team_season_stats_standings(
            format, season, request_options=request_options
        ).unwrap()

    def cfb_v3_scores_teams_basic_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamBasic1]:
        """The most basic top-line team information, such as team name and city, conference and division, stadium ID,
        coach info, and team colors. Returns all teams regardless of current active status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_teams_basic_all(format, request_options=request_options).unwrap()

    def cfb_v3_scores_week_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Number of the current week of the season. This value usually changes on Saturday into Sunday overnight, but
        in the rare case of a rescheduled or special game with a non-standard gameday this could change.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.cfb_v3_scores_week_current(format, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CfbV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncCfbV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCfbV3ScoresWithRawResponse(client, server, auth)

    async def cfb_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_are_games_in_progress(format, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_conference_hierarchy(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Conference1]:
        """A list of all conferences and their associated teams. Standings can be found here for each conference.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_conference_hierarchy(format, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Full scores and gameday info delivered live and post-game for a given date. Live data includes down and
        distance, as well as game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_games_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_games_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_games_by_week_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_games_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Full scores and gameday info delivered live and post-game for a given gameweek. Live data includes down and
        distance, as well as game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_games_by_week_live_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """This endpoint simply delivers quarter, clock, and total score live; no down and distance and no gameday info
        such as weather.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_games_basic_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_games_basic_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications,
        delivered as the game ends, called by week.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_games_basic_by_week_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic1]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications,
        delivered as the game ends, called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_games_basic_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_games_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_player_details_by_active(
                format, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_player_details_by_active2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_player_details_by_active2(
                format, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_player_details_by_injured(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """This endpoint provides all currently injured college football players, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_player_details_by_injured(
                format, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player1]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_player_details_by_team(
                format, team, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_player_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic1]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_player_profiles_by_team(
                format, team, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game4]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_schedules(format, season, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic1]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_schedules_basic(format, season, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> int:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_season_current(format, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_season_current_details(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Season1:
        """The current season year, its start and end years, season type, week etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_season_current_details(format, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_season_type_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> str | None:
        """The current type of season (e.g. REG, POST for regular or playoff.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_season_type_current(format, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium1]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.cfb_v3_scores_stadiums(format, request_options=request_options)).unwrap()

    async def cfb_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame1]:
        """Game by game log of total team statistics.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 1 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_team_game_logs_by_season(
                format, season, teamid, numberofgames, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_team_game_stats_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame1]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a all teams' games in a
        given week, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_team_game_stats_by_week_live_final(
                format, season, week, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team1]:
        """Full team information: team name, school and city, conference and division, and colors. Also contains basic
        fantasy info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current
        active status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_team_profiles_all(format, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_team_season_stats_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season. Also includes their standing information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_team_season_stats_standings(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def cfb_v3_scores_teams_basic_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamBasic1]:
        """The most basic top-line team information, such as team name and city, conference and division, stadium ID,
        coach info, and team colors. Returns all teams regardless of current active status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_teams_basic_all(format, request_options=request_options)
        ).unwrap()

    async def cfb_v3_scores_week_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> int | None:
        """Number of the current week of the season. This value usually changes on Saturday into Sunday overnight, but
        in the rare case of a rescheduled or special game with a non-standard gameday this could change.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.cfb_v3_scores_week_current(format, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCfbV3ScoresWithRawResponse:
        return self._with_raw_response


class CfbV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cfb_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, CfbV3ScoresAreGamesInProgressErrorBody]:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=cfb_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_conference_hierarchy(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Conference1], CfbV3ScoresConferenceHierarchyErrorBody]:
        """A list of all conferences and their associated teams. Standings can be found here for each conference.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/LeagueHierarchy"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Conference1]],
            error_mapper=cfb_v3_scores_conference_hierarchy_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game for a given date. Live data includes down and
        distance, as well as game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_games_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresGamesByWeekFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/GamesByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_games_by_week_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_games_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresGamesByWeekLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game for a given gameweek. Live data includes down and
        distance, as well as game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/GamesByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_games_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers quarter, clock, and total score live; no down and distance and no gameday info
        such as weather.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic1]],
            error_mapper=cfb_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_games_basic_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByWeekFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications,
        delivered as the game ends, called by week.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/ScoresBasicFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic1]],
            error_mapper=cfb_v3_scores_games_basic_by_week_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications,
        delivered as the game ends, called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic1]],
            error_mapper=cfb_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=cfb_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_player_details_by_active2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], CfbV3ScoresPlayerDetailsByActive2ErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/PlayersByActive"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic1]],
            error_mapper=cfb_v3_scores_player_details_by_active2_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_player_details_by_injured(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured college football players, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=cfb_v3_scores_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=cfb_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_player_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], CfbV3ScoresPlayerProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic1]],
            error_mapper=cfb_v3_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic1], CfbV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic1]],
            error_mapper=cfb_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int, CfbV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int],
            error_mapper=cfb_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_season_current_details(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season1, CfbV3ScoresSeasonCurrentDetailsErrorBody]:
        """The current season year, its start and end years, season type, week etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/CurrentSeasonDetails"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season1],
            error_mapper=cfb_v3_scores_season_current_details_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_season_type_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[str | None, CfbV3ScoresSeasonTypeCurrentErrorBody]:
        """The current type of season (e.g. REG, POST for regular or playoff.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/CurrentSeasonType"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[str | None],
            error_mapper=cfb_v3_scores_season_type_current_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium1], CfbV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium1]],
            error_mapper=cfb_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame1], CfbV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game by game log of total team statistics.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 1 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=cfb_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_team_game_stats_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame1], CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a all teams' games in a
        given week, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/TeamGameStatsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=cfb_v3_scores_team_game_stats_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team1], CfbV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name, school and city, conference and division, and colors. Also contains basic
        fantasy info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current
        active status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Teams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team1]],
            error_mapper=cfb_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_team_season_stats_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason1], CfbV3ScoresTeamSeasonStatsStandingsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season. Also includes their standing information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason1]],
            error_mapper=cfb_v3_scores_team_season_stats_standings_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_teams_basic_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamBasic1], CfbV3ScoresTeamsBasicAllErrorBody]:
        """The most basic top-line team information, such as team name and city, conference and division, stadium ID,
        coach info, and team colors. Returns all teams regardless of current active status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/TeamsBasic"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamBasic1]],
            error_mapper=cfb_v3_scores_teams_basic_all_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_scores_week_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, CfbV3ScoresWeekCurrentErrorBody]:
        """Number of the current week of the season. This value usually changes on Saturday into Sunday overnight, but
        in the rare case of a rescheduled or special game with a non-standard gameday this could change.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/CurrentWeek"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int | None],
            error_mapper=cfb_v3_scores_week_current_error_mapper,
            request_options=request_options,
        )


class AsyncCfbV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cfb_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, CfbV3ScoresAreGamesInProgressErrorBody]:
        """Returns <code>true</code> if there is at least one game being played at the time of the request or
        <code>false</code> if there are none.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=cfb_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_conference_hierarchy(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Conference1], CfbV3ScoresConferenceHierarchyErrorBody]:
        """A list of all conferences and their associated teams. Standings can be found here for each conference.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/LeagueHierarchy"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Conference1]],
            error_mapper=cfb_v3_scores_conference_hierarchy_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game for a given date. Live data includes down and
        distance, as well as game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_games_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresGamesByWeekFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score, delivered as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/GamesByWeekFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_games_by_week_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_games_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresGamesByWeekLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game for a given gameweek. Live data includes down and
        distance, as well as game clock. Gameday info includes referee, weather, TV channel etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/GamesByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_games_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """This endpoint simply delivers quarter, clock, and total score live; no down and distance and no gameday info
        such as weather.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic1]],
            error_mapper=cfb_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_games_basic_by_week_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByWeekFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications,
        delivered as the game ends, called by week.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/ScoresBasicFinal/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic1]],
            error_mapper=cfb_v3_scores_games_basic_by_week_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications,
        delivered as the game ends, called by date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the games.<br>Examples: <code>2021-SEP-12</code>, <code>2021-NOV-28</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic1]],
            error_mapper=cfb_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, including weather, referee, infotainment odds, as well as all of the quarter
        scores and full-time score as the game ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2016-SEP-01</code>, <code>2017-SEP-10</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=cfb_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_player_details_by_active2(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], CfbV3ScoresPlayerDetailsByActive2ErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/PlayersByActive"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic1]],
            error_mapper=cfb_v3_scores_player_details_by_active2_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_player_details_by_injured(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured college football players, along with injury details.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=cfb_v3_scores_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player1]],
            error_mapper=cfb_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_player_profiles_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic1], CfbV3ScoresPlayerProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position,
        college, and current team (if attached to a team.) Specify a team tricode parameter to receive all players
        currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>SF</code>, <code>NYY</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/PlayersBasic/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic1]],
            error_mapper=cfb_v3_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game4], CfbV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Games/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game4]],
            error_mapper=cfb_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic1], CfbV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2018</code>,
                <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/SchedulesBasic/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic1]],
            error_mapper=cfb_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int, CfbV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int],
            error_mapper=cfb_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_season_current_details(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season1, CfbV3ScoresSeasonCurrentDetailsErrorBody]:
        """The current season year, its start and end years, season type, week etc.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/CurrentSeasonDetails"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season1],
            error_mapper=cfb_v3_scores_season_current_details_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_season_type_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[str | None, CfbV3ScoresSeasonTypeCurrentErrorBody]:
        """The current type of season (e.g. REG, POST for regular or playoff.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/CurrentSeasonType"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[str | None],
            error_mapper=cfb_v3_scores_season_type_current_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium1], CfbV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium1]],
            error_mapper=cfb_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_team_game_logs_by_season(
        self,
        format: FormatOrStr,
        season: str,
        teamid: str,
        numberofgames: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame1], CfbV3ScoresTeamGameLogsBySeasonErrorBody]:
        """Game by game log of total team statistics.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Season to get games from. Example <code>2019POST</code>, <code>2020</code>
            teamid: Unique ID of team. Example <code> 1 </code>
            numberofgames: How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("teamid", teamid),
                param[str]("numberofgames", numberofgames),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=cfb_v3_scores_team_game_logs_by_season_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_team_game_stats_by_week_live_final(
        self, format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame1], CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a all teams' games in a
        given week, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2015</code>, <code>2016</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/TeamGameStatsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame1]],
            error_mapper=cfb_v3_scores_team_game_stats_by_week_live_final_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team1], CfbV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name, school and city, conference and division, and colors. Also contains basic
        fantasy info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current
        active status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/Teams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team1]],
            error_mapper=cfb_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_team_season_stats_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason1], CfbV3ScoresTeamSeasonStatsStandingsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season. Also includes their standing information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2017</code>,
                <code>2017POST</code>, <code>2018</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason1]],
            error_mapper=cfb_v3_scores_team_season_stats_standings_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_teams_basic_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamBasic1], CfbV3ScoresTeamsBasicAllErrorBody]:
        """The most basic top-line team information, such as team name and city, conference and division, stadium ID,
        coach info, and team colors. Returns all teams regardless of current active status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/TeamsBasic"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamBasic1]],
            error_mapper=cfb_v3_scores_teams_basic_all_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_scores_week_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[int | None, CfbV3ScoresWeekCurrentErrorBody]:
        """Number of the current week of the season. This value usually changes on Saturday into Sunday overnight, but
        in the rare case of a rescheduled or special game with a non-standard gameday this could change.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/scores/{format}/CurrentWeek"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[int | None],
            error_mapper=cfb_v3_scores_week_current_error_mapper,
            request_options=request_options,
        )
