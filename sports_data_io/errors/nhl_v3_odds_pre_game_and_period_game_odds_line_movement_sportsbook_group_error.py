from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupError:
    def map(self, response: HttpResponse) -> NhlV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper: Final[
    ErrorMapper[NhlV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]
] = _NhlV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupError()
