from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3OddsEventFightOddsLineMovementErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3OddsEventFightOddsLineMovementError:
    def map(self, response: HttpResponse) -> MmaV3OddsEventFightOddsLineMovementErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mma_v3_odds_event_fight_odds_line_movement_error_mapper: Final[
    ErrorMapper[MmaV3OddsEventFightOddsLineMovementErrorBody]
] = _MmaV3OddsEventFightOddsLineMovementError()
