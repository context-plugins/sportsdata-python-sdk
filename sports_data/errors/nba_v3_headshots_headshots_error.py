from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3HeadshotsHeadshotsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3HeadshotsHeadshotsError:
    def map(self, response: HttpResponse) -> NbaV3HeadshotsHeadshotsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_headshots_headshots_error_mapper: Final[
    ErrorMapper[NbaV3HeadshotsHeadshotsErrorBody]
] = _NbaV3HeadshotsHeadshotsError()
