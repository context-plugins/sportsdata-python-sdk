from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3StatsPlayerSeasonStatsByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3StatsPlayerSeasonStatsByTeamError:
    def map(self, response: HttpResponse) -> CbbV3StatsPlayerSeasonStatsByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_stats_player_season_stats_by_team_error_mapper: Final[
    ErrorMapper[CbbV3StatsPlayerSeasonStatsByTeamErrorBody]
] = _CbbV3StatsPlayerSeasonStatsByTeamError()
