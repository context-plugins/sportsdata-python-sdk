from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ProjectionsProjectedPlayerSeasonStatsError:
    def map(self, response: HttpResponse) -> NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_projections_projected_player_season_stats_error_mapper: Final[
    ErrorMapper[NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody]
] = _NbaV3ProjectionsProjectedPlayerSeasonStatsError()
