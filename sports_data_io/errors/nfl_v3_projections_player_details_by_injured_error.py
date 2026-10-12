from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsPlayerDetailsByInjuredErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsPlayerDetailsByInjuredError:
    def map(self, status_code: int, content: bytes) -> NflV3ProjectionsPlayerDetailsByInjuredErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_projections_player_details_by_injured_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsPlayerDetailsByInjuredErrorBody]
] = _NflV3ProjectionsPlayerDetailsByInjuredError()
