from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3StatsBoxScoresByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3StatsBoxScoresByDateFinalError:
    def map(self, response: HttpResponse) -> CbbV3StatsBoxScoresByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_stats_box_scores_by_date_final_error_mapper: Final[
    ErrorMapper[CbbV3StatsBoxScoresByDateFinalErrorBody]
] = _CbbV3StatsBoxScoresByDateFinalError()
