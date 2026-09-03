from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3OddsBettingResultsByMarketErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3OddsBettingResultsByMarketError:
    def map(self, response: HttpResponse) -> NflV3OddsBettingResultsByMarketErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_odds_betting_results_by_market_error_mapper: Final[
    ErrorMapper[NflV3OddsBettingResultsByMarketErrorBody]
] = _NflV3OddsBettingResultsByMarketError()
