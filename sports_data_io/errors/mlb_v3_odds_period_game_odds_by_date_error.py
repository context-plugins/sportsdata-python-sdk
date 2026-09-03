from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3OddsPeriodGameOddsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3OddsPeriodGameOddsByDateError:
    def map(self, response: HttpResponse) -> MlbV3OddsPeriodGameOddsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_odds_period_game_odds_by_date_error_mapper: Final[
    ErrorMapper[MlbV3OddsPeriodGameOddsByDateErrorBody]
] = _MlbV3OddsPeriodGameOddsByDateError()
