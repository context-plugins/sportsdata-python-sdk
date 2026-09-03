from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsInGameOddsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsInGameOddsByDateError:
    def map(self, response: HttpResponse) -> NbaV3OddsInGameOddsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_odds_in_game_odds_by_date_error_mapper: Final[
    ErrorMapper[NbaV3OddsInGameOddsByDateErrorBody]
] = _NbaV3OddsInGameOddsByDateError()
