from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsTournamentOddsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsTournamentOddsError:
    def map(self, status_code: int, content: bytes) -> GolfV3OddsTournamentOddsErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v3_odds_tournament_odds_error_mapper: Final[
    ErrorMapper[GolfV3OddsTournamentOddsErrorBody]
] = _GolfV3OddsTournamentOddsError()
