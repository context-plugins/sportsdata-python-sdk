from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsBettingMarketsByEventErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsBettingMarketsByEventError:
    def map(self, status_code: int, content: bytes) -> SoccerV4OddsBettingMarketsByEventErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


soccer_v4_odds_betting_markets_by_event_error_mapper: Final[
    ErrorMapper[SoccerV4OddsBettingMarketsByEventErrorBody]
] = _SoccerV4OddsBettingMarketsByEventError()
