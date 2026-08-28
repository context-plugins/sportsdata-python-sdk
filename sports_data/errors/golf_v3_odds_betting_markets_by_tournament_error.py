from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsBettingMarketsByTournamentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsBettingMarketsByTournamentError:
    def map(self, response: HttpResponse) -> GolfV3OddsBettingMarketsByTournamentErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v3_odds_betting_markets_by_tournament_error_mapper: Final[
    ErrorMapper[GolfV3OddsBettingMarketsByTournamentErrorBody]
] = _GolfV3OddsBettingMarketsByTournamentError()
