from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ProjectionsDfsSlatesByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ProjectionsDfsSlatesByDateError:
    def map(self, response: HttpResponse) -> SoccerV4ProjectionsDfsSlatesByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_projections_dfs_slates_by_date_error_mapper: Final[
    ErrorMapper[SoccerV4ProjectionsDfsSlatesByDateErrorBody]
] = _SoccerV4ProjectionsDfsSlatesByDateError()
