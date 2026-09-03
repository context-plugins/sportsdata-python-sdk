from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3OddsBettingEventsBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3OddsBettingEventsBySeasonError:
    def map(self, response: HttpResponse) -> CbbV3OddsBettingEventsBySeasonErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_odds_betting_events_by_season_error_mapper: Final[
    ErrorMapper[CbbV3OddsBettingEventsBySeasonErrorBody]
] = _CbbV3OddsBettingEventsBySeasonError()
