from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupError:
    def map(self, response: HttpResponse) -> CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper: Final[
    ErrorMapper[CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]
] = _CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupError()
