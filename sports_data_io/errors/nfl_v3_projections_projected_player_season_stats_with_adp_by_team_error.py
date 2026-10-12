from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamError:
    def map(self, status_code: int, content: bytes) -> NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_projections_projected_player_season_stats_with_adp_by_team_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody]
] = _NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamError()
