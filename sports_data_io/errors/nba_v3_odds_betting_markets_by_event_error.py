from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsBettingMarketsByEventErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsBettingMarketsByEventError:
    def map(self, response: HttpResponse) -> NbaV3OddsBettingMarketsByEventErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_odds_betting_markets_by_event_error_mapper: Final[
    ErrorMapper[NbaV3OddsBettingMarketsByEventErrorBody]
] = _NbaV3OddsBettingMarketsByEventError()
