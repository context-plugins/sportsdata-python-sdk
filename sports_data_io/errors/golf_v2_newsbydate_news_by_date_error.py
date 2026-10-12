from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2NewsbydateNewsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2NewsbydateNewsByDateError:
    def map(self, status_code: int, content: bytes) -> GolfV2NewsbydateNewsByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_newsbydate_news_by_date_error_mapper: Final[
    ErrorMapper[GolfV2NewsbydateNewsByDateErrorBody]
] = _GolfV2NewsbydateNewsByDateError()
