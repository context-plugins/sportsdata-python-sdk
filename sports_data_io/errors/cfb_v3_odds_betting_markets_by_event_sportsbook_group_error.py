from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsBettingMarketsByEventSportsbookGroupError:
    def map(self, response: HttpResponse) -> CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper: Final[
    ErrorMapper[CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]
] = _CfbV3OddsBettingMarketsByEventSportsbookGroupError()
