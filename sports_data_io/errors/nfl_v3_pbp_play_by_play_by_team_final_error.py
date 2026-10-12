from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3PbpPlayByPlayByTeamFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3PbpPlayByPlayByTeamFinalError:
    def map(self, status_code: int, content: bytes) -> NflV3PbpPlayByPlayByTeamFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_pbp_play_by_play_by_team_final_error_mapper: Final[
    ErrorMapper[NflV3PbpPlayByPlayByTeamFinalErrorBody]
] = _NflV3PbpPlayByPlayByTeamFinalError()
