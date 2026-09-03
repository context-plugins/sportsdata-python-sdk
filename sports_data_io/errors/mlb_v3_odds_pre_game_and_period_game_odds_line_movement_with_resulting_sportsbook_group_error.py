from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupError:
    def map(
        self, response: HttpResponse
    ) -> MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper: Final[
    ErrorMapper[MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]
] = _MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupError()
