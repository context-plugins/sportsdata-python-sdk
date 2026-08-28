from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CwbbV3ScoresTeamProfilesAllErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CwbbV3ScoresTeamProfilesAllError:
    def map(self, response: HttpResponse) -> CwbbV3ScoresTeamProfilesAllErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cwbb_v3_scores_team_profiles_all_error_mapper: Final[
    ErrorMapper[CwbbV3ScoresTeamProfilesAllErrorBody]
] = _CwbbV3ScoresTeamProfilesAllError()
