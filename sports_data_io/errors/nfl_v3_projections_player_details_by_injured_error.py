from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsPlayerDetailsByInjuredErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsPlayerDetailsByInjuredError:
    def map(self, response: HttpResponse) -> NflV3ProjectionsPlayerDetailsByInjuredErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_projections_player_details_by_injured_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsPlayerDetailsByInjuredErrorBody]
] = _NflV3ProjectionsPlayerDetailsByInjuredError()
