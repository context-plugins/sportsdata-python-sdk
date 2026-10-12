from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody: TypeAlias = (
    Unauthorized | RawError
)


@dataclass(frozen=True, slots=True)
class _GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateError:
    def map(
        self, status_code: int, content: bytes
    ) -> GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate_error_mapper: Final[
    ErrorMapper[GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody]
] = _GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateError()
