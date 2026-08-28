from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3StatsBoxScoresDeltaByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3StatsBoxScoresDeltaByDateError:
    def map(self, response: HttpResponse) -> NbaV3StatsBoxScoresDeltaByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_stats_box_scores_delta_by_date_error_mapper: Final[
    ErrorMapper[NbaV3StatsBoxScoresDeltaByDateErrorBody]
] = _NbaV3StatsBoxScoresDeltaByDateError()
