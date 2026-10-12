from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2DfsslatesbytournamentDfsSlatesByTournamentError:
    def map(self, status_code: int, content: bytes) -> GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_dfsslatesbytournament_dfs_slates_by_tournament_error_mapper: Final[
    ErrorMapper[GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody]
] = _GolfV2DfsslatesbytournamentDfsSlatesByTournamentError()
