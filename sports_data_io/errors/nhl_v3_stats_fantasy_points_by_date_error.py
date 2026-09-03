from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3StatsFantasyPointsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3StatsFantasyPointsByDateError:
    def map(self, response: HttpResponse) -> NhlV3StatsFantasyPointsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_stats_fantasy_points_by_date_error_mapper: Final[
    ErrorMapper[NhlV3StatsFantasyPointsByDateErrorBody]
] = _NhlV3StatsFantasyPointsByDateError()
