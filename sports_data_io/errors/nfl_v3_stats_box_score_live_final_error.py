from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsBoxScoreLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsBoxScoreLiveFinalError:
    def map(self, status_code: int, content: bytes) -> NflV3StatsBoxScoreLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_stats_box_score_live_final_error_mapper: Final[
    ErrorMapper[NflV3StatsBoxScoreLiveFinalErrorBody]
] = _NflV3StatsBoxScoreLiveFinalError()
