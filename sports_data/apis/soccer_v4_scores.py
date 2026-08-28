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
from ..errors.soccer_v4_scores_areas_countries_error import (
    SoccerV4ScoresAreasCountriesErrorBody,
    soccer_v4_scores_areas_countries_error_mapper,
)
from ..errors.soccer_v4_scores_competitions_leagues_error import (
    SoccerV4ScoresCompetitionsLeaguesErrorBody,
    soccer_v4_scores_competitions_leagues_error_mapper,
)
from ..errors.soccer_v4_scores_games_basic_by_date_final_error import (
    SoccerV4ScoresGamesBasicByDateFinalErrorBody,
    soccer_v4_scores_games_basic_by_date_final_error_mapper,
)
from ..errors.soccer_v4_scores_games_basic_by_date_live_final_error import (
    SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody,
    soccer_v4_scores_games_basic_by_date_live_final_error_mapper,
)
from ..errors.soccer_v4_scores_games_by_competition_live_final_error import (
    SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody,
    soccer_v4_scores_games_by_competition_live_final_error_mapper,
)
from ..errors.soccer_v4_scores_games_by_date_final_error import (
    SoccerV4ScoresGamesByDateFinalErrorBody,
    soccer_v4_scores_games_by_date_final_error_mapper,
)
from ..errors.soccer_v4_scores_games_by_date_live_final_error import (
    SoccerV4ScoresGamesByDateLiveFinalErrorBody,
    soccer_v4_scores_games_by_date_live_final_error_mapper,
)
from ..errors.soccer_v4_scores_memberships_by_active_error import (
    SoccerV4ScoresMembershipsByActiveErrorBody,
    soccer_v4_scores_memberships_by_active_error_mapper,
)
from ..errors.soccer_v4_scores_memberships_by_canceled_error import (
    SoccerV4ScoresMembershipsByCanceledErrorBody,
    soccer_v4_scores_memberships_by_canceled_error_mapper,
)
from ..errors.soccer_v4_scores_memberships_by_recently_changed_error import (
    SoccerV4ScoresMembershipsByRecentlyChangedErrorBody,
    soccer_v4_scores_memberships_by_recently_changed_error_mapper,
)
from ..errors.soccer_v4_scores_memberships_historical_by_team_error import (
    SoccerV4ScoresMembershipsHistoricalByTeamErrorBody,
    soccer_v4_scores_memberships_historical_by_team_error_mapper,
)
from ..errors.soccer_v4_scores_player_details_by_team_error import (
    SoccerV4ScoresPlayerDetailsByTeamErrorBody,
    soccer_v4_scores_player_details_by_team_error_mapper,
)
from ..errors.soccer_v4_scores_player_profiles_by_team_error import (
    SoccerV4ScoresPlayerProfilesByTeamErrorBody,
    soccer_v4_scores_player_profiles_by_team_error_mapper,
)
from ..errors.soccer_v4_scores_schedules_basic_error import (
    SoccerV4ScoresSchedulesBasicErrorBody,
    soccer_v4_scores_schedules_basic_error_mapper,
)
from ..errors.soccer_v4_scores_schedules_error import (
    SoccerV4ScoresSchedulesErrorBody,
    soccer_v4_scores_schedules_error_mapper,
)
from ..errors.soccer_v4_scores_standings_error import (
    SoccerV4ScoresStandingsErrorBody,
    soccer_v4_scores_standings_error_mapper,
)
from ..errors.soccer_v4_scores_team_game_stats_by_date_live_final_error import (
    SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody,
    soccer_v4_scores_team_game_stats_by_date_live_final_error_mapper,
)
from ..errors.soccer_v4_scores_team_profiles_by_competition_error import (
    SoccerV4ScoresTeamProfilesByCompetitionErrorBody,
    soccer_v4_scores_team_profiles_by_competition_error_mapper,
)
from ..errors.soccer_v4_scores_team_profiles_by_season_error import (
    SoccerV4ScoresTeamProfilesBySeasonErrorBody,
    soccer_v4_scores_team_profiles_by_season_error_mapper,
)
from ..errors.soccer_v4_scores_team_season_stats_error import (
    SoccerV4ScoresTeamSeasonStatsErrorBody,
    soccer_v4_scores_team_season_stats_error_mapper,
)
from ..errors.soccer_v4_scores_venues_error import SoccerV4ScoresVenuesErrorBody, soccer_v4_scores_venues_error_mapper
from ..models.area import Area
from ..models.canceled_membership import CanceledMembership
from ..models.competition import Competition
from ..models.competition_detail import CompetitionDetail
from ..models.enums.format import FormatOrStr
from ..models.game9 import Game9
from ..models.membership import Membership
from ..models.player7 import Player7
from ..models.player_basic6 import PlayerBasic6
from ..models.round1 import Round1
from ..models.schedule_basic7 import ScheduleBasic7
from ..models.score_basic6 import ScoreBasic6
from ..models.season_team import SeasonTeam
from ..models.team7 import Team7
from ..models.team_game6 import TeamGame6
from ..models.venue import Venue
from ..server.server import Server


