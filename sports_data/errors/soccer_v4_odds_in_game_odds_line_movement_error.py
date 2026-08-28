from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsInGameOddsLineMovementErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsInGameOddsLineMovementError:
    def map(self, response: HttpResponse) -> SoccerV4OddsInGameOddsLineMovementErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_odds_in_game_odds_line_movement_error_mapper: Final[
    ErrorMapper[SoccerV4OddsInGameOddsLineMovementErrorBody]
] = _SoccerV4OddsInGameOddsLineMovementError()
