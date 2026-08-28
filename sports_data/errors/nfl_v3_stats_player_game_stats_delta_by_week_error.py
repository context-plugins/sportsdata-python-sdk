from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsPlayerGameStatsDeltaByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsPlayerGameStatsDeltaByWeekError:
    def map(self, response: HttpResponse) -> NflV3StatsPlayerGameStatsDeltaByWeekErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_stats_player_game_stats_delta_by_week_error_mapper: Final[
    ErrorMapper[NflV3StatsPlayerGameStatsDeltaByWeekErrorBody]
] = _NflV3StatsPlayerGameStatsDeltaByWeekError()
