from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionError:
    def map(self, response: HttpResponse) -> SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_projections_upcoming_dfs_slates_by_competition_error_mapper: Final[
    ErrorMapper[SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody]
] = _SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionError()
