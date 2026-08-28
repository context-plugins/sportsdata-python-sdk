from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4StatsPlayerGameStatsByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4StatsPlayerGameStatsByDateFinalError:
    def map(self, response: HttpResponse) -> SoccerV4StatsPlayerGameStatsByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_stats_player_game_stats_by_date_final_error_mapper: Final[
    ErrorMapper[SoccerV4StatsPlayerGameStatsByDateFinalErrorBody]
] = _SoccerV4StatsPlayerGameStatsByDateFinalError()
