from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> NhlV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error_mapper: Final[
    ErrorMapper[NhlV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]
] = _NhlV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupError()
