from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsPlayerSeasonRedZoneStatsInsideTenError:
    def map(self, response: HttpResponse) -> NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_stats_player_season_red_zone_stats_inside_ten_error_mapper: Final[
    ErrorMapper[NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody]
] = _NflV3StatsPlayerSeasonRedZoneStatsInsideTenError()
