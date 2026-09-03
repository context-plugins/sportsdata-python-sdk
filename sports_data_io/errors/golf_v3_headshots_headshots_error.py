from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3HeadshotsHeadshotsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3HeadshotsHeadshotsError:
    def map(self, response: HttpResponse) -> GolfV3HeadshotsHeadshotsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v3_headshots_headshots_error_mapper: Final[
    ErrorMapper[GolfV3HeadshotsHeadshotsErrorBody]
] = _GolfV3HeadshotsHeadshotsError()
