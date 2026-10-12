from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupError:
    def map(
        self, status_code: int, content: bytes
    ) -> SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper: Final[
    ErrorMapper[SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]
] = _SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupError()
