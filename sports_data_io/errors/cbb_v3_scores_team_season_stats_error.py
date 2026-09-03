from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3ScoresTeamSeasonStatsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3ScoresTeamSeasonStatsError:
    def map(self, response: HttpResponse) -> CbbV3ScoresTeamSeasonStatsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_scores_team_season_stats_error_mapper: Final[
    ErrorMapper[CbbV3ScoresTeamSeasonStatsErrorBody]
] = _CbbV3ScoresTeamSeasonStatsError()
