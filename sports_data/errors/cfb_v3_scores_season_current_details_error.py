from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3ScoresSeasonCurrentDetailsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3ScoresSeasonCurrentDetailsError:
    def map(self, response: HttpResponse) -> CfbV3ScoresSeasonCurrentDetailsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_scores_season_current_details_error_mapper: Final[
    ErrorMapper[CfbV3ScoresSeasonCurrentDetailsErrorBody]
] = _CfbV3ScoresSeasonCurrentDetailsError()
