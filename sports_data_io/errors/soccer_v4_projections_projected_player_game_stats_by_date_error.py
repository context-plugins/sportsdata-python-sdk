from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ProjectionsProjectedPlayerGameStatsByDateError:
    def map(self, response: HttpResponse) -> SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_projections_projected_player_game_stats_by_date_error_mapper: Final[
    ErrorMapper[SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody]
] = _SoccerV4ProjectionsProjectedPlayerGameStatsByDateError()
