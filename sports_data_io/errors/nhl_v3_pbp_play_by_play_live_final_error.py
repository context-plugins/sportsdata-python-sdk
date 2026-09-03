from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3PbpPlayByPlayLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3PbpPlayByPlayLiveFinalError:
    def map(self, response: HttpResponse) -> NhlV3PbpPlayByPlayLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_pbp_play_by_play_live_final_error_mapper: Final[
    ErrorMapper[NhlV3PbpPlayByPlayLiveFinalErrorBody]
] = _NhlV3PbpPlayByPlayLiveFinalError()
