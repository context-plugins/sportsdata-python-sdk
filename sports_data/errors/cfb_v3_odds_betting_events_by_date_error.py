from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsBettingEventsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsBettingEventsByDateError:
    def map(self, response: HttpResponse) -> CfbV3OddsBettingEventsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_betting_events_by_date_error_mapper: Final[
    ErrorMapper[CfbV3OddsBettingEventsByDateErrorBody]
] = _CfbV3OddsBettingEventsByDateError()
