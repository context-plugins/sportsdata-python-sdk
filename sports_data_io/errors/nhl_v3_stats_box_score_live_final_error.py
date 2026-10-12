from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3StatsBoxScoreLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3StatsBoxScoreLiveFinalError:
    def map(self, status_code: int, content: bytes) -> NhlV3StatsBoxScoreLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_stats_box_score_live_final_error_mapper: Final[
    ErrorMapper[NhlV3StatsBoxScoreLiveFinalErrorBody]
] = _NhlV3StatsBoxScoreLiveFinalError()
