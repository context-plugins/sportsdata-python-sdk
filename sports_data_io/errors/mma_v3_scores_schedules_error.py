from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3ScoresSchedulesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3ScoresSchedulesError:
    def map(self, response: HttpResponse) -> MmaV3ScoresSchedulesErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mma_v3_scores_schedules_error_mapper: Final[ErrorMapper[MmaV3ScoresSchedulesErrorBody]] = _MmaV3ScoresSchedulesError()
