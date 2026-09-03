from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsPeriodGameOddsByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsPeriodGameOddsByWeekError:
    def map(self, response: HttpResponse) -> CfbV3OddsPeriodGameOddsByWeekErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_period_game_odds_by_week_error_mapper: Final[
    ErrorMapper[CfbV3OddsPeriodGameOddsByWeekErrorBody]
] = _CfbV3OddsPeriodGameOddsByWeekError()
