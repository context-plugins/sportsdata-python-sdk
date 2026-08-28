from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3StatsPlayerGameStatsByDateLiveFinalError:
    def map(self, response: HttpResponse) -> CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_stats_player_game_stats_by_date_live_final_error_mapper: Final[
    ErrorMapper[CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]
] = _CbbV3StatsPlayerGameStatsByDateLiveFinalError()
