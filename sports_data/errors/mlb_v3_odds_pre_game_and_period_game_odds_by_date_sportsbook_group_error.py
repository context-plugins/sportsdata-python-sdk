from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupError:
    def map(self, response: HttpResponse) -> MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error_mapper: Final[
    ErrorMapper[MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]
] = _MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupError()
