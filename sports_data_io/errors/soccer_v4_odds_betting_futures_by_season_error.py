from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsBettingFuturesBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsBettingFuturesBySeasonError:
    def map(self, response: HttpResponse) -> SoccerV4OddsBettingFuturesBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_odds_betting_futures_by_season_error_mapper: Final[
    ErrorMapper[SoccerV4OddsBettingFuturesBySeasonErrorBody]
] = _SoccerV4OddsBettingFuturesBySeasonError()
