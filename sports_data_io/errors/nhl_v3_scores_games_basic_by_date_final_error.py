from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3ScoresGamesBasicByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3ScoresGamesBasicByDateFinalError:
    def map(self, response: HttpResponse) -> NhlV3ScoresGamesBasicByDateFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_scores_games_basic_by_date_final_error_mapper: Final[
    ErrorMapper[NhlV3ScoresGamesBasicByDateFinalErrorBody]
] = _NhlV3ScoresGamesBasicByDateFinalError()
