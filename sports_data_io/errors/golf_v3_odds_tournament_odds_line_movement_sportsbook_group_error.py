from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsTournamentOddsLineMovementSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v3_odds_tournament_odds_line_movement_sportsbook_group_error_mapper: Final[
    ErrorMapper[GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody]
] = _GolfV3OddsTournamentOddsLineMovementSportsbookGroupError()
