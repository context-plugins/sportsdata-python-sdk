from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3StatsTeamGameStatsByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3StatsTeamGameStatsByDateFinalError:
    def map(self, response: HttpResponse) -> NbaV3StatsTeamGameStatsByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_stats_team_game_stats_by_date_final_error_mapper: Final[
    ErrorMapper[NbaV3StatsTeamGameStatsByDateFinalErrorBody]
] = _NbaV3StatsTeamGameStatsByDateFinalError()
