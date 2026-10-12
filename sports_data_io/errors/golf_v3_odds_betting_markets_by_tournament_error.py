from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsBettingMarketsByTournamentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsBettingMarketsByTournamentError:
    def map(self, status_code: int, content: bytes) -> GolfV3OddsBettingMarketsByTournamentErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v3_odds_betting_markets_by_tournament_error_mapper: Final[
    ErrorMapper[GolfV3OddsBettingMarketsByTournamentErrorBody]
] = _GolfV3OddsBettingMarketsByTournamentError()
