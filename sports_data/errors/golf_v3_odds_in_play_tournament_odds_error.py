from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsInPlayTournamentOddsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsInPlayTournamentOddsError:
    def map(self, response: HttpResponse) -> GolfV3OddsInPlayTournamentOddsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v3_odds_in_play_tournament_odds_error_mapper: Final[
    ErrorMapper[GolfV3OddsInPlayTournamentOddsErrorBody]
] = _GolfV3OddsInPlayTournamentOddsError()
