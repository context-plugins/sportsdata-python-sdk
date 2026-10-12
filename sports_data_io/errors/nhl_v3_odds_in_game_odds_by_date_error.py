from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsInGameOddsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsInGameOddsByDateError:
    def map(self, status_code: int, content: bytes) -> NhlV3OddsInGameOddsByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_odds_in_game_odds_by_date_error_mapper: Final[
    ErrorMapper[NhlV3OddsInGameOddsByDateErrorBody]
] = _NhlV3OddsInGameOddsByDateError()
