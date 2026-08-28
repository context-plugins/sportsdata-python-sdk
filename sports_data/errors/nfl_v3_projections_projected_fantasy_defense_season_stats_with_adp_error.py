from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpError:
    def map(self, response: HttpResponse) -> NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody]
] = _NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpError()
