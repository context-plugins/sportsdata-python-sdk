from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3ScoresPlayerProfilesByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3ScoresPlayerProfilesByActiveError:
    def map(self, response: HttpResponse) -> MlbV3ScoresPlayerProfilesByActiveErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_scores_player_profiles_by_active_error_mapper: Final[
    ErrorMapper[MlbV3ScoresPlayerProfilesByActiveErrorBody]
] = _MlbV3ScoresPlayerProfilesByActiveError()
