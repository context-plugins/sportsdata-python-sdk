from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2RaceresultfinalLeaderboardFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2RaceresultfinalLeaderboardFinalError:
    def map(self, response: HttpResponse) -> NascarV2RaceresultfinalLeaderboardFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nascar_v2_raceresultfinal_leaderboard_final_error_mapper: Final[
    ErrorMapper[NascarV2RaceresultfinalLeaderboardFinalErrorBody]
] = _NascarV2RaceresultfinalLeaderboardFinalError()
