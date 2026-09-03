from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresTeamGameStatsByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresTeamGameStatsByDateFinalError:
    def map(self, response: HttpResponse) -> WnbaV3ScoresTeamGameStatsByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


wnba_v3_scores_team_game_stats_by_date_final_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresTeamGameStatsByDateFinalErrorBody]
] = _WnbaV3ScoresTeamGameStatsByDateFinalError()
