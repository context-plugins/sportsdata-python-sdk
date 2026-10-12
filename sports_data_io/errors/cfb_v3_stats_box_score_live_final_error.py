from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3StatsBoxScoreLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3StatsBoxScoreLiveFinalError:
    def map(self, status_code: int, content: bytes) -> CfbV3StatsBoxScoreLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cfb_v3_stats_box_score_live_final_error_mapper: Final[
    ErrorMapper[CfbV3StatsBoxScoreLiveFinalErrorBody]
] = _CfbV3StatsBoxScoreLiveFinalError()
