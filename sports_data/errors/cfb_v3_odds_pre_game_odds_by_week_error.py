from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsPreGameOddsByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsPreGameOddsByWeekError:
    def map(self, response: HttpResponse) -> CfbV3OddsPreGameOddsByWeekErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_pre_game_odds_by_week_error_mapper: Final[
    ErrorMapper[CfbV3OddsPreGameOddsByWeekErrorBody]
] = _CfbV3OddsPreGameOddsByWeekError()
