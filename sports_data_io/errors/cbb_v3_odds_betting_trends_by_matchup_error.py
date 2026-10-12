from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CbbV3OddsBettingTrendsByMatchupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CbbV3OddsBettingTrendsByMatchupError:
    def map(self, status_code: int, content: bytes) -> CbbV3OddsBettingTrendsByMatchupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cbb_v3_odds_betting_trends_by_matchup_error_mapper: Final[
    ErrorMapper[CbbV3OddsBettingTrendsByMatchupErrorBody]
] = _CbbV3OddsBettingTrendsByMatchupError()
