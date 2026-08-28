from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV3OddsBettingMarketErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV3OddsBettingMarketError:
    def map(self, response: HttpResponse) -> NascarV3OddsBettingMarketErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nascar_v3_odds_betting_market_error_mapper: Final[
    ErrorMapper[NascarV3OddsBettingMarketErrorBody]
] = _NascarV3OddsBettingMarketError()
