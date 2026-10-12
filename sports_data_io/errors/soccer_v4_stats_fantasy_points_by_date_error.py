from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4StatsFantasyPointsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4StatsFantasyPointsByDateError:
    def map(self, status_code: int, content: bytes) -> SoccerV4StatsFantasyPointsByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


soccer_v4_stats_fantasy_points_by_date_error_mapper: Final[
    ErrorMapper[SoccerV4StatsFantasyPointsByDateErrorBody]
] = _SoccerV4StatsFantasyPointsByDateError()
