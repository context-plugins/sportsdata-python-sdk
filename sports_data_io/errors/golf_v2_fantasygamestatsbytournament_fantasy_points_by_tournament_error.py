from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentError:
    def map(
        self, status_code: int, content: bytes
    ) -> GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament_error_mapper: Final[
    ErrorMapper[GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody]
] = _GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentError()
