from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3ScoresNewsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3ScoresNewsByDateError:
    def map(self, status_code: int, content: bytes) -> NhlV3ScoresNewsByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_scores_news_by_date_error_mapper: Final[
    ErrorMapper[NhlV3ScoresNewsByDateErrorBody]
] = _NhlV3ScoresNewsByDateError()
