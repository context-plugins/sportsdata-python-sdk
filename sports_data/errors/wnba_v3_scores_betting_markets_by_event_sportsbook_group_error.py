from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresBettingMarketsByEventSportsbookGroupError:
    def map(self, response: HttpResponse) -> WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


wnba_v3_scores_betting_markets_by_event_sportsbook_group_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody]
] = _WnbaV3ScoresBettingMarketsByEventSportsbookGroupError()
