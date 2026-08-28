from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3StatsPlayerGameStatsByDateLiveFinalError:
    def map(self, response: HttpResponse) -> NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_stats_player_game_stats_by_date_live_final_error_mapper: Final[
    ErrorMapper[NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody]
] = _NbaV3StatsPlayerGameStatsByDateLiveFinalError()
