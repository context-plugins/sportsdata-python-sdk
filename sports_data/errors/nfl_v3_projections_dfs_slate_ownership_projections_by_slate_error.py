from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateError:
    def map(self, response: HttpResponse) -> NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_projections_dfs_slate_ownership_projections_by_slate_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody]
] = _NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateError()
