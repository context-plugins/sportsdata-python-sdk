from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ScoresPlayerDetailsByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ScoresPlayerDetailsByTeamError:
    def map(self, response: HttpResponse) -> NbaV3ScoresPlayerDetailsByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_scores_player_details_by_team_error_mapper: Final[
    ErrorMapper[NbaV3ScoresPlayerDetailsByTeamErrorBody]
] = _NbaV3ScoresPlayerDetailsByTeamError()
