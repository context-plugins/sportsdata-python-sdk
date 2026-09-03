from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2NewsbydateNewsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2NewsbydateNewsByDateError:
    def map(self, response: HttpResponse) -> GolfV2NewsbydateNewsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_newsbydate_news_by_date_error_mapper: Final[
    ErrorMapper[GolfV2NewsbydateNewsByDateErrorBody]
] = _GolfV2NewsbydateNewsByDateError()
