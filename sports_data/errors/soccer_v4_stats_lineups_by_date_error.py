from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4StatsLineupsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4StatsLineupsByDateError:
    def map(self, response: HttpResponse) -> SoccerV4StatsLineupsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_stats_lineups_by_date_error_mapper: Final[
    ErrorMapper[SoccerV4StatsLineupsByDateErrorBody]
] = _SoccerV4StatsLineupsByDateError()
