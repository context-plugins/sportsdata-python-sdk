from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ScoresPlayerProfilesByFreeAgentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ScoresPlayerProfilesByFreeAgentError:
    def map(self, response: HttpResponse) -> NbaV3ScoresPlayerProfilesByFreeAgentErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_scores_player_profiles_by_free_agent_error_mapper: Final[
    ErrorMapper[NbaV3ScoresPlayerProfilesByFreeAgentErrorBody]
] = _NbaV3ScoresPlayerProfilesByFreeAgentError()
