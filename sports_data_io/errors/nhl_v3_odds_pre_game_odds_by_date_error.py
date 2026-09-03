from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsPreGameOddsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsPreGameOddsByDateError:
    def map(self, response: HttpResponse) -> NhlV3OddsPreGameOddsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_odds_pre_game_odds_by_date_error_mapper: Final[
    ErrorMapper[NhlV3OddsPreGameOddsByDateErrorBody]
] = _NhlV3OddsPreGameOddsByDateError()
