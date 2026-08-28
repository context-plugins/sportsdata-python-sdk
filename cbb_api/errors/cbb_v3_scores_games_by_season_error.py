from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3ScoresGamesBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3ScoresGamesBySeasonError:
    def map(self, response: HttpResponse) -> CbbV3ScoresGamesBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_scores_games_by_season_error_mapper: Final[
    ErrorMapper[CbbV3ScoresGamesBySeasonErrorBody]
] = _CbbV3ScoresGamesBySeasonError()
