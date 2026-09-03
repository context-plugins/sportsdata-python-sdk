from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CwbbV3ScoresSchedulesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CwbbV3ScoresSchedulesError:
    def map(self, response: HttpResponse) -> CwbbV3ScoresSchedulesErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cwbb_v3_scores_schedules_error_mapper: Final[
    ErrorMapper[CwbbV3ScoresSchedulesErrorBody]
] = _CwbbV3ScoresSchedulesError()
