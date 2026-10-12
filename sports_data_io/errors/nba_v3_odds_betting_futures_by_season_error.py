from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsBettingFuturesBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsBettingFuturesBySeasonError:
    def map(self, status_code: int, content: bytes) -> NbaV3OddsBettingFuturesBySeasonErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nba_v3_odds_betting_futures_by_season_error_mapper: Final[
    ErrorMapper[NbaV3OddsBettingFuturesBySeasonErrorBody]
] = _NbaV3OddsBettingFuturesBySeasonError()
