from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsBettingMarketSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsBettingMarketSportsbookGroupError:
    def map(self, response: HttpResponse) -> NbaV3OddsBettingMarketSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_odds_betting_market_sportsbook_group_error_mapper: Final[
    ErrorMapper[NbaV3OddsBettingMarketSportsbookGroupErrorBody]
] = _NbaV3OddsBettingMarketSportsbookGroupError()
