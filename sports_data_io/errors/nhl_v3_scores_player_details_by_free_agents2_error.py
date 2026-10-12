from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3ScoresPlayerDetailsByFreeAgents2Error:
    def map(self, status_code: int, content: bytes) -> NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_scores_player_details_by_free_agents2_error_mapper: Final[
    ErrorMapper[NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody]
] = _NhlV3ScoresPlayerDetailsByFreeAgents2Error()
