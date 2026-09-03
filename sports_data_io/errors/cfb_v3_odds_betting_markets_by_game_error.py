from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsBettingMarketsByGameErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsBettingMarketsByGameError:
    def map(self, response: HttpResponse) -> CfbV3OddsBettingMarketsByGameErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_betting_markets_by_game_error_mapper: Final[
    ErrorMapper[CfbV3OddsBettingMarketsByGameErrorBody]
] = _CfbV3OddsBettingMarketsByGameError()
