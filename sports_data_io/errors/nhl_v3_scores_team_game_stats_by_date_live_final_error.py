from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3ScoresTeamGameStatsByDateLiveFinalError:
    def map(self, status_code: int, content: bytes) -> NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_scores_team_game_stats_by_date_live_final_error_mapper: Final[
    ErrorMapper[NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody]
] = _NhlV3ScoresTeamGameStatsByDateLiveFinalError()
