from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsPlayerGameLogsBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsPlayerGameLogsBySeasonError:
    def map(self, response: HttpResponse) -> NflV3StatsPlayerGameLogsBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_stats_player_game_logs_by_season_error_mapper: Final[
    ErrorMapper[NflV3StatsPlayerGameLogsBySeasonErrorBody]
] = _NflV3StatsPlayerGameLogsBySeasonError()
