from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2RaceresultLeaderboardLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2RaceresultLeaderboardLiveFinalError:
    def map(self, status_code: int, content: bytes) -> NascarV2RaceresultLeaderboardLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nascar_v2_raceresult_leaderboard_live_final_error_mapper: Final[
    ErrorMapper[NascarV2RaceresultLeaderboardLiveFinalErrorBody]
] = _NascarV2RaceresultLeaderboardLiveFinalError()
