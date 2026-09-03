from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ScoresPlayerProfilesByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ScoresPlayerProfilesByTeamError:
    def map(self, response: HttpResponse) -> SoccerV4ScoresPlayerProfilesByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_scores_player_profiles_by_team_error_mapper: Final[
    ErrorMapper[SoccerV4ScoresPlayerProfilesByTeamErrorBody]
] = _SoccerV4ScoresPlayerProfilesByTeamError()
