from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsBettingMarketsByMarketTypeErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsBettingMarketsByMarketTypeError:
    def map(self, status_code: int, content: bytes) -> NhlV3OddsBettingMarketsByMarketTypeErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_odds_betting_markets_by_market_type_error_mapper: Final[
    ErrorMapper[NhlV3OddsBettingMarketsByMarketTypeErrorBody]
] = _NhlV3OddsBettingMarketsByMarketTypeError()
