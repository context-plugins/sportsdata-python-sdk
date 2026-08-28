from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsFantasyPointsByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsFantasyPointsByWeekError:
    def map(self, response: HttpResponse) -> NflV3StatsFantasyPointsByWeekErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_stats_fantasy_points_by_week_error_mapper: Final[
    ErrorMapper[NflV3StatsFantasyPointsByWeekErrorBody]
] = _NflV3StatsFantasyPointsByWeekError()
