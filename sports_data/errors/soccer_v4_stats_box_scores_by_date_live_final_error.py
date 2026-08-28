from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4StatsBoxScoresByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4StatsBoxScoresByDateLiveFinalError:
    def map(self, response: HttpResponse) -> SoccerV4StatsBoxScoresByDateLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_stats_box_scores_by_date_live_final_error_mapper: Final[
    ErrorMapper[SoccerV4StatsBoxScoresByDateLiveFinalErrorBody]
] = _SoccerV4StatsBoxScoresByDateLiveFinalError()
