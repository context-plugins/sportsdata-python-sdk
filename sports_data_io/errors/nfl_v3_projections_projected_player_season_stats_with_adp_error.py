from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpError:
    def map(self, status_code: int, content: bytes) -> NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_projections_projected_player_season_stats_with_adp_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody]
] = _NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpError()
