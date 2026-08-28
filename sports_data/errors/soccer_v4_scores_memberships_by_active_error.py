from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ScoresMembershipsByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ScoresMembershipsByActiveError:
    def map(self, response: HttpResponse) -> SoccerV4ScoresMembershipsByActiveErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_scores_memberships_by_active_error_mapper: Final[
    ErrorMapper[SoccerV4ScoresMembershipsByActiveErrorBody]
] = _SoccerV4ScoresMembershipsByActiveError()
