from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2TournamentsScheduleBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2TournamentsScheduleBySeasonError:
    def map(self, response: HttpResponse) -> GolfV2TournamentsScheduleBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_tournaments_schedule_by_season_error_mapper: Final[
    ErrorMapper[GolfV2TournamentsScheduleBySeasonErrorBody]
] = _GolfV2TournamentsScheduleBySeasonError()
