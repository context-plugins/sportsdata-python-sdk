from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2CurrentseasonSeasonCurrentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2CurrentseasonSeasonCurrentError:
    def map(self, response: HttpResponse) -> GolfV2CurrentseasonSeasonCurrentErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_currentseason_season_current_error_mapper: Final[
    ErrorMapper[GolfV2CurrentseasonSeasonCurrentErrorBody]
] = _GolfV2CurrentseasonSeasonCurrentError()
