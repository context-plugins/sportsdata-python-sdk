from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4StatsBoxScoreLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4StatsBoxScoreLiveFinalError:
    def map(self, status_code: int, content: bytes) -> SoccerV4StatsBoxScoreLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


soccer_v4_stats_box_score_live_final_error_mapper: Final[
    ErrorMapper[SoccerV4StatsBoxScoreLiveFinalErrorBody]
] = _SoccerV4StatsBoxScoreLiveFinalError()
