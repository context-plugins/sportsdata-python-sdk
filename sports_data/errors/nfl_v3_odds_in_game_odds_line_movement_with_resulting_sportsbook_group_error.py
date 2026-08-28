from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupError:
    def map(self, response: HttpResponse) -> NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper: Final[
    ErrorMapper[NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]
] = _NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupError()
