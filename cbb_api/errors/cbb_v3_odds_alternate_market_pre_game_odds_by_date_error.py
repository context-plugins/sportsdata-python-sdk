from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3OddsAlternateMarketPreGameOddsByDateError:
    def map(self, response: HttpResponse) -> CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_odds_alternate_market_pre_game_odds_by_date_error_mapper: Final[
    ErrorMapper[CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody]
] = _CbbV3OddsAlternateMarketPreGameOddsByDateError()
