from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


wnba_v3_scores_betting_markets_by_market_type_sportsbook_group_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody]
] = _WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupError()
