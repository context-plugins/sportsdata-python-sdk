from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2TournamentsSchedulesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2TournamentsSchedulesError:
    def map(self, status_code: int, content: bytes) -> GolfV2TournamentsSchedulesErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_tournaments_schedules_error_mapper: Final[
    ErrorMapper[GolfV2TournamentsSchedulesErrorBody]
] = _GolfV2TournamentsSchedulesError()
