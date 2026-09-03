from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsTournamentOddsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsTournamentOddsError:
    def map(self, response: HttpResponse) -> GolfV3OddsTournamentOddsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v3_odds_tournament_odds_error_mapper: Final[
    ErrorMapper[GolfV3OddsTournamentOddsErrorBody]
] = _GolfV3OddsTournamentOddsError()
