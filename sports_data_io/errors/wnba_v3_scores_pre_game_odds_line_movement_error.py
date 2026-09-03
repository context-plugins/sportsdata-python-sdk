from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresPreGameOddsLineMovementErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresPreGameOddsLineMovementError:
    def map(self, response: HttpResponse) -> WnbaV3ScoresPreGameOddsLineMovementErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


wnba_v3_scores_pre_game_odds_line_movement_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresPreGameOddsLineMovementErrorBody]
] = _WnbaV3ScoresPreGameOddsLineMovementError()
