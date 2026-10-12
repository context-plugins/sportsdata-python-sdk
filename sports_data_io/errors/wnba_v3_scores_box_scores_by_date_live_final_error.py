from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresBoxScoresByDateLiveFinalError:
    def map(self, status_code: int, content: bytes) -> WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


wnba_v3_scores_box_scores_by_date_live_final_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody]
] = _WnbaV3ScoresBoxScoresByDateLiveFinalError()
