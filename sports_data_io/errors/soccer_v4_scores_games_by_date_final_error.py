from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ScoresGamesByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ScoresGamesByDateFinalError:
    def map(self, response: HttpResponse) -> SoccerV4ScoresGamesByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_scores_games_by_date_final_error_mapper: Final[
    ErrorMapper[SoccerV4ScoresGamesByDateFinalErrorBody]
] = _SoccerV4ScoresGamesByDateFinalError()
