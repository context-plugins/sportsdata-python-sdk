from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3StatsBoxScoreLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3StatsBoxScoreLiveFinalError:
    def map(self, response: HttpResponse) -> NhlV3StatsBoxScoreLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_stats_box_score_live_final_error_mapper: Final[
    ErrorMapper[NhlV3StatsBoxScoreLiveFinalErrorBody]
] = _NhlV3StatsBoxScoreLiveFinalError()
