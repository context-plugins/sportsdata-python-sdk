from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresPlayerDetailsByFreeAgentsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresPlayerDetailsByFreeAgentsError:
    def map(self, status_code: int, content: bytes) -> NflV3ScoresPlayerDetailsByFreeAgentsErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_scores_player_details_by_free_agents_error_mapper: Final[
    ErrorMapper[NflV3ScoresPlayerDetailsByFreeAgentsErrorBody]
] = _NflV3ScoresPlayerDetailsByFreeAgentsError()
