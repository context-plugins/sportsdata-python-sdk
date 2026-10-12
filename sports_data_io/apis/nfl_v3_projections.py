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
from ..errors.nfl_v3_projections_dfs_slate_ownership_projections_by_slate_error import (
    NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody,
    nfl_v3_projections_dfs_slate_ownership_projections_by_slate_error_mapper,
)
from ..errors.nfl_v3_projections_dfs_slate_ownership_projections_upcoming_error import (
    NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody,
    nfl_v3_projections_dfs_slate_ownership_projections_upcoming_error_mapper,
)
from ..errors.nfl_v3_projections_dfs_slates_by_date_error import (
    NflV3ProjectionsDfsSlatesByDateErrorBody,
    nfl_v3_projections_dfs_slates_by_date_error_mapper,
)
from ..errors.nfl_v3_projections_dfs_slates_by_week_error import (
    NflV3ProjectionsDfsSlatesByWeekErrorBody,
    nfl_v3_projections_dfs_slates_by_week_error_mapper,
)
from ..errors.nfl_v3_projections_idp_projected_player_game_stats_by_team_error import (
    NflV3ProjectionsIdpProjectedPlayerGameStatsByTeamErrorBody,
    nfl_v3_projections_idp_projected_player_game_stats_by_team_error_mapper,
)
from ..errors.nfl_v3_projections_idp_projected_player_game_stats_by_week_error import (
    NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody,
    nfl_v3_projections_idp_projected_player_game_stats_by_week_error_mapper,
)
from ..errors.nfl_v3_projections_player_details_by_injured_error import (
    NflV3ProjectionsPlayerDetailsByInjuredErrorBody,
    nfl_v3_projections_player_details_by_injured_error_mapper,
)
from ..errors.nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries_error import (
    NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody,
    nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries_error_mapper,
)
from ..errors.nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp_error import (
    NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody,
    nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp_error_mapper,
)
from ..errors.nfl_v3_projections_projected_player_game_stats_by_team_error import (
    NflV3ProjectionsProjectedPlayerGameStatsByTeamErrorBody,
    nfl_v3_projections_projected_player_game_stats_by_team_error_mapper,
)
from ..errors.nfl_v3_projections_projected_player_game_stats_by_week_error import (
    NflV3ProjectionsProjectedPlayerGameStatsByWeekErrorBody,
    nfl_v3_projections_projected_player_game_stats_by_week_error_mapper,
)
from ..errors.nfl_v3_projections_projected_player_season_stats_with_adp_by_team_error import (
    NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody,
    nfl_v3_projections_projected_player_season_stats_with_adp_by_team_error_mapper,
)
from ..errors.nfl_v3_projections_projected_player_season_stats_with_adp_error import (
    NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody,
    nfl_v3_projections_projected_player_season_stats_with_adp_error_mapper,
)
from ..models.dfs_slate import DfsSlate
from ..models.dfs_slate_with_ownership_projection import DfsSlateWithOwnershipProjection
from ..models.enums.format import Format, FormatOrStr
from ..models.fantasy_defense_game_projection import FantasyDefenseGameProjection
from ..models.fantasy_defense_season_projection import FantasyDefenseSeasonProjection
from ..models.player import Player
from ..models.player_game_projection import PlayerGameProjection
from ..models.player_season_projection import PlayerSeasonProjection
from ..server.server import Server


