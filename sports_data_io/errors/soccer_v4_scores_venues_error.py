from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4ScoresVenuesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4ScoresVenuesError:
    def map(self, status_code: int, content: bytes) -> SoccerV4ScoresVenuesErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


soccer_v4_scores_venues_error_mapper: Final[ErrorMapper[SoccerV4ScoresVenuesErrorBody]] = _SoccerV4ScoresVenuesError()
