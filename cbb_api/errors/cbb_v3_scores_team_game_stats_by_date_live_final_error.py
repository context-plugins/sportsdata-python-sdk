from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3ScoresTeamGameStatsByDateLiveFinalError:
    def map(self, response: HttpResponse) -> CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_scores_team_game_stats_by_date_live_final_error_mapper: Final[
    ErrorMapper[CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody]
] = _CbbV3ScoresTeamGameStatsByDateLiveFinalError()
