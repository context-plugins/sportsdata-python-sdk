from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupError:
    def map(
        self, status_code: int, content: bytes
    ) -> NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper: Final[
    ErrorMapper[NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]
] = _NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupError()
