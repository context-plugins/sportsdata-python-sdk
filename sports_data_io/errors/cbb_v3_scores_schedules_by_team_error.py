from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3ScoresSchedulesByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3ScoresSchedulesByTeamError:
    def map(self, response: HttpResponse) -> CbbV3ScoresSchedulesByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_scores_schedules_by_team_error_mapper: Final[
    ErrorMapper[CbbV3ScoresSchedulesByTeamErrorBody]
] = _CbbV3ScoresSchedulesByTeamError()
