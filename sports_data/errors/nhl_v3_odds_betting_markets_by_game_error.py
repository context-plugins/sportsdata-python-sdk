from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsBettingMarketsByGameErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsBettingMarketsByGameError:
    def map(self, response: HttpResponse) -> NhlV3OddsBettingMarketsByGameErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_odds_betting_markets_by_game_error_mapper: Final[
    ErrorMapper[NhlV3OddsBettingMarketsByGameErrorBody]
] = _NhlV3OddsBettingMarketsByGameError()
