from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresPlayerProfilesByFreeAgentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresPlayerProfilesByFreeAgentError:
    def map(self, response: HttpResponse) -> NflV3ScoresPlayerProfilesByFreeAgentErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_scores_player_profiles_by_free_agent_error_mapper: Final[
    ErrorMapper[NflV3ScoresPlayerProfilesByFreeAgentErrorBody]
] = _NflV3ScoresPlayerProfilesByFreeAgentError()
