from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3StatsTeamGameStatsByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3StatsTeamGameStatsByDateFinalError:
    def map(self, status_code: int, content: bytes) -> CbbV3StatsTeamGameStatsByDateFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cbb_v3_stats_team_game_stats_by_date_final_error_mapper: Final[
    ErrorMapper[CbbV3StatsTeamGameStatsByDateFinalErrorBody]
] = _CbbV3StatsTeamGameStatsByDateFinalError()
