from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ScoresTeamGameStatsByDateLiveFinalError:
    def map(self, response: HttpResponse) -> SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_scores_team_game_stats_by_date_live_final_error_mapper: Final[
    ErrorMapper[SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody]
] = _SoccerV4ScoresTeamGameStatsByDateLiveFinalError()
