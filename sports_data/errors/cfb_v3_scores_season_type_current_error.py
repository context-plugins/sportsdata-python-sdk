from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3ScoresSeasonTypeCurrentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3ScoresSeasonTypeCurrentError:
    def map(self, response: HttpResponse) -> CfbV3ScoresSeasonTypeCurrentErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_scores_season_type_current_error_mapper: Final[
    ErrorMapper[CfbV3ScoresSeasonTypeCurrentErrorBody]
] = _CfbV3ScoresSeasonTypeCurrentError()
