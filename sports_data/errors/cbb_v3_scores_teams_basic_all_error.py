from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3ScoresTeamsBasicAllErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3ScoresTeamsBasicAllError:
    def map(self, response: HttpResponse) -> CbbV3ScoresTeamsBasicAllErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_scores_teams_basic_all_error_mapper: Final[
    ErrorMapper[CbbV3ScoresTeamsBasicAllErrorBody]
] = _CbbV3ScoresTeamsBasicAllError()
