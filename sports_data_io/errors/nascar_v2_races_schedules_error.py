from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2RacesSchedulesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2RacesSchedulesError:
    def map(self, status_code: int, content: bytes) -> NascarV2RacesSchedulesErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nascar_v2_races_schedules_error_mapper: Final[
    ErrorMapper[NascarV2RacesSchedulesErrorBody]
] = _NascarV2RacesSchedulesError()
