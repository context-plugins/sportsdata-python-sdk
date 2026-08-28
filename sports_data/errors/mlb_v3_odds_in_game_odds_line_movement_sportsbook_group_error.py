from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3OddsInGameOddsLineMovementSportsbookGroupError:
    def map(self, response: HttpResponse) -> MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper: Final[
    ErrorMapper[MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]
] = _MlbV3OddsInGameOddsLineMovementSportsbookGroupError()
