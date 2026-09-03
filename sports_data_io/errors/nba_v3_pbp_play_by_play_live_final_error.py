from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3PbpPlayByPlayLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3PbpPlayByPlayLiveFinalError:
    def map(self, response: HttpResponse) -> NbaV3PbpPlayByPlayLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_pbp_play_by_play_live_final_error_mapper: Final[
    ErrorMapper[NbaV3PbpPlayByPlayLiveFinalErrorBody]
] = _NbaV3PbpPlayByPlayLiveFinalError()
