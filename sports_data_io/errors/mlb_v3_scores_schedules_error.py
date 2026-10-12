from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3ScoresSchedulesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3ScoresSchedulesError:
    def map(self, status_code: int, content: bytes) -> MlbV3ScoresSchedulesErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


mlb_v3_scores_schedules_error_mapper: Final[ErrorMapper[MlbV3ScoresSchedulesErrorBody]] = _MlbV3ScoresSchedulesError()
