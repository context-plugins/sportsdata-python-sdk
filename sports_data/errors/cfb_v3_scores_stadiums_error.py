from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3ScoresStadiumsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3ScoresStadiumsError:
    def map(self, response: HttpResponse) -> CfbV3ScoresStadiumsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_scores_stadiums_error_mapper: Final[ErrorMapper[CfbV3ScoresStadiumsErrorBody]] = _CfbV3ScoresStadiumsError()
