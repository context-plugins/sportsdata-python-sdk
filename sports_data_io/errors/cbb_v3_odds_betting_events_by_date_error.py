from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3OddsBettingEventsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3OddsBettingEventsByDateError:
    def map(self, response: HttpResponse) -> CbbV3OddsBettingEventsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_odds_betting_events_by_date_error_mapper: Final[
    ErrorMapper[CbbV3OddsBettingEventsByDateErrorBody]
] = _CbbV3OddsBettingEventsByDateError()
