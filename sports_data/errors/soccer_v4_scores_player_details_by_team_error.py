from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ScoresPlayerDetailsByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ScoresPlayerDetailsByTeamError:
    def map(self, response: HttpResponse) -> SoccerV4ScoresPlayerDetailsByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_scores_player_details_by_team_error_mapper: Final[
    ErrorMapper[SoccerV4ScoresPlayerDetailsByTeamErrorBody]
] = _SoccerV4ScoresPlayerDetailsByTeamError()
