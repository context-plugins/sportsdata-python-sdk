from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4StatsPlayerSeasonStatsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4StatsPlayerSeasonStatsError:
    def map(self, response: HttpResponse) -> SoccerV4StatsPlayerSeasonStatsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_stats_player_season_stats_error_mapper: Final[
    ErrorMapper[SoccerV4StatsPlayerSeasonStatsErrorBody]
] = _SoccerV4StatsPlayerSeasonStatsError()
