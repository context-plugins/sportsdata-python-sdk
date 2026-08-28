from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3OddsEventFightOddsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3OddsEventFightOddsError:
    def map(self, response: HttpResponse) -> MmaV3OddsEventFightOddsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mma_v3_odds_event_fight_odds_error_mapper: Final[
    ErrorMapper[MmaV3OddsEventFightOddsErrorBody]
] = _MmaV3OddsEventFightOddsError()
