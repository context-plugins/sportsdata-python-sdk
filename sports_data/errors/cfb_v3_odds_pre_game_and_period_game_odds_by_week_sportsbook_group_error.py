from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupError:
    def map(self, response: HttpResponse) -> CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error_mapper: Final[
    ErrorMapper[CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]
] = _CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupError()
