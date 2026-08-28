from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresPlayerDetailsByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresPlayerDetailsByActiveError:
    def map(self, response: HttpResponse) -> WnbaV3ScoresPlayerDetailsByActiveErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


wnba_v3_scores_player_details_by_active_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresPlayerDetailsByActiveErrorBody]
] = _WnbaV3ScoresPlayerDetailsByActiveError()
