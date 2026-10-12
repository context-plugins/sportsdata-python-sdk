from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3OddsInGameOddsLineMovementSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


mlb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper: Final[
    ErrorMapper[MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]
] = _MlbV3OddsInGameOddsLineMovementSportsbookGroupError()
