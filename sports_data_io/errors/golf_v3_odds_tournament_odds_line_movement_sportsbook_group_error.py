from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsTournamentOddsLineMovementSportsbookGroupError:
    def map(self, response: HttpResponse) -> GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v3_odds_tournament_odds_line_movement_sportsbook_group_error_mapper: Final[
    ErrorMapper[GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody]
] = _GolfV3OddsTournamentOddsLineMovementSportsbookGroupError()
