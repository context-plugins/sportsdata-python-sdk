from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsBettingMarketsByEventErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsBettingMarketsByEventError:
    def map(self, response: HttpResponse) -> SoccerV4OddsBettingMarketsByEventErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_odds_betting_markets_by_event_error_mapper: Final[
    ErrorMapper[SoccerV4OddsBettingMarketsByEventErrorBody]
] = _SoccerV4OddsBettingMarketsByEventError()
