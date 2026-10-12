from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV3OddsSportsbooksByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV3OddsSportsbooksByActiveError:
    def map(self, status_code: int, content: bytes) -> NascarV3OddsSportsbooksByActiveErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nascar_v3_odds_sportsbooks_by_active_error_mapper: Final[
    ErrorMapper[NascarV3OddsSportsbooksByActiveErrorBody]
] = _NascarV3OddsSportsbooksByActiveError()
