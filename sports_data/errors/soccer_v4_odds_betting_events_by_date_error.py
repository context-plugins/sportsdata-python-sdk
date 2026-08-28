from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsBettingEventsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsBettingEventsByDateError:
    def map(self, response: HttpResponse) -> SoccerV4OddsBettingEventsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_odds_betting_events_by_date_error_mapper: Final[
    ErrorMapper[SoccerV4OddsBettingEventsByDateErrorBody]
] = _SoccerV4OddsBettingEventsByDateError()
