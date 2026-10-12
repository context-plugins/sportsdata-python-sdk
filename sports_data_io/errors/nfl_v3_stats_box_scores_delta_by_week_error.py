from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsBoxScoresDeltaByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsBoxScoresDeltaByWeekError:
    def map(self, status_code: int, content: bytes) -> NflV3StatsBoxScoresDeltaByWeekErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_stats_box_scores_delta_by_week_error_mapper: Final[
    ErrorMapper[NflV3StatsBoxScoresDeltaByWeekErrorBody]
] = _NflV3StatsBoxScoresDeltaByWeekError()
