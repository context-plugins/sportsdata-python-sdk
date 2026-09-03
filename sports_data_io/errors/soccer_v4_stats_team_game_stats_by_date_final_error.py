from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4StatsTeamGameStatsByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4StatsTeamGameStatsByDateFinalError:
    def map(self, response: HttpResponse) -> SoccerV4StatsTeamGameStatsByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_stats_team_game_stats_by_date_final_error_mapper: Final[
    ErrorMapper[SoccerV4StatsTeamGameStatsByDateFinalErrorBody]
] = _SoccerV4StatsTeamGameStatsByDateFinalError()
