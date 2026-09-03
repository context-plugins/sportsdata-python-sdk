from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsDfsSlatesByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsDfsSlatesByDateError:
    def map(self, response: HttpResponse) -> NflV3ProjectionsDfsSlatesByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_projections_dfs_slates_by_date_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsDfsSlatesByDateErrorBody]
] = _NflV3ProjectionsDfsSlatesByDateError()
