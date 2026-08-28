from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsPeriodGameOddsLineMovementErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsPeriodGameOddsLineMovementError:
    def map(self, response: HttpResponse) -> NbaV3OddsPeriodGameOddsLineMovementErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_odds_period_game_odds_line_movement_error_mapper: Final[
    ErrorMapper[NbaV3OddsPeriodGameOddsLineMovementErrorBody]
] = _NbaV3OddsPeriodGameOddsLineMovementError()
