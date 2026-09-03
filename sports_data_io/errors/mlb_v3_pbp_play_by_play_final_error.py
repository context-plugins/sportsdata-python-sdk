from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3PbpPlayByPlayFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3PbpPlayByPlayFinalError:
    def map(self, response: HttpResponse) -> MlbV3PbpPlayByPlayFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_pbp_play_by_play_final_error_mapper: Final[
    ErrorMapper[MlbV3PbpPlayByPlayFinalErrorBody]
] = _MlbV3PbpPlayByPlayFinalError()
