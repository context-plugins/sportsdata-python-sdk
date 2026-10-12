from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3OddsAlternateMarketPreGameOddsByDateError:
    def map(self, status_code: int, content: bytes) -> CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cbb_v3_odds_alternate_market_pre_game_odds_by_date_error_mapper: Final[
    ErrorMapper[CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody]
] = _CbbV3OddsAlternateMarketPreGameOddsByDateError()