class NflV3Projections:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NflV3ProjectionsWithRawResponse(client, server, auth)

    def nfl_v3_projections_dfs_slate_ownership_projections_by_slate(
        self, slate_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> DfsSlateWithOwnershipProjection:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_projections_dfs_slate_ownership_projections_by_slate(
                slate_id, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_dfs_slate_ownership_projections_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlateWithOwnershipProjection]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_projections_dfs_slate_ownership_projections_upcoming(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate]:
        """Returns DFS slates, including eligible games, positions, captain mode, players and salaries, for a given
        date.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-SEP-25</code>, <code>2017-10-31</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_projections_dfs_slates_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_dfs_slates_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DfsSlate]:
        """Returns DFS slates, including eligible games, positions, captain mode, players and salaries, for a given
        week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>
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
            self._with_raw_response.nfl_v3_projections_dfs_slates_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_idp_projected_player_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameProjection]:
        """Individual Defensive Player (IDP stats, including DFS salary information and injuries, for fantasy players,
        called by team.

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
            self._with_raw_response.nfl_v3_projections_idp_projected_player_game_stats_by_team(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_idp_projected_player_game_stats_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameProjection]:
        """Individual Defensive Player (IDP stats, including DFS salary information and injuries, for fantasy players,
        called by week.

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
            self._with_raw_response.nfl_v3_projections_idp_projected_player_game_stats_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player]:
        """This endpoint provides all currently injured NFL players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_projections_player_details_by_injured(
                format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FantasyDefenseGameProjection]:
        """SportsDataIO's proprietary projections, including DFS salary information, for all fantasy defense teams.
        Called by season and week. Does not contain Individual Defensive Players (IDP), which have their own endpoint.

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
            self._with_raw_response.nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyDefenseSeasonProjection]:
        """SportsDataIO's proprietary projections, including average draft position, for all fantasy defense teams for
        the season. Does not contain Individual Defensive Players (IDP), which have their own endpoint.

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
            self._with_raw_response.nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_projected_player_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameProjection]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        for a given game, called by team.

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
            self._with_raw_response.nfl_v3_projections_projected_player_game_stats_by_team(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_projected_player_game_stats_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameProjection]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by week.

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
            self._with_raw_response.nfl_v3_projections_projected_player_game_stats_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_projected_player_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonProjection]:
        """SportsDataIO's proprietary projections on a season-long basis, including Average Draft Position (ADP), for
        fantasy players, for a given season.

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
            self._with_raw_response.nfl_v3_projections_projected_player_season_stats_with_adp(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_projections_projected_player_season_stats_with_adp_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeasonProjection]:
        """SportsDataIO's proprietary projections on a season-long basis, including ADP, for fantasy players, for a
        given season and team.

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
            self._with_raw_response.nfl_v3_projections_projected_player_season_stats_with_adp_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NflV3ProjectionsWithRawResponse:
        return self._with_raw_response


class AsyncNflV3Projections:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNflV3ProjectionsWithRawResponse(client, server, auth)

    async def nfl_v3_projections_dfs_slate_ownership_projections_by_slate(
        self, slate_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> DfsSlateWithOwnershipProjection:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_projections_dfs_slate_ownership_projections_by_slate(
                slate_id, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_dfs_slate_ownership_projections_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlateWithOwnershipProjection]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_projections_dfs_slate_ownership_projections_upcoming(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[DfsSlate]:
        """Returns DFS slates, including eligible games, positions, captain mode, players and salaries, for a given
        date.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-SEP-25</code>, <code>2017-10-31</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_projections_dfs_slates_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_dfs_slates_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DfsSlate]:
        """Returns DFS slates, including eligible games, positions, captain mode, players and salaries, for a given
        week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>
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
            await self._with_raw_response.nfl_v3_projections_dfs_slates_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_idp_projected_player_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameProjection]:
        """Individual Defensive Player (IDP stats, including DFS salary information and injuries, for fantasy players,
        called by team.

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
            await self._with_raw_response.nfl_v3_projections_idp_projected_player_game_stats_by_team(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_idp_projected_player_game_stats_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameProjection]:
        """Individual Defensive Player (IDP stats, including DFS salary information and injuries, for fantasy players,
        called by week.

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
            await self._with_raw_response.nfl_v3_projections_idp_projected_player_game_stats_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player]:
        """This endpoint provides all currently injured NFL players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_projections_player_details_by_injured(
                format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FantasyDefenseGameProjection]:
        """SportsDataIO's proprietary projections, including DFS salary information, for all fantasy defense teams.
        Called by season and week. Does not contain Individual Defensive Players (IDP), which have their own endpoint.

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
            await self._with_raw_response.nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[FantasyDefenseSeasonProjection]:
        """SportsDataIO's proprietary projections, including average draft position, for all fantasy defense teams for
        the season. Does not contain Individual Defensive Players (IDP), which have their own endpoint.

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
            await self._with_raw_response.nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_projected_player_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameProjection]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        for a given game, called by team.

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
            await self._with_raw_response.nfl_v3_projections_projected_player_game_stats_by_team(
                season, week, team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_projected_player_game_stats_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerGameProjection]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by week.

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
            await self._with_raw_response.nfl_v3_projections_projected_player_game_stats_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_projected_player_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeasonProjection]:
        """SportsDataIO's proprietary projections on a season-long basis, including Average Draft Position (ADP), for
        fantasy players, for a given season.

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
            await self._with_raw_response.nfl_v3_projections_projected_player_season_stats_with_adp(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_projections_projected_player_season_stats_with_adp_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PlayerSeasonProjection]:
        """SportsDataIO's proprietary projections on a season-long basis, including ADP, for fantasy players, for a
        given season and team.

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
            await self._with_raw_response.nfl_v3_projections_projected_player_season_stats_with_adp_by_team(
                season, team, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNflV3ProjectionsWithRawResponse:
        return self._with_raw_response


class NflV3ProjectionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfl_v3_projections_dfs_slate_ownership_projections_by_slate(
        self, slate_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DfsSlateWithOwnershipProjection, NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody]:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/projections/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("slateId", slate_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[DfsSlateWithOwnershipProjection],
            error_mapper=nfl_v3_projections_dfs_slate_ownership_projections_by_slate_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_dfs_slate_ownership_projections_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[DfsSlateWithOwnershipProjection], NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody
    ]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/projections/{format}/UpcomingDfsSlateOwnershipProjections"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlateWithOwnershipProjection]],
            error_mapper=nfl_v3_projections_dfs_slate_ownership_projections_upcoming_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate], NflV3ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS slates, including eligible games, positions, captain mode, players and salaries, for a given
        date.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-SEP-25</code>, <code>2017-10-31</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/projections/{format}/DfsSlatesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate]],
            error_mapper=nfl_v3_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_dfs_slates_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DfsSlate], NflV3ProjectionsDfsSlatesByWeekErrorBody]:
        """Returns DFS slates, including eligible games, positions, captain mode, players and salaries, for a given
        week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/projections/{format}/DfsSlatesByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[DfsSlate]],
            error_mapper=nfl_v3_projections_dfs_slates_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_idp_projected_player_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameProjection], NflV3ProjectionsIdpProjectedPlayerGameStatsByTeamErrorBody]:
        """Individual Defensive Player (IDP stats, including DFS salary information and injuries, for fantasy players,
        called by team.

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
                "/v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByTeam/{season}/{week}/{team}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection]],
            error_mapper=nfl_v3_projections_idp_projected_player_game_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_idp_projected_player_game_stats_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameProjection], NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody]:
        """Individual Defensive Player (IDP stats, including DFS salary information and injuries, for fantasy players,
        called by week.

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
                "/v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByWeek/{season}/{week}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection]],
            error_mapper=nfl_v3_projections_idp_projected_player_game_stats_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player], NflV3ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured NFL players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/projections/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player]],
            error_mapper=nfl_v3_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[FantasyDefenseGameProjection], NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody
    ]:
        """SportsDataIO's proprietary projections, including DFS salary information, for all fantasy defense teams.
        Called by season and week. Does not contain Individual Defensive Players (IDP), which have their own endpoint.

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
                "/v3/nfl/projections/{format}/FantasyDefenseProjectionsByGame/{season}/{week}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyDefenseGameProjection]],
            error_mapper=nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[FantasyDefenseSeasonProjection], NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody
    ]:
        """SportsDataIO's proprietary projections, including average draft position, for all fantasy defense teams for
        the season. Does not contain Individual Defensive Players (IDP), which have their own endpoint.

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
            url_template=self._server.default(
                "/v3/nfl/projections/{format}/FantasyDefenseProjectionsBySeason/{season}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[FantasyDefenseSeasonProjection]],
            error_mapper=nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_projected_player_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameProjection], NflV3ProjectionsProjectedPlayerGameStatsByTeamErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        for a given game, called by team.

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
                "/v3/nfl/projections/{format}/PlayerGameProjectionStatsByTeam/{season}/{week}/{team}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection]],
            error_mapper=nfl_v3_projections_projected_player_game_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_projected_player_game_stats_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameProjection], NflV3ProjectionsProjectedPlayerGameStatsByWeekErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by week.

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
                "/v3/nfl/projections/{format}/PlayerGameProjectionStatsByWeek/{season}/{week}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerGameProjection]],
            error_mapper=nfl_v3_projections_projected_player_game_stats_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_projected_player_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonProjection], NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody]:
        """SportsDataIO's proprietary projections on a season-long basis, including Average Draft Position (ADP), for
        fantasy players, for a given season.

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
            url_template=self._server.default("/v3/nfl/projections/{format}/PlayerSeasonProjectionStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonProjection]],
            error_mapper=nfl_v3_projections_projected_player_season_stats_with_adp_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_projections_projected_player_season_stats_with_adp_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeasonProjection], NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody]:
        """SportsDataIO's proprietary projections on a season-long basis, including ADP, for fantasy players, for a
        given season and team.

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
            url_template=self._server.default(
                "/v3/nfl/projections/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeasonProjection]],
            error_mapper=nfl_v3_projections_projected_player_season_stats_with_adp_by_team_error_mapper,
            request_options=request_options,
        )


class AsyncNflV3ProjectionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfl_v3_projections_dfs_slate_ownership_projections_by_slate(
        self, slate_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DfsSlateWithOwnershipProjection, NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody]:
        """Slate Ownership Projections for a specific slate. Projections are for Guaranteed Prize Pool (GPP) format
        ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

        Args:
            slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty
                SlateOwnershipProjections if this slate was not projected
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/projections/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("slateId", slate_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[DfsSlateWithOwnershipProjection],
            error_mapper=nfl_v3_projections_dfs_slate_ownership_projections_by_slate_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_dfs_slate_ownership_projections_upcoming(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[DfsSlateWithOwnershipProjection], NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody
    ]:
        """Returns DFS Slates which have not yet started for which we have DFS Ownership projections.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/projections/{format}/UpcomingDfsSlateOwnershipProjections"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DfsSlateWithOwnershipProjection]],
            error_mapper=nfl_v3_projections_dfs_slate_ownership_projections_upcoming_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_dfs_slates_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DfsSlate], NflV3ProjectionsDfsSlatesByDateErrorBody]:
        """Returns DFS slates, including eligible games, positions, captain mode, players and salaries, for a given
        date.

        Args:
            date: The date of the slates. <br>Examples: <code>2017-SEP-25</code>, <code>2017-10-31</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/projections/{format}/DfsSlatesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DfsSlate]],
            error_mapper=nfl_v3_projections_dfs_slates_by_date_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_dfs_slates_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DfsSlate], NflV3ProjectionsDfsSlatesByWeekErrorBody]:
        """Returns DFS slates, including eligible games, positions, captain mode, players and salaries, for a given
        week.

        Args:
            season: Year of the season and the season type. If no season type is provided, then the default is regular
                season. <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>
            week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason
                1 to 4. Example: <code>1</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/projections/{format}/DfsSlatesByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[DfsSlate]],
            error_mapper=nfl_v3_projections_dfs_slates_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_idp_projected_player_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameProjection], NflV3ProjectionsIdpProjectedPlayerGameStatsByTeamErrorBody]:
        """Individual Defensive Player (IDP stats, including DFS salary information and injuries, for fantasy players,
        called by team.

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
                "/v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByTeam/{season}/{week}/{team}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameProjection]],
            error_mapper=nfl_v3_projections_idp_projected_player_game_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_idp_projected_player_game_stats_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameProjection], NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody]:
        """Individual Defensive Player (IDP stats, including DFS salary information and injuries, for fantasy players,
        called by week.

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
                "/v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByWeek/{season}/{week}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameProjection]],
            error_mapper=nfl_v3_projections_idp_projected_player_game_stats_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_player_details_by_injured(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player], NflV3ProjectionsPlayerDetailsByInjuredErrorBody]:
        """This endpoint provides all currently injured NFL players, along with injury details.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/projections/{format}/InjuredPlayers"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Player]],
            error_mapper=nfl_v3_projections_player_details_by_injured_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[FantasyDefenseGameProjection], NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody
    ]:
        """SportsDataIO's proprietary projections, including DFS salary information, for all fantasy defense teams.
        Called by season and week. Does not contain Individual Defensive Players (IDP), which have their own endpoint.

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
                "/v3/nfl/projections/{format}/FantasyDefenseProjectionsByGame/{season}/{week}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyDefenseGameProjection]],
            error_mapper=nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        list[FantasyDefenseSeasonProjection], NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody
    ]:
        """SportsDataIO's proprietary projections, including average draft position, for all fantasy defense teams for
        the season. Does not contain Individual Defensive Players (IDP), which have their own endpoint.

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
            url_template=self._server.default(
                "/v3/nfl/projections/{format}/FantasyDefenseProjectionsBySeason/{season}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[FantasyDefenseSeasonProjection]],
            error_mapper=nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_projected_player_game_stats_by_team(
        self,
        season: str,
        week: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameProjection], NflV3ProjectionsProjectedPlayerGameStatsByTeamErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        for a given game, called by team.

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
                "/v3/nfl/projections/{format}/PlayerGameProjectionStatsByTeam/{season}/{week}/{team}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("team", team),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameProjection]],
            error_mapper=nfl_v3_projections_projected_player_game_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_projected_player_game_stats_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerGameProjection], NflV3ProjectionsProjectedPlayerGameStatsByWeekErrorBody]:
        """SportsDataIO's proprietary projections, including DFS salary information and injuries, for fantasy players,
        called by week.

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
                "/v3/nfl/projections/{format}/PlayerGameProjectionStatsByWeek/{season}/{week}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerGameProjection]],
            error_mapper=nfl_v3_projections_projected_player_game_stats_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_projected_player_season_stats_with_adp(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeasonProjection], NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody]:
        """SportsDataIO's proprietary projections on a season-long basis, including Average Draft Position (ADP), for
        fantasy players, for a given season.

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
            url_template=self._server.default("/v3/nfl/projections/{format}/PlayerSeasonProjectionStats/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonProjection]],
            error_mapper=nfl_v3_projections_projected_player_season_stats_with_adp_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_projections_projected_player_season_stats_with_adp_by_team(
        self,
        season: str,
        team: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PlayerSeasonProjection], NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody]:
        """SportsDataIO's proprietary projections on a season-long basis, including ADP, for fantasy players, for a
        given season and team.

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
            url_template=self._server.default(
                "/v3/nfl/projections/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}"
            ),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[PlayerSeasonProjection]],
            error_mapper=nfl_v3_projections_projected_player_season_stats_with_adp_by_team_error_mapper,
            request_options=request_options,
        )
