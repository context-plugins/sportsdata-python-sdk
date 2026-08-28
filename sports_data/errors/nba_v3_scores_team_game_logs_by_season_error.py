from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ScoresTeamGameLogsBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ScoresTeamGameLogsBySeasonError:
    def map(self, response: HttpResponse) -> NbaV3ScoresTeamGameLogsBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_scores_team_game_logs_by_season_error_mapper: Final[
    ErrorMapper[NbaV3ScoresTeamGameLogsBySeasonErrorBody]
] = _NbaV3ScoresTeamGameLogsBySeasonError()
