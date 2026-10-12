from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2LeaderboardbasicfinalLeaderboardBasicFinalError:
    def map(self, status_code: int, content: bytes) -> GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_leaderboardbasicfinal_leaderboard_basic_final_error_mapper: Final[
    ErrorMapper[GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody]
] = _GolfV2LeaderboardbasicfinalLeaderboardBasicFinalError()
