from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3OddsBettingMarketsByEventErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3OddsBettingMarketsByEventError:
    def map(self, response: HttpResponse) -> MmaV3OddsBettingMarketsByEventErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mma_v3_odds_betting_markets_by_event_error_mapper: Final[
    ErrorMapper[MmaV3OddsBettingMarketsByEventErrorBody]
] = _MmaV3OddsBettingMarketsByEventError()
