from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsBettingMarketsByGameSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


soccer_v4_odds_betting_markets_by_game_sportsbook_group_error_mapper: Final[
    ErrorMapper[SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody]
] = _SoccerV4OddsBettingMarketsByGameSportsbookGroupError()
