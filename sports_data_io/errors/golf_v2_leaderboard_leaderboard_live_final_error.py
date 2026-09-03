from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2LeaderboardLeaderboardLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2LeaderboardLeaderboardLiveFinalError:
    def map(self, response: HttpResponse) -> GolfV2LeaderboardLeaderboardLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_leaderboard_leaderboard_live_final_error_mapper: Final[
    ErrorMapper[GolfV2LeaderboardLeaderboardLiveFinalErrorBody]
] = _GolfV2LeaderboardLeaderboardLiveFinalError()
