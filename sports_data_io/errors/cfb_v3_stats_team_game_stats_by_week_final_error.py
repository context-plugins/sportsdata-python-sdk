from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3StatsTeamGameStatsByWeekFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3StatsTeamGameStatsByWeekFinalError:
    def map(self, status_code: int, content: bytes) -> CfbV3StatsTeamGameStatsByWeekFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cfb_v3_stats_team_game_stats_by_week_final_error_mapper: Final[
    ErrorMapper[CfbV3StatsTeamGameStatsByWeekFinalErrorBody]
] = _CfbV3StatsTeamGameStatsByWeekFinalError()
