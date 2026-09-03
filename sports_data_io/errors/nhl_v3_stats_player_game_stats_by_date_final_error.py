from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3StatsPlayerGameStatsByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3StatsPlayerGameStatsByDateFinalError:
    def map(self, response: HttpResponse) -> NhlV3StatsPlayerGameStatsByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_stats_player_game_stats_by_date_final_error_mapper: Final[
    ErrorMapper[NhlV3StatsPlayerGameStatsByDateFinalErrorBody]
] = _NhlV3StatsPlayerGameStatsByDateFinalError()
