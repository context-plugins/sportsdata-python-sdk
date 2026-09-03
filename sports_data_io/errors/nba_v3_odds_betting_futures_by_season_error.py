from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsBettingFuturesBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsBettingFuturesBySeasonError:
    def map(self, response: HttpResponse) -> NbaV3OddsBettingFuturesBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_odds_betting_futures_by_season_error_mapper: Final[
    ErrorMapper[NbaV3OddsBettingFuturesBySeasonErrorBody]
] = _NbaV3OddsBettingFuturesBySeasonError()
