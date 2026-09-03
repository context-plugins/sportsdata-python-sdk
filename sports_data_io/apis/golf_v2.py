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
from ..errors.golf_v2_courses_courses_error import GolfV2CoursesCoursesErrorBody, golf_v2_courses_courses_error_mapper
from ..errors.golf_v2_currentseason_season_current_error import (
    GolfV2CurrentseasonSeasonCurrentErrorBody,
    golf_v2_currentseason_season_current_error_mapper,
)
from ..errors.golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate_error import (
    GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody,
    golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate_error_mapper,
)
from ..errors.golf_v2_dfsslatesbytournament_dfs_slates_by_tournament_error import (
    GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody,
    golf_v2_dfsslatesbytournament_dfs_slates_by_tournament_error_mapper,
)
from ..errors.golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament_error import (
    GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody,
    golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament_error_mapper,
)
from ..errors.golf_v2_leaderboard_leaderboard_live_final_error import (
    GolfV2LeaderboardLeaderboardLiveFinalErrorBody,
    golf_v2_leaderboard_leaderboard_live_final_error_mapper,
)
from ..errors.golf_v2_leaderboardbasic_leaderboard_basic_error import (
    GolfV2LeaderboardbasicLeaderboardBasicErrorBody,
    golf_v2_leaderboardbasic_leaderboard_basic_error_mapper,
)
from ..errors.golf_v2_leaderboardbasicfinal_leaderboard_basic_final_error import (
    GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody,
    golf_v2_leaderboardbasicfinal_leaderboard_basic_final_error_mapper,
)
from ..errors.golf_v2_leaderboardfinal_leaderboard_final_error import (
    GolfV2LeaderboardfinalLeaderboardFinalErrorBody,
    golf_v2_leaderboardfinal_leaderboard_final_error_mapper,
)
from ..errors.golf_v2_news_news_error import GolfV2NewsNewsErrorBody, golf_v2_news_news_error_mapper
from ..errors.golf_v2_newsbydate_news_by_date_error import (
    GolfV2NewsbydateNewsByDateErrorBody,
    golf_v2_newsbydate_news_by_date_error_mapper,
)
from ..errors.golf_v2_player_player_error import GolfV2PlayerPlayerErrorBody, golf_v2_player_player_error_mapper
from ..errors.golf_v2_players_player_profiles_all_error import (
    GolfV2PlayersPlayerProfilesAllErrorBody,
    golf_v2_players_player_profiles_all_error_mapper,
)
from ..errors.golf_v2_playerseasonstats_player_season_stats_error import (
    GolfV2PlayerseasonstatsPlayerSeasonStatsErrorBody,
    golf_v2_playerseasonstats_player_season_stats_error_mapper,
)
from ..errors.golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final_error import (
    GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody,
    golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final_error_mapper,
)
from ..errors.golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final_error import (
    GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody,
    golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final_error_mapper,
)
from ..errors.golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament_error import (
    GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody,
    golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament_error_mapper,
)
from ..errors.golf_v2_playertournamentroundscores_scores_by_tournament_live_final_error import (
    GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody,
    golf_v2_playertournamentroundscores_scores_by_tournament_live_final_error_mapper,
)
from ..errors.golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final_error import (
    GolfV2PlayertournamentroundscoresfinalScoresByTournamentFinalErrorBody,
    golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final_error_mapper,
)
from ..errors.golf_v2_rankings_rankings_error import (
    GolfV2RankingsRankingsErrorBody,
    golf_v2_rankings_rankings_error_mapper,
)
from ..errors.golf_v2_tournaments_schedule_by_season_error import (
    GolfV2TournamentsScheduleBySeasonErrorBody,
    golf_v2_tournaments_schedule_by_season_error_mapper,
)
from ..errors.golf_v2_tournaments_schedules_error import (
    GolfV2TournamentsSchedulesErrorBody,
    golf_v2_tournaments_schedules_error_mapper,
)
from ..errors.golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming_error import (
    GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody,
    golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming_error_mapper,
)
from ..models.courses import Courses
from ..models.dfs_slate2 import DfsSlate2
from ..models.dfs_slate_with_ownership_projection import DfsSlateWithOwnershipProjection
from ..models.enums.format import FormatOrStr
from ..models.fantasy_tournament import FantasyTournament
from ..models.leaderboard import Leaderboard
from ..models.leaderboard_basic import LeaderboardBasic
from ..models.news2 import News2
from ..models.player8 import Player8
from ..models.player_season9 import PlayerSeason9
from ..models.player_tournament_basic import PlayerTournamentBasic
from ..models.player_tournament_projection import PlayerTournamentProjection
from ..models.season7 import Season7
from ..models.tournament1 import Tournament1
from ..models.tournament_round import TournamentRound
from ..server.server import Server


