from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsInGameOddsLineMovementErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsInGameOddsLineMovementError:
    def map(self, status_code: int, content: bytes) -> NhlV3OddsInGameOddsLineMovementErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_odds_in_game_odds_line_movement_error_mapper: Final[
    ErrorMapper[NhlV3OddsInGameOddsLineMovementErrorBody]
] = _NhlV3OddsInGameOddsLineMovementError()