class SoccerV4Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoccerV4ScoresWithRawResponse(client, server, auth)

    def soccer_v4_scores_areas_countries(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Area]:
        """A list of countries, continents etc. for finding their respective competitions.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_areas_countries(
            format, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_competitions_leagues(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Competition]:
        """A list of all competitions (leagues, cups etc.) and their associated countries or areas.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_competitions_leagues(
            format, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_games_by_competition_live_final(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompetitionDetail:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info, delivered
        by competition.

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
        return self._with_raw_response.soccer_v4_scores_games_by_competition_live_final(
            format, competition, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_games_by_date_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game9]:
        """Full scores and gameday info, as well as half and full-time score, delivered post-game.

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
        return self._with_raw_response.soccer_v4_scores_games_by_date_final(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_games_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game9]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

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
        return self._with_raw_response.soccer_v4_scores_games_by_date_live_final(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_games_basic_by_date_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic6]:
        """The most top-line full-time information, ideal for basic applications, called by competition and date,
        delivered post-game.

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
        return self._with_raw_response.soccer_v4_scores_games_basic_by_date_final(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic6]:
        """Full scores and gameday info delivered live and post-game, called by date and competition.

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
        return self._with_raw_response.soccer_v4_scores_games_basic_by_date_live_final(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_memberships_by_active(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Membership]:
        """Players currently active on teams within a specified competition.

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
        return self._with_raw_response.soccer_v4_scores_memberships_by_active(
            format, competition, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_memberships_by_canceled(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> CanceledMembership:
        """Memberships (players' membership of a team) that have since been revoked by our system.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_memberships_by_canceled(
            format, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_memberships_by_recently_changed(
        self, format: FormatOrStr, competition: str, days: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Membership]:
        """A list of all recently changed memberships (e.g. player transfers, releases) for a given competition, called
        by number of days ago.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            days: The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll
                receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>,
                <code>2</code> ... <code>30</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_memberships_by_recently_changed(
            format, competition, days, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_memberships_historical_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Membership]:
        """Historical memberships of a team, i.e. players who were once on the roster but have since left.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_memberships_historical_by_team(
            format, competition, teamid, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_player_details_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player7]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_player_details_by_team(
            format, competition, teamid, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_player_profiles_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic6]:
        """Roster information for a given team. Player profiles include basic biographical information, position, etc.
        Specify a TeamId parameter to receive all players currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_player_profiles_by_team(
            format, competition, teamid, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_schedules(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Round1]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_schedules(
            format, competition, season, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_schedules_basic(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic7]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_schedules_basic(
            format, competition, season, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_standings(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Round1]:
        """Includes regular season standings in a given league or tournament and season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_standings(
            format, competition, season, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame6]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date within a competition, both live and post-game.

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
        return self._with_raw_response.soccer_v4_scores_team_game_stats_by_date_live_final(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_team_profiles_by_competition(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team7]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams ever associated with a
        competition; use Team Profiles - by Season for just the current ones.

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
        return self._with_raw_response.soccer_v4_scores_team_profiles_by_competition(
            format, competition, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_team_profiles_by_season(
        self,
        format: FormatOrStr,
        competition: str,
        seasonid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SeasonTeam]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently associated with a
        competition's active season; use Team Profiles - by Competition for all-time (e.g. teams since relegated from
        the EPL.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League
                Hierarchy). Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_team_profiles_by_season(
            format, competition, seasonid, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_team_season_stats(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Round1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_team_season_stats(
            format, competition, season, request_options=request_options
        ).unwrap()

    def soccer_v4_scores_venues(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Venue]:
        """Stadium information from across the world

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_scores_venues(format, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SoccerV4ScoresWithRawResponse:
        return self._with_raw_response


class AsyncSoccerV4Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoccerV4ScoresWithRawResponse(client, server, auth)

    async def soccer_v4_scores_areas_countries(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Area]:
        """A list of countries, continents etc. for finding their respective competitions.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_areas_countries(format, request_options=request_options)
        ).unwrap()

    async def soccer_v4_scores_competitions_leagues(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Competition]:
        """A list of all competitions (leagues, cups etc.) and their associated countries or areas.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_competitions_leagues(format, request_options=request_options)
        ).unwrap()

    async def soccer_v4_scores_games_by_competition_live_final(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CompetitionDetail:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info, delivered
        by competition.

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
            await self._with_raw_response.soccer_v4_scores_games_by_competition_live_final(
                format, competition, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_games_by_date_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game9]:
        """Full scores and gameday info, as well as half and full-time score, delivered post-game.

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
            await self._with_raw_response.soccer_v4_scores_games_by_date_final(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_games_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game9]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

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
            await self._with_raw_response.soccer_v4_scores_games_by_date_live_final(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_games_basic_by_date_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic6]:
        """The most top-line full-time information, ideal for basic applications, called by competition and date,
        delivered post-game.

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
            await self._with_raw_response.soccer_v4_scores_games_basic_by_date_final(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic6]:
        """Full scores and gameday info delivered live and post-game, called by date and competition.

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
            await self._with_raw_response.soccer_v4_scores_games_basic_by_date_live_final(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_memberships_by_active(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Membership]:
        """Players currently active on teams within a specified competition.

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
            await self._with_raw_response.soccer_v4_scores_memberships_by_active(
                format, competition, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_memberships_by_canceled(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> CanceledMembership:
        """Memberships (players' membership of a team) that have since been revoked by our system.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_memberships_by_canceled(
                format, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_memberships_by_recently_changed(
        self, format: FormatOrStr, competition: str, days: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Membership]:
        """A list of all recently changed memberships (e.g. player transfers, releases) for a given competition, called
        by number of days ago.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            days: The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll
                receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>,
                <code>2</code> ... <code>30</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_memberships_by_recently_changed(
                format, competition, days, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_memberships_historical_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Membership]:
        """Historical memberships of a team, i.e. players who were once on the roster but have since left.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_memberships_historical_by_team(
                format, competition, teamid, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_player_details_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player7]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_player_details_by_team(
                format, competition, teamid, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_player_profiles_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerBasic6]:
        """Roster information for a given team. Player profiles include basic biographical information, position, etc.
        Specify a TeamId parameter to receive all players currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_player_profiles_by_team(
                format, competition, teamid, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_schedules(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Round1]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_schedules(
                format, competition, season, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_schedules_basic(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScheduleBasic7]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_schedules_basic(
                format, competition, season, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_standings(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Round1]:
        """Includes regular season standings in a given league or tournament and season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_standings(
                format, competition, season, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame6]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date within a competition, both live and post-game.

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
            await self._with_raw_response.soccer_v4_scores_team_game_stats_by_date_live_final(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_team_profiles_by_competition(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team7]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams ever associated with a
        competition; use Team Profiles - by Season for just the current ones.

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
            await self._with_raw_response.soccer_v4_scores_team_profiles_by_competition(
                format, competition, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_team_profiles_by_season(
        self,
        format: FormatOrStr,
        competition: str,
        seasonid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SeasonTeam]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently associated with a
        competition's active season; use Team Profiles - by Competition for all-time (e.g. teams since relegated from
        the EPL.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League
                Hierarchy). Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_team_profiles_by_season(
                format, competition, seasonid, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_team_season_stats(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Round1]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_scores_team_season_stats(
                format, competition, season, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_scores_venues(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Venue]:
        """Stadium information from across the world

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.soccer_v4_scores_venues(format, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoccerV4ScoresWithRawResponse:
        return self._with_raw_response


class SoccerV4ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def soccer_v4_scores_areas_countries(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Area], SoccerV4ScoresAreasCountriesErrorBody]:
        """A list of countries, continents etc. for finding their respective competitions.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Areas"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Area]],
            error_mapper=soccer_v4_scores_areas_countries_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_competitions_leagues(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Competition], SoccerV4ScoresCompetitionsLeaguesErrorBody]:
        """A list of all competitions (leagues, cups etc.) and their associated countries or areas.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Competitions"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Competition]],
            error_mapper=soccer_v4_scores_competitions_leagues_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_by_competition_live_final(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompetitionDetail, SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info, delivered
        by competition.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/CompetitionDetails/{competition}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[CompetitionDetail],
            error_mapper=soccer_v4_scores_games_by_competition_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_by_date_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game9], SoccerV4ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, as well as half and full-time score, delivered post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/GamesByDateFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game9]],
            error_mapper=soccer_v4_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game9], SoccerV4ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

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
            url_template=self._server.default("/v4/soccer/scores/{format}/GamesByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game9]],
            error_mapper=soccer_v4_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_basic_by_date_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic6], SoccerV4ScoresGamesBasicByDateFinalErrorBody]:
        """The most top-line full-time information, ideal for basic applications, called by competition and date,
        delivered post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ScoresBasicFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic6]],
            error_mapper=soccer_v4_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic6], SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game, called by date and competition.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ScoresBasic/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic6]],
            error_mapper=soccer_v4_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_memberships_by_active(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsByActiveErrorBody]:
        """Players currently active on teams within a specified competition.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ActiveMemberships/{competition}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_by_active_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_memberships_by_canceled(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CanceledMembership, SoccerV4ScoresMembershipsByCanceledErrorBody]:
        """Memberships (players' membership of a team) that have since been revoked by our system.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/CanceledMemberships"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[CanceledMembership],
            error_mapper=soccer_v4_scores_memberships_by_canceled_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_memberships_by_recently_changed(
        self, format: FormatOrStr, competition: str, days: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsByRecentlyChangedErrorBody]:
        """A list of all recently changed memberships (e.g. player transfers, releases) for a given competition, called
        by number of days ago.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            days: The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll
                receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>,
                <code>2</code> ... <code>30</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/scores/{format}/RecentlyChangedMemberships/{competition}/{days}"
            ),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("days", days)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_by_recently_changed_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_memberships_historical_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsHistoricalByTeamErrorBody]:
        """Historical memberships of a team, i.e. players who were once on the roster but have since left.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/scores/{format}/HistoricalMembershipsByTeam/{competition}/{teamid}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_historical_by_team_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_player_details_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player7], SoccerV4ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/PlayersByTeam/{competition}/{teamid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player7]],
            error_mapper=soccer_v4_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_player_profiles_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic6], SoccerV4ScoresPlayerProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position, etc.
        Specify a TeamId parameter to receive all players currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/PlayersByTeamBasic/{competition}/{teamid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic6]],
            error_mapper=soccer_v4_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_schedules(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Round1], SoccerV4ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Schedule/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round1]],
            error_mapper=soccer_v4_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_schedules_basic(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic7], SoccerV4ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/SchedulesBasic/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic7]],
            error_mapper=soccer_v4_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_standings(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Round1], SoccerV4ScoresStandingsErrorBody]:
        """Includes regular season standings in a given league or tournament and season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Standings/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round1]],
            error_mapper=soccer_v4_scores_standings_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame6], SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date within a competition, both live and post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/TeamGameStatsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame6]],
            error_mapper=soccer_v4_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_team_profiles_by_competition(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team7], SoccerV4ScoresTeamProfilesByCompetitionErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams ever associated with a
        competition; use Team Profiles - by Season for just the current ones.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/Teams/{competition}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team7]],
            error_mapper=soccer_v4_scores_team_profiles_by_competition_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_team_profiles_by_season(
        self,
        format: FormatOrStr,
        competition: str,
        seasonid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SeasonTeam], SoccerV4ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently associated with a
        competition's active season; use Team Profiles - by Competition for all-time (e.g. teams since relegated from
        the EPL.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League
                Hierarchy). Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/SeasonTeams/{competition}/{seasonid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("seasonid", seasonid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[SeasonTeam]],
            error_mapper=soccer_v4_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_team_season_stats(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Round1], SoccerV4ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/TeamSeasonStats/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round1]],
            error_mapper=soccer_v4_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_venues(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Venue], SoccerV4ScoresVenuesErrorBody]:
        """Stadium information from across the world

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Venues"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Venue]],
            error_mapper=soccer_v4_scores_venues_error_mapper,
            request_options=request_options,
        )


class AsyncSoccerV4ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def soccer_v4_scores_areas_countries(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Area], SoccerV4ScoresAreasCountriesErrorBody]:
        """A list of countries, continents etc. for finding their respective competitions.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Areas"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Area]],
            error_mapper=soccer_v4_scores_areas_countries_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_competitions_leagues(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Competition], SoccerV4ScoresCompetitionsLeaguesErrorBody]:
        """A list of all competitions (leagues, cups etc.) and their associated countries or areas.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Competitions"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Competition]],
            error_mapper=soccer_v4_scores_competitions_leagues_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_by_competition_live_final(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CompetitionDetail, SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info, delivered
        by competition.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/CompetitionDetails/{competition}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[CompetitionDetail],
            error_mapper=soccer_v4_scores_games_by_competition_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_by_date_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game9], SoccerV4ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, as well as half and full-time score, delivered post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/GamesByDateFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game9]],
            error_mapper=soccer_v4_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game9], SoccerV4ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

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
            url_template=self._server.default("/v4/soccer/scores/{format}/GamesByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game9]],
            error_mapper=soccer_v4_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_basic_by_date_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic6], SoccerV4ScoresGamesBasicByDateFinalErrorBody]:
        """The most top-line full-time information, ideal for basic applications, called by competition and date,
        delivered post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ScoresBasicFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic6]],
            error_mapper=soccer_v4_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic6], SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game, called by date and competition.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ScoresBasic/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic6]],
            error_mapper=soccer_v4_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_memberships_by_active(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsByActiveErrorBody]:
        """Players currently active on teams within a specified competition.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ActiveMemberships/{competition}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_by_active_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_memberships_by_canceled(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CanceledMembership, SoccerV4ScoresMembershipsByCanceledErrorBody]:
        """Memberships (players' membership of a team) that have since been revoked by our system.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/CanceledMemberships"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[CanceledMembership],
            error_mapper=soccer_v4_scores_memberships_by_canceled_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_memberships_by_recently_changed(
        self, format: FormatOrStr, competition: str, days: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsByRecentlyChangedErrorBody]:
        """A list of all recently changed memberships (e.g. player transfers, releases) for a given competition, called
        by number of days ago.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            days: The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll
                receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>,
                <code>2</code> ... <code>30</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/scores/{format}/RecentlyChangedMemberships/{competition}/{days}"
            ),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("days", days)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_by_recently_changed_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_memberships_historical_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsHistoricalByTeamErrorBody]:
        """Historical memberships of a team, i.e. players who were once on the roster but have since left.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/scores/{format}/HistoricalMembershipsByTeam/{competition}/{teamid}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_historical_by_team_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_player_details_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player7], SoccerV4ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/PlayersByTeam/{competition}/{teamid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player7]],
            error_mapper=soccer_v4_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_player_profiles_by_team(
        self, format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerBasic6], SoccerV4ScoresPlayerProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position, etc.
        Specify a TeamId parameter to receive all players currently on that team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/PlayersByTeamBasic/{competition}/{teamid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic6]],
            error_mapper=soccer_v4_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_schedules(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Round1], SoccerV4ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Schedule/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round1]],
            error_mapper=soccer_v4_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_schedules_basic(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScheduleBasic7], SoccerV4ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/SchedulesBasic/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic7]],
            error_mapper=soccer_v4_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_standings(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Round1], SoccerV4ScoresStandingsErrorBody]:
        """Includes regular season standings in a given league or tournament and season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Standings/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round1]],
            error_mapper=soccer_v4_scores_standings_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame6], SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date within a competition, both live and post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/TeamGameStatsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame6]],
            error_mapper=soccer_v4_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_team_profiles_by_competition(
        self, format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team7], SoccerV4ScoresTeamProfilesByCompetitionErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams ever associated with a
        competition; use Team Profiles - by Season for just the current ones.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/Teams/{competition}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("competition", competition)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team7]],
            error_mapper=soccer_v4_scores_team_profiles_by_competition_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_team_profiles_by_season(
        self,
        format: FormatOrStr,
        competition: str,
        seasonid: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SeasonTeam], SoccerV4ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently associated with a
        competition's active season; use Team Profiles - by Competition for all-time (e.g. teams since relegated from
        the EPL.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League
                Hierarchy). Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/SeasonTeams/{competition}/{seasonid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("seasonid", seasonid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[SeasonTeam]],
            error_mapper=soccer_v4_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_team_season_stats(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Round1], SoccerV4ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/TeamSeasonStats/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round1]],
            error_mapper=soccer_v4_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_venues(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Venue], SoccerV4ScoresVenuesErrorBody]:
        """Stadium information from across the world

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Venues"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Venue]],
            error_mapper=soccer_v4_scores_venues_error_mapper,
            request_options=request_options,
        )
