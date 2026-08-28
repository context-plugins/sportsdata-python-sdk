from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3OddsBettingMarketsByMarketTypeErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3OddsBettingMarketsByMarketTypeError:
    def map(self, response: HttpResponse) -> MmaV3OddsBettingMarketsByMarketTypeErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mma_v3_odds_betting_markets_by_market_type_error_mapper: Final[
    ErrorMapper[MmaV3OddsBettingMarketsByMarketTypeErrorBody]
] = _MmaV3OddsBettingMarketsByMarketTypeError()
