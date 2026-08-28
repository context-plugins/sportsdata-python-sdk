from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpError:
    def map(self, response: HttpResponse) -> NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_projections_projected_player_season_stats_with_adp_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody]
] = _NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpError()
