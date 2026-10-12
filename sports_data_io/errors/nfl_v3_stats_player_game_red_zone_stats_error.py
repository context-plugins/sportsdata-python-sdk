from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsPlayerGameRedZoneStatsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsPlayerGameRedZoneStatsError:
    def map(self, status_code: int, content: bytes) -> NflV3StatsPlayerGameRedZoneStatsErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_stats_player_game_red_zone_stats_error_mapper: Final[
    ErrorMapper[NflV3StatsPlayerGameRedZoneStatsErrorBody]
] = _NflV3StatsPlayerGameRedZoneStatsError()
