from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3OddsInGameOddsByWeekSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_odds_in_game_odds_by_week_sportsbook_group_error_mapper: Final[
    ErrorMapper[NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody]
] = _NflV3OddsInGameOddsByWeekSportsbookGroupError()
