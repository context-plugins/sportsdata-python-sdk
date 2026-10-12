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
from ..models.enums.format import Format, FormatOrStr
from ..models.game17 import Game17
from ..models.membership import Membership
from ..models.player7 import Player7
from ..models.player_basic6 import PlayerBasic6
from ..models.round import Round
from ..models.schedule_basic7 import ScheduleBasic7
from ..models.score_basic7 import ScoreBasic7
from ..models.season_team import SeasonTeam
from ..models.team8 import Team8
from ..models.team_game7 import TeamGame7
from ..models.venue import Venue
from ..server.server import Server


class SoccerV4Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoccerV4ScoresWithRawResponse(client, server, auth)

    def soccer_v4_scores_areas_countries(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Area]:
        """A list of countries, continents etc. for finding their respective competitions.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_areas_countries(format_=format_, request_options=request_options)
        )

    def soccer_v4_scores_competitions_leagues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Competition]:
        """A list of all competitions (leagues, cups etc.) and their associated countries or areas.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_competitions_leagues(
                format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_games_by_competition_live_final(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompetitionDetail:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info, delivered
        by competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_games_by_competition_live_final(
                competition, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_games_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Game17]:
        """Full scores and gameday info, as well as half and full-time score, delivered post-game.

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
            self._with_raw_response.soccer_v4_scores_games_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_games_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Game17]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

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
            self._with_raw_response.soccer_v4_scores_games_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_games_basic_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScoreBasic7]:
        """The most top-line full-time information, ideal for basic applications, called by competition and date,
        delivered post-game.

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
            self._with_raw_response.soccer_v4_scores_games_basic_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_games_basic_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScoreBasic7]:
        """Full scores and gameday info delivered live and post-game, called by date and competition.

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
            self._with_raw_response.soccer_v4_scores_games_basic_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_memberships_by_active(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Membership]:
        """Players currently active on teams within a specified competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_memberships_by_active(
                competition, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_memberships_by_canceled(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> CanceledMembership:
        """Memberships (players' membership of a team) that have since been revoked by our system.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_memberships_by_canceled(
                format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_memberships_by_recently_changed(
        self,
        competition: str,
        days: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Membership]:
        """A list of all recently changed memberships (e.g. player transfers, releases) for a given competition, called
        by number of days ago.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            days: The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll
                receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>,
                <code>2</code> ... <code>30</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_memberships_by_recently_changed(
                competition, days, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_memberships_historical_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Membership]:
        """Historical memberships of a team, i.e. players who were once on the roster but have since left.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_memberships_historical_by_team(
                competition, teamid, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_player_details_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Player7]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_player_details_by_team(
                competition, teamid, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_player_profiles_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerBasic6]:
        """Roster information for a given team. Player profiles include basic biographical information, position, etc.
        Specify a TeamId parameter to receive all players currently on that team.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_player_profiles_by_team(
                competition, teamid, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_schedules(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Round]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

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
            self._with_raw_response.soccer_v4_scores_schedules(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_schedules_basic(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScheduleBasic7]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

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
            self._with_raw_response.soccer_v4_scores_schedules_basic(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_standings(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Round]:
        """Includes regular season standings in a given league or tournament and season.

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
            self._with_raw_response.soccer_v4_scores_standings(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_team_game_stats_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame7]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date within a competition, both live and post-game.

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
            self._with_raw_response.soccer_v4_scores_team_game_stats_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_team_profiles_by_competition(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Team8]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams ever associated with a
        competition; use Team Profiles - by Season for just the current ones.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_team_profiles_by_competition(
                competition, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_team_profiles_by_season(
        self,
        competition: str,
        seasonid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SeasonTeam]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently associated with a
        competition's active season; use Team Profiles - by Competition for all-time (e.g. teams since relegated from
        the EPL.)

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League
                Hierarchy). Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.soccer_v4_scores_team_profiles_by_season(
                competition, seasonid, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_team_season_stats(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Round]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

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
            self._with_raw_response.soccer_v4_scores_team_season_stats(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    def soccer_v4_scores_venues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Venue]:
        """Stadium information from across the world

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(self._with_raw_response.soccer_v4_scores_venues(format_=format_, request_options=request_options))

    @property
    def with_raw_response(self) -> SoccerV4ScoresWithRawResponse:
        return self._with_raw_response


class AsyncSoccerV4Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoccerV4ScoresWithRawResponse(client, server, auth)

    async def soccer_v4_scores_areas_countries(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Area]:
        """A list of countries, continents etc. for finding their respective competitions.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_areas_countries(
                format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_competitions_leagues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Competition]:
        """A list of all competitions (leagues, cups etc.) and their associated countries or areas.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_competitions_leagues(
                format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_games_by_competition_live_final(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompetitionDetail:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info, delivered
        by competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_games_by_competition_live_final(
                competition, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_games_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Game17]:
        """Full scores and gameday info, as well as half and full-time score, delivered post-game.

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
            await self._with_raw_response.soccer_v4_scores_games_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_games_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Game17]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

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
            await self._with_raw_response.soccer_v4_scores_games_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_games_basic_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScoreBasic7]:
        """The most top-line full-time information, ideal for basic applications, called by competition and date,
        delivered post-game.

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
            await self._with_raw_response.soccer_v4_scores_games_basic_by_date_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_games_basic_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScoreBasic7]:
        """Full scores and gameday info delivered live and post-game, called by date and competition.

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
            await self._with_raw_response.soccer_v4_scores_games_basic_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_memberships_by_active(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Membership]:
        """Players currently active on teams within a specified competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_memberships_by_active(
                competition, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_memberships_by_canceled(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> CanceledMembership:
        """Memberships (players' membership of a team) that have since been revoked by our system.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_memberships_by_canceled(
                format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_memberships_by_recently_changed(
        self,
        competition: str,
        days: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Membership]:
        """A list of all recently changed memberships (e.g. player transfers, releases) for a given competition, called
        by number of days ago.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            days: The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll
                receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>,
                <code>2</code> ... <code>30</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_memberships_by_recently_changed(
                competition, days, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_memberships_historical_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Membership]:
        """Historical memberships of a team, i.e. players who were once on the roster but have since left.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_memberships_historical_by_team(
                competition, teamid, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_player_details_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Player7]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_player_details_by_team(
                competition, teamid, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_player_profiles_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerBasic6]:
        """Roster information for a given team. Player profiles include basic biographical information, position, etc.
        Specify a TeamId parameter to receive all players currently on that team.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_player_profiles_by_team(
                competition, teamid, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_schedules(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Round]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

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
            await self._with_raw_response.soccer_v4_scores_schedules(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_schedules_basic(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ScheduleBasic7]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

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
            await self._with_raw_response.soccer_v4_scores_schedules_basic(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_standings(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Round]:
        """Includes regular season standings in a given league or tournament and season.

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
            await self._with_raw_response.soccer_v4_scores_standings(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_team_game_stats_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[TeamGame7]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date within a competition, both live and post-game.

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
            await self._with_raw_response.soccer_v4_scores_team_game_stats_by_date_live_final(
                competition, date, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_team_profiles_by_competition(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Team8]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams ever associated with a
        competition; use Team Profiles - by Season for just the current ones.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_team_profiles_by_competition(
                competition, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_team_profiles_by_season(
        self,
        competition: str,
        seasonid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SeasonTeam]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently associated with a
        competition's active season; use Team Profiles - by Competition for all-time (e.g. teams since relegated from
        the EPL.)

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League
                Hierarchy). Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_team_profiles_by_season(
                competition, seasonid, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_team_season_stats(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Round]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

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
            await self._with_raw_response.soccer_v4_scores_team_season_stats(
                competition, season, format_=format_, request_options=request_options
            ),
        )

    async def soccer_v4_scores_venues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Venue]:
        """Stadium information from across the world

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.soccer_v4_scores_venues(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncSoccerV4ScoresWithRawResponse:
        return self._with_raw_response


class SoccerV4ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def soccer_v4_scores_areas_countries(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Area], SoccerV4ScoresAreasCountriesErrorBody]:
        """A list of countries, continents etc. for finding their respective competitions.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Areas"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Area]],
            error_mapper=soccer_v4_scores_areas_countries_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_competitions_leagues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Competition], SoccerV4ScoresCompetitionsLeaguesErrorBody]:
        """A list of all competitions (leagues, cups etc.) and their associated countries or areas.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Competitions"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Competition]],
            error_mapper=soccer_v4_scores_competitions_leagues_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_by_competition_live_final(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompetitionDetail, SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info, delivered
        by competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/CompetitionDetails/{competition}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("competition", competition)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[CompetitionDetail],
            error_mapper=soccer_v4_scores_games_by_competition_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Game17], SoccerV4ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, as well as half and full-time score, delivered post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/GamesByDateFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game17]],
            error_mapper=soccer_v4_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Game17], SoccerV4ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

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
            url_template=self._server.default("/v4/soccer/scores/{format}/GamesByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game17]],
            error_mapper=soccer_v4_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_basic_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScoreBasic7], SoccerV4ScoresGamesBasicByDateFinalErrorBody]:
        """The most top-line full-time information, ideal for basic applications, called by competition and date,
        delivered post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ScoresBasicFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic7]],
            error_mapper=soccer_v4_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_games_basic_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScoreBasic7], SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game, called by date and competition.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ScoresBasic/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic7]],
            error_mapper=soccer_v4_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_memberships_by_active(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsByActiveErrorBody]:
        """Players currently active on teams within a specified competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/ActiveMemberships/{competition}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("competition", competition)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_by_active_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_memberships_by_canceled(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CanceledMembership, SoccerV4ScoresMembershipsByCanceledErrorBody]:
        """Memberships (players' membership of a team) that have since been revoked by our system.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/CanceledMemberships"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[CanceledMembership],
            error_mapper=soccer_v4_scores_memberships_by_canceled_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_memberships_by_recently_changed(
        self,
        competition: str,
        days: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsByRecentlyChangedErrorBody]:
        """A list of all recently changed memberships (e.g. player transfers, releases) for a given competition, called
        by number of days ago.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            days: The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll
                receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>,
                <code>2</code> ... <code>30</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/scores/{format}/RecentlyChangedMemberships/{competition}/{days}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("days", days)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_by_recently_changed_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_memberships_historical_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsHistoricalByTeamErrorBody]:
        """Historical memberships of a team, i.e. players who were once on the roster but have since left.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/scores/{format}/HistoricalMembershipsByTeam/{competition}/{teamid}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_historical_by_team_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_player_details_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Player7], SoccerV4ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/PlayersByTeam/{competition}/{teamid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player7]],
            error_mapper=soccer_v4_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_player_profiles_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerBasic6], SoccerV4ScoresPlayerProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position, etc.
        Specify a TeamId parameter to receive all players currently on that team.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/PlayersByTeamBasic/{competition}/{teamid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerBasic6]],
            error_mapper=soccer_v4_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_schedules(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Round], SoccerV4ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/Schedule/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round]],
            error_mapper=soccer_v4_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_schedules_basic(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScheduleBasic7], SoccerV4ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/SchedulesBasic/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScheduleBasic7]],
            error_mapper=soccer_v4_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_standings(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Round], SoccerV4ScoresStandingsErrorBody]:
        """Includes regular season standings in a given league or tournament and season.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/Standings/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round]],
            error_mapper=soccer_v4_scores_standings_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_team_game_stats_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame7], SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date within a competition, both live and post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/TeamGameStatsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame7]],
            error_mapper=soccer_v4_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_team_profiles_by_competition(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Team8], SoccerV4ScoresTeamProfilesByCompetitionErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams ever associated with a
        competition; use Team Profiles - by Season for just the current ones.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Teams/{competition}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("competition", competition)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team8]],
            error_mapper=soccer_v4_scores_team_profiles_by_competition_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_team_profiles_by_season(
        self,
        competition: str,
        seasonid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SeasonTeam], SoccerV4ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently associated with a
        competition's active season; use Team Profiles - by Competition for all-time (e.g. teams since relegated from
        the EPL.)

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League
                Hierarchy). Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/SeasonTeams/{competition}/{seasonid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("seasonid", seasonid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[SeasonTeam]],
            error_mapper=soccer_v4_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_team_season_stats(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Round], SoccerV4ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/TeamSeasonStats/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Round]],
            error_mapper=soccer_v4_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_scores_venues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Venue], SoccerV4ScoresVenuesErrorBody]:
        """Stadium information from across the world

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Venues"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Venue]],
            error_mapper=soccer_v4_scores_venues_error_mapper,
            request_options=request_options,
        )


class AsyncSoccerV4ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def soccer_v4_scores_areas_countries(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Area], SoccerV4ScoresAreasCountriesErrorBody]:
        """A list of countries, continents etc. for finding their respective competitions.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Areas"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Area]],
            error_mapper=soccer_v4_scores_areas_countries_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_competitions_leagues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Competition], SoccerV4ScoresCompetitionsLeaguesErrorBody]:
        """A list of all competitions (leagues, cups etc.) and their associated countries or areas.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Competitions"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Competition]],
            error_mapper=soccer_v4_scores_competitions_leagues_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_by_competition_live_final(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompetitionDetail, SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info, delivered
        by competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/CompetitionDetails/{competition}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("competition", competition)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[CompetitionDetail],
            error_mapper=soccer_v4_scores_games_by_competition_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Game17], SoccerV4ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, as well as half and full-time score, delivered post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/GamesByDateFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game17]],
            error_mapper=soccer_v4_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Game17], SoccerV4ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes weather, TV channel etc

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
            url_template=self._server.default("/v4/soccer/scores/{format}/GamesByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Game17]],
            error_mapper=soccer_v4_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_basic_by_date_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScoreBasic7], SoccerV4ScoresGamesBasicByDateFinalErrorBody]:
        """The most top-line full-time information, ideal for basic applications, called by competition and date,
        delivered post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ScoresBasicFinal/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScoreBasic7]],
            error_mapper=soccer_v4_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_games_basic_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScoreBasic7], SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game, called by date and competition.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/ScoresBasic/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScoreBasic7]],
            error_mapper=soccer_v4_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_memberships_by_active(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsByActiveErrorBody]:
        """Players currently active on teams within a specified competition.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/ActiveMemberships/{competition}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("competition", competition)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_by_active_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_memberships_by_canceled(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CanceledMembership, SoccerV4ScoresMembershipsByCanceledErrorBody]:
        """Memberships (players' membership of a team) that have since been revoked by our system.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/CanceledMemberships"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[CanceledMembership],
            error_mapper=soccer_v4_scores_memberships_by_canceled_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_memberships_by_recently_changed(
        self,
        competition: str,
        days: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsByRecentlyChangedErrorBody]:
        """A list of all recently changed memberships (e.g. player transfers, releases) for a given competition, called
        by number of days ago.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            days: The number of days since memberships were updated. For example, if you pass <code>3</code>, you'll
                receive all memberships that have been updated in the past 3 days. Valid entries are: <code>1</code>,
                <code>2</code> ... <code>30</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/scores/{format}/RecentlyChangedMemberships/{competition}/{days}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("days", days)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_by_recently_changed_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_memberships_historical_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Membership], SoccerV4ScoresMembershipsHistoricalByTeamErrorBody]:
        """Historical memberships of a team, i.e. players who were once on the roster but have since left.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/scores/{format}/HistoricalMembershipsByTeam/{competition}/{teamid}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Membership]],
            error_mapper=soccer_v4_scores_memberships_historical_by_team_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_player_details_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Player7], SoccerV4ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/PlayersByTeam/{competition}/{teamid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player7]],
            error_mapper=soccer_v4_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_player_profiles_by_team(
        self,
        competition: str,
        teamid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerBasic6], SoccerV4ScoresPlayerProfilesByTeamErrorBody]:
        """Roster information for a given team. Player profiles include basic biographical information, position, etc.
        Specify a TeamId parameter to receive all players currently on that team.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            teamid: Unique FantasyData Team ID. Example:<code>516</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/PlayersByTeamBasic/{competition}/{teamid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("teamid", teamid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerBasic6]],
            error_mapper=soccer_v4_scores_player_profiles_by_team_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_schedules(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Round], SoccerV4ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), weather conditions, and broadcast information.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/Schedule/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Round]],
            error_mapper=soccer_v4_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_schedules_basic(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ScheduleBasic7], SoccerV4ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/SchedulesBasic/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[ScheduleBasic7]],
            error_mapper=soccer_v4_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_standings(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Round], SoccerV4ScoresStandingsErrorBody]:
        """Includes regular season standings in a given league or tournament and season.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/Standings/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Round]],
            error_mapper=soccer_v4_scores_standings_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_team_game_stats_by_date_live_final(
        self,
        competition: str,
        date: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[TeamGame7], SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date within a competition, both live and post-game.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/TeamGameStatsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[TeamGame7]],
            error_mapper=soccer_v4_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_team_profiles_by_competition(
        self,
        competition: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Team8], SoccerV4ScoresTeamProfilesByCompetitionErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams ever associated with a
        competition; use Team Profiles - by Season for just the current ones.

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Teams/{competition}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("competition", competition)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Team8]],
            error_mapper=soccer_v4_scores_team_profiles_by_competition_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_team_profiles_by_season(
        self,
        competition: str,
        seasonid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SeasonTeam], SoccerV4ScoresTeamProfilesBySeasonErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns the teams currently associated with a
        competition's active season; use Team Profiles - by Competition for all-time (e.g. teams since relegated from
        the EPL.)

        Args:
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League
                Hierarchy). Examples: <code>1</code>, <code>2</code>, <code>3</code>, etc
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/SeasonTeams/{competition}/{seasonid}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("seasonid", seasonid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[SeasonTeam]],
            error_mapper=soccer_v4_scores_team_profiles_by_season_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_team_season_stats(
        self,
        competition: str,
        season: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Round], SoccerV4ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

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
            url_template=self._server.default("/v4/soccer/scores/{format}/TeamSeasonStats/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Round]],
            error_mapper=soccer_v4_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_scores_venues(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Venue], SoccerV4ScoresVenuesErrorBody]:
        """Stadium information from across the world

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/scores/{format}/Venues"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Venue]],
            error_mapper=soccer_v4_scores_venues_error_mapper,
            request_options=request_options,
        )
