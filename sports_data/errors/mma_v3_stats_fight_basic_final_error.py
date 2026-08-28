from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3StatsFightBasicFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3StatsFightBasicFinalError:
    def map(self, response: HttpResponse) -> MmaV3StatsFightBasicFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mma_v3_stats_fight_basic_final_error_mapper: Final[
    ErrorMapper[MmaV3StatsFightBasicFinalErrorBody]
] = _MmaV3StatsFightBasicFinalError()
