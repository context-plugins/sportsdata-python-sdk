from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3ScoresSchedulesBasicErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3ScoresSchedulesBasicError:
    def map(self, response: HttpResponse) -> CbbV3ScoresSchedulesBasicErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_scores_schedules_basic_error_mapper: Final[
    ErrorMapper[CbbV3ScoresSchedulesBasicErrorBody]
] = _CbbV3ScoresSchedulesBasicError()
