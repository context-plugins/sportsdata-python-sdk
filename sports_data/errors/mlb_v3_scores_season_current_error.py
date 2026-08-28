from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3ScoresSeasonCurrentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3ScoresSeasonCurrentError:
    def map(self, response: HttpResponse) -> MlbV3ScoresSeasonCurrentErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_scores_season_current_error_mapper: Final[
    ErrorMapper[MlbV3ScoresSeasonCurrentErrorBody]
] = _MlbV3ScoresSeasonCurrentError()
