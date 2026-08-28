from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3OddsBettingMarketSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3OddsBettingMarketSportsbookGroupError:
    def map(self, response: HttpResponse) -> CbbV3OddsBettingMarketSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_odds_betting_market_sportsbook_group_error_mapper: Final[
    ErrorMapper[CbbV3OddsBettingMarketSportsbookGroupErrorBody]
] = _CbbV3OddsBettingMarketSportsbookGroupError()
