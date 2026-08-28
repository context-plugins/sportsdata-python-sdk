from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3ScoresGamesByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3ScoresGamesByDateFinalError:
    def map(self, response: HttpResponse) -> NhlV3ScoresGamesByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_scores_games_by_date_final_error_mapper: Final[
    ErrorMapper[NhlV3ScoresGamesByDateFinalErrorBody]
] = _NhlV3ScoresGamesByDateFinalError()
