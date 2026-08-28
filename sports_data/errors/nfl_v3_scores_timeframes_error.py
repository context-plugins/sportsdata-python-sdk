from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresTimeframesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresTimeframesError:
    def map(self, response: HttpResponse) -> NflV3ScoresTimeframesErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_scores_timeframes_error_mapper: Final[
    ErrorMapper[NflV3ScoresTimeframesErrorBody]
] = _NflV3ScoresTimeframesError()
