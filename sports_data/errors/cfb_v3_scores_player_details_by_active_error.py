from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3ScoresPlayerDetailsByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3ScoresPlayerDetailsByActiveError:
    def map(self, response: HttpResponse) -> CfbV3ScoresPlayerDetailsByActiveErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_scores_player_details_by_active_error_mapper: Final[
    ErrorMapper[CfbV3ScoresPlayerDetailsByActiveErrorBody]
] = _CfbV3ScoresPlayerDetailsByActiveError()
