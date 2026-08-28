from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3ScoresPlayerDetailsByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3ScoresPlayerDetailsByActiveError:
    def map(self, response: HttpResponse) -> MlbV3ScoresPlayerDetailsByActiveErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_scores_player_details_by_active_error_mapper: Final[
    ErrorMapper[MlbV3ScoresPlayerDetailsByActiveErrorBody]
] = _MlbV3ScoresPlayerDetailsByActiveError()
