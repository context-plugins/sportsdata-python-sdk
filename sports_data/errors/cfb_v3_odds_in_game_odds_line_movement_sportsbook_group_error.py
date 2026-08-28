from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsInGameOddsLineMovementSportsbookGroupError:
    def map(self, response: HttpResponse) -> CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper: Final[
    ErrorMapper[CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]
] = _CfbV3OddsInGameOddsLineMovementSportsbookGroupError()
