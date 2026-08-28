from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ProjectionsProjectedPlayerGameStatsByDateError:
    def map(self, response: HttpResponse) -> NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_projections_projected_player_game_stats_by_date_error_mapper: Final[
    ErrorMapper[NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]
] = _NbaV3ProjectionsProjectedPlayerGameStatsByDateError()
