from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsBettingMarketsByMarketTypeErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsBettingMarketsByMarketTypeError:
    def map(self, response: HttpResponse) -> NbaV3OddsBettingMarketsByMarketTypeErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_odds_betting_markets_by_market_type_error_mapper: Final[
    ErrorMapper[NbaV3OddsBettingMarketsByMarketTypeErrorBody]
] = _NbaV3OddsBettingMarketsByMarketTypeError()
