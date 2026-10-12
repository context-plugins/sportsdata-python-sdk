from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3StatsBoxScoresByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3StatsBoxScoresByDateLiveFinalError:
    def map(self, status_code: int, content: bytes) -> CbbV3StatsBoxScoresByDateLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cbb_v3_stats_box_scores_by_date_live_final_error_mapper: Final[
    ErrorMapper[CbbV3StatsBoxScoresByDateLiveFinalErrorBody]
] = _CbbV3StatsBoxScoresByDateLiveFinalError()
