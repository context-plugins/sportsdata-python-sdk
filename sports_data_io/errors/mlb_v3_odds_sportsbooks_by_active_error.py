from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3OddsSportsbooksByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3OddsSportsbooksByActiveError:
    def map(self, status_code: int, content: bytes) -> MlbV3OddsSportsbooksByActiveErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


mlb_v3_odds_sportsbooks_by_active_error_mapper: Final[
    ErrorMapper[MlbV3OddsSportsbooksByActiveErrorBody]
] = _MlbV3OddsSportsbooksByActiveError()
