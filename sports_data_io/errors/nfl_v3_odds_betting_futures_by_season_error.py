from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3OddsBettingFuturesBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3OddsBettingFuturesBySeasonError:
    def map(self, response: HttpResponse) -> NflV3OddsBettingFuturesBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_odds_betting_futures_by_season_error_mapper: Final[
    ErrorMapper[NflV3OddsBettingFuturesBySeasonErrorBody]
] = _NflV3OddsBettingFuturesBySeasonError()
