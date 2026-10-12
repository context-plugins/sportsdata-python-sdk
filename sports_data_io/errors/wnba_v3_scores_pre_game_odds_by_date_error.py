from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresPreGameOddsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresPreGameOddsByDateError:
    def map(self, status_code: int, content: bytes) -> WnbaV3ScoresPreGameOddsByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


wnba_v3_scores_pre_game_odds_by_date_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresPreGameOddsByDateErrorBody]
] = _WnbaV3ScoresPreGameOddsByDateError()
