from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3PbpPlayByPlayFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3PbpPlayByPlayFinalError:
    def map(self, response: HttpResponse) -> NbaV3PbpPlayByPlayFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_pbp_play_by_play_final_error_mapper: Final[
    ErrorMapper[NbaV3PbpPlayByPlayFinalErrorBody]
] = _NbaV3PbpPlayByPlayFinalError()
