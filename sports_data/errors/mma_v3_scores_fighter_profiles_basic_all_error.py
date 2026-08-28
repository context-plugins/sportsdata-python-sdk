from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3ScoresFighterProfilesBasicAllErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3ScoresFighterProfilesBasicAllError:
    def map(self, response: HttpResponse) -> MmaV3ScoresFighterProfilesBasicAllErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mma_v3_scores_fighter_profiles_basic_all_error_mapper: Final[
    ErrorMapper[MmaV3ScoresFighterProfilesBasicAllErrorBody]
] = _MmaV3ScoresFighterProfilesBasicAllError()
