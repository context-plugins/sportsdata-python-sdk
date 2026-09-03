from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3StatsPlayerSeasonStatsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3StatsPlayerSeasonStatsError:
    def map(self, response: HttpResponse) -> CbbV3StatsPlayerSeasonStatsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_stats_player_season_stats_error_mapper: Final[
    ErrorMapper[CbbV3StatsPlayerSeasonStatsErrorBody]
] = _CbbV3StatsPlayerSeasonStatsError()
