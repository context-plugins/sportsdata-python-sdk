from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3StatsPlayerSeasonSplitStatsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3StatsPlayerSeasonSplitStatsError:
    def map(self, response: HttpResponse) -> MlbV3StatsPlayerSeasonSplitStatsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_stats_player_season_split_stats_error_mapper: Final[
    ErrorMapper[MlbV3StatsPlayerSeasonSplitStatsErrorBody]
] = _MlbV3StatsPlayerSeasonSplitStatsError()
