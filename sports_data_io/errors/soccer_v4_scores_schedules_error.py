from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ScoresSchedulesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ScoresSchedulesError:
    def map(self, response: HttpResponse) -> SoccerV4ScoresSchedulesErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_scores_schedules_error_mapper: Final[
    ErrorMapper[SoccerV4ScoresSchedulesErrorBody]
] = _SoccerV4ScoresSchedulesError()
