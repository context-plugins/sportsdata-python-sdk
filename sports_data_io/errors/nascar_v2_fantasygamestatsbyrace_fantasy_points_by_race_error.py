from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2FantasygamestatsbyraceFantasyPointsByRaceError:
    def map(self, response: HttpResponse) -> NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race_error_mapper: Final[
    ErrorMapper[NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody]
] = _NascarV2FantasygamestatsbyraceFantasyPointsByRaceError()