class GolfV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GolfV2WithRawResponse(client, server, auth)

    def golf_v2_courses_courses(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Courses]:
        """Courses

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_courses_courses(format, request_options=request_options).unwrap()

    def golf_v2_currentseason_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Season7:
        """Season Current

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_currentseason_season_current(
            format, request_options=request_options
        ).unwrap()

    def golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate(
        self, format: FormatOrStr, slate_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> DfsSlateWithOwnershipProjection:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate(
            format, slate_id, request_options=request_options
        ).unwrap()

    def golf_v2_dfsslatesbytournament_dfs_slates_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate2]:
        """DFS Slates - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_dfsslatesbytournament_dfs_slates_by_tournament(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FantasyTournament:
        """Fantasy Points - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_leaderboard_leaderboard_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Leaderboard:
        """Leaderboard [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_leaderboard_leaderboard_live_final(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_leaderboardbasic_leaderboard_basic(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LeaderboardBasic:
        """Leaderboard (Basic)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_leaderboardbasic_leaderboard_basic(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_leaderboardbasicfinal_leaderboard_basic_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LeaderboardBasic:
        """Leaderboard (Basic) [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_leaderboardbasicfinal_leaderboard_basic_final(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_leaderboardfinal_leaderboard_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Leaderboard:
        """Leaderboard [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_leaderboardfinal_leaderboard_final(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_news_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_news_news(format, request_options=request_options).unwrap()

    def golf_v2_newsbydate_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_newsbydate_news_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def golf_v2_player_player(
        self, format: FormatOrStr, playerid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Player8:
        """Player

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            playerid: Unique FantasyData Player ID. Example:<code>40000019</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_player_player(format, playerid, request_options=request_options).unwrap()

    def golf_v2_players_player_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player8]:
        """Player Profiles - All

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_players_player_profiles_all(
            format, request_options=request_options
        ).unwrap()

    def golf_v2_playerseasonstats_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason9]:
        """Player Season Stats

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_playerseasonstats_player_season_stats(
            format, season, request_options=request_options
        ).unwrap()

    def golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerTournamentBasic]:
        """Player Hole Scores - by Tournament [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerTournamentBasic]:
        """Player Hole Scores - by Tournament [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerTournamentProjection]:
        """Player Projected Stats - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_playertournamentroundscores_scores_by_tournament_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TournamentRound]:
        """Scores - by Tournament [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_playertournamentroundscores_scores_by_tournament_live_final(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TournamentRound]:
        """Scores - by Tournament [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v2_rankings_rankings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason9]:
        """Rankings

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_rankings_rankings(
            format, season, request_options=request_options
        ).unwrap()

    def golf_v2_tournaments_schedule_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Tournament1]:
        """Schedule - by Season

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_tournaments_schedule_by_season(
            format, season, request_options=request_options
        ).unwrap()

    def golf_v2_tournaments_schedules(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Tournament1]:
        """Schedules

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_tournaments_schedules(format, request_options=request_options).unwrap()

    def golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlateWithOwnershipProjection]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming(
            format, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> GolfV2WithRawResponse:
        return self._with_raw_response


class AsyncGolfV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGolfV2WithRawResponse(client, server, auth)

    async def golf_v2_courses_courses(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Courses]:
        """Courses

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.golf_v2_courses_courses(format, request_options=request_options)).unwrap()

    async def golf_v2_currentseason_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Season7:
        """Season Current

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_currentseason_season_current(format, request_options=request_options)
        ).unwrap()

    async def golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate(
        self, format: FormatOrStr, slate_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> DfsSlateWithOwnershipProjection:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate(
                format, slate_id, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_dfsslatesbytournament_dfs_slates_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate2]:
        """DFS Slates - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_dfsslatesbytournament_dfs_slates_by_tournament(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FantasyTournament:
        """Fantasy Points - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_leaderboard_leaderboard_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Leaderboard:
        """Leaderboard [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_leaderboard_leaderboard_live_final(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_leaderboardbasic_leaderboard_basic(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LeaderboardBasic:
        """Leaderboard (Basic)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_leaderboardbasic_leaderboard_basic(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_leaderboardbasicfinal_leaderboard_basic_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LeaderboardBasic:
        """Leaderboard (Basic) [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_leaderboardbasicfinal_leaderboard_basic_final(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_leaderboardfinal_leaderboard_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Leaderboard:
        """Leaderboard [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_leaderboardfinal_leaderboard_final(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_news_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.golf_v2_news_news(format, request_options=request_options)).unwrap()

    async def golf_v2_newsbydate_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[News2]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_newsbydate_news_by_date(format, date, request_options=request_options)
        ).unwrap()

    async def golf_v2_player_player(
        self, format: FormatOrStr, playerid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Player8:
        """Player

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            playerid: Unique FantasyData Player ID. Example:<code>40000019</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_player_player(format, playerid, request_options=request_options)
        ).unwrap()

    async def golf_v2_players_player_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player8]:
        """Player Profiles - All

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_players_player_profiles_all(format, request_options=request_options)
        ).unwrap()

    async def golf_v2_playerseasonstats_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason9]:
        """Player Season Stats

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_playerseasonstats_player_season_stats(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerTournamentBasic]:
        """Player Hole Scores - by Tournament [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerTournamentBasic]:
        """Player Hole Scores - by Tournament [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerTournamentProjection]:
        """Player Projected Stats - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_playertournamentroundscores_scores_by_tournament_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TournamentRound]:
        """Scores - by Tournament [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_playertournamentroundscores_scores_by_tournament_live_final(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TournamentRound]:
        """Scores - by Tournament [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_rankings_rankings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason9]:
        """Rankings

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_rankings_rankings(format, season, request_options=request_options)
        ).unwrap()

    async def golf_v2_tournaments_schedule_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Tournament1]:
        """Schedule - by Season

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_tournaments_schedule_by_season(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def golf_v2_tournaments_schedules(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Tournament1]:
        """Schedules

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_tournaments_schedules(format, request_options=request_options)
        ).unwrap()

    async def golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlateWithOwnershipProjection]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming(
                format, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncGolfV2WithRawResponse:
        return self._with_raw_response


class GolfV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def golf_v2_courses_courses(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Courses], GolfV2CoursesCoursesErrorBody]:
        """Courses

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Courses"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Courses]],
            error_mapper=golf_v2_courses_courses_error_mapper,
            request_options=request_options,
        )

    def golf_v2_currentseason_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season7, GolfV2CurrentseasonSeasonCurrentErrorBody]:
        """Season Current

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season7],
            error_mapper=golf_v2_currentseason_season_current_error_mapper,
            request_options=request_options,
        )

    def golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate(
        self, format: FormatOrStr, slate_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        DfsSlateWithOwnershipProjection,
        GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody,
    ]:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}"),
            path_params=[param[FormatOrStr]("format", format), param[int]("slateId", slate_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[DfsSlateWithOwnershipProjection],
            error_mapper=golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate_error_mapper,
            request_options=request_options,
        )

    def golf_v2_dfsslatesbytournament_dfs_slates_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate2], GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody]:
        """DFS Slates - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/DfsSlatesByTournament/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate2]],
            error_mapper=golf_v2_dfsslatesbytournament_dfs_slates_by_tournament_error_mapper,
            request_options=request_options,
        )

    def golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FantasyTournament, GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody]:
        """Fantasy Points - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/FantasyGameStatsByTournament/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FantasyTournament],
            error_mapper=golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament_error_mapper,
            request_options=request_options,
        )

    def golf_v2_leaderboard_leaderboard_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Leaderboard, GolfV2LeaderboardLeaderboardLiveFinalErrorBody]:
        """Leaderboard [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Leaderboard/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Leaderboard],
            error_mapper=golf_v2_leaderboard_leaderboard_live_final_error_mapper,
            request_options=request_options,
        )

    def golf_v2_leaderboardbasic_leaderboard_basic(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LeaderboardBasic, GolfV2LeaderboardbasicLeaderboardBasicErrorBody]:
        """Leaderboard (Basic)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/LeaderboardBasic/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[LeaderboardBasic],
            error_mapper=golf_v2_leaderboardbasic_leaderboard_basic_error_mapper,
            request_options=request_options,
        )

    def golf_v2_leaderboardbasicfinal_leaderboard_basic_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LeaderboardBasic, GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody]:
        """Leaderboard (Basic) [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/LeaderboardBasicFinal/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[LeaderboardBasic],
            error_mapper=golf_v2_leaderboardbasicfinal_leaderboard_basic_final_error_mapper,
            request_options=request_options,
        )

    def golf_v2_leaderboardfinal_leaderboard_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Leaderboard, GolfV2LeaderboardfinalLeaderboardFinalErrorBody]:
        """Leaderboard [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/LeaderboardFinal/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Leaderboard],
            error_mapper=golf_v2_leaderboardfinal_leaderboard_final_error_mapper,
            request_options=request_options,
        )

    def golf_v2_news_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], GolfV2NewsNewsErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/News"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=golf_v2_news_news_error_mapper,
            request_options=request_options,
        )

    def golf_v2_newsbydate_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], GolfV2NewsbydateNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=golf_v2_newsbydate_news_by_date_error_mapper,
            request_options=request_options,
        )

    def golf_v2_player_player(
        self, format: FormatOrStr, playerid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Player8, GolfV2PlayerPlayerErrorBody]:
        """Player

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            playerid: Unique FantasyData Player ID. Example:<code>40000019</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Player/{playerid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("playerid", playerid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Player8],
            error_mapper=golf_v2_player_player_error_mapper,
            request_options=request_options,
        )

    def golf_v2_players_player_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player8], GolfV2PlayersPlayerProfilesAllErrorBody]:
        """Player Profiles - All

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player8]],
            error_mapper=golf_v2_players_player_profiles_all_error_mapper,
            request_options=request_options,
        )

    def golf_v2_playerseasonstats_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason9], GolfV2PlayerseasonstatsPlayerSeasonStatsErrorBody]:
        """Player Season Stats

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason9]],
            error_mapper=golf_v2_playerseasonstats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[PlayerTournamentBasic], GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody
    ]:
        """Player Hole Scores - by Tournament [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentHoleScores/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerTournamentBasic]],
            error_mapper=golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final_error_mapper,
            request_options=request_options,
        )

    def golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[PlayerTournamentBasic], GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody
    ]:
        """Player Hole Scores - by Tournament [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentHoleScoresFinal/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerTournamentBasic]],
            error_mapper=golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final_error_mapper,
            request_options=request_options,
        )

    def golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[PlayerTournamentProjection], GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody
    ]:
        """Player Projected Stats - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentProjectionStats/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerTournamentProjection]],
            error_mapper=golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament_error_mapper,
            request_options=request_options,
        )

    def golf_v2_playertournamentroundscores_scores_by_tournament_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TournamentRound], GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody]:
        """Scores - by Tournament [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentRoundScores/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TournamentRound]],
            error_mapper=golf_v2_playertournamentroundscores_scores_by_tournament_live_final_error_mapper,
            request_options=request_options,
        )

    def golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TournamentRound], GolfV2PlayertournamentroundscoresfinalScoresByTournamentFinalErrorBody]:
        """Scores - by Tournament [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentRoundScoresFinal/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TournamentRound]],
            error_mapper=golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final_error_mapper,
            request_options=request_options,
        )

    def golf_v2_rankings_rankings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason9], GolfV2RankingsRankingsErrorBody]:
        """Rankings

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Rankings/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason9]],
            error_mapper=golf_v2_rankings_rankings_error_mapper,
            request_options=request_options,
        )

    def golf_v2_tournaments_schedule_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Tournament1], GolfV2TournamentsScheduleBySeasonErrorBody]:
        """Schedule - by Season

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Tournaments/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Tournament1]],
            error_mapper=golf_v2_tournaments_schedule_by_season_error_mapper,
            request_options=request_options,
        )

    def golf_v2_tournaments_schedules(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Tournament1], GolfV2TournamentsSchedulesErrorBody]:
        """Schedules

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Tournaments"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Tournament1]],
            error_mapper=golf_v2_tournaments_schedules_error_mapper,
            request_options=request_options,
        )

    def golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[DfsSlateWithOwnershipProjection],
        GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody,
    ]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/UpcomingDfsSlateOwnershipProjections"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlateWithOwnershipProjection]],
            error_mapper=golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming_error_mapper,
            request_options=request_options,
        )


class AsyncGolfV2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def golf_v2_courses_courses(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Courses], GolfV2CoursesCoursesErrorBody]:
        """Courses

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Courses"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Courses]],
            error_mapper=golf_v2_courses_courses_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_currentseason_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season7, GolfV2CurrentseasonSeasonCurrentErrorBody]:
        """Season Current

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season7],
            error_mapper=golf_v2_currentseason_season_current_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate(
        self, format: FormatOrStr, slate_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        DfsSlateWithOwnershipProjection,
        GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody,
    ]:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}"),
            path_params=[param[FormatOrStr]("format", format), param[int]("slateId", slate_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[DfsSlateWithOwnershipProjection],
            error_mapper=golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_dfsslatesbytournament_dfs_slates_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate2], GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody]:
        """DFS Slates - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/DfsSlatesByTournament/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate2]],
            error_mapper=golf_v2_dfsslatesbytournament_dfs_slates_by_tournament_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FantasyTournament, GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody]:
        """Fantasy Points - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/FantasyGameStatsByTournament/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[FantasyTournament],
            error_mapper=golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_leaderboard_leaderboard_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Leaderboard, GolfV2LeaderboardLeaderboardLiveFinalErrorBody]:
        """Leaderboard [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Leaderboard/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Leaderboard],
            error_mapper=golf_v2_leaderboard_leaderboard_live_final_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_leaderboardbasic_leaderboard_basic(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LeaderboardBasic, GolfV2LeaderboardbasicLeaderboardBasicErrorBody]:
        """Leaderboard (Basic)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/LeaderboardBasic/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[LeaderboardBasic],
            error_mapper=golf_v2_leaderboardbasic_leaderboard_basic_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_leaderboardbasicfinal_leaderboard_basic_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LeaderboardBasic, GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody]:
        """Leaderboard (Basic) [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/LeaderboardBasicFinal/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[LeaderboardBasic],
            error_mapper=golf_v2_leaderboardbasicfinal_leaderboard_basic_final_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_leaderboardfinal_leaderboard_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Leaderboard, GolfV2LeaderboardfinalLeaderboardFinalErrorBody]:
        """Leaderboard [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/LeaderboardFinal/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Leaderboard],
            error_mapper=golf_v2_leaderboardfinal_leaderboard_final_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_news_news(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], GolfV2NewsNewsErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/News"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=golf_v2_news_news_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_newsbydate_news_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[News2], GolfV2NewsbydateNewsByDateErrorBody]:
        """Basic RotoBaller news feed, with limited stories available - usually 0-1 stories per day. Ideal for test
        purposes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2015-JUL-31</code>, <code>2015-SEP-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/NewsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[News2]],
            error_mapper=golf_v2_newsbydate_news_by_date_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_player_player(
        self, format: FormatOrStr, playerid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Player8, GolfV2PlayerPlayerErrorBody]:
        """Player

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            playerid: Unique FantasyData Player ID. Example:<code>40000019</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Player/{playerid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("playerid", playerid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Player8],
            error_mapper=golf_v2_player_player_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_players_player_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player8], GolfV2PlayersPlayerProfilesAllErrorBody]:
        """Player Profiles - All

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player8]],
            error_mapper=golf_v2_players_player_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_playerseasonstats_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason9], GolfV2PlayerseasonstatsPlayerSeasonStatsErrorBody]:
        """Player Season Stats

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason9]],
            error_mapper=golf_v2_playerseasonstats_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[PlayerTournamentBasic], GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody
    ]:
        """Player Hole Scores - by Tournament [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentHoleScores/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerTournamentBasic]],
            error_mapper=golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[PlayerTournamentBasic], GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody
    ]:
        """Player Hole Scores - by Tournament [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentHoleScoresFinal/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerTournamentBasic]],
            error_mapper=golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[PlayerTournamentProjection], GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody
    ]:
        """Player Projected Stats - by Tournament

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>78</code>, <code>79</code>, <code>80</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentProjectionStats/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerTournamentProjection]],
            error_mapper=golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_playertournamentroundscores_scores_by_tournament_live_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TournamentRound], GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody]:
        """Scores - by Tournament [Live & Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentRoundScores/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TournamentRound]],
            error_mapper=golf_v2_playertournamentroundscores_scores_by_tournament_live_final_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TournamentRound], GolfV2PlayertournamentroundscoresfinalScoresByTournamentFinalErrorBody]:
        """Scores - by Tournament [Final]

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/PlayerTournamentRoundScoresFinal/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TournamentRound]],
            error_mapper=golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_rankings_rankings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason9], GolfV2RankingsRankingsErrorBody]:
        """Rankings

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Rankings/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason9]],
            error_mapper=golf_v2_rankings_rankings_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_tournaments_schedule_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Tournament1], GolfV2TournamentsScheduleBySeasonErrorBody]:
        """Schedule - by Season

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. <br>Examples: <code>2016</code>, <code>2017</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Tournaments/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Tournament1]],
            error_mapper=golf_v2_tournaments_schedule_by_season_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_tournaments_schedules(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Tournament1], GolfV2TournamentsSchedulesErrorBody]:
        """Schedules

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/Tournaments"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Tournament1]],
            error_mapper=golf_v2_tournaments_schedules_error_mapper,
            request_options=request_options,
        )

    async def golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[DfsSlateWithOwnershipProjection],
        GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody,
    ]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/golf/v2/{format}/UpcomingDfsSlateOwnershipProjections"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlateWithOwnershipProjection]],
            error_mapper=golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming_error_mapper,
            request_options=request_options,
        )
