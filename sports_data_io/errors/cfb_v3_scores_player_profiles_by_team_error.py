from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3ScoresPlayerProfilesByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3ScoresPlayerProfilesByTeamError:
    def map(self, response: HttpResponse) -> CfbV3ScoresPlayerProfilesByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_scores_player_profiles_by_team_error_mapper: Final[
    ErrorMapper[CfbV3ScoresPlayerProfilesByTeamErrorBody]
] = _CfbV3ScoresPlayerProfilesByTeamError()
