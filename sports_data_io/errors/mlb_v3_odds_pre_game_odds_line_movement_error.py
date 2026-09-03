from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3OddsPreGameOddsLineMovementErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3OddsPreGameOddsLineMovementError:
    def map(self, response: HttpResponse) -> MlbV3OddsPreGameOddsLineMovementErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_odds_pre_game_odds_line_movement_error_mapper: Final[
    ErrorMapper[MlbV3OddsPreGameOddsLineMovementErrorBody]
] = _MlbV3OddsPreGameOddsLineMovementError()
