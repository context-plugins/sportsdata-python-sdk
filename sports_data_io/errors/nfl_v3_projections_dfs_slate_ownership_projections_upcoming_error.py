from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingError:
    def map(self, status_code: int, content: bytes) -> NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_projections_dfs_slate_ownership_projections_upcoming_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody]
] = _NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingError()
