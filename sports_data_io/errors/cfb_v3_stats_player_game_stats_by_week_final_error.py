from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3StatsPlayerGameStatsByWeekFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3StatsPlayerGameStatsByWeekFinalError:
    def map(self, status_code: int, content: bytes) -> CfbV3StatsPlayerGameStatsByWeekFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cfb_v3_stats_player_game_stats_by_week_final_error_mapper: Final[
    ErrorMapper[CfbV3StatsPlayerGameStatsByWeekFinalErrorBody]
] = _CfbV3StatsPlayerGameStatsByWeekFinalError()
