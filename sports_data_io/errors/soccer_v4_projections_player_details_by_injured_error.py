from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ProjectionsPlayerDetailsByInjuredError:
    def map(self, status_code: int, content: bytes) -> SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


soccer_v4_projections_player_details_by_injured_error_mapper: Final[
    ErrorMapper[SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody]
] = _SoccerV4ProjectionsPlayerDetailsByInjuredError()
