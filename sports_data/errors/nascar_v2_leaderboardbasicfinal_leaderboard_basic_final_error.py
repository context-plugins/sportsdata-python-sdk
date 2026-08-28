from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2LeaderboardbasicfinalLeaderboardBasicFinalError:
    def map(self, response: HttpResponse) -> NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nascar_v2_leaderboardbasicfinal_leaderboard_basic_final_error_mapper: Final[
    ErrorMapper[NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody]
] = _NascarV2LeaderboardbasicfinalLeaderboardBasicFinalError()
