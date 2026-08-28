from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3ProjectionsDfsSlatesByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3ProjectionsDfsSlatesByDateError:
    def map(self, response: HttpResponse) -> MlbV3ProjectionsDfsSlatesByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_projections_dfs_slates_by_date_error_mapper: Final[
    ErrorMapper[MlbV3ProjectionsDfsSlatesByDateErrorBody]
] = _MlbV3ProjectionsDfsSlatesByDateError()
