from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ScoresPlayerProfilesByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ScoresPlayerProfilesByActiveError:
    def map(self, status_code: int, content: bytes) -> NbaV3ScoresPlayerProfilesByActiveErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nba_v3_scores_player_profiles_by_active_error_mapper: Final[
    ErrorMapper[NbaV3ScoresPlayerProfilesByActiveErrorBody]
] = _NbaV3ScoresPlayerProfilesByActiveError()
