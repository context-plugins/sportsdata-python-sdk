from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2LeaderboardbasicLeaderboardBasicErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2LeaderboardbasicLeaderboardBasicError:
    def map(self, status_code: int, content: bytes) -> GolfV2LeaderboardbasicLeaderboardBasicErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_leaderboardbasic_leaderboard_basic_error_mapper: Final[
    ErrorMapper[GolfV2LeaderboardbasicLeaderboardBasicErrorBody]
] = _GolfV2LeaderboardbasicLeaderboardBasicError()
