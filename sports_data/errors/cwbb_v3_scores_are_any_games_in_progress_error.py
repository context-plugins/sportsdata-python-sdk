from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CwbbV3ScoresAreAnyGamesInProgressErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CwbbV3ScoresAreAnyGamesInProgressError:
    def map(self, response: HttpResponse) -> CwbbV3ScoresAreAnyGamesInProgressErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cwbb_v3_scores_are_any_games_in_progress_error_mapper: Final[
    ErrorMapper[CwbbV3ScoresAreAnyGamesInProgressErrorBody]
] = _CwbbV3ScoresAreAnyGamesInProgressError()
