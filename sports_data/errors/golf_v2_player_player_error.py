from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2PlayerPlayerErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2PlayerPlayerError:
    def map(self, response: HttpResponse) -> GolfV2PlayerPlayerErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_player_player_error_mapper: Final[ErrorMapper[GolfV2PlayerPlayerErrorBody]] = _GolfV2PlayerPlayerError()
