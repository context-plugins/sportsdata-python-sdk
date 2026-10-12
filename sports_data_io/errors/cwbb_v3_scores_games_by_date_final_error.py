from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CwbbV3ScoresGamesByDateFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CwbbV3ScoresGamesByDateFinalError:
    def map(self, status_code: int, content: bytes) -> CwbbV3ScoresGamesByDateFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cwbb_v3_scores_games_by_date_final_error_mapper: Final[
    ErrorMapper[CwbbV3ScoresGamesByDateFinalErrorBody]
] = _CwbbV3ScoresGamesByDateFinalError()
