from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3StatsBoxScoreFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3StatsBoxScoreFinalError:
    def map(self, response: HttpResponse) -> NhlV3StatsBoxScoreFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_stats_box_score_final_error_mapper: Final[
    ErrorMapper[NhlV3StatsBoxScoreFinalErrorBody]
] = _NhlV3StatsBoxScoreFinalError()
