from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3StatsTeamStatsAllowedByPositionErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3StatsTeamStatsAllowedByPositionError:
    def map(self, response: HttpResponse) -> NbaV3StatsTeamStatsAllowedByPositionErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_stats_team_stats_allowed_by_position_error_mapper: Final[
    ErrorMapper[NbaV3StatsTeamStatsAllowedByPositionErrorBody]
] = _NbaV3StatsTeamStatsAllowedByPositionError()
