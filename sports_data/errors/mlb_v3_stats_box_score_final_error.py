from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3StatsBoxScoreFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3StatsBoxScoreFinalError:
    def map(self, response: HttpResponse) -> MlbV3StatsBoxScoreFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_stats_box_score_final_error_mapper: Final[
    ErrorMapper[MlbV3StatsBoxScoreFinalErrorBody]
] = _MlbV3StatsBoxScoreFinalError()
