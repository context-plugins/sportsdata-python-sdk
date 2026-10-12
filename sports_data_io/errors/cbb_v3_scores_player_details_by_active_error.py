from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3ScoresPlayerDetailsByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3ScoresPlayerDetailsByActiveError:
    def map(self, status_code: int, content: bytes) -> CbbV3ScoresPlayerDetailsByActiveErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cbb_v3_scores_player_details_by_active_error_mapper: Final[
    ErrorMapper[CbbV3ScoresPlayerDetailsByActiveErrorBody]
] = _CbbV3ScoresPlayerDetailsByActiveError()
