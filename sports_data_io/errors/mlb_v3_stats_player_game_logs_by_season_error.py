from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3StatsPlayerGameLogsBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3StatsPlayerGameLogsBySeasonError:
    def map(self, status_code: int, content: bytes) -> MlbV3StatsPlayerGameLogsBySeasonErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


mlb_v3_stats_player_game_logs_by_season_error_mapper: Final[
    ErrorMapper[MlbV3StatsPlayerGameLogsBySeasonErrorBody]
] = _MlbV3StatsPlayerGameLogsBySeasonError()
