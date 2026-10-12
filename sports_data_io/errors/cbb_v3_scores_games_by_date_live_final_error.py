from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3ScoresGamesByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3ScoresGamesByDateLiveFinalError:
    def map(self, status_code: int, content: bytes) -> CbbV3ScoresGamesByDateLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cbb_v3_scores_games_by_date_live_final_error_mapper: Final[
    ErrorMapper[CbbV3ScoresGamesByDateLiveFinalErrorBody]
] = _CbbV3ScoresGamesByDateLiveFinalError()
