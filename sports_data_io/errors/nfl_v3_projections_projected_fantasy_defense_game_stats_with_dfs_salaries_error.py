from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesError:
    def map(
        self, status_code: int, content: bytes
    ) -> NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody]
] = _NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesError()
