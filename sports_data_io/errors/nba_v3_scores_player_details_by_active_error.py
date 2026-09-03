from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ScoresPlayerDetailsByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ScoresPlayerDetailsByActiveError:
    def map(self, response: HttpResponse) -> NbaV3ScoresPlayerDetailsByActiveErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_scores_player_details_by_active_error_mapper: Final[
    ErrorMapper[NbaV3ScoresPlayerDetailsByActiveErrorBody]
] = _NbaV3ScoresPlayerDetailsByActiveError()
