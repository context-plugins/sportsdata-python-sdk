from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3PbpPlayByPlayLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3PbpPlayByPlayLiveFinalError:
    def map(self, response: HttpResponse) -> NflV3PbpPlayByPlayLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_pbp_play_by_play_live_final_error_mapper: Final[
    ErrorMapper[NflV3PbpPlayByPlayLiveFinalErrorBody]
] = _NflV3PbpPlayByPlayLiveFinalError()
