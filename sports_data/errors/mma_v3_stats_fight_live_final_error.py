from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3StatsFightLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3StatsFightLiveFinalError:
    def map(self, response: HttpResponse) -> MmaV3StatsFightLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mma_v3_stats_fight_live_final_error_mapper: Final[
    ErrorMapper[MmaV3StatsFightLiveFinalErrorBody]
] = _MmaV3StatsFightLiveFinalError()
