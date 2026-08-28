from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ProjectionsPlayerDetailsByInjuredError:
    def map(self, response: HttpResponse) -> SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_projections_player_details_by_injured_error_mapper: Final[
    ErrorMapper[SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody]
] = _SoccerV4ProjectionsPlayerDetailsByInjuredError()
