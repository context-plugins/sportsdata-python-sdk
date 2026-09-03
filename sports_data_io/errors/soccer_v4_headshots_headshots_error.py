from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4HeadshotsHeadshotsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4HeadshotsHeadshotsError:
    def map(self, response: HttpResponse) -> SoccerV4HeadshotsHeadshotsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_headshots_headshots_error_mapper: Final[
    ErrorMapper[SoccerV4HeadshotsHeadshotsErrorBody]
] = _SoccerV4HeadshotsHeadshotsError()
