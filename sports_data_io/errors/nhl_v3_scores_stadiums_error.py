from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3ScoresStadiumsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3ScoresStadiumsError:
    def map(self, response: HttpResponse) -> NhlV3ScoresStadiumsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_scores_stadiums_error_mapper: Final[ErrorMapper[NhlV3ScoresStadiumsErrorBody]] = _NhlV3ScoresStadiumsError()
