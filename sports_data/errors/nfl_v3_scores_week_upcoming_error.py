from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresWeekUpcomingErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresWeekUpcomingError:
    def map(self, response: HttpResponse) -> NflV3ScoresWeekUpcomingErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_scores_week_upcoming_error_mapper: Final[
    ErrorMapper[NflV3ScoresWeekUpcomingErrorBody]
] = _NflV3ScoresWeekUpcomingError()
