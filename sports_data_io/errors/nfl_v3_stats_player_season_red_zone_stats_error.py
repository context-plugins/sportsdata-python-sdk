from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsPlayerSeasonRedZoneStatsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsPlayerSeasonRedZoneStatsError:
    def map(self, response: HttpResponse) -> NflV3StatsPlayerSeasonRedZoneStatsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_stats_player_season_red_zone_stats_error_mapper: Final[
    ErrorMapper[NflV3StatsPlayerSeasonRedZoneStatsErrorBody]
] = _NflV3StatsPlayerSeasonRedZoneStatsError()
