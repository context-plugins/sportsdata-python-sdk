from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamError:
    def map(self, status_code: int, content: bytes) -> NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nba_v3_projections_projected_player_season_stats_by_team_error_mapper: Final[
    ErrorMapper[NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody]
] = _NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamError()
