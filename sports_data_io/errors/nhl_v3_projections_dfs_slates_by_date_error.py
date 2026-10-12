from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3ProjectionsDfsSlatesByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3ProjectionsDfsSlatesByDateError:
    def map(self, status_code: int, content: bytes) -> NhlV3ProjectionsDfsSlatesByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_projections_dfs_slates_by_date_error_mapper: Final[
    ErrorMapper[NhlV3ProjectionsDfsSlatesByDateErrorBody]
] = _NhlV3ProjectionsDfsSlatesByDateError()
