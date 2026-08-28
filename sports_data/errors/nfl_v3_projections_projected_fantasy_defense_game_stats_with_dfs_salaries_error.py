from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesError:
    def map(self, response: HttpResponse) -> NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody]
] = _NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesError()
