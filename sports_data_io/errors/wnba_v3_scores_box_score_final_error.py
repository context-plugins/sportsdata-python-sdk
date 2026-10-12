from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

WnbaV3ScoresBoxScoreFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _WnbaV3ScoresBoxScoreFinalError:
    def map(self, status_code: int, content: bytes) -> WnbaV3ScoresBoxScoreFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


wnba_v3_scores_box_score_final_error_mapper: Final[
    ErrorMapper[WnbaV3ScoresBoxScoreFinalErrorBody]
] = _WnbaV3ScoresBoxScoreFinalError()
