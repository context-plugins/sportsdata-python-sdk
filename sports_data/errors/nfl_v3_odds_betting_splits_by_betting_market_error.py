from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3OddsBettingSplitsByBettingMarketErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3OddsBettingSplitsByBettingMarketError:
    def map(self, response: HttpResponse) -> NflV3OddsBettingSplitsByBettingMarketErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_odds_betting_splits_by_betting_market_error_mapper: Final[
    ErrorMapper[NflV3OddsBettingSplitsByBettingMarketErrorBody]
] = _NflV3OddsBettingSplitsByBettingMarketError()
