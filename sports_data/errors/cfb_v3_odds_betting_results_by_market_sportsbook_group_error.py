from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsBettingResultsByMarketSportsbookGroupError:
    def map(self, response: HttpResponse) -> CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_betting_results_by_market_sportsbook_group_error_mapper: Final[
    ErrorMapper[CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]
] = _CfbV3OddsBettingResultsByMarketSportsbookGroupError()
