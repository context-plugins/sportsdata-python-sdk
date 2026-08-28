from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2RacesSchedulesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2RacesSchedulesError:
    def map(self, response: HttpResponse) -> NascarV2RacesSchedulesErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nascar_v2_races_schedules_error_mapper: Final[
    ErrorMapper[NascarV2RacesSchedulesErrorBody]
] = _NascarV2RacesSchedulesError()
