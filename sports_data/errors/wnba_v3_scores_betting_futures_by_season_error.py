from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresBettingFuturesBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresBettingFuturesBySeasonError:
    def map(self, response: HttpResponse) -> WnbaV3ScoresBettingFuturesBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


wnba_v3_scores_betting_futures_by_season_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresBettingFuturesBySeasonErrorBody]
] = _WnbaV3ScoresBettingFuturesBySeasonError()
