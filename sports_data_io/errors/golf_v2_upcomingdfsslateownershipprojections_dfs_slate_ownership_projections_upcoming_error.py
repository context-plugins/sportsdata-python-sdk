from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody: TypeAlias = (
    Unauthorized | RawError
)


@dataclass(frozen=True, slots=True)
class _GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingError:
    def map(
        self, response: HttpResponse
    ) -> GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming_error_mapper: Final[
    ErrorMapper[GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody]
] = _GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingError()
