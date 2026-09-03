from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3OddsPreGameOddsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3OddsPreGameOddsByDateError:
    def map(self, response: HttpResponse) -> CbbV3OddsPreGameOddsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_odds_pre_game_odds_by_date_error_mapper: Final[
    ErrorMapper[CbbV3OddsPreGameOddsByDateErrorBody]
] = _CbbV3OddsPreGameOddsByDateError()
