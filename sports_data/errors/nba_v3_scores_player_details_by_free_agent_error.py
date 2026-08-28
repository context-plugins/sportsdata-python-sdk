from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ScoresPlayerDetailsByFreeAgentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ScoresPlayerDetailsByFreeAgentError:
    def map(self, response: HttpResponse) -> NbaV3ScoresPlayerDetailsByFreeAgentErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_scores_player_details_by_free_agent_error_mapper: Final[
    ErrorMapper[NbaV3ScoresPlayerDetailsByFreeAgentErrorBody]
] = _NbaV3ScoresPlayerDetailsByFreeAgentError()
